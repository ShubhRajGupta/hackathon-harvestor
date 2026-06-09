# 🛠️ REST API & Database Schema

This document details the Flask endpoints and the database schema used in the Hackathon Harvester.

---

## 1. REST API Endpoints

### Home Page
- **Endpoint**: `GET /`
- **Description**: Renders the dashboard showing all active hackathons.
- **Response**: `200 OK` (HTML)

---

### Run Custom Scrape
- **Endpoint**: `POST /scrape`
- **Description**: Triggers a manual AI search and scraper run.
- **Request Headers**: `Content-Type: application/json`
- **Request Body**:
  ```json
  {
    "query": "AI/ML hackathons 2026"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "count": 5
  }
  ```

---

### Get Hackathons API (JSON)
- **Endpoint**: `GET /api/hackathons`
- **Description**: Returns a raw JSON array of all hackathons currently in the database.
- **Response**: `200 OK` (JSON)
  ```json
  [
    {
      "id": "647b0e...",
      "title": "InnoFusion 3.0",
      "platform": "devfolio",
      "status": "open",
      "website_url": "https://devfolio.co/hackathons/innofusion-3-0",
      "registration_deadline": "2026-07-27",
      "event_date": "2026-07-27",
      "prize_pool": "TBD",
      "tags": ["no restrictions", "hackathon"],
      "scraped_at": "2026-06-09T22:30:00Z"
    }
  ]
  ```

---

### View Hackathon Details
- **Endpoint**: `GET /hackathon/<id>`
- **Description**: Renders the detail page for a single hackathon.
- **Response**: `200 OK` (HTML)

---

### Update Hackathon
- **Endpoint**: `POST /update/<id>`
- **Description**: Updates fields for a specific hackathon.
- **Request Type**: `application/x-www-form-urlencoded` (Form POST)
- **Response**: `302 Found` (Redirect to `/hackathon/<id>`)

---

### Delete Hackathon
- **Endpoint**: `POST /delete/<id>`
- **Description**: Deletes a hackathon from the database.
- **Response**: `200 OK` (JSON)
  ```json
  {
    "success": true
  }
  ```

---

## 2. MongoDB Document Schema

Each hackathon is stored as a document in the `hackathons` collection with the following structure:

```json
{
  "_id": "ObjectId",
  "title": "Hackathon Name",
  "description": "Detailed description of the event, eligibility, and rules.",
  "organizer": "Name of the organizing body",
  "registration_deadline": "YYYY-MM-DD",
  "event_date": "YYYY-MM-DD",
  "prize_pool": "Prize money amount (e.g., '$10,000' or 'TBD')",
  "website_url": "https://...",
  "platform": "unstop | devfolio | hackerearth | mlh | other",
  "status": "open | closed | upcoming",
  "tags": ["tag1", "tag2"],
  "eligibility": "Eligibility criteria details",
  "scraped_at": "2026-06-09T22:30:00Z",
  "source": "gemini_search"
}
```
