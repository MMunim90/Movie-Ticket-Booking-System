from time import sleep
from hall import Hall
import random

my_hall = Hall(2, 6, 8)
my_hall.enter_show(127, 'Domm', '10:00 AM')
my_hall.enter_show(205, 'Bonolota Express', '01:00 PM')
my_hall.enter_show(241, 'Rakkhosh', '04:00 PM')
my_hall.enter_show(321, 'Hati', '07:00 PM')
my_hall.enter_show(345, 'Gora', '10:00 PM')

while True:
    print("\n------------------------------------------------------------------\n")
    print("1. View all show today.")
    print("2. View available seats.")
    print("3. Book tickets.")
    print("4. Exit.")

    option = int(input("Enter your option: "))
    if option == 1:
        print("\n------------------------------------------------------------------\n")
        my_hall.view_show_list()
    elif option == 2:
        id = int(input("Enter Show ID: "))
        print("\n------------------------------------------------------------------\n")
        my_hall.view_available_seats(id)
    elif option == 3:
        pass
    elif option == 4:
        print("Please wait.....")
        sleep(1)
        print("Shutting down.....")
        sleep(random.randint(2,3))
        break
    else:
        print("Wrong option. choose again.\n")