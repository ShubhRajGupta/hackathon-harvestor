# 📝 Contributing Guidelines

Thank you for your interest in contributing to Hackathon Harvester! Follow these guidelines to set up your development environment and submit changes.

---

## 1. Local Development Setup
1. **Fork the repository** on GitHub.
2. **Clone your fork** and navigate to the directory:
   ```bash
   git clone https://github.com/ShubhRajGupta/hackathon-harvestor.git
   cd hackathon-harvestor
   ```
3. Set up your virtual environment and install dependencies as described in the [Setup Guide](./setup.md).
4. Run testing scripts before making edits to ensure a stable baseline.

---

## 2. Coding Guidelines
- **PEP 8 Compliance**: Follow Python PEP 8 conventions for code style.
- **Documentation**: Add docstrings to new functions and classes.
- **Comments**: Comment complex algorithms or tricky edge cases.
- **Preserve Comments**: Maintain existing code comments that are unrelated to your edits.

---

## 3. Git Commit Message Guidelines
Use clear and semantic commit messages:
- `feat:` for new features (e.g., `feat: add email notifications`)
- `fix:` for bug fixes (e.g., `fix: repair unicode emoji crash on Windows`)
- `docs:` for documentation changes (e.g., `docs: update setup steps`)
- `style:` for changes that do not affect code logic (formatting, css updates)

---

## 4. Submitting a Pull Request
1. Create a dedicated feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
2. Commit your changes.
3. Push to your fork:
   ```bash
   git push origin feature/amazing-feature
   ```
4. Open a Pull Request against our `main` branch. Provide a clear explanation of what your changes accomplish.
