import tkinter as tk
from tkinter import ttk
from interface.calc_frame import CalcFrame
from interface.experiment_frame import ExperimentFrame


class ControlFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.calc_button = ttk.Label(self, text='Расчет')
        self.calc_button.grid(column=0, row=0, padx=5, pady=5)
        self.calc_button.bind('<Button-1>', lambda event: self.change_frame(0))
        self.calc_button.bind("<Enter>", lambda event: self.calc_button.config(cursor="hand2"))

        self.experiment_button = ttk.Label(self, text='Эксперимент')
        self.experiment_button.grid(column=1, row=0, padx=5, pady=5)
        self.experiment_button.bind('<Button-1>', lambda event: self.change_frame(1))
        self.experiment_button.bind("<Enter>", lambda event: self.experiment_button.config(cursor="hand2"))

        self.grid(row=0, column=0, sticky=tk.EW)

        self.frames = [
            CalcFrame(container),
            ExperimentFrame(container)
        ]
        self.change_frame(0)

    def change_frame(self, new_frame_ind: int):
        cur_frame = self.frames[1 - new_frame_ind]
        cur_frame.grid_remove()

        new_frame = self.frames[new_frame_ind]
        new_frame.grid()

