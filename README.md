# 🧠 EcoHands : News-to-Sign Language Converter

## 📌 Project Description
A full-stack application that helps convert news articles into sign language sequences — making current events more accessible to the deaf and hard-of-hearing community.

## 🚀 Problem Statement
The deaf community often faces challenges when consuming written or spoken news due to differences in language structure and accessibility. This tool aims to bridge that gap by automatically converting news articles into sign language visuals, allowing users to visually understand complex news topics.

## 🎯 Core Objective
Take a news URL as input → extract the article → generate a summary using NLP → convert the summary into sign language visuals → display the visuals in a React frontend.

## 🛠️ How It Works

### User Input
- User submits a news article URL through the React frontend.

### Web Scraping (Backend)
- The backend uses **newspaper3k** to:
  - Download and parse the article.
  - Extract title, body text, author, and date.

### Summarization using NLP
- The extracted article body is fed to a pre-trained NLP model (e.g., **T5** or **BART**) from **HuggingFace** to generate a concise summary.

### Text-to-Sign Mapping
- The summary is tokenized word-by-word:
  - If a word has a direct sign image → use it.
  - If not → break it down to alphabet signs (e.g., “chatGPT” → C, H, A, T, G, P, T).

### Frontend Sign Playback (React)
- Sign images are sequentially rendered in the frontend, simulating a real-time sign language interpreter. Features like play/pause, delays, and subtitles can be added.

## 🧱 Tech Stack

| Layer            | Tech Used                                       |
|------------------|-------------------------------------------------|
| **Frontend**     | React.js                                        |
| **Backend**      | FastAPI                                         |
| **Web Scraping** | newspaper3k                                     |
| **NLP Model**    | HuggingFace Transformers (T5, BART)            |
| **Image Mapping**| Python (os, PIL, local assets)                  |
| **UI Tools**     | React Components / Tailwind / CSS               |

## 📁 Project Structure

```bash
/backend
│
├── main.py               # FastAPI server
├── scraper.py            # Web scraping logic
├── summarizer.py         # NLP summarization
├── converter.py          # Text to sign mapping
└── assets/signs/         # Images of sign language symbols

/frontend
└── React project files   # User interface
```

## ✨ Features

- **📰 Article Extraction**: Cleanly extracts news content from article URLs.
- **🧠 NLP Summarization**: Summarizes long articles into concise, easy-to-understand summaries using natural language processing (NLP).
- **🤟 Sign Language Conversion**: Converts the article summary into sign language sequences.
- **📺 Visual Sign Playback**: Plays the sign language sequences as visuals on the frontend for easy understanding.
- **🌐 Full Integration**: End-to-end integration between the React frontend and FastAPI backend to provide a seamless user experience.

## 🌱 Future Enhancements

- **Gesture Animations**: Replace static images with dynamic gesture animations or videos for a more immersive sign language experience.
- **Audio Narration & Subtitles**: Add audio narration along with subtitles for better accessibility and understanding.
- **ML-based Sign Generation**: Integrate machine learning models to generate signs dynamically instead of using static assets.
- **Cloud Deployment**: Deploy the application to the cloud (Render/Netlify for frontend + Railway for backend) for better scalability and availability.

## 🚀 Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/parthnarkar/EcoHands.git
    cd EcoHands
    ```

2. **Install backend dependencies (FastAPI):**
    ```bash
    cd backend
    pip install -r requirements.txt
    ```

3. **Install frontend dependencies (React):**
    ```bash
    cd frontend
    npm install
    ```

4. **Run the backend and frontend:**
    - Backend (FastAPI):
      ```bash
      uvicorn main:app --reload
      ```
    - Frontend (React):
      ```bash
      npm start
      ```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
