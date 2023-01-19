
# Imports

import pandas as p
import turtle as t


# Setting up the screen

screen = t.Screen()
screen.addshape("map.gif")

t.shape("map.gif")


# Loading the indian state's data
file = p.read_csv("IndianStates.csv")

# Containers

states = file.states.to_list()    # All states

guessedStates = []  # User's guessed states will be appended

attempts = 0


# Game loop

gameOn = True

while gameOn:

    # Condition to stop the game
    if(len(guessedStates) >= 28):

        end = t.Turtle()
        end.penup()
        end.hideturtle()
        end.goto(150,-200)
        end.color("green")
        end.write("You won!", align="center", font=("Arial", "30", "bold"))
        end.goto(150, -230)
        end.write("You named all 28 states, we are proud of you!",align="center", font=("Arial", "12", "bold"))
        end.goto(150, -250)
        end.write(f"Attempts used : {attempts}",align="center", font=("Arial", "12", "bold"))
        
        gameOn = False
        break
        



    # Taking user input 
    userGuess = screen.textinput(title = f"India : {len(guessedStates)}/28 in {attempts} attempts", prompt = "Name of a state (No Union Territory)").title()

    attempts += 1

    if userGuess == "Exit":
        screen.bye()
        break

    # If user already guessed it, then don't check
    if userGuess not in guessedStates:  # if NOT guessed before

        if userGuess in states: # if guessed state is in the states list

            # Finding the state which user guessed
            state = file[file.states == userGuess ]
            stateX = int(state.x)
            stateY = int(state.y)

            # Creating a turtle to go to that place and mark it
            point = t.Turtle()
            point.shape("circle")
            point.shapesize(stretch_wid=0.2)
            point.penup()
            point.goto(stateX, stateY)
            point.write(f"{state.states.item()}", font=("Arial", "8" ,"bold"))   # item allows us to get the first data

            # adding the guessed states in list
            guessedStates.append(state.states.item())


screen.mainloop()
