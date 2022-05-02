import vehicle, plane, boat, train, car, location
test = vehicle.Vehicle()
plane= plane.Plane()
boat= boat.Boat()
train= train.Train()
car= car.Car()
a=location.Location()

print(a.chosen_location())
# Asks the user from an input to choose the type of transport
user = input("\nChoose a mode of transport. Enter 1 for plane, Enter 2 for Boat, "
             "Enter 3 for Train and enter 4 for car ")
# Loop ensures a valid input is entered
while user.isdigit() == False or int(user) <=0 or int(user)>=5:
    print("invalid input")
    user = input("\nChoose a mode of transport. Enter 1 for plane, Enter 2 for Boat, Enter 3 for Train "
                 "and enter 4 for car ")
# control flow is used to set the variable "User_transport" to the correct class
if int(user) == 1:
    user_transport = plane
    print(user_transport.move())
elif int(user) == 2: 
    user_transport = boat
elif int(user) == 3:
    user_transport = train
    print(user_transport.move())
else:
    user_transport = car
print("You have chosen option " + user)

# Loop below allows the user to change the speed with 15 minute intervals
distance = a.dist
time = 0
while distance > 0:
    user_speed = input("Press 1 to  accelerate and 2 to decelerate ")
    if user_speed == str(1) and user_speed.isdigit():
        user_transport.current_speed += user_transport.speed_cont
        distance -= (user_transport.current_speed/4)
        time += 15
        if distance <= 0:
            print(f'Your current speed is 0\n')
        else:
            print(f'Your current speed is {user_transport.current_speed} mph, minutes passed: {time}')
            print(f'You are {distance} miles away from your destination\n')
    elif user_speed == str(2):
        user_transport.current_speed -= user_transport.speed_cont
        distance -= (user_transport.current_speed / 4)
        time+=15
        if distance <= 0:
            print(f'Your current speed is 0\n')
        else:
            print(f'Your current speed is {user_transport.current_speed} mph,  minutes passed: {time}')
            print(f'You are {distance} miles away from your destination\n')
    else:
        print("Invalid input")


print(f"{time} minutes have passed and you have reached your destination!")