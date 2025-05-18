from abc import ABC, abstractmethod
import random

class Animal(ABC):
    def __init__(self, name, energy=100, speed=5):
        self.__name = name
        self.__energy = energy
        self.__speed = speed
        self._ecosystem = None

    @abstractmethod
    def eat(self, food):
        pass

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_energy(self):
        return self.__energy

    def set_energy(self, energy):
        if energy < 0:
            raise ValueError('Энергия не может быть отрицательной!')
        self.__energy = energy

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed < 0:
            raise ValueError('Скорость не может быть отрицательной!')
        self.__speed = speed

    def set_ecosystem(self, ecosystem):
        self._ecosystem = ecosystem

    def move(self):
        if self.get_energy() > 0:
            print(f'{self.get_name()} переместилось со скоростью {self.get_speed()}')
            self.set_energy(self.get_energy()-5)

    def is_alive(self):
        return self.get_energy() > 0

    def can_reproduce(self):
        return self.get_energy() >= 150

    def reproduce(self):
        raise NotImplementedError('Необходимо переопеределить метод в классе-потомке')

    def is_dead(self, death_chance):
        base_chance = 0.05
        actual_chance = death_chance * base_chance
        return random.random() < actual_chance


class Herbalvore(Animal): # Травоядное
    def __init__(self, name, energy=80):
        super().__init__(name, energy)

    def eat(self, food):
        if hasattr(food, 'is_plant') and food.is_plant():
            print(f'{self.get_name()} съел растение')
            self.set_energy(self.get_energy() + 20)
            self._remove_food_from_ecosystem(food)
        else:
            print('Травоядное не может есть мясо')

    def _remove_food_from_ecosystem(self, food):
        if self._ecosystem:
            self._ecosystem.remove_entity(food)

    def reproduce(self):
        new_name = f'{self.get_name()}-child'
        child = Herbalvore(new_name, 80)
        child.set_ecosystem(self._ecosystem)
        return child


class Carnivore(Animal): # Хищное
    def __init__(self, name, energy=120):
        super().__init__(name, energy)

    def eat(self, food):
        if isinstance(food, Animal) and not hasattr(food, 'is_plant'):
            print(f'{self.get_name()} съел {food.get_name()}')
            self.set_energy(self.get_energy()+30)
            self._remove_food_from_ecosystem(food)
        else:
            print('Хищник не может съесть растение')

    def _remove_food_from_ecosystem(self, food):
        if self._ecosystem:
            self._ecosystem.remove_entity(food)

    def reproduce(self):
        new_name = f'{self.get_name()}-child'
        child = Carnivore(new_name, 120)
        child.set_ecosystem(self._ecosystem)
        return child