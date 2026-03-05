# Databricks Summit Session Monitor 🚀

A lightweight Python automation tool designed to monitor the number of available sessions at the **Databricks Data + AI Summit**. It notifies stakeholders via **Telegram** whenever new sessions are added to the official agenda.

## 🛠️ Tech Stack

- **Language:** Python 3.9
- **Libraries:** BeautifulSoup4 (Web Scraping), Requests (API calls), Python-dotenv
- **Automation:** GitHub Actions (CI/CD)
- **Notifications:** Telegram Bot API

## 📋 Features

- **Automated Scraping:** Periodically checks the Databricks Summit agenda website.
- **State Persistence:** Uses a local `last_count.txt` file to track the previous session count and avoid redundant alerts.
- **Serverless Execution:** Runs entirely on GitHub Actions infrastructure (no hosting costs).
- **Instant Alerts:** Sends real-time notifications to a Telegram group/user when changes are detected.

## ⚙️ Setup & Configuration

### 1. Telegram Bot
1. Create a bot using [@BotFather](https://t.me/botfather) to get your `TELEGRAM_TOKEN`.
2. Get your `CHAT_ID` (or group ID) using `@userinfobot` or the Telegram API.

### 2. GitHub Secrets
To run this project, add the following secrets to your GitHub repository (**Settings > Secrets and variables > Actions**):

| Secret | Description |
| :--- | :--- |
| `TELEGRAM_TOKEN` | Your Telegram Bot API Token |
| `CHAT_ID` | The ID of the user or group to receive alerts |