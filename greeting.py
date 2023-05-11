def greeting():
    print("Hello!")

class Human:
    def __init__(self, name):
        self.name = name

    def self_intro(self):
        print(f"my name is {self.name}!")

    def human_greeting(self, daytime):
        if daytime == "morning":
            print("Hello!")
        elif daytime == "night":
            print("Good night!")
        else:
            print("Good afternoon!")