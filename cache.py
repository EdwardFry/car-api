from classes import *

car_storage = DataStore()

cars_dict = {}

car_storage.append(Car("Honda", "Jazz", "25/09/2011", 1))
car_storage.append(Car("Ford", "GT", "25/09/2006", 1))
car_storage.append(Car("Nissan", "Micra", "25/09/2012", 1))
car_storage.append(Car("Citroen", "C1", "25/09/2010", 1))


colour_storage = DataStore()

colour_storage.append('red')
colour_storage.append('blue')
colour_storage.append('white')
colour_storage.append('black')