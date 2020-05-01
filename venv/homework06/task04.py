class Car():
    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        print(f"Current speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Slow down!")
            
            
class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self.is_police = True

    def siren(self):
        print("Wo-wo-wo-wo-wo-wo-wo-wo!")


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Slow down!")
        

class SportCar(Car):
   def show_speed(self):
        super().show_speed()
        if self.speed < 60:
            print("Speed up!")


police_car = PoliceCar(120,"black","SFPD")
print(police_car.name)
police_car.siren()

town_car = TownCar(70,"yellow","Yaris")
print(town_car.color)
town_car.show_speed()

sport_car = SportCar(90,"red","Mustang")
print(sport_car.color)
sport_car.show_speed()

work_car = WorkCar(50,"white","Tundra")
print(work_car.name)
work_car.show_speed()
