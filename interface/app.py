import tkinter as tk
from ttkthemes import ThemedStyle


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = 400
        self.y = 400

        self.title('Свекла')
        self.geometry(f'{self.x}x{self.y}+{(self.screen_width - self.x) // 2}+{(self.screen_height - self.y) // 2}')
        self.style = ThemedStyle(self)
        self.style.set_theme('black')
        self.configure(bg=self.style.lookup('TFrame', 'background'))


