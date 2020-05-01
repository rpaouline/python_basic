class Road():
    def __init__(self, length: int, width: int):
        """
        :param length: m
        :param width: m
        """
        self._length = length
        self._width = width

    def asphalt_weight(self, depth: int) -> int:
        """
        :param depth: cm
        :return: weight of asphalt of defined depth
        """
        ro = 25

        return self._length * self._width * depth * ro


country_road = Road(10000,6)
print(country_road.asphalt_weight(8))
