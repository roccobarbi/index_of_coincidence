import sys

from letter_count.letter_counter import LetterCounter


class Config:
    def __init__(self):
        self.estimate_language = False
        self.infile_name = None

    def set_estimate_language(self):
        self.estimate_language = True

    def unset_estimate_language(self):
        self.estimate_language = False

    def set_infile_name(self, infile_name):
        self.infile_name = infile_name


def parse_args(args):
    config = Config()
    for index, arg in enumerate(args):
        if arg[0] == "-":
            for option in arg[1:]:
                if option == "E":
                    config.set_estimate_language()
        else:
            if index == len(args) - 1:
                config.set_infile_name(arg)
    return config


def main(args):
    if len(args) < 1:
        raise Exception("no arguments passed")
    config = parse_args()
    counter = LetterCounter()
    with open(config.infile_name, "r") as infile:
        text = infile.read()
        counter.set_text(text)
    count = counter.count()
    ic = 0
    for letter in counter.get_alphabet():
        ic += count[letter]/len(text) * (count[letter] - 1)/(len(text) - 1)
    print("Index of coincidence: %.2f %%" % (ic * 100))
    if config.estimate_language:
        pass


if __name__ == "__main__":
    main(sys.argv[1:])