import random
import time

class Pet:
    def nap(self):
        print("napping")

    def play(self):
        print("playing")
        # seek human, chase tail, rock back and forth

    def eat(self):
        print("asking for food")

    # TODOS/ideas
    # beg for food
    # keep track of food/play ratio to determine whether pet gets round
    # play with toy
    # play a color matching game with color matchy thing YESSS I'M EXCITED
    # cpe displays the color it wants, try to point the pet at it

    behaviors = (nap, play, eat)

    def __init__(self):
        n = len(self.behaviors)
        random_weights = random.choices(range(100), k=n)
        total = sum(random_weights)
        self.personality = [weight/total for weight in random_weights]

    def behave(self):
        behavior = random.choices(population=self.behaviors, weights=self.personality)
        behavior[0](self)

    def run(self):
        while True:
            self.behave()
            sleep_for = random.choice(range(10))
            print(sleep_for)
            time.sleep(sleep_for)
