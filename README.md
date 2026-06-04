## 🛠️ Rofcoder v6.0
A lightweight GUI frontend wrapper designed to make Python packaging and C++ compilation entirely seamless.

## ⚡ Quick-Start (For Beginners)
Follow these steps to get up and running immediately:
1. **Download:** Go to the Releases tab and download `Rofcoder_Setup.msi`.
2. **Launch:** Run the application via the desktop shortcut or the installation directory.
3. **Source Verification:** To inspect the underlying logic or run the application directly from source, you can execute the `Rofcoder.pyw` script.

---

## ✨ Key Features
* **Multi-Language Support:** Quickly switch between bundling Python (`.py`) scripts and compiling C++ (`.cpp`) code.
* **Backend Automation:** Runs PyInstaller or MinGW (`g++`) under the hood so you do not have to touch the terminal.
* **Integrated Directory Explorer:** Keep track of your system folders and project paths directly from the UI panel.

---

## 🚀 How to Build Your First EXE
1. Select your target environment (**Python** or **C++**).
2. Paste or write your code directly into the editor pane.
3. Click `BUILD EXE ⚡` and select your output folder to generate your standalone Windows executable.

*Note: The application utilizes a standard configuration template (`Rofcoder.spec`) to manage custom PyInstaller compilation flags.*

---

## 📦 Required Dependencies & Core Architecture
Rofcoder automates terminal compilation tools. To successfully build standalone executables, ensure your system has these prerequisites installed:

### 🐍 Python Environment & PyInstaller (For Python Scripts)
* **The Core:** Python 3.x must be installed natively on your system.
* **The Bundler:** PyInstaller must be installed (`pip install pyinstaller`) to convert scripts.
* **File Formats:** Rofcoder automates compilation for both standard console scripts (`.py`) and windowed GUI applications (`.pyw`).

### 🛠️ MinGW Toolchain (For C/C++ Code)
* **The Compiler:** MinGW or MinGW64 must be installed to compile low-level code.
* **Languages Supported:** This toolchain provides the necessary binary environment to compile C and C++ source code via `g++`.

---

## 🔧 Advanced Configuration & Environment Variables

If Rofcoder cannot automatically detect your toolchains, you can use the included `sysdm.pyw` utility. This helper script automates the installation of PyInstaller, checks for MinGW, and configures the required environment variables.

### 🐍 Python Path Overrides
By default, the UI checks the Windows Registry for standard Python paths. If you are running an environment manager like Anaconda, Miniconda, or a local virtual environment (`venv`), paste your direct path override:
* Example 1: `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python311\python.exe`
* Example 2: `C:\Program Files\Python312\python.exe`

### 🛠️ MinGW64 Path Configuration (C++ Mode)
If the system yields a `g++ is not recognized` error, you can manually update your environment variables:
1. Press `Win + R`, type `sysdm.cpl`, and press **Enter**.
2. Navigate to the **Advanced** tab and click **Environment Variables**.
3. Under **System Variables**, locate `Path` and click **Edit**.
4. Add your MinGW bin path (Default: `C:\msys64\ucrt64\bin` or `C:\MinGW\bin`).

---

## 🔒 Code Fetch Module

The integrated **DOWNLOAD** module leverages raw HTTP requests to fetch source code snippets directly into the editor pane. Please follow these guidelines to prevent build failures:

1. **Use Raw Endpoints:** Ensure your source web links point explicitly to raw text fields (such as GitHub Raw links).
2. **Source Code Only:** Do not pass URLs of pre-compiled binaries (`.exe`) into the text box. The system is designed to compile raw source scripts, and injecting a binary will break the compilation architecture.
---
Enjoy and ***BYE!!***
