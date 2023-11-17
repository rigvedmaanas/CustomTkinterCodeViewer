# CustomTkinter CodeViewer
This is a package for displaying code with syntax highlighting in a customtkinter application

![CTkCodeViewer](https://github.com/rigvedmaanas/CustomTkinterCodeViewer/assets/77579661/725c765f-b01e-4da4-b0ba-e0f6a441854d)


# Example

```python
codeviewer = CTkCodeViewer(root, code=code, language="python", theme="monokai")
```

# Arguments
| Argument | Value |
|---------|-------|
| root | root, tkinter.Frame or CTkFrame |
| width | textbox width in px |
| height | textbox height in px |
| code | code to display |
| allow_selecting | allow users to select or not (True or False)|
| language | the language given (default = "python"). This supports all the languages available in pygments|
| theme | theme of the syntax highlighting (default = "monokai"). This supports all the themes available in pygments|

# Methods
- .allstyles()
  
  returns all the available themes

