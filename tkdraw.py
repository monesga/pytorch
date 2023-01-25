import tkinter as tk

brush_width = 3

def paint(event):
    x1, y1 = (event.x - brush_width), (event.y - brush_width)
    x2, y2 = (event.x + brush_width), (event.y + brush_width)
    canvas.create_oval(x1, y1, x2, y2, fill="black")

root = tk.Tk()
root.title("Drawing Program")

canvas = tk.Canvas(root, bg="white", width=400, height=400)
canvas.pack()

canvas.bind("<B1-Motion>", paint)

root.mainloop()
