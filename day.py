from appointment import Appointment

class Day :
    def __init__(self, date :str, weekDay :str) -> None:
        self.date :str = date
        self.weekDay = weekDay
        self.numOfApp :int = 0
        self.AppList = list()

    def appointmentAdd(self, app :Appointment) -> None:
        self.AppList.append(app)
        print(f"Now you have {self.numOfApp} appointments on the {self.date}, {self.weekDay}")