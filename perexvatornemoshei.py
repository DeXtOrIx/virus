import keyboard
import mouse
import threading
import time

def block_keyboard():
    """Перехватывает и блокирует все клавиши."""
    while True:
        event = keyboard.read_event(suppress=True)  # Перехватывает и блокирует клавиши
        print(f"Блокирована клавиша: {event.name}")

def block_mouse():
    """Перехватывает и блокирует клики мыши."""
    while True:
        mouse.on_click(lambda event: False)  # Блокируем клики
        mouse.on_right_click(lambda event: False)  # Блокируем ПКМ
        mouse.on_middle_click(lambda event: False)  # Блокируем СКМ
        mouse.on_wheel(lambda event: False)  # Блокируем прокрутку
        time.sleep(0.1)

# Запускаем блокировщики в отдельных потоках
threading.Thread(target=block_keyboard, daemon=True).start()
threading.Thread(target=block_mouse, daemon=True).start()

# Бесконечный цикл, чтобы программа не закрывалась
while True:
    time.sleep(1)
