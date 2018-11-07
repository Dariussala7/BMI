#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ThinkPad
#
# Created:     23/10/2018
# Copyright:   (c) ThinkPad 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#prompts user to enter number of members
numMembers = input(" Enter number of members ")
numMembers = int(numMembers)

counter = 1
while (counter <= numMembers):

    #prompts user to enter the name
    name = input ("please enter your name")
    name = (name)

    #prompts user to enter metric or imperial
    measure = input (" metric or imperial: enter M for Metric, I for Imperial")

    #If user types metric, pyscripter will run the program underneath
    if measure == "M" or measure == "m":
        #metric
        weight = input (" Please enter your weight in kg ")
        weight = float(weight)
        print(weight)

        height = input (" Please enter your height in meters ")
        height = float(height)
        print(height)

        bmi = weight / (height * height)


    #If user types imperial, pyscripter will run the program underneath
    elif measure == "I" or measure == "i":
        #imperial
        weightimperial = input (" Please enter your weight in pounds ")
        weightimperial = float(weightimperial)
        print(weightimperial)

        heightimperial = input (" Please enter your height in inches ")
        heightimperial = float(heightimperial)
        print(heightimperial)

        bmi = weightimperial *703/ (heightimperial * heightimperial)

    print(name, "you have a BMI of", bmi)


    if bmi <= 18.5:
        print("You are underweight")

    elif bmi > 18.5 and bmi <25:
        print("You are normal")

    elif bmi >= 25 and bmi <30:
        print("You are overweight")

    elif bmi >= 30:
        print("You are obese")


    counter = counter + 1

