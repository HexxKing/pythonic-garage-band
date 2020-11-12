class Dog():
    def sleep(self):
      return "zzz"

class Puggle(Dog):

    count = 0

    def __init__(self, name="unknown poochie")
      self.name = name
      Puggle.count += 1 #everytime a new Puggle is made, the counter goes up

    def greet(self, name)
      return f"I am {self.name}. I am SO HAPPY to meet you!"

    #can override Dog's method
    def sleep(self):
        return "runs in sleep"

    @staticmethod
    def get_characteristics(cls):
        return "Like a mini boxer"

    @classmethod
    def get_breed_count(cls):
        return cls.count


class Boxer(Dog): #don't forget to add Boxer to import tests file
    def __init__(self, name="unknown")
      self.name = name 
    
    def greet(self)
      return f"The name's {self.name}. Pleasure."

#only run this when running directly as a "script"
if __name__ == "__main__":
    print('hi there')
    boxer = Boxer()
    print(boxer)
