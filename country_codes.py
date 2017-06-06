from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n

def get_country_code(country_name):#передаем название страны
    """Возвращает для заданной страны её код Pygal, сотоящий из 2 букв"""
    for code, name in COUNTRIES.items():
        if name == country_name:#если название найдено, возвращается код страны
            return code
    #если страна не найдена, вернуть None
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))