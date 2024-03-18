## SweetBeet

Приложение для сравнения алгоритмов решения задачи о назначениях на примере переработки нескольких сортов сахарной свёклы

Скачивание доступно по [ссылке](https://cloud.unn.ru/s/G8MX9PMBAGmnfaF/download/SweetBeetInstaller.msi)

Работу выполнили: [aartyomm](https://github.com/aartyomm), [un1i](https://github.com/un1i), [JKurdina](https://github.com/JKurdina), [Veto1234-ii](https://github.com/Veto1234-ii), [IonovvA](https://github.com/IonovvA)

### Основные возможности программы

- **Проведение заданного количества экспериментов с введёнными параметрами и построение графика на основе средних значений**

  ![exp_sample_2](sample_images/exp_sample_unif_2.png)

  ![exp_sample_1](sample_images/exp_sample_norm_2.png)

- **Проведение расчёта данных из введённой матрицы и вывод ответов**

  ![calc_sample](sample_images/calc_sample_vengmax_2.png)

### Вспомогательные инструменты

- **При проведении расчёта ответы могут быть выведены для разных алгоритмов**

  |![calc_sample_1_cut](sample_images/calc_sample_vengmax_2_cut.png)|![calc_sample_2_cut](sample_images/calc_sample_greedy_2_cut.png)|![calc_sample_3_cut](sample_images/calc_sample_gt_2_cut.png)|
  |-|-|-|

  |![calc_sample_4_cut](sample_images/calc_sample_vengmin_2_cut.png)|![calc_sample_5_cut](sample_images/calc_sample_thrifty_2_cut.png)|![calc_sample_6_cut](sample_images/calc_sample_tg_2_cut.png)|
  |-|-|-|

- **Есть возможность скрыть выбранные графики**

  ![graph_sample_1](sample_images/exp_sample_graph_3.png)
  ![graph_sample_2](sample_images/exp_sample_graph_4.png)

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

	В первой строке вводится количество столбцов (сортов свёклы), затем вводится матрица. (Количество пробелов не иммеет значения)
	
	|![input_calc_1](sample_images/input_calc_sample_1.png)|![input_calc_2](sample_images/input_calc_sample_2.png)|
	|-|-|
	
- **А также вывода в файл**

  - "Сохранить" - вывод всех текстовых данных

    |!||
    |-|-|

  - Экспорт графика

    При нажатии правой кнопки мыши в области графика и выборе подпункта "Export" можно выбрать формат сохранения, и некоторые параметры, такие как цвет заднего фона графика, его размер и так далее

    ![export_graph](sample_images/export_graph_example.png)

- **Настройки графика**

  Есть возможность изменить некоторые настройки графика, нажав в его области на правую кнопку мыши. Например, добавить сетку

  ![graph_settings](sample_images/graph_settings_example.png)

### Инструкции

- **Установка**

  При открытии установщика сначала нажмите "Подробнее", а затем выберете "Выполнить в любом случае"

  |![open_1](sample_images/smartscreen_example.png)|![open_2](sample_images/smartscreen_example_2.png)|
  |-|-|

  При установке программы НЕ выбирайте путь "C:\Program Files", так как в таком случае для сохранения данных в файл нужно будет запускать программу от имени администратора

  ![install_1](sample_images/install_example_2.png)

  
