class SayHell:
    def __init__(self, target="World"):
        self.target = target

    def say(self):
        print(f"Hello, {self.target}!!")


if __name__ == '__main__':
    app = SayHell()
    app.say()
    app = SayHell("Someone")
    app.say()