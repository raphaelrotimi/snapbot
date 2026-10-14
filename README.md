
***

# 👻 Snapchat Automation Bot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Automation-Playwright-green.svg)](https://playwright.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional-grade automation tool designed to assist in adding users on Snapchat. By leveraging **Playwright** and **Stealth** technology, this bot mimics human browsing behavior to minimize the risk of account flagging and detection.

---

## ✨ Key Features
- **Session Persistence:** Automatically saves your login state, meaning you only have to log in once.
- **Stealth Mode:** Integrates `playwright-stealth` to hide automation signatures from Snapchat's security systems.
- **Human-Like Jitter:** Uses randomized wait times between actions to avoid "bot-like" patterns.
- **Secure Configuration:** Keeps your passwords safe using environment variables (`.env`).


***

### 💻 System Requirements

To run this bot successfully, your machine must meet the following specifications:

#### 1. Operating System (OS)
The bot is designed to run on the following platforms:
*   **Linux** (Recommended: **Kali Linux**, Ubuntu, or Debian).
*   **Windows 10/11**.
*   **macOS**.
*   *Note: This bot will NOT run on mobile phones (Android/iOS) directly; you must use a terminal emulator like Termux (advanced) or a PC.*

#### 2. Software Requirements
*   **Python 3.8 or higher:** The bot relies on `asyncio`, which requires a modern version of Python.
*   **Web Browser:** The bot automatically installs **Chromium** (a version of Chrome). You must have a stable internet connection to download the browser binaries during setup.
*   **Display/GUI:** 
    *   Since the bot handles login and 2FA manually, you need a machine with a **Desktop Environment** (a screen) for the first login. 
    *   If you are using a **VPS (Headless Server)**, you will need to configure the bot to `headless=True` after your first manual login.

#### 3. Hardware Minimums
*   **RAM:** At least **2GB of RAM** (Browsers consume significant memory).
*   **Storage:** Approx **500MB** of free space for the browser installation and session profiles.

---



## 🛠 Installation

### 1. Clone the Repository
First, clone this project to your local machine:
```bash
git clone https://github.com/raphaelrotimi/snapbot.git
cd snapbot
```

### 2. Install Dependencies
Install the required Python libraries:
```bash
pip install playwright playwright-stealth python-dotenv
```

Install the browser binaries and system dependencies:
```bash
playwright install chromium
playwright install-deps
```

---

## ⚙️ Configuration

### 1. Set Up Credentials
To protect your privacy, this bot does not hardcode passwords. Create a file named `.env` in the project folder:
```bash
nano .env
```
Paste the following and replace with your own details:
```env
SNAP_USER=your_username_here
SNAP_PASS=your_password_here
```

### 2. Set Up Target List
Create a file named `targets.txt` and add the usernames you want to add, **one per line**:
```text
username_one
username_two
username_three
```

---

## 🚀 Usage

Run the bot with the following command:
```bash
python3 snapbot.py
```

### ⚠️ Critical: The First Run
During the first launch, a browser window will open for authentication:
1. **Login:** The bot will attempt to fill in your details.
2. **2FA:** If you have Two-Factor Authentication enabled, **manually enter the code** in the browser window.
3. **Completion:** Once you land on the Snapchat home page, the bot will save your session and start processing your `targets.txt` list automatically.

*On all future runs, the bot will skip the login process and go straight to adding users.*

---

## 🛡️ Anti-Ban Strategy

To keep your account safe, we recommend the following:
- **Timing:** Keep the `wait_time` in the script between **30 to 90 seconds**.
- **Volume:** Do not add more than 100 people per day on a fresh account.
- **Behavior:** If you encounter a CAPTCHA, solve it manually in the browser window and let the bot resume.

---

## 📂 Project Structure
| File | Description |
| :--- | :--- |
| `snapbot.py` | The main execution script |
| `.env` | Secret credentials (not uploaded to GitHub) |
| `targets.txt` | List of usernames to add |
| `.gitignore` | Tells Git which files to keep private |
| `snap_profile/` | Folder where your login session is stored |

---

## 👤 Author
**Raphael Rotimi**  
*Feel free to star ⭐ this repository if you find it useful!*
**Which automation bot do you want me to build next?**
***

