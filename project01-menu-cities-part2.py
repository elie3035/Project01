# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:33:23 2024

@author: User
"""

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

#Sample city map data for neighboring cities
city_map = {
    "Akkar": ["Tripoli", "Batroun"],
    "Saida": ["Beirut", "Zahle"],
    "Jbeil": ["Batroun", "Tripoli"],
    "Batroun": ["Jbeil", "Tripoli"]
}

cities = ["Akkar", "Saida", "Jbeil", "Batroun"] 

# drivers_list = [
#         Driver("ID001", "Max Verstappen", "Akkar"),
#         Driver("ID002", "Charles Leclerc", "Saida"),
#         Driver("ID003", "Lando Norris", "Jbeil"),
#         Driver("ID004", "Atef Abi Sleiman", "Batroun"),
#         Driver("ID005", "Sasha Abi Sleiman", "Batroun"),
#         Driver("ID006", "Atef Harb", "Saida")
#                        ]

# Integrating the CITIES' MENU into the main program loop
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
        print_drivers_delivering_to_city(city, drivers_list, city_map)
    elif city_choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
        
       
        