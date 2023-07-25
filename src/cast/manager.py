from cast.draftsman import Draftsman

class Manager:
    def __init__(self) -> None:
        self.drafter = Draftsman()

    def SetData(self, data: list):
        self._data = data

    def PrintData(self):
        self.drafter.PrintData(self._data)