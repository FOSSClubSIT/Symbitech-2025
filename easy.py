# Currently, both the blue rectangle and the red circle are drawn on top of each other.
# To achieve the goal of revealing the red circle while keeping the blue rectangle visible:
# Think about how you can adjust the order of the shapes, or their visibility.

import tkinter as tk

window = tk.Tk()
window.title("Layered Shapes")
window.geometry("400x400")

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

canvas.create_rectangle(50, 50, 350, 150, fill="blue")
canvas.create_oval(100, 100, 300, 300, fill="red")

window.mainloop()   
