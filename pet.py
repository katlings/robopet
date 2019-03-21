import random
import time

class Pet:
    def nap(self):
        print("napping")
        pass

    def play(self):
        print("playing")
        pass

    behaviors = (nap, play)

    def __init__(self):
        n = len(self.behaviors)
        random_weights = random.choices(range(100), k=n)
        total = sum(random_weights)
        self.personality = [weight/total for weight in random_weights]
        print(list(self.personality))

    def behave(self):
        behavior = random.choices(population=self.behaviors, weights=self.personality)
        behavior[0](self)

    def run(self):
        while True:
            self.behave()
            sleep_for = random.choice(range(10))
            print(sleep_for)
            time.sleep(sleep_for)
