import tkinter as tk
from tkinter import messagebox
import threading

def create_error():
    """Функция создает бесконечные окна с ошибками."""
    while True:
        root = tk.Tk()
        root.withdraw()  # Скрыть основное окно
        messagebox.showerror("Ошибка", "Критическая ошибка системы!")
        root.destroy()  # Уничтожить окно после закрытия

def start_attack(threads=10):
    """Запускает несколько потоков с окнами ошибок."""
    for _ in range(threads):
        threading.Thread(target=create_error, daemon=True).start()

if __name__ == "__main__":
    start_attack(threads=50)  # Запуск 50 потоков (можно увеличить)
