# Задача 3
# Паттерн «Фабричный метод»:
# - создать абстрактный класс Animal, у которого есть
# абстрактный метод speak.
# - классы Dog и Cat, которые наследуют от Animal
# и реализуют метод speak.
# - класс AnimalFactory, который использует
# паттерн «Фабричный метод» для создания экземпляра
# Animal. В этом классе должен быть метод create_animal,
# который принимает урок («dog» или «cat») и возвращается
# соответствующий объект (Dog или Cat)

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "Гав!"

class Cat(Animal):
    def speak(self) -> str:
        return "Мяу!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        animal_type = animal_type.lower()
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")

if __name__ == "__main__":
    try:
        dog = AnimalFactory.create_animal("dog")
        cat = AnimalFactory.create_animal("cat")

        print(dog.speak())  # Гав!
        print(cat.speak())  # Мяу!

    except ValueError as e:
        print(e)