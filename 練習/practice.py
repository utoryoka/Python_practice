import tkinter as tk
import random
def dispLabel():
    # lbl.configure(text="こんにちは")
    kuji = ["大吉","中吉","小吉","凶"]
    lbl.configure(text=random.choice(kuji))

root = tk.Tk()
root.geometry("200x100")
lbl = tk.Label(text="Label")
btn = tk.Button(text="PUSH",command=dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()