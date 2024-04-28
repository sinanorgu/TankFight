class araba:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.__a = x
        self.__b = y

    def __getxy(self):
        return self.x,self.y

    def getall(self):
        return self.y,self.x
    def getsome(self):
        return self.__getxy()

    def getab(self):
        return self.__a,self.__b
    def __get_a(self):
        return  self.__a,self.__b

a = araba(1,2)

print(a.x)
print(a.__a) #private, error!!!