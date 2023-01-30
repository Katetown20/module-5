class String_Var:
    #изменение строки
    def set(self, string):
        self.string = string
        str = string.upper()
        print(str)

    # получение строки
    def get(self, string):
        print(string)

s = String_Var()
s.set('hello world')
s.get('hello world')