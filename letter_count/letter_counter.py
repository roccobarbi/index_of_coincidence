class LetterCounter:
    def __init__(self, text):
        self.text = text
        self.counter = {}

    def __init__(self):
        self.text = ""
        self.counter = {}

    def count(self):
        if self.counter == {}:
            for character in self.text:
                if character not in self.counter.keys():
                    self.counter[character] = 1
                else:
                    self.counter[character] += 1
        return self.counter

    def set_text(self, text):
        self.text = text
        self.counter = {}

    def get_text(self):
        return self.text

    def get_alphabet(self):
        return self.counter.keys()