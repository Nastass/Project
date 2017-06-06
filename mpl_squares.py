import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values, squares, linewidth=5)# создаем список для хранения квадратов и передаем его функции plot()
# функция plot() строит осмысленное представление для заданных чисел

#Назначение заголовка диаграммы и меток осей
plt.title("Square Numbers", fontsize=24)# fontsize управляет размером текста
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Назначетние размера шрифта делений на осях
plt.tick_params(axis='both', labelsize=14)# axis='both - относятся к обоим осям

plt.show()# открывает окно просмотра matplotlib  и выводит график