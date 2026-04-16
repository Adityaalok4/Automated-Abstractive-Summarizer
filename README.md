# Domain Abstractive Summarizer with Google Authentication

An end-to-end web app for abstractive summarization with Google OAuth authentication, provider fallback (DeepSeek + Hugging Face), URL/file ingestion, preprocessing, and MongoDB caching.The exponential growth of digital text — spanning research publications, legal doc-
uments, corporate reports, and technical manuals — has created a critical need for
intelligent systems capable of distilling lengthy content into concise, meaningful
summaries. Traditional approaches to summarization, both manual and automated,
fall short in high-stakes professional environments where precision, contextual fi-
delity, and domain-specific understanding are non-negotiable. This project presents
an Automated Abstractive Summarizer built upon advanced Natural Language Gen-
eration (NLG) techniques. Unlike extractive methods that simply copy sentences
from source documents, this system comprehends the source material and generates
novel, human-like summaries that preserve the intent, terminology, and logical flow
of the original content. The core challenge addressed is not merely shortening text,
but intelligently reconstructing its meaning in a condensed form suitable for expert
decision-making. The proposed system leverages transformer-based pre-trained lan-
Department of Computer Science and Engineering(DS), SKIT, Jaipur 2
guage models, fine-tuned on domain-specific corpora to ensure terminological accu-
racy. Key problems encountered during design include hallucination in generated
text, loss of critical domain vocabulary, and maintaining factual consistency — each
addressed through targeted model selection, fine-tuning strategies, and post-process-
ing evaluation pipelines using metrics such as ROUGE and BERTScore.

## Features
- ✅ **Google OAuth Authentication** (Sign in, Sign up, Sign out)
- ✅ **User Authorization** and session management
- ✅ **Protected Summarization** endpoints
- ✅ **UI with tabs** for Text, URL, and File inputs
- ✅ **Flask API** serving both frontend and backend
- ✅ **Provider fallback** (DeepSeek → Hugging Face)
- ✅ **File parsing** (PDF, DOCX, TXT)
- ✅ **URL article extraction**
- ✅ **Loading indicators** and error handling
- ✅ **MongoDB caching** (optional)

## Setup

### 1. Google OAuth Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the **Google+ API** and **Google OAuth2 API**
4. Go to **Credentials** → **Create Credentials** → **OAuth 2.0 Client IDs**
5. Set **Application type** to "Web application"
6. Add **Authorized redirect URIs**: `http://localhost:5000/auth/callback`
7. Copy the **Client ID** and **Client Secret**

### 2. Environment Setup
1. Copy `.env.example` to `.env`
2. Fill in your credentials:

```env
# Google OAuth (Required)
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here
GOOGLE_REDIRECT_URI=http://localhost:5000/auth/callback

# Optional: AI Providers
DEEPSEEK_API_KEY=your_deepseek_key_here
HUGGINGFACE_API_KEY=your_huggingface_key_here

# Optional: MongoDB for user storage and caching
MONGODB_URI=mongodb://localhost:27017

# Security
SECRET_KEY=your-secret-key-change-in-production
```

### 3. Install Dependencies
```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run
```bash
python -m backend.app
```
Open `http://localhost:5000` in your browser.

## Quick start (Windows PowerShell)

If you want a one-command start on Windows PowerShell, from the project root run:

```powershell
.\run.ps1
```

This script will activate a `.venv` virtual environment (if present) and start the Flask dev server.

## Authentication Flow
1. **Sign In**: Click "Sign in with Google" → Redirects to Google OAuth
2. **Authorization**: User grants permissions to your app
3. **Callback**: Google redirects back with authorization code
4. **Session**: User is logged in and can use summarization features
5. **Sign Out**: Click logout to clear session

## API Endpoints

### Authentication
- `GET /auth/login` - Get Google OAuth URL
- `GET /auth/callback` - Handle OAuth callback
- `POST /auth/logout` - Logout user
- `GET /auth/status` - Check authentication status
- `GET /auth/me` - Get current user info

### Summarization (Protected)
- `POST /api/summarize` - Summarize text/URL/file (requires authentication)

## User Management
- Users are automatically created on first login
- User data stored in MongoDB (if configured)
- Session-based authentication with secure cookies
- Automatic session expiration handling

## Security Features
- OAuth 2.0 with Google
- Secure session management
- Protected API endpoints
- CORS configuration
- Input validation and sanitization

## Notes
- **Google OAuth is required** - the app won't work without proper Google credentials
- DeepSeek requires `DEEPSEEK_API_KEY` and possibly `DEEPSEEK_BASE_URL` if self-hosted
- Hugging Face can work without a token for public models but set `HUGGINGFACE_API_KEY` to avoid rate limits
- Large inputs are truncated by `MAX_INPUT_CHARS`
- MongoDB is optional but recommended for user persistence
