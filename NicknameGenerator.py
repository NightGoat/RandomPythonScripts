from random_word import RandomWords
import random

r = RandomWords()
randoms = r.get_random_words()
randomNumber = random.randint(0,999)
nickname = randoms[0].capitalize() + randoms[1].capitalize() + str(randomNumber)
print(nickname.replace(" ", ""))