import re
from appointment import Appointment

class Day :
    def __init__(self, date :str, weekDay :str) -> None:
        self.date :str = date
        self.weekDay :str = weekDay
        self.numOfApp :int = 0
        self.AppList = list()

    def appointmentAdd(self, app :str) -> None:
        self.AppList.append(app)
        self.numOfApp += 1
        print(f"{app} added to day {self.date}, {self.weekDay}")
        print(f"Now you have {self.numOfApp} appointments on the {self.date}, {self.weekDay}\n")

    def appointmentPrint(self) -> None:
        print(f"Appointments for the day {self.date}:")
        print(*self.AppList, sep=", ")

    def writeDown(self, fileName :str = "data.txt") -> None:
        fh = open(fileName, 'a+')
        for app in self.AppList:
            fh.write("\t" + app + "\n")
        fh.close()

day = Day("19.08.2024", "Monday")
day.appointmentAdd("eto")
day.appointmentAdd("to")
day.appointmentAdd("drugoje")
day.appointmentAdd("delo")
day.appointmentPrint()
day.writeDown()