# Manhwa Chatbot

Welcome to **Manhwa Chatbot**! 🌟 This interactive web app delivers personalized manhwa recommendations and engaging AI-powered conversations.

![Manhwa](https://madakiba.com/files/child_tree_product_categories/2023/11/13/MANHWA.png)
## 📍 Deployed App

Explore the live app here: [Manhwa Chatbot](https://manhwa-chatbot.streamlit.app/)

## 🚀 Features

- **Interactive Manhwa Recommendations**: Receive tailored manhwa suggestions based on your interests.
- **AI-Powered Conversations**: Engage in intelligent dialogues with our chatbot about manhwa or just for fun.
- **Customizable Experience**: Adjust AI model, temperature, and max tokens to personalize your chat experience.

## 💡 How It Works

1. **Enter Your API Key**: Provide your Groq API key in the sidebar to authenticate and interact with the AI model.
2. **Select Preferences**: Choose the AI model, set the temperature, and specify max tokens for a customized chat experience.
3. **Start Chatting**: Type your questions or preferences to get recommendations or have a conversation with the AI.

## 🛠️ Local Development

To run the app locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Shiv-D-Coder/ManhwaChatbot/
   cd ManhwaChatbot
   ```
2. **Install Dependencies**
Make sure you have Python 3.7 or higher installed. Then, create a virtual environment and install the required packages:

   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3. **Run the app**

   ```bash
   streamlit run app.py --server.port 8051
   ```

Open your web browser and go to http://localhost:8051 to view the app.

## 🐳 Running with Docker

You can also run the app using Docker. Here’s how:

1. Build the Docker Image

   ```bash
   docker build -t manhwa_chatbot:latest .
   ```
2. Run the Docker Container
   
   ```bash
   docker run -p 8051:8051 manhwa_chatbot:latest
   ```
   The app will be available at http://localhost:8051.

You can also pull images directly from my Dockerhub to do that run below command

   ```bash
   docker login
   docker pull shiv37/manhwa_chatbot:latest
   ```
   
Enjoy using Manhwa Chatbot! If you have any suggestions or issues, please let me know. Happy chatting! 😊
   
