<div align="center">

# LockTab

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078d4?logo=windows&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**AES-256 File Encryption Tool with a Classic Windows 95/XP Interface**

<br>

</div>

## About

**LockTab** is a desktop file encryption application that uses AES-256 encryption via the Fernet library. It features a classic Windows 95/XP-style interface with full Arabic and English language support.

Lock your files with a single key. Lose the key, and the data becomes permanently unreadable.

## Features

- **AES-256 Encryption** — Strong encryption using the Fernet standard
- **Classic UI** — Windows 95/XP style with gray backgrounds and raised borders
- **Bilingual** — Full Arabic and English support with a one-click language toggle
- **Folder-wide Encryption** — Walks through all files and subfolders automatically
- **Key Generation** — Secure random key generation built-in
- **Progress Bar** — Real-time encryption/decryption progress tracking
- **Standalone Installer** — Works on all Windows systems with no dependencies

## Screenshots

```
+--------------------------------------------------------------+
|         LockTab - File Encryption Tool               [عربي]  |
+--------------------------------------------------------------+
|  Key                                                         |
|  +----------------------------------------------------------+|
|  | gAAAAABl...encrypted_key_string_here...                  ||
|  +----------------------------------------------------------+|
|  [Generate New Key]  [Copy Key]  [Paste Key]                 |
|                                                              |
|  Folder                                                      |
|  +----------------------------------------------------------+|
|  | Selected: C:\Users\...\Documents                          ||
|  +----------------------------------------------------------+|
|  [Choose Folder...]                                          |
|                                                              |
|  [   Encrypt Entire Folder   ]  [   Decrypt Folder   ]       |
|                                                              |
|  Status                                                      |
|  [████████████████████████████████████████] 100%             |
|  Ready                                                       |
|                                                              |
|                    Powered by the L house                     |
+--------------------------------------------------------------+
```

## Installation

### Option 1: Installer (Recommended)

1. Download `LockTab_Setup_1.0.0.exe` from [Releases](../../releases)
2. Run the installer and follow the steps
3. Launch LockTab from the Start Menu or Desktop

### Option 2: Standalone Executable

1. Download `LockTab.exe` from the `dist` folder
2. Run it directly — no installation needed

### Option 3: Run from Source

```bash
git clone https://github.com/i6gu1/LockTab.git
cd LockTab
pip install -r requirements.txt
python LockTab.py
```

## How to Use

### Encrypting Files

1. Click **"Generate New Key"**
2. **Copy the key** and save it somewhere safe (critical!)
3. Click **"Choose Folder..."** and select the folder to encrypt
4. Click the red **"Encrypt Entire Folder"** button
5. Confirm by clicking "Yes"

### Decrypting Files

1. Open the app (if closed)
2. Click **"Choose Folder..."** and select the encrypted folder
3. **Paste your key** into the key field
4. Click the green **"Decrypt Folder"** button
5. Confirm by clicking "Yes"

## Project Structure

```
LockTab/
├── LockTab.py                  # Main application source code
├── icon.ico                    # Application icon
├── requirements.txt            # Python dependencies
├── LockTab.iss                 # Inno Setup installer script
├── dist/
│   └── LockTab.exe             # Standalone executable
├── installer/
│   └── LockTab_Setup_1.0.0.exe # Setup installer
├── README.md
└── .gitignore
```

## Requirements

- **OS:** Windows 7 / 8 / 10 / 11 (64-bit)
- **Python:** 3.8+ (only needed when running from source)
- **Dependencies:**
  - `cryptography >= 41.0.0`
  - `tkinter` (bundled with Python)

## Security

- Uses AES-256 encryption via the Fernet standard
- Keys are generated randomly and securely
- No keys are stored by the application
- The user is always prompted to save the key before encryption begins

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find a bug or want to add a feature:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

<div align="center">

**Powered by the L house**

</div>
