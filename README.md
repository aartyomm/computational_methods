## SweetBeet

Приложение для сравнения алгоритмов решения задачи о назначениях на примере переработки нескольких сортов сахарной свёклы

Работу выполнили: [aartyomm](https://github.com/aartyomm), [un1i](https://github.com/un1i), [JKurdina](https://github.com/JKurdina)

### Основные возможности программы

- **Проведение заданного количества экспериментов с введёнными параметрами и построение графика на основе средних значений**

  ![exp_sample_2](sample_images/exp_sample_unif.png)

  ![exp_sample_1](sample_images/exp_sample_norm.png)

- **Проведение расчёта данных из введённой матрицы и вывод ответов**

  ![calc_sample](sample_images/calc_sample_vengmax.png)

### Вспомогательные инструменты

- **При проведении расчёта ответы могут быть выведены для разных алгоритмов**

  |![calc_sample_1_cut](sample_images/calc_sample_vengmax_cut.png)|![calc_sample_2_cut](sample_images/calc_sample_greedy_cut.png)|![calc_sample_3_cut](sample_images/calc_sample_gt_cut.png)|
  |-|-|-|

  |![calc_sample_4_cut](sample_images/calc_sample_vengmin_cut.png)|![calc_sample_5_cut](sample_images/calc_sample_thrifty_cut.png)|![calc_sample_6_cut](sample_images/calc_sample_tg_cut.png)|
  |-|-|-|

- **Есть возможность скрыть выбранные графики**

  ![graph_sample_1](sample_images/exp_sample_graph.png)
  ![graph_sample_2](sample_images/exp_sample_graph_2.png)

- **Реализована возможность ввода данных из файла**

  *Данные вводятся из .txt файла. Для того, чтобы данные ввелись корректно, необходимо правильное форматирование*

  - "Эксперимент"

	В каждой строке вводятся, соответственно:
	- количество сортов свёклы
	- диапазон сахаристости до переработки
	- распределение
	- параметры выбранного распределения
	- учёт влияния неорганики - "да" или "нет"
	- количество экспериметов

	![input_exp_1](sample_images/input_exp_sample_2.png)


  - "Расчёт"

	В первой строке вводится количество столбцов (сортов свёклы), затем вводится матрица
	Количество пробелов не иммеет значения
	
	|![input_calc_1](sample_images/input_calc_sample_1.png)|![input_calc_2](sample_images/input_calc_sample_2.png)|
	|-|-|
	
- **А также вывода в файл**
