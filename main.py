import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

all_states = data["state"].tolist()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"Score {len(correct_guesses)}/50", prompt="What's the name of a state?").title()
    if answer_state == "Exit" or answer_state == "Quit":
        missing_states = []
        for state in all_states:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("remaining_states.csv")
        break
    if answer_state in all_states:
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




