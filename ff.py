import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk

def draw_heart(size, color):
    # Создаем изображение
    img = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Рисуем сердце
    draw.polygon([(size[0]/2, size[1]), (0, size[1]/4),
                  (size[0]/4, 0), (size[0]/2, size[1]/6),
                  (size[0]*3/4, 0), (size[0], size[1]/4)], fill=color)

    # Преобразуем изображение для tkinter
    return ImageTk.PhotoImage(img)

def increment_age():
    global age
    age += 1
    year_label.config(text=f"Год: {start_year + age}")
    chat_box.insert(tk.END, f"Вы прожили {age} год\n")
    if age == 1:
        # Создаем окно с двумя кнопками "Плакать" и "Молчать"
        vaccination_window = tk.Toplevel(root)
        vaccination_window.title("Вакцинация")
        vaccination_window.geometry("300x100")
        
        def cry():
            vaccination_window.destroy()
            chat_box.insert(tk.END, "Вы плакали во время вакцинации, но вас вакцинировали.\n")
            chat_box.insert(tk.END, "В стране началась война.\n")
        def silent():
            vaccination_window.destroy()
            chat_box.insert(tk.END, "Вы промолчали во время вакцинации и вас успешно вакцинировали.\n")
            chat_box.insert(tk.END, "В стране началась война.\n")
            

        cry_button = tk.Button(vaccination_window, text="Плакать", command=cry)
        cry_button.pack(side=tk.LEFT, padx=10, pady=10)

        silent_button = tk.Button(vaccination_window, text="Молчать", command=silent)
        silent_button.pack(side=tk.RIGHT, padx=10, pady=10)

    elif age == 6:
        messagebox.showinfo("Школа", "Вы пошли в школу.")
        chat_box.insert(tk.END, "Вы пошли в школу.\n")

# Создаем основное окно
root = tk.Tk()
root.title("Жизнь Натали")

# Устанавливаем размеры окна
root.geometry("800x600")

# Создаем изображение сердца
heart_img = draw_heart((50, 50), "red")

# Создаем рамку для кнопки
frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM)

# Создаем круглую кнопку с изображением сердца
heart_button = tk.Button(frame, image=heart_img, bd=0, bg='white', command=increment_age)
heart_button.pack(pady=20)

# Создаем чат для вывода сообщений
chat_box = tk.Text(root, width=80, height=40)
chat_box.pack(pady=20)

# Добавляем информацию о персонаже
chat_box.insert(tk.END, "Вы родились в Украине. Ваши родители Ольга и Николай назвали вас Наталией.\n")

# Создаем метку для отображения года
start_year = 2022
year_label = tk.Label(root, text=f"Год: {start_year}", font=("Arial", 8))
year_label.place(x=10, y=10)

# Инициализируем возраст
age = 0

# Запускаем главный цикл обработки событий
root.mainloop()
