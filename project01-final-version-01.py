# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:33:23 2024

@author: User
"""
# Driver's menu
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

#Cities menu

def show_cities(cities):
    print("\nThe company delivers to the following cities:")
    for city in sorted(cities, reverse=True):
        print(city)

def search_city(cities):
    key = input("Enter the key to search for cities: ").lower()  
    matches = []
    
    for city in cities:  
        if key in city.lower():
            matches.append(city)
    if matches:
        print("Cities matching your search:")
        for match in matches:
            print(match)
    else:
        print("No cities found with that key.")
    
def print_neighboring_cities(city_map):
    city = input("Enter the city name: ").title()
    if city in city_map:
        neighbors = city_map[city]
        print("Cities that can be reached from", city, ":", ", ".join(neighbors))
    else:
        print(city,"is not in the database.")

def find_drivers_delivering_to_city(drivers_list, graph):
    target_city = input("Enter the city name to find delivering drivers: ").lower()
    reachable_drivers = []

    for driver in drivers_list:
        start_city = driver.start_city.lower()
        visited = set()
        cities_to_visit = [start_city]

        while cities_to_visit:
            current_city = cities_to_visit.pop(0)

            if current_city == target_city:
                reachable_drivers.append(driver.name)
                break

            if current_city not in visited:
                visited.add(current_city)

                if current_city in graph:
                    cities_to_visit.extend(graph[current_city])

    if reachable_drivers:
        print(f"Drivers delivering to {target_city.capitalize()}: {', '.join(reachable_drivers)}")
    else:
        print(f"No drivers can deliver to {target_city.capitalize()}.")


if __name__ == "__main__":
    # Sample data
    drivers_list = [
        Driver("ID001", "Max Verstappen", "Akkar"),
        Driver("ID002", "Charles Leclerc", "Saida"),
        Driver("ID003", "Lando Norris", "Jbeil"),
        Driver("ID004", "Atef Abi Sleiman", "Batroun"),
        Driver("ID005", "Sasha Abi Sleiman", "Batroun"),
        Driver("ID006", "Atef Harb", "Saida")
    ]

    cities = ["akkar", "saida", "jbeil", "batroun"]

    city_map = {
        "Akkar": ["Tripoli", "Beirut"],
        "Saida": ["Beirut", "Zahle"],
        "Jbeil": ["Batroun", "Tripoli"],
        "Batroun": ["Jbeil", "Tripoli"],
        "Tripoli": ["Akkar", "Jbeil"],
        "Beirut": ["Saida", "Akkar", "Zahle"],
        "Zahle": ["Saida", "Beirut"]
            }
     
    graph = {
         "batroun": ["beirut","jbeil"],
         "jbeil": ["saida","beirut",],
         "akkar": ["beirut","batroun"],
         "beirut": ["saida"],
         "saida": ["beirut"]
     }
    
 
    while True:
        print("Hello! Please enter:")
        print("1. To go to the drivers’ menu")
        print("2. To go to the cities’ menu")
        print("3. To exit the system")
        main_choice = input("Enter your choice: ").strip()
        
        if main_choice == "1":
            while True:
                print("\nDRIVERS’ MENU")
                print("1. To view all the drivers")
                print("2. To add a driver")
                print("3. Check similar drivers")
                print("4. To go back to the main menu")
                driver_choice = input("Enter your choice: ").strip()

                if driver_choice == "1":
                    Driver.view_drivers(drivers_list)

                elif driver_choice == "2":
                    Driver.add_driver(drivers_list, cities)

                elif driver_choice == "3":
                    Driver.check_similar_drivers(drivers_list)

                elif driver_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif main_choice == "2":    
          while True:
              print("\nCITIES' MENU")
              print("1. Show cities")
              print("2. Search city")
              print("3. Print neighboring cities")
              print("4. Print drivers delivering to a city")
              print("5. Go back to the main menu")
              city_choice = input("Enter your choice: ").strip()

              if city_choice == "1":
                  show_cities(cities)
              elif city_choice == "2":
                  search_city(cities)
              elif city_choice == "3":
                  print_neighboring_cities(city_map)
              elif city_choice == "4":
                   city = input("Enter the city name: ").title()
                   find_drivers_delivering_to_city(drivers_list, graph)
              elif city_choice == "5":
                  break
              else:
                  print("Invalid choice. Please try again.")    

        elif main_choice == "3":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")






        
       
        