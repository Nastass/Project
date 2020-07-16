import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной
while True:
    # Построение случайного блуждания и нанесение точек на диаграмму
    rw = RandomWalk()
    rw.fill_walk()

    #Назначение размера области просмотра
    plt.figure(dpi=250, figsize=(10,6))# функция figure() управляет шириной, высотой, разрешением и цветом фона диаграммы

    # Вывод точек и отображение диаграммы
    point_numbers = list(range(rw.num_points))# range() используется для генерирования списка чисел, размер которого
    # павен количеству точек в блуждании
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Выделение первой и последней точек
    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Удаление осей
    plt.axes().get_xaxis().set_visible(False)# делает оси невидимыми
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break