class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self,name = None,age = None,isHappy = None):
        self.set_data(name,age,isHappy)

        self.get_data()
    def set_data(self, name = None, age = None , isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name, "age" ,self.age,"happy" ,self.isHappy)

cat1 = Cat()
cat1.set_data()



cat2 = Cat( "mia", 2, False)

