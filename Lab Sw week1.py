from tkinter import *
textvariable = Tk()
textvariable.option_add("*Font", "consolas 20")
Label(textvariable, text="Lab1", bg="green").pack(fill=X)
Label(textvariable, text="Software Lab", bg="deep sky blue").pack(fill=X)
Label(textvariable, text="Just be yourself, because life’s too short to be anybody else.",
bg="gold").pack(fill=X)
Label(textvariable, text="Just be yourself, because life’s too short to be anybody else.",
bg="orange", wraplength=700, justify=RIGHT).pack(fill=X)
Label(textvariable, text="Just be yourself, because life’s too short to be anybody else.",
bg="deep sky blue", wraplength=1000, justify=RIGHT).pack(fill=X)
Label(textvariable, text="Just be yourself, because life’s too short to be anybody else.",
bg="hot pink", wraplength=1000, justify=RIGHT).pack(fill=X)
Label(textvariable, text="",bg="hot pink").pack(fill=X)
Label(textvariable, text="Step Up 2:The Streets",bg="hot pink").pack(fill=X)
textvariable.mainloop()