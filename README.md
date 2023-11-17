# CustomTkinter CodeViewer
This is a small package for displaying code in a customtkinter application

![CTkCodeViewer](https://github.com/rigvedmaanas/CustomTkinterCodeViewer/assets/77579661/725c765f-b01e-4da4-b0ba-e0f6a441854d)


# Example

```python
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
```

# Methods
- .allstyles()
  returns all the available themes

