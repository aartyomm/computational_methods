from tkinter import ttk


class NormalDistribFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.options = {'padx': 5, 'pady': 5}

        self.avg_degradation_label = ttk.Label(self, text='Среднее значение:')
        self.avg_degradation_label.grid(row=0, column=0, **self.options)
        self.avg_degradation = ttk.Entry(self, width=7)
        self.avg_degradation.insert(0, '0.5')
        self.avg_degradation.grid(row=0, column=1, **self.options)

        self.deviation_degradation_label = ttk.Label(self, text='Отклонение:')
        self.deviation_degradation_label.grid(row=1, column=0, **self.options)
        self.deviation_degradation = ttk.Entry(self, width=7)
        self.deviation_degradation.insert(0, '0.1')
        self.deviation_degradation.grid(row=1, column=1, **self.options)
