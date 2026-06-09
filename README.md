# 🏆 Hackathon Harvester

An AI-powered web scraper that discovers and indexes active hackathons across platforms like Unstop, Devfolio, HackerEarth, and more. It utilizes Google's Gemini AI with integrated Google Search tools to automatically extract structured event data.

![UI Badge](https://img.shields.io/badge/UI-GitHub%20Docs%20Style-blue)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-green)
![Flask Badge](https://img.shields.io/badge/Flask-3.0-red)
![MongoDB Badge](https://img.shields.io/badge/MongoDB-Atlas%20Ready-brightgreen)
![Gemini Badge](https://img.shields.io/badge/AI-Google%20Gemini-orange)

---

## ✨ Features

-   🔍 **AI-Powered Discovery**: Leverages Gemini 2.5 Flash and Google Search tools to search and scrape hackathons semantically.
-   📊 **Robust Ingestion**: Cleans, validates, and deduplicates events using name similarity heuristics before saving them.
-   🎨 **GitHub Docs Interface**: Features a clean, responsive, accessible interface with built-in Light and Dark themes.
-   ⏱️ **Background Syncing**: Spawns daemon threads to automatically scrape new contests and purge expired items every 6 hours.

---

## 📖 Documentation Directory

For deep-dive topics, refer to our modular guides:

| Document | Topic |
| :--- | :--- |
| [🚀 Setup & Installation](docs/setup.md) | System requirements, virtual environment, and local/cloud DB configurations. |
| [🏗️ Architecture Overview](docs/architecture.md) | Component breakdown, scheduling workflows, and system data flows. |
| [🛠️ REST API & Schema](docs/api.md) | Flask routes details and database document schemas. |
| [📖 Usage Guide](docs/usage.md) | Search options, updates, deletions, and search fallback guides. |
| [🎨 Customization Guide](docs/customization.md) | Customizing prompt patterns, styles, themes, and Jinja2 templates. |
| [📝 Contributing Guidelines](docs/contributing.md) | Coding style rules and pull request procedures. |
| [🔍 Troubleshooting Guide](docs/troubleshooting.md) | Solutions for MongoDB connection issues, Unicode shell errors, and more. |

---

## ⚡ Quick Start

### 1. Configure Environment Variables
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
MONGODB_URI=mongodb://localhost:27017/
MONGODB_DB=hackathon_db
```

### 2. Install & Launch
Run the automated runner to check dependencies and boot the application:
```powershell
python test/run.py
```
*Note: If you encounter emoji rendering issues on Windows Command Prompt or PowerShell, prefix with the environment variable:*
```powershell
$env:PYTHONIOENCODING="utf-8"; python test/run.py
```

Open `http://localhost:5000` in your web browser.

---

## 🗺️ Roadmap

- [ ] Email notifications for newly discovered hackathons
- [ ] Calendar sync integration (Google Calendar, iCal)
- [ ] Direct team formation tools within cards
- [ ] Advanced filter tags and custom technology matching
- [ ] Desktop/Browser companion extension
- [ ] Slack/Discord webhook alerts integration
