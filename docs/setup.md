# 🚀 Setup & Installation Guide

This guide details how to set up the Hackathon Harvester application, including prerequisites, environment configurations, and database options.

---

## Prerequisites
Before starting, ensure you have the following installed and available:
- **Python**: Version 3.8 or higher.
- **MongoDB**: A running local MongoDB instance or a [MongoDB Atlas](https://www.mongodb.com/atlas) account.
- **Gemini API Key**: A valid key from [Google AI Studio](https://makersuite.google.com/app/apikey).

---

## Installation Options

### Option 1: Automated Setup (Recommended)

**On Windows (PowerShell/CMD):**
```bash
setup.bat
```

**On Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

---

### Option 2: Manual Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShubhRajGupta/hackathon-harvestor.git
   cd hackathon-harvestor
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   *   **Windows:**
       ```powershell
       venv\Scripts\activate
       ```
   *   **Linux/Mac:**
       ```bash
       source venv/bin/activate
       ```

4. **Install all dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your environment variables:**
   Copy the `.env.example` template to a new file named `.env`:
   ```bash
   cp .env.example .env
   ```

---

## Environment Configuration

Open the newly created `.env` file and configure the variables:

```env
# Google Gemini API Key (Required)
GEMINI_API_KEY=your_gemini_api_key_here

# MongoDB Connection String (Required)
# Local: mongodb://localhost:27017/
# Atlas: mongodb+srv://username:password@cluster.mongodb.net/
MONGODB_URI=mongodb://localhost:27017/
MONGODB_DB=hackathon_db

# Flask Configuration (Optional)
FLASK_ENV=development
FLASK_DEBUG=True
```

---

## Database Configuration

### Option A: Local MongoDB
1. Install MongoDB Community Server on your system.
2. Start the MongoDB service. On Windows:
   ```powershell
   Start-Service -Name MongoDB
   ```
3. Set your connection string in `.env`:
   ```env
   MONGODB_URI=mongodb://localhost:27017/
   ```

### Option B: MongoDB Atlas (Cloud)
1. Register for a free account at [MongoDB Atlas](https://www.mongodb.com/atlas).
2. Create a new shared cluster (M0 is free).
3. Under **Database Access**, create a user with read/write access.
4. Under **Network Access**, allow access from anywhere (`0.0.0.0/0`) or whitelist your IP.
5. Click **Connect** -> **Connect your application** to copy your connection string.
6. Replace `<password>` in the connection string and add it to `.env`:
   ```env
   MONGODB_URI=mongodb+srv://username:password@cluster0.xxxx.mongodb.net/
   ```
