import board
import busio
from adafruit_circuitplayground.express import cpx
import adafruit_tcs34725

import random
import time

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

def see_color(actual, desired):
    ar, ag, ab = actual
    dr, dg, db = desired
    # we're gonna check the ratio because it's hella hard to get 'pure red' irl
    total = ar + ag + ab
    print(ar/total, ag/total, ab/total)
    print(dr, dg, db)

    threshold = 0.6
    if sum(desired)/255 > 1.5:
        threshold = 0.4

    if dr and ar/total < threshold:
        return False
    if dg and ag/total < threshold:
        return False
    if db and ab/total < threshold:
        return False

    print("saw", actual, "counts as", desired)

    return True


while True:
    # pick a color
    # display the color
    r = random.randint(0, 1) * 255
    g = random.randint(0, 1) * 255
    b = random.randint(0, 1) * 255

    desired = [r, g, b]

    if all(desired):
        desired[random.randint(0, 2)] = 0
    if not any(desired):
        desired[random.randint(0, 2)] = 255

    desired = tuple(desired)
    print("Looking for", desired)
    cpx.pixels.fill(desired)

    actual = sensor.color_rgb_bytes
    print("Seeing", actual)

    while not see_color(actual, desired):
        actual = sensor.color_rgb_bytes
        time.sleep(0.1)

    # flash for correct
    for _ in range(3):
        cpx.pixels.fill((255, 255, 255))
        time.sleep(0.1)
        cpx.pixels.fill((0, 0, 0))
        time.sleep(0.1)


