class Animal(object): #继承object， object为基类
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def run(self):
        print("animal is running")

class Dog(Animal): #继承Animal
    def run(self):
        print("dog is running")

def animalRun(animal):
    animal.run()

def test():
    animal = Animal("animal~")
    dog = Dog("dog~")
    print(dog.getName())
    animal.run()
    dog.run()
    #print(dir(dog))
    print(dir('abc'))
    print(type(True))
    print(type('123'))
    print(type(dog) == Animal)

if __name__ == '__main__':
    test()