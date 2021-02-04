#Python 3.9
import winreg
import time
import subprocess

RegistryKeyName = r"SYSTEM\\CurrentControlSet\\Services\\USBSTOR"

try:
#キーに繋ぐ
    RegConnection = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
#キーを開く
    Key = winreg.OpenKeyEx(RegConnection,RegistryKeyName,reserved=0,access=winreg.KEY_WRITE)
#レジストリの書き換え
    settings = winreg.SetValueEx(Key,"Start",0,winreg.REG_DWORD,4)
    winreg.CloseKey(Key)
    
    print("USBポートがロックされました。")
    print("3秒後に画面がロックされます。")

    time.sleep(3)

    subprocess.run("rundll32.exe user32.dll,LockWorkStation")
except:
    print("正常に動作しませんでした。")