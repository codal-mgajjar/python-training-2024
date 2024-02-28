from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def wheels(self):
        pass


class Mercedes(Car):
    def wheels(self):
        pass

    def test(self):
        pass


m = Mercedes()
# m.wheels()
