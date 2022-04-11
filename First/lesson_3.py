# 1) Заменить в произвольной строке согласные буквы на гласные.

text = 'bakepimobyn'
text2 = text.replace('a', 'b')
text3 = text2.replace('e', 'm')
text4 = text3.replace('i', 'k')
text5 = text4.replace('o', 'm')
text6 = text5.replace('y', 'm')
print(text6)

# 2) Дан массив из словарей

# data = [
  # {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
  # {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
  # {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
  # {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
  # {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
  # {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# 2.1) отсортировать массив из словарей по значению ключа ‘age'
data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30 },
   {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
   {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
   {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
   {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
   {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]
sorted_data = sorted(data, key=lambda d: d['age'])
print(sorted_data)

# 2.2) сгруппировать данные по значению ключа 'city'

cities = {}

for item in data:
    cityName = item['city']
    del item['city']
    if not cityName in cities.keys():
        cities[cityName] = []
    cities[cityName].append(item)
print (cities)



# 3) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.

def most_frequent(List):
    return max(set(List), key=List.count)
List = ['a', 'a', 'bi', 'bi', 'bi']
print(most_frequent(List))
