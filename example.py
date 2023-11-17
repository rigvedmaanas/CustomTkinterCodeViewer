from CTkCodeView import CTkCodeViewer
from customtkinter import *

root = CTk()
root.geometry("1000x1000")
root.title("CTkCodeView")

with open("CTkCodeView.py", "r") as f:
    code = f.read()

codeviewer = CTkCodeViewer(root, code=code, language="python", theme="monokai")
codeviewer.pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()