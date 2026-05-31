## 🛠️ Rofcoder v6.0
A lightweight GUI frontend wrapper designed to make Python packaging and C++ compilation entirely seamless. 

## ✨ Key Features
* **Multi-Language Support:** Quickly switch between bundling Python (`.py`) scripts and compiling C++ (`.cpp`) code.
* **Backend Automation:** Runs PyInstaller or MinGW (`g++`) under the hood so you don't have to touch the terminal.
* **Integrated Directory Explorer:** Keep track of your system folders and project paths directly from the UI panel.


[With the web feature, do not download malware. This needs PyInstaller, Python and MinGW to work. Move Rofcoder.exe into the internal folder, and copy python's 3.x .dll right into Rofcoder's folder]

To install, Go to Dist on my releases. Not Build.

lol.spec was an example of a spec for an exe, the actual one is Rofcoder.spec!

## 🚀 Getting Started
1. Select your target environment (Python or C++).
2. Paste or write your code directly into the editor pane.
3. Click `BUILD EXE ⚡` and select your output folder to generate your clean, native Windows executable!


It's that easy.
## 🔧 Advanced Configuration & Environment Variables

If Rofcoder cannot automatically detect your toolchains, you must define them manually in your Windows System Environment Variables or configure a `config.json` inside the application directory.

### 🐍 Python Path Overrides
By default, the UI checks your Windows Registry for standard Python paths. If you are running an environment manager like Anaconda, Miniconda, or a local virtual environment (`venv`), paste your direct path override:
* Target: `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python311\python.exe`
* Target: `C:\Program Files\Python312\python.exe`



### Required
MinGW: C++ and C? Well, what else?

Python: It was made in Python. I used PyInstaller. So how do you compile .py and .pyw? 


PyInstaller: You? Bro, .py and .pyw is needed for compiling. 

### 🛠️ MinGW64 Path Configuration
If clicking "BUILD EXE" in C++ mode yields a `g++ is not recognized` terminal panic, check your paths variable:
1. Hit `Win + R`, type `sysdm.cpl`, and press Enter.
2. Navigate to Advanced -> Environment Variables.
3. Under System Variables, find `Path` and click Edit.
4. Add: `C:\msys64\ucrt64\bin` (or your corresponding MinGW bin folder path).

---

## 🛠️ The Web Feature: Secure Fetch Protocol

The integrated blue **DOWNLOAD** module leverages raw HTTP requests to fetch snippets directly. Follow these ground rules to avoid breaking your builds:

1. **Verify Raw Endpoints:** Ensure your source web links end explicitly in raw text fields (e.g., `https://githubusercontent.com`).
2. **Never Fetch Pre-Compiled Files:** Do not pass an existing binary download URL into the editor box. It will attempt to wrap an `.exe` inside another `.exe`, completely corrupting the architecture.
3. **No Dynamic Payload Execution:** Avoid using `eval()` or `exec()` commands inside your code targets when pulling web lines down to remain securely under the radar of heuristic defenses.


Use Rofcoder.pyw if it returns .dll errors that are hard to remove.

Enjoy and ***BYE!!***
