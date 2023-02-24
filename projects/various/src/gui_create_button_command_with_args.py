from functools import partial
import tkinter as tk
from tkinter import messagebox


def btn_clicked(text):
    messagebox.showinfo(title='Image path', message=text)


image_paths = ["V:/repos/uploads/movies_lib_explorer/2_movie_alien_ridley scott.png",
               "V:/repos/uploads/movies_lib_explorer/2_movie_Manhattan_Woody Allen.png",
               "V:/repos/uploads/movies_lib_explorer/2_movie_To Have and Have Not_Howard Hawks.png"]
images = []
buttons = []

root = tk.Tk()
root.title("Example How to call button command with parameters")
root.geometry("1400x900")

x_pos = 75
for image_path in image_paths:
    img = tk.PhotoImage(file=image_path)
    button = tk.Button(image=img, borderwidth=0, highlightthickness=0,
                       command=partial(btn_clicked, image_path), relief="flat")
    button.place(x=x_pos, y=520, width=390, height=180)
    x_pos += 400
    images += [img]
    buttons += [button]

root.mainloop()
