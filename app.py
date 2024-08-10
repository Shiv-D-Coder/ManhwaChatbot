import streamlit as st
from groq import Groq

# Set Streamlit page configuration
st.set_page_config(page_title="Groq Chat Interface", page_icon=":speech_balloon:")

# Define CSS for styling
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f0f0;
    }
    .css-18e3th9 {
        background-color: #e6e6e6;
    }
    .submit-button > button {
        background-color: #28a745; /* Green color for Submit button */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .submit-button > button:hover {
        background-color: #218838; /* Darker green for hover */
    }
    .end-conversation-button > button {
        background-color: #dc3545; /* Red color for End Conversation button */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .end-conversation-button > button:hover {
        background-color: #c82333; /* Darker red for hover */
    }
    .chat-message {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        max-width: 80%;
        word-wrap: break-word;
    }
    .user-message {
        background-color: #007bff;
        color: white;
        align-self: flex-end;
    }
    .assistant-message {
        background-color: #f8f9fa;
        color: #000;
        align-self: flex-start;
    }
    </style>
""", unsafe_allow_html=True)

# Add title and description to the main page
st.title("Groq Chat Interface")
st.write("Welcome to the Manhwa Recommendation Bot! Ask me about manhwa and get detailed responses.")

# Sidebar for API key and parameters
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter your Groq API key:")
    
    if api_key:
        st.write("**Configure API parameters:**")

        model = st.selectbox(
            "Select model:",
            options=[
                "gemma-7b-it",
                "gemma2-9b-it",
                "llama-3.1-70b-versatile",
                "llama-3.1-8b-instant",
                "llama-guard-3-8b",
                "llama3-70b-8192",
                "llama3-8b-8192",
                "llama3-groq-70b-8192-tool-use-preview",
                "llama3-groq-8b-8192-tool-use-preview",
                "mixtral-8x7b-32768"
            ],
            index=0,
            help="Choose the model for generating responses. Different models may vary in performance and capabilities."
        )

        temperature = st.slider(
            "Set temperature (0 to 2):",
            min_value=0.0,
            max_value=2.0,
            value=1.57,
            step=0.01,
            help="Temperature controls the randomness of the responses. Lower values make the responses more focused and deterministic, while higher values make them more random."
        )

        max_tokens = st.number_input(
            "Max tokens:",
            min_value=1,
            max_value=5000,
            value=2500,
            step=10,
            help="Maximum number of tokens to generate in the response. Increasing this allows for longer responses."
        )

        st.write("**How to use the app:**")
        st.write("1. Enter your Groq API key.")
        st.write("2. Choose the model, set the temperature, and input the maximum number of tokens.")
        st.write("3. Start chatting by typing your message and pressing 'Submit'.")
        st.write("4. You can continue asking questions until you press 'End Conversation'.")

# Initialize Groq client with API key
if api_key:
    client = Groq(api_key=api_key)

   # Initialize session state for conversation history and current input
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    if 'clear_input' not in st.session_state:
        st.session_state.clear_input = False

    # Function to clear input
    def clear_input():
        st.session_state.clear_input = True

    # Display conversation history
    st.write("### Chat History")
    for entry in st.session_state.history:
        st.markdown(f"<div class='chat-message user-message'>{entry['user']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-message assistant-message'>{entry['response']}</div>", unsafe_allow_html=True)

    # User input for new message
    if st.session_state.clear_input:
        st.session_state.user_input = ""
        st.session_state.clear_input = False

    user_input = st.text_input("Ask me about manhwa:", key="user_input")

    # Submit button for sending queries
    if st.button("Submit", key="submit", help="Submit your question"):
        if user_input:
            with st.spinner("Generating response..."):
                # API call
                chat_completion = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=temperature,
                    max_tokens=max_tokens,
                    response_format={"type": "text"}
                )
                
                # Append user input and response to history
                st.session_state.history.append({
                    'user': user_input,
                    'response': chat_completion.choices[0].message.content
                })

                # Set flag to clear input on next rerun
                clear_input()
                st.rerun()

    # End Conversation button to clear history
    if st.button("End Conversation", key="end_conversation", help="Clear chat history"):
        st.session_state.history = []
        clear_input()
        st.rerun()