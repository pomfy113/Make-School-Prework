# Make School OOP Coding Challenge Python Problem 8

import sys

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
#/*~Above this is uneditable code~*/           
#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
#Ferdinand Cruz

#Animal superclass
#Prints out default animal strings
#If an animal has an override, they're listed on the comments above each subclass
class Animal(object):
    # A variable to count population
    population = 0
    
    #Add 1 to animal population per initialization
    def __init__(self, name):
        self.name = name
        Animal.population +=1
    
    #Default string for sleeping; overrides in class inits
    def sleep(self):
        sleepString = self.name + " sleeps for 8 hours"
        print sleepString
        
    #Default string for eating; overrides in class inits
    def eat(self, food):    
        foodString = self.name + " eats " + food
        print foodString
        if food == self.favoriteFood:
            print "YUM! " + self.name + " wants more " + food    
    
    #Class method; returns total population
    @classmethod        
    def populationCount(cls):
        return cls.population

#Tiger class
#No changes
class Tiger(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.favoriteFood = "meat"

#Bear class
#Hibernation instead of sleep; diff string
class Bear(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.favoriteFood = "fish"
    def sleep(self):
        sleepString = self.name + " hibernates for 4 months"
        print sleepString

#Unicorn class
#"Sleeps in a cloud" instead of regular sleep
class Unicorn(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.favoriteFood = "marshmallows"
    def sleep(self):
        sleepString = self.name + " sleeps in a cloud"
        print sleepString

#Giraffe class
#Only eats leaves; spits out other food
class Giraffe(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.favoriteFood = "leaves"
    def eat(self, food):    
        foodString = self.name + " eats " + food
        print foodString
        if food == self.favoriteFood:
            print "YUM! " + self.name + " wants more " + food
        else:
            print "YUCK! " + self.name + " spits out " + food

#Bee class
#Never sleeps
#Only eats pollen; spits out other food
class Bee(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.favoriteFood = "pollen"
        
    def sleep(self):
        sleepString = self.name + " never sleeps"
        print sleepString
        
    def eat(self, food):    
        foodString = self.name + " eats " + food
        print foodString
        if food == self.favoriteFood:
            print "YUM! " + self.name + " wants more " + food
        else:
            print "YUCK! " + self.name + " spits out " + food

#Zookeeper class
#Prints out name, amount of animals being fed by checking input, and population of animals
#Loops through the animals (based on size of array), then calls their eat (using food from input) and sleep function

class Zookeeper(object):
    def __init__(self, name):
        self.name = name
        
    def feedAnimals(self, animals, food):
        print self.name + " is feeding " + food + " to " + str(len(animals)) + " of " + str(Animal.populationCount()) + " total animals"
        for i in range(len(animals)):
            animals[i].eat(food)
            animals[i].sleep()

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
#/*~Below this is uneditable code~*/           
#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

# This code tests the Animal, Tiger, Bear, Unicorn, Giraffe and Bee classes
# and then tests the Zookeeper class and its feedAnimals method, which will
# also test the Animal.populationCount class method
def test():
    def getline():
        # Read a line from standard input and strip surrounding whitespace
        return sys.stdin.readline().strip()
    # Get the number of animals
    animalCount = int(getline())
    animals = []
    # Iterate through the input for each animal
    for count in range(animalCount):
        # Get the animal's species and name
        species = getline()
        name = getline()
        animal = None
        # Check what species the animal is
        if species == "tiger":
            # Create a Tiger object
            animal = Tiger(name)
        elif species == "bear":
            # Create a Bear object
            animal = Bear(name)
        elif species == "unicorn":
            # Create a Unicorn object
            animal = Unicorn(name)
        elif species == "giraffe":
            # Create a Giraffe object
            animal = Giraffe(name)
        elif species == "bee":
            # Create a Bee object
            animal = Bee(name)
        else:
            # Create an Animal object
            animal = Animal(name, "kibble")
        # Add the animal to the list of animals
        animals.append(animal)
    # Remove the first and last animal from the list of animals
    animalsToFeed = animals[1:-1]
    # Get the zookeeper's name and food to feed the animals
    name = getline()
    food = getline()
    # Create a Zookeeper object and test its feedAnimals method
    zookeeper = Zookeeper(name)
    zookeeper.feedAnimals(animalsToFeed, food)


if __name__ == "__main__":
    test()
