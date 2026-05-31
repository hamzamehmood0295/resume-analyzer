# 📄 AI Resume Analyzer

An AI-powered resume analysis tool built with Streamlit and Groq API. Upload your resume and get instant, detailed feedback from an expert AI model.

## ✨ Features

- 📤 Upload resume in PDF format
- ✅ Identifies strengths in your resume
- ❌ Highlights weaknesses and missing elements
- 💡 Provides specific improvement suggestions
- 🎯 Suggests job roles that match your profile
- ⚡ Powered by Groq's ultra-fast LLaMA 3.3 70B model

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — Web UI
- [Groq API](https://console.groq.com/) — AI inference
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) — PDF text extraction
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Environment variable management

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/hamzamehmood0295/resume-analyzer.git
cd resume-analyzer
```

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install streamlit pymupdf groq python-dotenv
```

### 4. Setup environment variables

Create a `.env` file in the root folder:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key from [console.groq.com](https://console.groq.com)

### 5. Run the app

```bash
python -m streamlit run app.py
```

## 📁 Project Structure

```
resume-analyzer/
│
├── app.py          # Main application file
├── .env            # API key (not uploaded to GitHub)
├── .gitignore      # Ignored files
└── README.md       # Project documentation
```

## ⚠️ Important

Never upload your `.env` file to GitHub. It contains your secret API key.

## 👨‍💻 Developer

**Hamza Mehmood**  
GitHub: [@hamzamehmood0295](https://github.com/hamzamehmood0295)
