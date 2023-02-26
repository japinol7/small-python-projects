from functools import partial
import os
import tkinter as tk
from tkinter import messagebox

IM_FOLDER_PATH = os.path.join('..', 'res', 'im')
IM_WITH = 300
IM_HEIGHT = 440


def btn_clicked(text):
    messagebox.showinfo(title='Image path', message=text)


def main():
    image_paths = [
        os.path.join(IM_FOLDER_PATH, 'movie_alien_ridley scott.png'),
        os.path.join(IM_FOLDER_PATH, 'movie_Manhattan_Woody Allen.png'),
        os.path.join(IM_FOLDER_PATH, 'movie_Ran_Akira_Kurosawa_1985.png'),
        os.path.join(IM_FOLDER_PATH, 'movie_To Have and Have Not_Howard Hawks.png'),
    ]
    images = []
    buttons = []

    root = tk.Tk()
    root.title("Example How to call button command with parameters")
    root.geometry("1400x780")

    x_pos = 25
    for image_path in image_paths:
        img = tk.PhotoImage(file=image_path)
        button = tk.Button(image=img, borderwidth=0, highlightthickness=0,
                           command=partial(btn_clicked, image_path), relief="flat")
        button.place(x=x_pos, y=150, width=IM_WITH, height=IM_HEIGHT)
        x_pos += IM_WITH + 50
        images += [img]
        buttons += [button]

    root.mainloop()


if __name__ == '__main__':
    main()
