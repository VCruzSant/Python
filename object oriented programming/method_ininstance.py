# Métodos em instancias python
# Classe - molde (sem dados)
# instancia da classe - Objeto -> dados
# Classe pode gerar instancias 
# Na Classe o self é sua própria instancia 

class Car:
    def __init__(self, name_car=None):
        # self.name = 'fusca' #Hard Coded -> escrevendo valor na mão
        if name_car is None:
            self.name_car = "name not defined"
            return

        self.name_car = name_car

    def racing(self):
        print(f"{self.name_car} are racing")
        print()


auto_name = Car()
mustang = Car("mustang")
ferrari = Car("ferrari")


print(auto_name.name_car)


print(mustang.name_car)
mustang.racing()


print(ferrari.name_car)
ferrari.racing()
