#Python 3.9
import winreg
import time
import subprocess

RegistryKeyName = r"SYSTEM\\CurrentControlSet\\Services\\USBSTOR"


#キーに繋ぐ
RegConnection = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
#キーを開く
Key = winreg.OpenKeyEx(RegConnection,RegistryKeyName,reserved=0,access=winreg.KEY_WRITE)
#レジストリの書き換え
settings = winreg.SetValueEx(Key,"Start",0,winreg.REG_SZ,"5")
winreg.CloseKey(Key)

print ("3秒後に画面ロックされます。")
#ディレイ
time.sleep(3)
#画面ロック
subprocess.run ("rundll32.exe user32.dll,LockWorkStation")