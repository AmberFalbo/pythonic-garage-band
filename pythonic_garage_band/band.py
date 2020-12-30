class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        # Band.instance.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    def play_solos(self):
        return [player.play_solo() for player in self.members]       

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician:
    pass

class Guitarist(Band):
    def __str__(self):
      return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"  

    def get_instrument(self):
        return "guitar"  

    def play_solo(self):
        return  "face melting guitar solo"      

class Bassist(Band):
    def __str__(self):
      return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass" 

    def play_solo(self):
        return  "bom bom buh bom" 

class Drummer(Band):
    def __str__(self):
      return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"     

    def play_solo(self):
        return  "rattle boom crash" 