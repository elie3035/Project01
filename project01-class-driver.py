# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:15:28 2024

@author: User
"""

class Driver:
    def __init__(self, work_id, name, start_city):
        self.work_id = work_id
        self.name = name
        self.start_city = start_city

   
    def view_drivers(drivers):
        for driver in drivers:
            print(driver.work_id,driver.name,driver.start_city)

  
    def add_driver(drivers_list, cities):
        name = input('Enter the driver name: ').lower()
        start_city = input("Enter the start city of the driver: ").lower()
        
        if start_city in ["akkar","saida","jbeil","batroun"]:
            work_id = "ID" + "00" + str(len(drivers_list) + 1)
            new_driver= Driver(work_id,name,start_city)
            drivers_list.append(new_driver)
            return
        else:
            additional=True
            while additional:
                new_city=input("do you want to add new city? y/n").lower()
                if new_city=="y":
                  start_city = input("Enter the new city name: ").title()
                  work_id = f"ID{len(drivers_list) + 1:03}" 
                  new_driver = Driver(work_id, name, start_city)
                  drivers_list.append(new_driver)
                  additional = False
                else:
                  print("No new driver added.")
                  return   

    def check_similar_drivers(drivers_list): 
     city_map = {}

     for driver in drivers_list:
       city = driver.start_city
       
       if city not in city_map:
           city_map[city] = []
       
       city_map[city].append(driver.name)

     for city, driver_names in city_map.items():  
       print(city + ": " + ", ".join(driver_names))