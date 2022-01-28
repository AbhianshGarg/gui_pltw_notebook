from tkinter import * 

root = Tk()

canvas = Canvas(width=175, height=200)
canvas.create_rectangle(0, 0, 100, 100, fill='blue')
canvas.create_rectangle(000, 100, 100, 200, fill='red')
canvas.create_rectangle(100, 000, 175, 100, fill='green')
canvas.create_rectangle(100, 100, 175, 200, fill='yellow')
canvas.pack()

canvas.mainloop()