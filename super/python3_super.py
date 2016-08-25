class Foo:
    def say(self):
        print('foo printed')

class Bar(Foo):
    def say(self):
        super().say()
        print('bar printed')


b = Bar()
b.say()
