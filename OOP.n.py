class Building:
    year = None
    city = None

    def __init__(self,year,city):
        self.year = year
        self.city = city

    def get_info(self):
        print("year",self.year,". city:",self.city)

class school(Building):
    pupils = 0
    def __init__(self,pupils,year,city):
        super(school,self).__init__(year,city)
        self.pupils = pupils
    def get_info(self):
        super().get_info()
        print("pupils:",self.pupils)


class house(Building):
    pass

class shop(Building):
    pass

school = school(100, 2000,"Buenos Aires")
school.get_info()
house = house( 2000,"Buenos Aires")
shop = shop( 2000,"Buenos Aires")
shop.get_info()