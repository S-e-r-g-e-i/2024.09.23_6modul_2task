# Доступ к свойствам родителя. Переопределение свойств.

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner                 # владелец транспорта. (владелец может меняться)
        self.__model = __model             # модель (марка) транспорта. (мы не можем менять название модели)
        self.__color = __color             # название цвета. (мы не можем менять цвет автомобиля своими руками
        self.__engine_power = __engine_power      # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)

    def get_model(self):                   # возвращает строку: "Модель: <название модели транспорта>"
        return self.__model

    def get_horsepower(self):              # возвращает строку: "Мощность двигателя: <мощность>"
        return self.__engine_power

    def get_color(self):                   # возвращает строку: "Цвет: <цвет транспорта>"
        return self.__color

    def print_info(self):                  # распечатывает результаты методов, а так же владельца
        print(f'Модель: {self.__model}')
        print(f'Мощность двигателя: {self.__engine_power}')
        print(f'Цвет: {self.__color}')
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color): # принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
        for i in self.__COLOR_VARIANTS:
            if new_color.upper() == i.upper():
                self.__color = new_color
                break
        else:
            print(f'Нельзя сменить цвет на {new_color}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()