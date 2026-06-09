# 🔍 Troubleshooting Guide

This guide compiles solutions for common issues encountered during setup and execution.

---

## 1. MongoDB Connection Issues
### Symptom
- Running `python test/run.py` prints a traceback pointing to a `ServerSelectionTimeoutError`.
- The web page loads but does not display any hackathons, showing a "Failed to connect to Database" warning.

### Solution
Your MongoDB instance is either not installed or not currently running.
- **On Windows**: Open PowerShell as **Administrator** and run:
  ```powershell
  Start-Service -Name MongoDB
  ```
- **Using Cloud DB**: Create a free cloud cluster on [MongoDB Atlas](https://www.mongodb.com/atlas) and replace the local URI in your `.env` file with the Altas URI:
  ```env
  MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.xxxx.mongodb.net/
  ```

---

## 2. Unicode / Emoji Output Failures on Windows
### Symptom
Executing `python test/run.py` or diagnostic scripts crashes immediately with:
`UnicodeEncodeError: 'charmap' codec can't encode character...`

### Solution
The Windows command shell is using legacy encoding (typically `cp1252`), which cannot render the Unicode emojis (like 🔍, ✅, ❌) printed by the scripts.
- **Fix**: Override the default encoding by prefixing the launch command with the `PYTHONIOENCODING` variable:
  ```powershell
  $env:PYTHONIOENCODING="utf-8"; python test/run.py
  ```

---

## 3. Gemini API Credentials Errors
### Symptom
- Scraping runs fail with a `Google API key not found` or `API key is invalid` error.

### Solution
- Ensure that the `.env` file contains your actual key, not the template placeholder:
  `GEMINI_API_KEY=AQ.Ab8RN...`
- Verify that there are no spaces or quotes surrounding the key in your `.env` file.
- Verify that your key has not expired or exceeded its quota on [Google AI Studio](https://makersuite.google.com/app/apikey).

---

## 4. Module Import Failures
### Symptom
Running a script results in:
`ModuleNotFoundError: No module named 'llama_index'` (or other package).

### Solution
This occurs if the script is run in the global shell environment rather than the virtual environment.
- Make sure to activate the virtual environment first (`venv\Scripts\activate` on Windows).
- Alternatively, call the interpreter directly inside your active workspace directory:
  ```powershell
  .\venv\Scripts\python.exe test/run.py
  ```
