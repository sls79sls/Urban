Почему не работает закомментаренная строка, если её раскомментарить?

class Human:
    def __init__(self):
        self.about()
    Head = True
    _legs = True
    __arms = True
    def say_hello(self):
        print("Здравствуйте")

class Student(Human):
    def about(self):
        print("Я студент")


class Teacher(Human):
    pass

#H=Human()
S=Student()

#H.say_hello()
S.about()
S.say_hello()
#H.about()
