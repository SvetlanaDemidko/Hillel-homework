class Vehicle:
    def __init__(self,mark,model, body, color, speed):
        self.__mark = mark
        self.__model = model
        self.__body=body
        self.__color=color
        self.__speed=speed

    def Show_Vehicle(self):
        print(self.__mark+" "+ self.__model + " is "+self.__body+ " with "+self.__color+" color and top speed is "+str(self.__speed))

    @property
    def color(self):
        return(self.__color)#show color
    @color.setter
    def color(self,color):
        self.__color=color#change color
    @color.deleter
    def color(self):
        self.__color = "Red"#back to standart color

class Car(Vehicle):
    def __init__(self,mark,model,body,color, speed):
        Vehicle.__init__(self,mark,model,body, color, speed)

class Bus(Vehicle):
    def __init__(self,mark,model, color, speed):
        Vehicle.__init__(self,mark,model,"Bus", color, speed)



l=Car("Mercedes-Benz","CLA250","Sedan","White",220)
l.Show_Vehicle()

l2=Bus("Volvo","Electric-Bus","White",160)
l2.Show_Vehicle()
print(l2.color)