import json

from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from country_codes import get_country_code

# заполнение списка данными
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# построение словаря с данными численности населения
cc_populations = {}#словарь для хранения кодов стран и численности населения
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Группировка стран по 3 уровням населения
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}#создаем словари для каждой категории
for cc, pop in cc_populations.items():# проверяем население каждой страны
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Проверяем количество стран на каждом уровне
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))#выводим длину для определения размера групп

wm_style = RS('#336600', base_style=LCS)
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')

