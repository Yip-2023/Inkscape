#Yazan chat gpt
#Düzenleyen Yiğit çıtak

import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            content = text.get("1.0", tk.END)
            file.write(content)

root = tk.Tk()
root.title("Konsol Y - Simple Text Editor")

text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
text.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Yeni", command=new_file)
file_menu.add_command(label="Aç", command=open_file)
file_menu.add_command(label="Kaydet", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Çıkış", command=root.quit)
menu_bar.add_cascade(label="Dosya", menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()

