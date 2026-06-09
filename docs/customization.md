# 🎨 Customization Guide

This document describes how to customize styles, prompts, and interface templates.

---

## 1. Style & Theme Customization
Styling is configured using the **GitHub Primer CSS** framework with custom variables and styling blocks.

To edit styles:
- Open `static/css/custom.css`.
- **Colors**: Modify the root CSS variables at the top of the file to adjust the Light/Dark mode themes.
- **Alerts**: Adjust the `.alert-success`, `.alert-error`, `.alert-warning`, and `.alert-info` blocks to style notifications.
- **Buttons & Cards**: Modify `.btn-primary` or `.Box` class shadows and borders to tweak the Neo-Brutalist or Swiss elements.

---

## 2. Scraping Prompt Customization
To customize how Gemini searches and parses hackathons:
- Open `app.py`.
- Search for `async def search_hackathons` inside `HackathonScraper`.
- **Query structure**: You can modify the search query string structure or include more platforms (e.g., Devpost, Kaggle, Major League Hacking).
- **Prompt instructions**: You can adjust the LLM instruction prompts (e.g., telling the model to focus on specific regions, remote-only events, or particular technologies).

---

## 3. Template Customization
The HTML layout is powered by Flask's Jinja2 template engine:
- `templates/base.html`: Common layout containing page headers, sidebars, theme script, and footers.
- `templates/index.html`: Dashboard showing the side-by-side search interface and list cards.
- `templates/detail.html`: Individual details page for a specific hackathon.
- `templates/edit.html`: Edit form with date validation.
