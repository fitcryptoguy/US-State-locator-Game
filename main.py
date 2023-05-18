from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.screensize(700, 700)
screen.addshape("us_states.gif")

tim = Turtle()
tim.shape("us_states.gif")

data = pandas.read_csv("50_states.csv")
state_column = data["state"]

states_answered = []
states_missed = []


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(prompt_input, align="left", font=("Courier", 9, "normal"))


while True:
    prompt_input = screen.textinput(title=f"Guessed:{len(states_answered)}/50", prompt="what's another state name")
    if prompt_input is None:
        break
    prompt_input = prompt_input.title()

    try:
        row = data[state_column == prompt_input]
        x_cor = row.at[row.index[0], "x"]
        y_cor = row.at[row.index[0], "y"]
        states = States()
        states_answered.append(prompt_input)


    except:
        print("invalid state")


states_list = state_column.to_list()
for state in states_list:
    if state not in states_answered:
        states_missed.append(state)
print(f"states missed: {len(states_missed)}")
print(f"states answered: {len(states_answered)}")
state_missed_file = pandas.DataFrame(states_missed)
state_missed_file.to_csv("states missed.csv")


screen.exitonclick()
