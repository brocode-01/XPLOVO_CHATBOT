# XPLOVO_CHATBOT
**Overview**
Xplovo is an AI-powered chatbot designed to assist users with mental health support and assess the risk of diabetes. The chatbot provides empathetic and non-judgmental advice, encourages users to seek professional help when necessary, and offers personalized recommendations based on user input.
Features
Mental Health Support:
Offers empathetic and compassionate advice for mental health concerns.
Provides coping strategies and resources without offering medical diagnoses or treatment plans.
Maintains a supportive and respectful tone throughout the conversation.
Diabetes Risk Assessment:
Allows users to input their health and lifestyle details.
Analyzes data to estimate the user's risk of developing diabetes.
Provides personalized recommendations based on the risk score.
**Real-Time Interaction:**
Powered by Google Gemini-Pro AI to ensure responsive and context-aware interactions.
Maintains a sequential conversation to understand user concerns better.
User-Friendly Interface:
Streamlit-based interface for an intuitive user experience.
Forms for structured data collection in diabetes risk assessment.
**Technology Stack**
Frontend: Streamlit for interactive UI/UX.
Backend: Python for chatbot logic and API integration.
AI Model: Google Gemini-Pro AI for natural language understanding and response generation.
APIs: Local API for diabetes risk prediction.
Data Analysis: Matplotlib, Pandas, Numpy, MS Excel, and MS Power BI for data processing and visualization.
Environment Management: Python dotenv for secure handling of environment variables.
**Installation**
Clone the Repository:
git clone <repository-url>
cd <repository-directory>
Install Dependencies:
pip install -r requirements.txt
Set Up Environment Variables:
Create a .env file in the root directory.
Add your Google API key: GOOGLE_API_KEY=your_google_api_key
Run the Application: streamlit run app.py
How It Works
**Mental Health Chatbot**
The chatbot starts with an empathetic greeting, encouraging users to share their concerns.
Conversations are processed through Google Gemini-Pro AI, which generates context-aware and supportive responses.
**Diabetes Risk Assessment**
Users provide health and lifestyle information via a structured form.
The chatbot sends the data to a local API endpoint (http://localhost:5000/predict).
The API processes the data and returns a risk score.
Xplovo presents the risk assessment and provides tailored recommendations.
Key Components
File Structure
.
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── README.md             # Documentation
└── other-support-files   # Supporting files for the project


.
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── README.md             # Documentation
└── other-support-files   # Supporting files for the project

Chatbot Logic
Chat history is maintained using Streamlit's session state.
User inputs are processed and responded to via Google Gemini-Pro AI.
User roles are translated between Streamlit and the AI model for consistent interaction.
Diabetes Risk Prediction
Health data is collected using a Streamlit form.
The data is sent as a POST request to a local Flask API.
The API returns a prediction based on the input data.
Usage
Start the Chatbot:
Run the Streamlit app and navigate to the provided URL.
Interact with Xplovo by typing your questions or concerns in the chat input.
Diabetes Risk Assessment:
Mention "diabetes" or "risk" in the chat to trigger the risk assessment workflow.
Fill out the form with accurate health and lifestyle details.
Submit the form to receive your risk assessment.


