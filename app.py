import os
import requests
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Medical Chatbot!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Mental health chatbot prompt
initial_system_prompt = """
You are a compassionate and supportive mental health chatbot. 
Your purpose is to help users with their mental health concerns, offering empathetic, non-judgmental advice. 
You provide coping strategies, suggest resources, and listen attentively. 
Be respectful and reassuring, but remember not to offer medical diagnoses or specific treatment plans. 
Encourage users to seek professional help if needed.
Keep the chat in a sequence with the person, ask him more about his problem.
Keep the answers precise.
"""

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[{"role": "model", "parts": [{"text": "🤖 **Xplovo - Mental Health ChatBot**\nHello! I'm **Xplovo**, your friendly medical assistant. Feel free to talk to me about anything, whether it's related to your mental health or questions about diabetes risk.\nI'm here to help guide you with advice, support, and even assess your risk for diabetes. Just type your question, and I’ll do my best to assist you!"}]}])

# Display the chatbot's title on the page
st.title("🤖 Xplovo - Mental Health ChatBot")

# Diabetes Prediction API endpoint
api_endpoint = "http://localhost:5000/predict"

# Function to get diabetes prediction
def get_diabetes_prediction(data):
    """
    Sends a POST request to the diabetes prediction API with the user-provided health data.
    
    Parameters:
        data (dict): Health data for diabetes prediction. Includes values for pregnancies, glucose,
                     blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, and age.
    
    Returns:
        int: The prediction result (1 for at-risk, 0 for not at-risk) or None if there's an error.
    """
    try:
        response = requests.post(api_endpoint, json=data)
        if response.status_code == 200:
            # Extract and return the prediction from the JSON response
            return response.json().get("prediction")
        else:
            print("Error:", response.status_code, response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return None

def generate_response(user_input):
    # Lowercase user input for case-insensitive detection
    user_input = user_input.lower()

    # If the user asks about diabetes prediction
    if "diabetes" in user_input or "risk" in user_input:
        st.write("Sure, I can help you assess your risk of developing diabetes. Please answer the following questions:")

        # Form for health data input
        with st.form("diabetes_form"):
            age = st.number_input("Age", min_value=0, value=30)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            weight = st.number_input("Weight (lbs)", min_value=0, value=150)
            height = st.number_input("Height (inches)", min_value=0, value=65)
            waist = st.number_input("Waist circumference (inches)", min_value=0, value=30)
            activity_level = st.selectbox("Physical activity level", ["Sedentary", "Moderately Active", "Very Active"])
            family_history = st.radio("Family history of diabetes?", ["Yes", "No"])
            ethnicity = st.text_input("Race/ethnicity", value="Asian")
            prediabetes = st.radio("Have you ever been diagnosed with prediabetes?", ["Yes", "No"])
            conditions = st.radio("Do you have any of the following conditions: high blood pressure, high cholesterol, or heart disease?", ["Yes", "No"])

            submit_button = st.form_submit_button("Get Risk Assessment")

        if submit_button:
            # Request body to send the collected data
            request_body = {
                "Age": age,
                "Gender": gender,
                "Weight": weight,
                "Height": height,
                "WaistCircumference": waist,
                "PhysicalActivityLevel": activity_level,
                "FamilyHistory": family_history,
                "Ethnicity": ethnicity,
                "Prediabetes": prediabetes,
                "Conditions": conditions
            }

            # Display the user's data
            st.write(f"Thanks for providing your details. I will calculate your diabetes risk based on the following data: {request_body}")
            # You can replace this line with actual diabetes risk calculation logic or call an API for prediction

            # Placeholder for risk score calculation (this should be replaced with the actual model or API logic)
            # For now, you can simulate a simple message:
            st.write("Based on your data, I will calculate your risk score and provide you with personalized recommendations.")
            
            # Example result (you can replace this logic with the prediction API or risk calculation)
            st.write("Your diabetes risk score is 45%. It's recommended to monitor your health regularly.")
    else:
        # Handle non-diabetes queries normally
        response = model.generate(user_input)
        st.write(response)


# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("ASK XPLOVO...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
