from tkinter import ttk
import tkinter as tk
from experiment import experiment
import algorithms as alg


class ExperimentFrame(ttk.Frame):
    algorithms = [
        alg.Algorithm('Венгерский мин', alg.hungarian_min),
        alg.Algorithm('Венгерский макс', alg.hungarian_max),
        alg.Algorithm('Жадный', alg.greedy_max),
        alg.Algorithm('Бережливый', alg.greedy_min),
        alg.Algorithm('Жадно-бережливый', alg.greedy_thrifty),
        alg.Algorithm('Бережливо-жадный', alg.thrifty_greedy)
    ]

    def __init__(self, container):
        super().__init__(container)

        self.grid(row=1, column=0)
        self.options = {'padx': 5, 'pady': 5}

        self.num_variety_label = ttk.Label(self, text='Количество сортов свеклы')
        self.num_variety_label.grid(row=0, column=0, **self.options)
        self.num_variety = ttk.Entry(self, width=7)
        self.num_variety.insert(0, '20')
        self.num_variety.grid(row=0, column=1, **self.options)

        self.sugar_content_label = ttk.Label(self, text='Диапазон сахаристости до переработки:')
        self.sugar_content_label.grid(row=1, column=0, **self.options)
        self.min_sugar_content_label = ttk.Label(self, text='min')
        self.min_sugar_content_label.grid(row=2, column=0, **self.options)
        self.min_sugar_content = ttk.Entry(self, width=7)
        self.min_sugar_content.insert(0, '0.1')
        self.min_sugar_content.grid(row=2, column=1, **self.options)
        self.max_sugar_content_label = ttk.Label(self, text='max')
        self.max_sugar_content_label.grid(row=3, column=0, **self.options)
        self.max_sugar_content = ttk.Entry(self, width=7)
        self.max_sugar_content.insert(0, '0.11')
        self.max_sugar_content.grid(row=3, column=1, **self.options)

        self.degradation_label = ttk.Label(self, text='Диапазон деградации:')
        self.degradation_label.grid(row=4, column=0, **self.options)
        self.min_degradation_label = ttk.Label(self, text='min')
        self.min_degradation_label.grid(row=5, column=0, **self.options)
        self.min_degradation = ttk.Entry(self, width=7)
        self.min_degradation.insert(0, '0.95')
        self.min_degradation.grid(row=5, column=1, **self.options)
        self.max_degradation_label = ttk.Label(self, text='max')
        self.max_degradation_label.grid(row=6, column=0, **self.options)
        self.max_degradation = ttk.Entry(self, width=7)
        self.max_degradation.insert(0, '1')
        self.max_degradation.grid(row=6, column=1, **self.options)

        self.inorganic_influence_check = tk.IntVar()
        self.inorganic_influence_label = ttk.Label(self, text='Учитывать влияние неорганики')
        self.inorganic_influence_label.grid(row=7, column=0, **self.options)
        self.inorganic_influence = ttk.Checkbutton(self, variable=self.inorganic_influence_check)
        self.inorganic_influence.grid(row=7, column=1, **self.options)

        self.num_experiments_label = ttk.Label(self, text='Количество экспериментов')
        self.num_experiments_label.grid(row=8, column=0, **self.options)
        self.num_experiments = ttk.Entry(self, width=7)
        self.num_experiments.insert(0, '50')
        self.num_experiments.grid(row=8, column=1, **self.options)

        self.calculate_button = ttk.Button(self, text='Рассчитать', command=self.run_experiment)
        self.calculate_button.grid(row=9, column=0, **self.options, sticky=tk.E)

    def run_experiment(self):
        n = int(self.num_variety.get())
        t = int(self.num_experiments.get())
        min_a = float(self.min_sugar_content.get())
        max_a = float(self.max_sugar_content.get())
        min_b = float(self.min_degradation.get())
        max_b = float(self.max_degradation.get())
        inorganic_res = False
        if self.inorganic_influence_check.get():
            inorganic_res = True
        experiment(n, t, min_a, max_a, min_b, max_b, self.algorithms, inorganic_res)
