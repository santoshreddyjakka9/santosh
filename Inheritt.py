class Car(object):
    def __init__(self,Wheels,Brakes):
        self.Wheels = Wheels
        self.Brakes = Brakes

    def Display(self):
            print(self.Wheels)
            print(self.Brakes)

    def Details(self):
                print("Wheels {}".format(self.Wheels))
                print("Brakes {}".format(self.Brakes))

class Toyota(Car):
                    def __init__(self,Wheels,Brakes,Price,Color):
                        self.Price = Price
                        self.Color = Color
                        Car.__init__(self,Wheels,Brakes)

                    def Details(self):
                            print("Wheels :{}",self.Wheels)
                            print("Brakes {}",self.Brakes)
                            print("Price: {}",self.Price)
                            print("Color {}",self.Color)
s = Toyota(4,'pump',20000,'Red')
s.Display()
s.Details()

