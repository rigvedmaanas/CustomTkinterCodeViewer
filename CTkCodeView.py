from customtkinter import CTkTextbox
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name, get_all_styles

class CTkCodeViewer(CTkTextbox):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 code=None,
                 allow_selecting=True,
                 language="python",
                 theme="monokai",
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self._monokai_style = get_style_by_name(theme)
        self._style_parsed = self._monokai_style.list_styles()
        for key in self._style_parsed:
            if key[1]["color"] != "" and key[1]["color"] != None:
                color = "#" + key[1]["color"]
                self.tag_config(str(key[0]), foreground=color)
        if code != None:
            self._add_code(code, language)
            if allow_selecting:
                self.bind("<Key>", lambda e: "break")
            else:
                self.configure(state="disabled")

    def _add_code(self, code, language):
        lexer = get_lexer_by_name(language, stripall=True)
        tokens = list(lexer.get_tokens(code))

        for text in tokens:
            self.insert("end", text[1], str(text[0]))

    def allstyles(self):
        return list(get_all_styles())
