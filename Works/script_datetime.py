import datetime
import random

aniversario = datetime.datetime(2020, 1, 1, 0, 0, 0,0)

print(aniversario)
agora = datetime.datetime.now()

print(agora)

print(datetime.datetime.now())
print(agora.year)

# Random number generation
print(random.random()) # Generates a random float between 0 and 1 (exclusive)
print(random.uniform(1, 10)) # Generates a random float within a specified range (inclusive)
print(random.randint(1, 6)) # Generates a random integer within a specified range (inclusive)
print(random.randrange(0, 101, 5)) #Generates a random integer in a specified range with a step