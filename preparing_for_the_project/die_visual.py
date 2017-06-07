import pygal
from die import Die

# создание кубика D6(шестигранный)
die = Die()

# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000):# количество бросков
    result = die.roll()
    results.append(result)

# Анализ результатов
frequencies = []# список для хранения количества выпадения каждого значения
for value in range(1, die.num_sides+1):# перебор возможных значений в цикле
    frequency = results.count(value)# подсчет количества вхождения каждого числа в результатах
    frequencies.append(frequency)# сприсоединение полученного значения в список

# Визуализация результатов
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)#добавление на гистограмму серии значений
hist.render_to_file('die_visual.svg')

print(frequencies)