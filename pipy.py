import math_pi
import json


def guess_number(num):
    global current_index
    global tries
    if num == int(math_pi.pi(b=current_index+1)[-1]):
        current_index += 1
    else:
        tries -= 1
        print("wrong")


def end(index):
    print(f"Next numbers are: {math_pi.pi(b=index + 8)[index + 2:]}")
    hs = high_score_file()
    if hs < index:
        print(f"New highscore is: {index}!")
        high_score_file(index)


def high_score_file(hs=0):
    if hs == 0:
        with open("highscore.json", "r") as file:
            high_score = json.load(file)
        return high_score["high_score"]
    else:
        with open("highscore.json", "w") as file:
            high_score = {"high_score": hs}
            json.dump(high_score, file)


if __name__ == '__main__':
    display_high_score = high_score_file()

    tries = 3
    current_index = 0

    while tries >= 1:
        print(math_pi.pi(b=current_index))
        number = input("Type next number:")
        if number.isdigit():
            number = int(number)
            guess_number(number)
        else:
            print("Enter a number")

    end(current_index)
