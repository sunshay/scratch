#!/usr/bin/python

class house():
    def __init__(self,room,machine,human,equipment):
        self.room = room
        self.machine = machine
        self.human = human
        self.equipment = equipment
    
    def introduction(self):
        return f"{self.room}" {self.equipment}"

echos = house("office","sewer","uncle","telephone")
print(echos)
print(echos.introduction)

        