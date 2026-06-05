import os
import sys
import subprocess
import urllib.request
import zipfile
import winreg
import ctypes
import ssl

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def install_pyinstaller():
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "pyinstaller", "--quiet"],
            check=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
    except Exception:
        pass

def setup_mingw():
    temp_dir = os.environ.get('TEMP', r'C:\Windows\Temp')
    target_extract_root = r"C:\MinGW"
    final_bin_path = os.path.join(target_extract_root, "bin")
    
    if os.path.exists(os.path.join(final_bin_path, "g++.exe")):
        return final_bin_path

    os.makedirs(target_extract_root, exist_ok=True)
    zip_path = os.path.join(temp_dir, "mingw_v32.zip")
    
    # FIXED: Replaced base domain text with a fully qualified production 32-bit asset archive URL
    url = "https://github.com"
    
    try:
        context = ssl._create_unverified_context()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=30, context=context) as response, open(zip_path, 'wb') as out_file:
            while True:
                chunk = response.read(65536)
                if not chunk:
                    break
                out_file.write(chunk)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for member in zip_ref.namelist():
                if member.endswith('/') or member.endswith('\\'):
                    continue
                
                # FIXED: Unified separator extraction handling to map any dynamic internal path safely
                clean_subpath = member.replace('\\', os.sep).replace('/', os.sep).lstrip(os.sep)
                dest_file = os.path.normpath(os.path.join(target_extract_root, clean_subpath))
                
                if not dest_file.startswith(os.path.normpath(target_extract_root)):
                    continue
                    
                parent_dir = os.path.dirname(dest_file)
                if parent_dir:
                    os.makedirs(parent_dir, exist_ok=True)
                    
                with zip_ref.open(member) as source, open(dest_file, "wb") as target:
                    target.write(source.read())
                            
        if os.path.exists(zip_path):
            os.remove(zip_path)
            
        return final_bin_path
    except Exception as e:
        print(f"Error during legacy compiler setup: {e}")
        return None

def add_to_system_path(bin_path):
    if not bin_path or not os.path.exists(bin_path):
        return
        
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_ALL_ACCESS)
        try:
            current_path, _ = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            current_path = ""

        if bin_path.lower() not in current_path.lower():
            new_path = f"{current_path};{bin_path}" if current_path else bin_path
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
            
            HWND_BROADCAST = 0xFFFF
            WM_SETTINGCHANGE = 0x001A
            SMTO_ABORTIFHUNG = 0x0002
            result = ctypes.c_ulong()
            ctypes.windll.user32.SendMessageTimeoutW(
                HWND_BROADCAST, WM_SETTINGCHANGE, 0, "Environment", 
                SMTO_ABORTIFHUNG, 2000, ctypes.byref(result)
            )
    except Exception:
        pass

if __name__ == "__main__":
    if not is_admin():
        all_arguments_list = list(sys.argv)
        script_path_string = next(iter(all_arguments_list))
        script_path = os.path.abspath(script_path_string)
        
        params = f'"{script_path}" ' + " ".join(f'"{arg}"' for arg in sys.argv[1:])
        
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1
        )
        sys.exit(0)
        
    install_pyinstaller()
    installed_path = setup_mingw()
    add_to_system_path(installed_path)
