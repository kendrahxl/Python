### Label Widget - Example ###

import tkinter as tk
root = tk.Tk()
root.title("Hello World")
root.geometry("600x400")
root.resizable(True, True)

label = tk.Label(root,
                 text = "Hello World!",
                 font = ("Times New Roman", 24),
                 bg = "yellow", fg = "green",
                 padx = 15, pady = 15,
                 relief = tk.RAISED,
                 borderwidth = 20,
                 anchor = tk.CENTER,
                 cursor = "box_spiral",
                 wraplength = 150)
label.pack(pady = 20)

root.mainloop()
