# Domain Abstractive Summarizer with Google Authentication

An end-to-end web app for abstractive summarization with Google OAuth authentication, provider fallback (DeepSeek + Hugging Face), URL/file ingestion, preprocessing, and MongoDB caching.

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
