# 📖 Usage Guide

This guide explains how to use the Hackathon Harvester web interface to discover and manage hackathons.

---

## 1. Navigating the Dashboard
When you open `http://localhost:5000` in your browser, you'll see a clean, GitHub-styled dashboard:
- **Search Panel (Left)**: Input custom search terms and trigger the AI agent.
- **Listing Panel (Right)**: Interactive cards showing the scraped hackathons currently in the database.
- **Theme Switcher (Top Right)**: Switch between Light and Dark mode.

---

## 2. Searching for Hackathons
To query the web for new hackathons:
1. Locate the **AI Search** section.
2. Enter your query (e.g., `"AI hackathons 2026"`, `"web3 development hackathons"`).
3. Click **Search Hackathons**.
4. The system will start searching and parsing. This process takes a few seconds. Once finished, the page will reload with the new listings.

---

## 3. Viewing & Editing Hackathon Details
- **View Details**: Click on a hackathon card's title to view a detailed breakdown of its organizers, eligibility, rules, prize pools, and deadlines.
- **Edit Details**: Click **Edit** on a hackathon card or details page. You can modify any field (description, dates, organizer, website) manually.
  - *Tip: The edit form validates URLs and dates before submitting.*

---

## 4. Deleting & Google Search Fallback
- **Delete**: Click **Delete** on the card or detail page. This instantly removes the hackathon from the MongoDB collection.
- **Search Fallback**: If a registration URL is broken or outdated, click the **Search** icon/link next to the URL. The app will auto-generate a search query and redirect you to Google to find the updated registration page.
