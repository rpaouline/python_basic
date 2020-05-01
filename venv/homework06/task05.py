class Stationery():
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print("Start drawing.")


class Pen(Stationery):
    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        print("Start drawing with a pen.")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        print("Start drawing with a pencil.")


class Handle(Stationery):
    def __init__(self):
        super().__init__("Handle")

    def draw(self):
        print("Start drawing with a handle.")


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
