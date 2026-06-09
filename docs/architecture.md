# 🏗️ Architecture Overview

This document describes the design and components of the Hackathon Harvester application.

---

## Technical Stack

The application uses a lightweight, modern tech stack designed for speed and reliability:

-   **Backend**: Flask (Python 3.8+)
-   **AI Scraper Engine**: LlamaIndex + Gemini 2.5 Flash
-   **Database**: MongoDB (PyMongo client)
-   **Scheduler**: Advanced Python Scheduler (APScheduler)
-   **Frontend**: Jinja2 templates styled with GitHub Primer CSS design system

---

## Component Diagram

```
┌────────────────────────────────────────────────────────┐
│                      Web UI                            │
│           (Jinja2 + GitHub Primer CSS)                 │
└────────────────────────┬───────────────────────────────┘
                         │ REST / HTML
                         ▼
┌────────────────────────────────────────────────────────┐
│                   Flask Backend                        │
│                     (app.py)                           │
└─────┬──────────────────┬─────────────────────────┬─────┘
      │                  │                         │
      ▼                  ▼                         ▼
┌───────────┐      ┌───────────┐             ┌───────────┐
│  MongoDB  │      │Scheduler  │             │  Scraper  │
│ Database  │      │ (APSched) │             │ (Gemini)  │
└───────────┘      └───────────┘             └─────┬─────┘
                                                   │
                                                   ▼
                                             ┌───────────┐
                                             │  Google   │
                                             │  Search   │
                                             └───────────┘
```

---

## Key Modules

### 1. Web Application (`app.py`)
Serves Flask endpoints, manages sessions, runs database queries, and handles user CRUD actions (creation, editing, deletion).

### 2. Scraping Engine (`scrapper/scraper.py`)
Responsible for search orchestration. It queries Google Search using LlamaIndex's Gemini integration, retrieves unstructured search results, and parses them into a structured database format.

### 3. Background Scheduler
An automated cron-like scheduler running as a background thread inside `app.py`. It initiates a cleanup and scraping run:
1. On app startup (deferred by 2 seconds to allow the web server to start).
2. Every 6 hours to sync new hackathons and drop expired ones.

---

## Data Flow

1.  **Trigger**: User clicks "Search" on the UI or the background scheduler wakes up.
2.  **Web Search**: Gemini uses Google Search to query active hackathons on platforms like Devfolio, Unstop, and HackerEarth.
3.  **Extraction**: Gemini reads search snippets/pages, converts them to structured JSON data, and parses the deadlines.
4.  **Sanitization & Deduplication**: The backend parses the JSON, validates dates, removes expired contests, and cleans duplicates using case-insensitive matches and string similarity metrics.
5.  **Persistence**: Cleaned hackathons are inserted into MongoDB.
6.  **Presentation**: The user loads the dashboard and sees the parsed hackathons.
