# TO get the coordinates of each state

import pandas as pd
import turtle as t


screen = t.Screen()

# image = "C:\\Users\\ACER\\Documents\\VSC WORKSPACE\\PYTHON\\DAY 25\\QuizProject\\map.gif"  

image = "DAY 25\QuizProject\map.gif"

screen.addshape(image)

t.shape(image)


# Volatile Storage
stateNames = []

xcor = []
ycor = []


def getData(x,y):
    """To collect data from the user about the state's name and coordinates"""

    xcor.append(x)
    ycor.append(y)

    name = screen.textinput("The Indian Map", "Enter the name of the state")
    stateNames.append(name)

    length = len(stateNames)

    if(length == 28):
        
        data = {
            "states" : stateNames,
            "x": xcor,
            "y": ycor
        }

        StateData = pd.DataFrame(data)

        StateData.to_csv("DAY 25/QuizProject/states.csv")


 



screen.onscreenclick(getData)




screen.mainloop()