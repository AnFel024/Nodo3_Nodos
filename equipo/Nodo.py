from django.shortcuts import render

class Nodo:
    def __init__(self):
        self.value = 0

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

EquipoB = Nodo()

def getValue():
    return EquipoB.get_value()

def setValue(value):
    print(value)
    EquipoB.set_value(value)