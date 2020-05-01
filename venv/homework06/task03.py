class Worker():
    def __init__(self,name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


CPA = Position("Mark","Ruby","CPA",60000,30000)
print(CPA.get_full_name())
print(CPA.get_total_income())
