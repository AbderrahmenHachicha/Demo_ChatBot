# Demo Chatbot

An intelligent, conversational AI chatbot built with Flask and powered by the Groq API. This application provides a responsive web interface for real-time interactions with advanced language models.

## Features

- **Real-time AI Conversations:** Powered by LLaMA 3.1 via Groq API
- **User-Friendly Interface:** Clean and intuitive web-based chat interface
- **Fast Response Times:** Optimized for quick API communication
- **Easy Setup:** Simple configuration with environment variables

## Tech Stack

- **Backend:** Python 3.x / Flask
- **Frontend:** HTML5 / CSS3 / JavaScript
- **AI Engine:** Groq API with LLaMA 3.1
- **Configuration:** Python-dotenv

## Prerequisites

- Python 3.8 or higher
- pip package manager
- A Groq API key (free account available at [console.groq.com](https://console.groq.com))

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AbderrahmenHachicha/Demo_ChatBot.git
cd Demo_ChatBot
```

### 2. Install dependencies

```bash
pip install flask groq python-dotenv
```

### 3. Configure environment variables

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get a free API key at: [https://console.groq.com](https://console.groq.com)

## Usage

### Run the application

```bash
python app.py
```

### Access the chatbot

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

Start typing your questions or messages to interact with the AI chatbot.

## Project Structure

```
Demo_ChatBot/
├── app.py                 # Flask application and API routes
├── .env                   # Environment variables (excluded from version control)
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── LICENSE                # MIT License
└── templates/
    └── index.html         # Web interface
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Abderrahmen Hachicha