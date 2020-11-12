class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician(Band):
    pass

class Guitarist(Musician):
    def __str__(self):
      return f"My name is {self.name} and I play guitar"

    def __repr__(self):
      return f"Guitarist instance. Name = {self.name}"

class Bassist:
    pass

class Drummer(Musician):
    def __str__(self):
      return f"My name is {self.name} and I play drums"