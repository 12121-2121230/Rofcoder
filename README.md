## 🛠️ Rofcoder v6.0
A lightweight GUI frontend wrapper designed to make Python packaging and C++ compilation entirely seamless. 

## ⚡ Quick-Start (For Beginners)
Follow these 4 steps to get up and running immediately:
1. **Download:** Go to the Releases tab and download `Rofcoder_Setup.msi`, and make sure you are on the C: Drive and Program Files is located there.
2. **Move Executable:** After installation, move `Rofcoder.exe` into the internal folder.
3. **Add the DLL:** Copy your system's `python3x.dll` (e.g., `python311.dll`) directly into the Rofcoder folder.
4. **Launch:** Run the app! (If you face `.dll` errors, just double-click `Rofcoder.pyw` instead, and if you have env errors, use sysdm.pyw).

---

## ✨ Key Features
* **Multi-Language Support:** Quickly switch between bundling Python (`.py`) scripts and compiling C++ (`.cpp`) code.
* **Backend Automation:** Runs PyInstaller or MinGW (`g++`) under the hood so you don't have to touch the terminal.
* **Integrated Directory Explorer:** Keep track of your system folders and project paths directly from the UI panel.

---

## 🚀 How to Build Your First EXE
1. Select your target environment (**Python** or **C++**).
2. Paste or write your code directly into the editor pane.
3. Click `BUILD EXE ⚡` and select your output folder to generate your clean, native Windows executable!

*Note: `lol.spec` was just an example file. The actual configuration file used by the system is `Rofcoder.spec`.*

---

## 📦 Required Dependencies & Core Architecture
Rofcoder is built on Python and automates terminal compilation tools. To successfully build standalone executables, ensure your system has these prerequisites installed:

### 🐍 Python Environment & PyInstaller (For Python Scripts)
* **The Core:** Python 3.x must be installed natively on your system [1].
* **The Bundler:** You need PyInstaller installed (`pip install pyinstaller`) to convert scripts.
* **File Formats:** Rofcoder uses PyInstaller under the hood to compile both standard console scripts (`.py`) and windowed/GUI applications (`.pyw`).
* **The Spec File:** The application uses `Rofcoder.spec` to handle the actual compilation tracking.

### 🛠️ MinGW Toolchain (For C/C++ Code)
* **The Compiler:** You must have MinGW or MinGW64 installed to compile low-level code.
* **Languages Supported:** This toolchain provides the necessary background environment to compile both C and C++ source code into standalone Windows binaries via `g++`.

---

## 🔧 Advanced Configuration & Environment Variables

If Rofcoder cannot automatically detect your toolchains, you must define them manually in your Windows System Environment Variables.

Luckily, I built `sysdm.pyw`. This file installs PyInstaller and MinGW, sets it to your environment variables, and doesn't do anything else. Clean, good, and superior if you can't set your environment variables up good.

### 🐍 Python Path Overrides
By default, the UI checks your Windows Registry for standard Python paths. If you are running an environment manager like Anaconda, Miniconda, or a local virtual environment (`venv`), paste your direct path override:
* Target 1: `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python311\python.exe`
* Target 2: `C:\Program Files\Python312\python.exe`

### 🛠️ MinGW64 Path Configuration (C++ Mode)
If clicking "BUILD EXE" in C++ mode yields a `g++ is not recognized` terminal panic, fix your environment variables:
1. Hit `Win + R`, type `sysdm.cpl`, and press **Enter**.
2. Navigate to **Advanced** ➡️ **Environment Variables**.
3. Under **System Variables**, find `Path` and click **Edit**.
4. Add your MinGW bin path (Default: `C:\msys64\ucrt64\bin` or `C:\MinGW\bin`).
Or, Install `sysdm.pyw`!
---

## 🔒 The Web Feature: Secure Fetch Protocol

The integrated blue **DOWNLOAD** module leverages raw HTTP requests to fetch snippets directly. Follow these ground rules to avoid breaking your builds:

1. **Verify Raw Endpoints:** Ensure your source web links end explicitly in raw text fields (like [GitHub Raw](https://githubusercontent.com)).
2. **Never Fetch Pre-Compiled Files:** Do not pass an existing binary download URL into the editor box. It will attempt to wrap an `.exe` inside another `.exe`, completely corrupting the architecture.
3. **No Dynamic Payload Execution:** Avoid using `eval()` or `exec()` commands inside your code targets when pulling web lines down to remain securely under the radar of heuristic defenses.

---

Enjoy and ***BYE!!***
