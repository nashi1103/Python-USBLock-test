#Python 3.9
import winreg

RegistryKeyName = r"SYSTEM\\CurrentControlSet\\Services\\USBSTOR"

try:
#キーに繋ぐ
    RegConnection = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
#キーを開く
    Key = winreg.OpenKeyEx(RegConnection,RegistryKeyName,reserved=0,access=winreg.KEY_WRITE)
#レジストリの書き換え
    settings = winreg.SetValueEx(Key,"Start",0,winreg.REG_DWORD,3)
    winreg.CloseKey(Key)
    print("USBロックが解除されました。")
except:
    print("正常に動作しませんでした。")