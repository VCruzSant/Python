class SellMotor:
    def __init__(self, name_sell):
        self._name_sell = name_sell
        self._motor_type = []

   
    def insert_motor(self, type_m, value):
        # Relação de Composição
        self._motor_type.append(Motor(type_m, value)) 
    
    def print_motor(self):
        for t in self._motor_type:
            print(t.type_m, t.value)
    

class Motor:
    def __init__(self, type_m, value):
        self.type_m = type_m
        self.value = value

c1 = SellMotor("Sant")
c1.insert_motor('tipo-v', 10.000)
c1.insert_motor('tipo-V', 50.000)

c1.print_motor()
