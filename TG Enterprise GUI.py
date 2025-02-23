import PySimpleGUI as sg

# initialize variables to keep track of the number of available cars for each model
available_Mira = 2
available_Revo = 2
available_Vezel = 3

# dictionary to store the cost and insurance information for each car name
car_info = {
    "1": {"model": "Mira", "price": 90, "liability": 20, "full": 50},
    "2": {"model": "Revo", "price": 150, "liability": 30, "full": 70},
    "3": {"model": "Vezel", "price": 70, "liability": 20, "full": 50}
}

# variables to keep track of the total number of rentals and total revenue
total_rentals = 0
total_revenue = 0

# main menu layout
layout = [[sg.Text("Please select one:")],
          [sg.Button("Car rental"), sg.Button("Car return"), sg.Button("Print the totals")]]

# create the main window
window = sg.Window("TG Enterprises", layout)

# main menu loop
while True:
    # show the main menu and get the user's selection
    event, values = window.read()

    # car rental option
    if event == "Car rental":
        # car rental layout
        layout = [
            [sg.Text("Select one of the available cars:")],
            [sg.Text("Models Available        "), sg.Text("1. Mira"), sg.Text("2. Revo"), sg.Text("3. Vezel")],
            [sg.Text("Number Of Cars Available"), sg.Text("   2   "), sg.Text("    2    "), sg.Text("    3   ")],
            [sg.Text("Price   /   Day         "), sg.Text("PKR 90 "), sg.Text("PKR 150  "), sg.Text("PKR 70  ")],
            [sg.Text("Liability Insurance/day "), sg.Text("PKR 20 "), sg.Text("PKR 30   "), sg.Text("PKR 20  ")],
            [sg.Text("Full insurance Day      "), sg.Text("PKR 50 "), sg.Text("PKR 70   "), sg.Text("PKR 50  ")],
            [sg.Text("Enter Car type: "), sg.Input(key="car_type")],
            [sg.Text("Enter How Many Days: "), sg.Input(key="days")],
            [sg.Text("Enter 'L' for liability , 'F' for full insurance: "), sg.Input(key="insurance")],
            [sg.Button("OK")]]

        # create the car rental window
        car_rental_window = sg.Window("Car Rental", layout)
        # show the car rental window and get the user's input
        event, values = car_rental_window.read()
        if event == "OK":
            car_rental_window.close()

            # validate user input for car type
            if values["car_type"] not in ["1", "2", "3"]:
                sg.popup("Invalid car type. Please try again.")
                continue

            # convert days input to integer
            days = int(values["days"])
            # get insurance type from user input
            insurance = values["insurance"]
            # validate user input for insurance
            # validate user input for insurance type
            if insurance.upper() not in ["L", "F"]:
                sg.popup("Invalid insurance type. Please try again.")
                continue

            # check if the selected car model is available
            if values["car_type"] == "1" and available_Mira == 0:
                sg.popup("This type of cars is not available now.")
                continue
            elif values["car_type"] == "2" and available_Revo == 0:
                sg.popup("This type of cars is not available now.")
                continue
            elif values["car_type"] == "3" and available_Vezel == 0:
                sg.popup("This type of cars is not available now.")
                continue

            # calculate the cost of the rental
            rent_cost = car_info[values["car_type"]]["price"] * days
            # calculate the cost of insurance
            if insurance.upper() == "L":
                insurance_cost = car_info[values["car_type"]]["liability"] * days
            if insurance.upper() == "F":
                insurance_cost = car_info[values["car_type"]]["full"] * days
            else:
                sg.popup("Enter a Valid Input")
                continue
            # calculate the tax on the rental cost
            tax = rent_cost * 0.05
            # calculate the total cost
            total_cost = rent_cost + insurance_cost + tax

            # update the number of available cars for the selected car model
            if values["car_type"] == "1":
                available_Mira -= 1
            elif values["car_type"] == "2":
                available_Revo -= 1
            elif values["car_type"] == "3":
                available_Vezel -= 1

            # update the total number of rentals and total revenue
            total_rentals += 1
            total_revenue += total_cost

            # display the cost details
            sg.popup("Rent Cost: {} PKR".format(rent_cost),
                    "Insurance Cost: {} PKR".format(insurance_cost),
                    "Tax (5% on rental): {} PKR".format(tax),
                    "Total: {} PKR".format(total_cost))

    # car return option
    elif event == "Car return":
        # car return layout
        layout = [[sg.Text("Select what type of car is returned:")],
                  [sg.Button("Mira"), sg.Button("Revo"), sg.Button("Vezel")]]

        # create the car return window
        car_return_window = sg.Window("Car Return", layout)
        # show the car return window and get the user's selection
        event, values = car_return_window.read()
        car_return_window.close()

        # update the number of available cars for the selected car model
        if event == "Mira":
            available_Mira += 1
        elif event == "Revo":
            available_Revo += 1
        elif event == "Vezel":
            available_Vezel += 1

        # print the totals option
    elif event == "Print the totals":
        sg.popup("Total rentals:", total_rentals,
                "Total revenue:", total_revenue)
        # ask the user if they want to perform more operations
    more_ops = sg.popup_yes_no("More Options")
    if more_ops == "No":
        break

window.close()