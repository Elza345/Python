class fish():
    name = None
    color = None
    age = None
    issmall = None

    def __init__(self,name,color,age,issmall):
        self.set_data(name, color, age, issmall)
        self.get_data()


    def set_data(self,name,color,age,issmall ):
        self.name = name
        self.color = color
        self.age = age
        self.issmall = issmall

    def get_data(self):
        print(self.name,"color:",self.color,"age:",self.age,"small:",self.issmall)

fish1 = fish("Dory","blue",5,True)
fish2 = fish("Nemo","orange",6,True)



