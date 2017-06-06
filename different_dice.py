from die import Die

import pygal

# создание двух кубиков D6(шестигранный) и D10
die_1 = Die()
die_2 = Die(10)

# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(50000):# количество бросков
    result = die_1.roll() + die_2.roll()#бросаем кубики и вычисляем сумму для каждого броска
    results.append(result)

# Анализ результатов
frequencies = []# список для хранения количества выпадения каждого значения
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):# перебор возможных значений в цикле
    frequency = results.count(value)# подсчет количества вхождения каждого числа в результатах
    frequencies.append(frequency)# сприсоединение полученного значения в список

# Визуализация результатов
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6' + 'D10', frequencies)#добавление на гистограмму серии значений
hist.render_to_file('dice_visual.svg')

print(frequencies)