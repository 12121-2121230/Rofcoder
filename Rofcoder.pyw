import os
import ast
import shutil
import subprocess
import time
import getpass
import urllib.request
import tkinter as tk

from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


class RofcoderStudio:

    def __init__(self, root):

        self.root = root

        self.root.title("Rofcoder")
        self.root.geometry("1200x720")
        self.root.configure(bg="#121214")
        self.root.resizable(False, False)

        self.active_user = getpass.getuser()

        self.output_dir = os.path.expanduser("~/Desktop")
        self.current_browser_dir = os.path.expanduser("~")

        self.main_font = ("Consolas", 10)
        self.bold_font = ("Consolas", 10, "bold")
        self.editor_font = ("Consolas", 11)

        # =========================================================
        # SAFE TYPE SYSTEM
        # =========================================================

        self.supported_types = {
            ".py": {
                "label": "Python (.py)",
                "mode": "compile"
            },

            ".pyw": {
                "label": "Python Windowless (.pyw)",
                "mode": "compile"
            },

            ".c": {
                "label": "C (.c)",
                "mode": "compile"
            },

            ".cpp": {
                "label": "C++ (.cpp)",
                "mode": "compile"
            },

            ".txt": {
                "label": "Text (.txt)",
                "mode": "view"
            },

            ".json": {
                "label": "JSON (.json)",
                "mode": "view"
            },

            ".html": {
                "label": "HTML (.html)",
                "mode": "view"
            },

            ".css": {
                "label": "CSS (.css)",
                "mode": "view"
            },

            ".js": {
                "label": "JavaScript (.js)",
                "mode": "view"
            },

            ".md": {
                "label": "Markdown (.md)",
                "mode": "view"
            },

            ".xml": {
                "label": "XML (.xml)",
                "mode": "view"
            },

            ".yml": {
                "label": "YAML (.yml)",
                "mode": "view"
            },

            ".yaml": {
                "label": "YAML (.yaml)",
                "mode": "view"
            }
        }

        self.blocked_extensions = {
            ".exe",
            ".dll",
            ".sys",
            ".scr",
            ".com",
            ".msi"
        }

        # =========================================================
        # LEFT PANEL
        # =========================================================

        self.left_frame = tk.Frame(
            root,
            bg="#1a1a1e",
            width=300
        )

        self.left_frame.pack(
            side=tk.LEFT,
            fill=tk.Y,
            padx=(15, 5),
            pady=15
        )

        self.left_frame.pack_propagate(False)

        tk.Label(
            self.left_frame,
            text="ROFCODER CONTROL",
            bg="#1a1a1e",
            fg="#00a2ff",
            font=("Consolas", 14, "bold")
        ).pack(anchor=tk.W, padx=15, pady=(15, 10))

        tk.Label(
            self.left_frame,
            text=f"User: {self.active_user}",
            bg="#1a1a1e",
            fg="#00ff66",
            font=self.bold_font
        ).pack(anchor=tk.W, padx=15)

        tk.Label(
            self.left_frame,
            text="TARGET TYPE",
            bg="#1a1a1e",
            fg="#aaaaaa",
            font=self.bold_font
        ).pack(anchor=tk.W, padx=15, pady=(20, 5))

        self.type_var = tk.StringVar()

        self.dropdown_values = [
            info["label"]
            for info in self.supported_types.values()
        ]

        self.type_var.set("Python (.py)")

        self.type_menu = ttk.Combobox(
            self.left_frame,
            textvariable=self.type_var,
            values=self.dropdown_values,
            state="readonly"
        )

        self.type_menu.pack(
            fill=tk.X,
            padx=15
        )

        self.compile_btn = tk.Button(
            self.left_frame,
            text="BUILD EXE ⚡",
            bg="#00a2ff",
            fg="white",
            bd=0,
            font=self.bold_font,
            cursor="hand2",
            command=self.compile_editor_text
        )

        self.compile_btn.pack(
            fill=tk.X,
            padx=15,
            pady=20,
            ipady=8
        )

        self.folder_btn = tk.Button(
            self.left_frame,
            text="SELECT OUTPUT FOLDER",
            bg="#2a2a30",
            fg="white",
            bd=0,
            font=self.bold_font,
            cursor="hand2",
            command=self.select_output_directory
        )

        self.folder_btn.pack(
            fill=tk.X,
            padx=15,
            ipady=6
        )

        # =========================================================
        # CENTER
        # =========================================================

        self.center_frame = tk.Frame(
            root,
            bg="#121214"
        )

        self.center_frame.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx=(5, 15),
            pady=15
        )

        # URL BAR

        self.url_frame = tk.Frame(
            self.center_frame,
            bg="#1a1a1e"
        )

        self.url_frame.pack(
            fill=tk.X
        )

        self.url_entry = tk.Entry(
            self.url_frame,
            bg="#121214",
            fg="white",
            insertbackground="white",
            font=self.main_font
        )

        self.url_entry.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            padx=(10, 5),
            pady=10,
            ipady=4
        )

        self.download_btn = tk.Button(
            self.url_frame,
            text="DOWNLOAD",
            bg="#00a2ff",
            fg="white",
            bd=0,
            font=self.bold_font,
            command=self.download_web_file
        )

        self.download_btn.pack(
            side=tk.RIGHT,
            padx=(5, 10),
            pady=10,
            ipady=4
        )

        # EDITOR

        self.code_editor = tk.Text(
            self.center_frame,
            bg="#0f0f11",
            fg="white",
            insertbackground="white",
            font=self.editor_font,
            padx=10,
            pady=10
        )

        self.code_editor.pack(
            fill=tk.BOTH,
            expand=True,
            pady=(5, 5)
        )

        self.code_editor.insert(
            1.0,
            "print('Hello from Rofcoder')"
        )

        self.code_editor.bind(
            "<KeyRelease>",
            self.trigger_live_validation
        )

        # VALIDATOR

        self.validator_lbl = tk.Label(
            self.center_frame,
            text="Validator ready.",
            bg="#221818",
            fg="#ffaa00",
            anchor=tk.W,
            font=self.bold_font
        )

        self.validator_lbl.pack(
            fill=tk.X
        )

        # =========================================================
        # BOTTOM
        # =========================================================

        self.bottom_frame = tk.Frame(
            self.center_frame,
            bg="#1a1a1e",
            height=220
        )

        self.bottom_frame.pack(
            fill=tk.BOTH,
            expand=False,
            pady=(10, 0)
        )

        # FILE BROWSER

        self.browser_frame = tk.Frame(
            self.bottom_frame,
            bg="#1a1a1e",
            width=300
        )

        self.browser_frame.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            padx=(10, 5),
            pady=10
        )

        self.file_listbox = tk.Listbox(
            self.browser_frame,
            bg="#121214",
            fg="white",
            font=self.main_font,
            bd=0
        )

        self.file_listbox.pack(
            fill=tk.BOTH,
            expand=True
        )

        self.file_listbox.bind(
            "<<ListboxSelect>>",
            self.on_file_browser_click
        )

        self.file_listbox.bind(
            "<Double-1>",
            self.on_file_browser_double_click
        )

        # CONSOLE

        self.console_frame = tk.Frame(
            self.bottom_frame,
            bg="#1a1a1e"
        )

        self.console_frame.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=True,
            padx=(5, 10),
            pady=10
        )

        self.console_box = tk.Text(
            self.console_frame,
            bg="#0c0c0e",
            fg="#00ff66",
            insertbackground="white",
            font=self.main_font
        )

        self.console_box.pack(
            fill=tk.BOTH,
            expand=True
        )

        self.refresh_local_file_system()

        self.log_message("System initialized.")

    # =========================================================
    # LOGGING
    # =========================================================

    def log_message(self, message):

        timestamp = time.strftime("[%H:%M:%S]")

        self.console_box.insert(
            tk.END,
            f"{timestamp} {message}\n"
        )

        self.console_box.see(tk.END)

    # =========================================================
    # OUTPUT DIRECTORY
    # =========================================================

    def select_output_directory(self):

        folder = filedialog.askdirectory(
            initialdir=self.output_dir
        )

        if folder:

            self.output_dir = folder

            self.log_message(
                f"Output directory -> {folder}"
            )

    # =========================================================
    # VALIDATOR
    # =========================================================

    def trigger_live_validation(self, event=None):

        code = self.code_editor.get(1.0, tk.END)

        selected = self.type_var.get()

        if "Python" in selected:

            try:

                ast.parse(code)

                self.validator_lbl.config(
                    text="✅ Python syntax valid.",
                    fg="#00ff66"
                )

            except SyntaxError as e:

                self.validator_lbl.config(
                    text=f"❌ Line {e.lineno}: {e.msg}",
                    fg="#ff4444"
                )

        else:

            self.validator_lbl.config(
                text="Validator active.",
                fg="#ffaa00"
            )

    # =========================================================
    # COMPILER
    # =========================================================

    def compile_editor_text(self):

        selected_type = self.type_var.get()

        extension_map = {
            info["label"]: ext
            for ext, info in self.supported_types.items()
        }

        ext = extension_map.get(selected_type)

        if not ext:

            messagebox.showerror(
                "Unknown Type",
                selected_type
            )

            return

        if self.supported_types[ext]["mode"] != "compile":

            messagebox.showwarning(
                "View Only",
                f"{selected_type} cannot compile."
            )

            return

        code_content = self.code_editor.get(
            1.0,
            tk.END
        )

        if not code_content.strip():

            messagebox.showwarning(
                "Empty Editor",
                "No source code detected."
            )

            return

        output_exe = filedialog.asksaveasfilename(
            initialdir=self.output_dir,
            title="Build EXE",
            filetypes=[
                ("Windows Executable", "*.exe")
            ],
            defaultextension=".exe"
        )

        if not output_exe:
            return

        if not output_exe.lower().endswith(".exe"):
            output_exe += ".exe"

        temp_dir = os.getenv("TEMP")

        temp_src = os.path.join(
            temp_dir,
            f"_rofcoder_temp{ext}"
        )

        with open(
            temp_src,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(code_content)

        try:

            # =====================================================
            # PYTHON
            # =====================================================

            if ext in [".py", ".pyw"]:

                try:
                    ast.parse(code_content)

                except SyntaxError as e:

                    messagebox.showerror(
                        "Syntax Error",
                        f"Line {e.lineno}: {e.msg}"
                    )

                    return

                noconsole = ""

                if ext == ".pyw":
                    noconsole = "--noconsole"

                # FIXED: Added [0] index to resolve tuple string conversion crash
                cmd = (
                    f'pyinstaller --onefile {noconsole} '
                    f'--distpath "{os.path.dirname(output_exe)}" '
                    f'--name "{os.path.splitext(os.path.basename(output_exe))[0]}" '
                    f'"{temp_src}"'
                )

            # =====================================================
            # C
            # =====================================================

            elif ext == ".c":

                cmd = (
                    f'gcc "{temp_src}" '
                    f'-o "{output_exe}"'
                )

            # =====================================================
            # C++
            # =====================================================

            elif ext == ".cpp":

                cmd = (
                    f'g++ "{temp_src}" '
                    f'-o "{output_exe}"'
                )

            else:

                messagebox.showerror(
                    "Unsupported Compiler",
                    ext
                )

                return

            self.log_message(f"RUNNING: {cmd}")

            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                shell=True
            )

            if result.returncode == 0:

                self.log_message(
                    f"SUCCESS -> {output_exe}"
                )

                messagebox.showinfo(
                    "Build Complete",
                    f"EXE created:\n{output_exe}"
                )

            else:

                self.log_message(result.stderr)

                messagebox.showerror(
                    "Build Failed",
                    result.stderr
                )

        finally:

            if os.path.exists(temp_src):
                os.remove(temp_src)

    # =========================================================
    # DOWNLOAD
    # =========================================================

    def download_web_file(self):

        url = self.url_entry.get().strip()

        if not url.startswith(("http://", "https://")):

            messagebox.showwarning(
                "Invalid URL",
                "Enter a valid URL."
            )

            return

        try:

            request = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

            with urllib.request.urlopen(request) as response:

                raw = response.read()

            content = raw.decode(
                "utf-8",
                errors="replace"
            )

            self.code_editor.delete(
                1.0,
                tk.END
            )

            self.code_editor.insert(
                1.0,
                content
            )

            # FIXED: Added [1] index extraction to properly extract extension string string mapping
            ext = os.path.splitext(url)[1].lower()

            if ext in self.supported_types:

                self.type_var.set(
                    self.supported_types[ext]["label"]
                )

            self.log_message(
                f"Downloaded -> {url}"
            )

            self.trigger_live_validation()

        except Exception as e:

            self.log_message(str(e))

    # =========================================================
    # FILE BROWSER
    # =========================================================

    def refresh_local_file_system(self):

        self.file_listbox.delete(0, tk.END)

        try:

            for item in os.listdir(self.current_browser_dir):

                full = os.path.join(
                    self.current_browser_dir,
                    item
                )

                if os.path.isdir(full):

                    self.file_listbox.insert(
                        tk.END,
                        f"📁 {item}"
                    )

                else:

                    self.file_listbox.insert(
                        tk.END,
                        f"📄 {item}"
                    )

        except Exception:

            self.file_listbox.insert(
                tk.END,
                "Access denied."
            )

    def on_file_browser_click(self, event):

        if not self.file_listbox.curselection():
            return

        selection = self.file_listbox.get(
            self.file_listbox.curselection()
        )

        if "📄 " not in selection:
            return

        filename = selection.replace("📄 ", "")

        full_path = os.path.join(
            self.current_browser_dir,
            filename
        )

        ext = os.path.splitext(filename)[1].lower()

        if ext in self.blocked_extensions:

            self.code_editor.delete(
                1.0,
                tk.END
            )

            self.code_editor.insert(
                1.0,
                "[BLOCKED EXECUTABLE FILE]"
            )

            self.log_message(
                f"Blocked executable -> {filename}"
            )

            return

        try:

            with open(full_path, "rb") as f:
                header = f.read(1024)

            if b"\x00" in header and ext not in self.supported_types:

                self.code_editor.delete(
                    1.0,
                    tk.END
                )

                self.code_editor.insert(
                    1.0,
                    "[BINARY FILE DETECTED]"
                )

                return

            with open(
                full_path,
                "r",
                encoding="utf-8",
                errors="replace"
            ) as f:

                content = f.read()

            self.code_editor.delete(
                1.0,
                tk.END
            )

            self.code_editor.insert(
                1.0,
                content
            )

            if ext in self.supported_types:

                self.type_var.set(
                    self.supported_types[ext]["label"]
                )

            self.trigger_live_validation()

        except Exception as e:

            self.log_message(str(e))

    def on_file_browser_double_click(self, event):

        selection = self.file_listbox.curselection()

        if not selection:
            return

        selected = self.file_listbox.get(selection)

        if "📁 " in selected:

            folder = selected.replace("📁 ", "")

            self.current_browser_dir = os.path.join(
                self.current_browser_dir,
                folder
            )

            self.refresh_local_file_system()

            self.log_message(
                f"Entered folder -> {folder}"
            )


if __name__ == "__main__":

    root = tk.Tk()

    app = RofcoderStudio(root)

    root.mainloop()
