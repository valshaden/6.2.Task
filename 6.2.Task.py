# 6.2. Задание
## Добавьте проверку корректности введённого времени в программу напоминаний. 
## Программа должна сообщать пользователю что он не должен вводить время 
## с часами меньше 0 и больше 23, и минутами больше 59 и меньше 0.

# Код программы.

from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time

t = None
music = False  # Переменная для отслеживания проигрывания музыки

def set():
    global t
    ##rem = sd.askstring("Время напоминания", "Введите время в формате ЧЧ:ММ (24-часовой формат)")
    rem = sd.askstring("Время напоминания", "Введите время в формате ЧЧ:ММ (24-часовой формат)\n"+
                       "               часы от 0 и до 23, минуты от 0 и до 59                ")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            t = dt.timestamp()
            label.config(text=f"Напоминание установлено на: {hour:02}:{minute:02}")
        except ValueError:
            mb.showerror("Ошибка", "Неверный формат времени")
            mb.showinfo("Обратите внимание", "часы от 0 и до 23\nминуты от 0 и до 59\nразделитель - знак :")

def check():
    global t
    if t:
###        now = time.time() # Строчка из задания
        now = datetime.datetime.now()
        print(f"now={now}")
        dt = now.replace(second=0, microsecond=0)
        print(f" dt={dt}\n")
        now = dt.timestamp()
        #print(f"now1={now1}")
        #print(f"now2={now2}")
        print(f"  t={t}")
        print(f"now={now}")
        
###        if now >= t:  # Строчка из задания
        if now == t:  # так правильно
            mb.showinfo("Напоминание", "Время напоминания наступило!")
            play_snd()
            t = None
    window.after(10000, check)

def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()

def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text="Установить новое напоминание")

window = Tk()
window.title("Напоминание")

label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку", command=stop_music)
stop_button.pack(pady=5)

check()

window.mainloop()