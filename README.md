🤖 Titan Voice Assistant

Titan Voice Assistant is a web-based virtual assistant built using Python (Flask) for the backend and HTML, CSS, and JavaScript for the frontend.
It supports both text and voice interaction, processes commands in real time, and dynamically fetches information using external APIs.

📌 Project Overview

Titan allows users to interact through a browser by typing or speaking commands.
The assistant processes these commands on the server side and responds both visually (chat interface) and audibly (text-to-speech).

The project demonstrates practical use of Flask, REST-style communication, API integration, and browser speech technologies.

🚀 Features

⏰ Current time, date, day, month, and year

🌦 Real-time weather updates

📰 Automated technology news (API-based)

😂 Automated jokes with fallback support

💬 Automated motivational quotes

📚 Wikipedia search summaries

🎲 Utility features (random number, coin flip, dice roll)

🗣 Greetings and conversational responses

🔊 Text-to-speech output

🎤 Voice command input (browser-based)

🌐 Open Google, YouTube, and GitHub

🛠 Technologies Used
Backend

Python 3

Flask

requests – API communication

wikipedia – Wikipedia summaries

datetime, random – utility functions

Frontend

HTML

CSS

JavaScript

Web Speech API:

Speech Recognition

Speech Synthesis

AJAX (fetch) for client–server communication

📂 Project Structure
Titan-Voice-Assistant/
├── app.py
├── requirements.txt
├── RUN_INSTRUCTIONS.md
├── PROJECT_DESCRIPTION.md
├── LICENSE
├── README.md
├── templates/
│   └── index.html

⚙️ Installation & Setup
Prerequisites

Python 3.9 or higher

Internet connection

Modern web browser (Chrome recommended)

Steps

Clone the repository:

git clone https://github.com/your-username/Titan-Voice-Assistant.git


Navigate to the project directory:

cd Titan-Voice-Assistant


Install dependencies:

pip install -r requirements.txt


Run the application:

python app.py


Open your browser and visit:

http://127.0.0.1:5000/

🧠 How It Works

User enters a command using text or voice.

JavaScript sends the command to the Flask backend via AJAX.

Flask processes the command and routes it to the appropriate handler.

External APIs are used for dynamic content (news, weather, jokes, quotes).

Flask returns a JSON response.

The frontend displays the response and speaks it aloud.

✅ Advantages

Lightweight and easy to run locally

Supports both voice and text input

Automated content using real-time APIs

Clean, modular, and beginner-friendly code

Easy to extend with additional commands

⚠️ Limitations

Requires internet connection for API-based features

Keyword-based command recognition (no NLP)

Runs locally by default (not deployed)

Voice recognition depends on browser support

🔮 Future Enhancements

NLP-based intent recognition

User authentication and profiles

Task scheduling and reminders

Cloud deployment (Render / Docker)

Mobile application support

Command history and logging

📜 License

This project is licensed under the MIT License.
