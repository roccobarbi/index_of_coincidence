import sys

from letter_count.letter_counter import LetterCounter


def main(args):
    if len(args) < 1:
        raise Exception("no arguments passed")
    counter = LetterCounter()
    with open(args[0], "r") as infile:
        text = infile.read()
        counter.set_text(text)
    count = counter.count()
    ic = 0
    for letter in counter.get_alphabet():
        ic += count[letter]/len(text) * (count[letter] - 1)/(len(text) - 1)
    print("Index of coincidence: %.2f %%" % (ic * 100))


if __name__ == "__main__":
    main(sys.argv[1:])