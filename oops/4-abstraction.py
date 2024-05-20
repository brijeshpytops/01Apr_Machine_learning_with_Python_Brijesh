from abc import ABC, abstractmethod


class animal(ABC):
    @abstractmethod
    def voice(self):
        pass

class dog(animal):
    def voice(self):
        print("Bhow, Bhow")

class cat(animal):
    def voice(self):
        print("meow, meow")

obj = cat()
obj.voice()

obj = dog()
obj.voice()