# embeded list

#emb_list= [[1,2,3],[3,4,5]]

#for item in emb_list:
#    print(item)
#    for number in item:
#        print(number)

# embeded dictiona

#dict_data= {1:{"name":"Paula", "course":"data"}, 2:{"name":"bob","course":"dev"} }

#for item in dict_data.values():
#    print(item)
user_prompt = True

while user_prompt :
    age = input("what is your age? ")
    if age.isdigit():
        if int(age) < 117:
            #user_prompt= False
            break
        else:
            print("Impossible")
    else:
        print("Please provide your age in digits ")

print(f"Your age is : {age}")

