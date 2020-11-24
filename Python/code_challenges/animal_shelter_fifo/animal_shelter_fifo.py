class Animal :
    def __init__(self, animal, next_ = None):
        self.animal = animal
        self.next = next_

class InvalidOperationError(Exception):
    pass

class Waiting_list:
    def __init__(self):
        self.first_up = None

    def none_available(self):
        while self.first_up is None:
            return True
        if self.first_up:
            return False

    def whos_next(self):
        if self.none_available():
            raise InvalidOperationError("All animals have been adopted!")
        return self.first_up.animal

    def intake (self, animal):
        new_animal = Animal(animal)
        if self.first_up == None:
            self.first_up = new_animal
        else:
            new_animal.next = self.first_up
            self.first_up = new_animal
        return self.first_up

    def discharge(self):
        if self.first_up:
            bye_bye = self.first_up
            self.first_up = self.first_up.next
            return bye_bye.animal

class AnimalShelter():
    def __init__(self):
        self.shelter = Waiting_list()
        self.temp_cage = []

    def welcome_in(self, animal):
        if animal in ['cat','dog']:
            self.shelter.intake(animal)
            print(self.shelter.first_up)
        else:
            print("Sorry we only take dogs & cats here.")

    def adoption_out(self, animal_type):
        if animal_type in ['cat', 'dog']:
            while self.shelter.whos_next() != animal_type:
              self.temp_cage.append(self.shelter.discharge())
            adopted = self.shelter.discharge()
            while self.temp_cage != []:
                self.shelter.intake(self.temp_cage[-1])
            print(self.shelter)
            return adopted
        if animal_type not in ['cat', 'dog']:
            return None


if __name__ == "__main__":
    pass

testrun = AnimalShelter()
testrun.welcome_in("dog")
testrun.welcome_in("cat")
print(testrun.shelter.first_up.animal)







