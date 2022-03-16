import tkinter as tk

r = tk.Tk()
r.geometry("800x450")
r.title('Website Blocker')

is_on = True

header = tk.Label (r, text="Website Blocker", font="Arial 30")
header.pack(pady=(70, 40))

url = tk.Entry(r, font=('Arial 20'), width=35)
url.insert(0, "Enter URL here...")
def some_callback(event):
    url.delete(0, "end")
    return None
url.bind("<FocusIn>", some_callback)
url.pack(pady=20)

button = tk.Button(r, text='Block!', font='Arial 15', width=30)
button.pack(pady=5)

def switch():
    global is_on
    if is_on:
        toggle.config(image = off)
        is_on = False
    else:
        toggle.config(image = on)
        is_on = True
 
on = tk.PhotoImage(file = "on.png")
off = tk.PhotoImage(file = "off.png")
toggle = tk.Button(r, image = on, bd = 0, command = switch)
toggle.pack(pady = 50)

r.mainloop()