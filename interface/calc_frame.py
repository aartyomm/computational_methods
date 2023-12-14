from tkinter import ttk
import tkinter as tk
import algorithms as alg
import numpy as np
from experiment import reset_ans, run_algorithms
from graph import show_graph


class CalcFrame(ttk.Frame):
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

        self.start_frame = ttk.Frame(self)
        self.start_frame.grid(row=1, column=0, sticky=tk.W)
        self.options = {'padx': 5, 'pady': 5}
        self.matrix_cells = []
        self.matrix_frame = None
        self.n = 0

        self.num_variety_label = ttk.Label(self.start_frame, text='Количество сортов свеклы')
        self.num_variety_label.grid(row=0, column=0, **self.options)
        self.num_variety = ttk.Entry(self.start_frame, width=7)
        self.num_variety.grid(row=0, column=1, **self.options)
        self.num_variety_button = ttk.Button(self.start_frame, text='Ввести', command=self.generate_matrix)
        self.num_variety_button.grid(row=0, column=2, **self.options)

    def generate_matrix(self):
        self.n = int(self.num_variety.get())
        if self.matrix_frame:
            self.matrix_frame.destroy()
        self.matrix_frame = ttk.Frame(self)
        self.matrix_frame.grid(row=2, column=0, sticky=tk.W)

        self.matrix_cells = [[ttk.Entry(self.matrix_frame, width=5) for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                self.matrix_cells[i][j].grid(row=i + 1, column=j + 1, **self.options)

        ttk.Button(self.matrix_frame, text='Рассчитать', command=self.calculate
                   ).grid(row=self.n+1, column=1, columnspan=self.n)
        ttk.Label(self.matrix_frame, text='Сорт').grid(row=0, column=self.n // 2)
        ttk.Label(self.matrix_frame, text='Дни').grid(row=self.n // 2, column=0)

    def calculate(self):
        matrix = [[0.0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                matrix[i][j] = float(self.matrix_cells[i][j].get())

        reset_ans(self.algorithms, self.n)
        run_algorithms(self.algorithms, np.matrix(np.array(matrix)), self.n)
        for algorithm in self.algorithms:
            for i in range(1, self.n):
                algorithm.ans[i] += algorithm.ans[i - 1]

        show_graph(self.algorithms)



