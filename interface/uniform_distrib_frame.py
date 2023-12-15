from tkinter import ttk


class UniformDistribFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.options = {'padx': 5, 'pady': 5}
        self.min_degradation_label = ttk.Label(self, text='min')
        self.min_degradation_label.grid(row=0, column=0, **self.options)
        self.min_degradation = ttk.Entry(self, width=7)
        self.min_degradation.insert(0, '0.95')
        self.min_degradation.grid(row=0, column=1, **self.options)
        self.max_degradation_label = ttk.Label(self, text='max')
        self.max_degradation_label.grid(row=1, column=0, **self.options)
        self.max_degradation = ttk.Entry(self, width=7)
        self.max_degradation.insert(0, '1')
        self.max_degradation.grid(row=1, column=1, **self.options)
