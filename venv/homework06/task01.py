from time import sleep

class TrafficLight():
    def running(self):
        self.__color = "red"
        while True:
            print(self.__color)
            if self.__color == "red":
                sleep(7)
                self.__color = "yellow"
            elif self.__color == "yellow":
                sleep(2)
                self.__color = "green"
            elif self.__color == "green":
                sleep(5)
                self.__color = "red"


traffic_signal = TrafficLight()
traffic_signal.running()
