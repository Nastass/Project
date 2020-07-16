import matplotlib.pyplot as plt

x_values = list(range(1001))# списки содержащие числа вводимые в квадрат
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)# s задает размер точек, edgecolor отвечает за контур
#Назначение заголовка диаграммы и меток осе
plt.title("Square Numbers", fontsize=24)# fontsize управляет размером текста
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Назначетние размера шрифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)

#назначение диапазона для каждой оси
plt.axis([0, 1100, 0, 1100000])# значения по осям x,y max и min

plt.show()#просто вызов
#plt.savefig('squares_plot.png', bbox_inches='tight')# 1 аргумент содержит имя файла, 2 отсекает от диаграммы лишние пропуски
