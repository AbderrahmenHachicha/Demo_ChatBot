# Demo Chatbot

A simple AI-powered chatbot built with Flask and Groq API.

## Tech Stack
- Python / Flask (Backend)
- HTML / CSS / JavaScript (Frontend)
- Groq API with LLaMA 3.1 (AI)

## Setup

### 1. Clone the repository
git clone https://github.com/yourusername/demo_chatbot.git
cd demo_chatbot

### 2. Install dependencies
pip install flask groq python-dotenv

### 3. Create your .env file
Create a file called .env in the root folder and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

Get a free API key at: https://console.groq.com

### 4. Run the app
python app.py

### 5. Open your browser
Go to: http://127.0.0.1:5000

## Project Structure
demo_chatbot/
├── app.py
├── .env (not pushed to GitHub)
├── .gitignore
├── README.md
└── templates/
    └── index.html

## Author
Abderrahmen
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.