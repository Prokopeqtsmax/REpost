# class Student:
#     def __init__(self): #конструктор
#         self.height = 170
#
#     height = 160
#
#     def printer(self):
#         print(self.height)
#
# nick = Student()
# nick.printer()
#
#
#
#
#
#
#
#
#
#
#
# import random
# class Student:
#     def __init__(self, name):  #створюємо студента
#         self.name = name
#         self.gladness = 50
#         self.progress = 0
#         self.alive = True
#
#     def to_study(self): #студент навчається
#         print("Time to study")
#         self.progress += 0.12
#         self.gladness -= 5
#
#     def to_sleep(self): #спить
#         print("I will sleep")
#         self.gladness += 3
#
#     def to_chill(self): #відпочиває
#         print("Rest time")
#         self.gladness += 5
#         self.progress -= 0.1
#
#     def is_alive(self): #статистика, слідкуюи за його характеристиками
#         if self.progress < -0.5:
#             print("Cast out…")
#             self.alive = False
#         elif self.gladness <= 0:
#             print("Depression…")
#             self.alive = False
#         elif self.progress > 5:
#             print("Passed externally…")
#             self.alive = False
#
#     def end_of_day(self): # кінець дня
#         print(f"Gladness = {self.gladness}")
#         print(f"Progress = {round(self.progress, 2)}")
#
#     def live(self, day): # генерація дня студента
#         day = "Day" + str(day) + "of" +self.name + "life"
#         print(f"{day:=^50}")
#         live_cube = random.randint(1, 3)
#         if live_cube == 1:
#             self.to_study()
#         elif live_cube == 2:
#             self.to_sleep()
#         elif live_cube == 3:
#             self.to_chill()
#         self.end_of_day()
#         self.is_alive()
#
# nick = Student(name="Nick")
# for day in range(365): #проходимось по всім дням у році
#     if nick.alive == False:
#         break
#     nick.live(day)



class Pet:
    def __init__(self,name="pet",age=0,type="cat"):
        self.name=name
        self.age=age
        self.type=type


class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.listpet=[]
    def add_pets(self, *args):
        for pet in args:
            self.listpet.append(pet)


    def print_info(self):
        if self.listpet!=[]:
            for pet in self.listpet:
                print(f"Name pet{pet.name} Age={pet.age}Type = {pet.type}")
            else:
                print(f"Тваринок немає")
class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = [] #список
    def add_passenger(self, human):
        self.passengers.append(human)
    # def add_passenger(self, *args):
    #     for passenger in args:
    #         self.passengers.append(passenger)
    def print_passengers_names(self):
        if self.passengers!= []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengersin {self.brand}")

nick = Human("Nick") #екземпляр класу (об'єкт)
kate = Human("Kate") #екземпляр класу (об'єкт)
car = Auto("Mercedes") #екземпляр класу (об'єкт)

car.add_passenger(nick)  #зв'язок класів
car.add_passenger(kate)
car.print_passengers_names()

pet=Pet("L",12,"cat")
pet2=Pet("h",20,"dog")
nick.add_pets(pet,pet2)
nick.print_info()