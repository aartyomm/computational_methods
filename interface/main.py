from app import App
from control_frame import ControlFrame

if __name__ == '__main__':
    app = App()
    ControlFrame(app)
    app.mainloop()




# class BeetProcessing:
#     root = tk.Tk()
#     algorithms = [
#         alg.Algorithm('Венгерский мин', alg.hungarian_min),
#         alg.Algorithm('Венгерский макс', alg.hungarian_max),
#         alg.Algorithm('Жадный', alg.greedy_max),
#         alg.Algorithm('Бережливый', alg.greedy_min)
#     ]
#
#     def __init__(self):
#         frame1 = tk.Frame(self.root, width=200, height=200)
#         frame2 = tk.Frame(self.root, width=200, height=200)
#         frame1.pack()
#         frame2.pack()
#         frame2.tkraise()
#         lbl = tk.Label(frame1, text='ЧТОТО')
#         lbl.pack()
#         btn = tk.Button(text='1', command=lambda: [frame2.pack_forget(), frame1.pack()])
#         btn.pack()
#         btn2 = tk.Button(text='2', command=lambda: [frame1.pack_forget(), frame2.pack()])
#         btn2.pack()
#
#         # self.create_interface()
#         # self.show_interface()
#         self.root.mainloop()
#
#     def create_interface(self):
#         default = tk.StringVar
#         self.num_variety_label = tk.Label(self.root, text='Количество сортов свеклы')
#         self.num_variety = tk.Entry(self.root, textvariable=default(value='20'))
#
#         self.sugar_content_label = tk.Label(self.root, text='Диапазон сахаристости до переработки:')
#         self.min_sugar_content_label = tk.Label(self.root, text='min')
#         self.min_sugar_content = tk.Entry(self.root, textvariable=default(value='0.1'))
#         self.max_sugar_content_label = tk.Label(self.root, text='max')
#         self.max_sugar_content = tk.Entry(self.root, textvariable=default(value='0.11'))
#
#         self.degradation_label = tk.Label(self.root, text='Диапазон деградации:')
#         self.min_degradation_label = tk.Label(self.root, text='min')
#         self.min_degradation = tk.Entry(self.root, textvariable=default(value='0.95'))
#         self.max_degradation_label = tk.Label(self.root, text='max')
#         self.max_degradation = tk.Entry(self.root, textvariable=default(value='1'))
#
#         self.inorganic_influence_label = tk.Label(self.root, text='Учитывать влияние неорганики')
#         self.inorganic_influence = tk.Checkbutton(self.root)
#
#         self.num_experiments_label = tk.Label(self.root, text='Количество экспериментов')
#         self.num_experiments = tk.Entry(self.root, textvariable=default(value='50'))
#
#         self.calculate_button = tk.Button(self.root, text='Рассчитать', command=self.run_experiment)
#
#     def show_interface(self):
#         self.num_variety_label.pack()
#         self.num_variety.pack()
#         self.sugar_content_label.pack()
#         self.min_sugar_content_label.pack()
#         self.min_sugar_content.pack()
#         self.max_sugar_content_label.pack()
#         self.max_sugar_content.pack()
#
#         self.degradation_label.pack()
#         self.min_degradation_label.pack()
#         self.min_degradation.pack()
#         self.max_degradation_label.pack()
#         self.max_degradation.pack()
#
#         self.inorganic_influence_label.pack()
#         self.inorganic_influence.pack()
#
#         self.num_experiments_label.pack()
#         self.num_experiments.pack()
#
#         self.calculate_button.pack()
#
#     def run_experiment(self):
#         n = int(self.num_variety.get())
#         t = int(self.num_experiments.get())
#         min_a = float(self.min_sugar_content.get())
#         max_a = float(self.max_sugar_content.get())
#         min_b = float(self.min_degradation.get())
#         max_b = float(self.max_degradation.get())
#         experiment(n, t, min_a, max_a, min_b, max_b, self.algorithms)
#
#
# app = BeetProcessing()



