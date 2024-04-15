from turtle import Screen, shape, Turtle
import pandas as pd

screen = Screen()
screen.setup(725, 491)
screen.title('U.S States Game')
screen.bgpic("blank_states_img.gif")

pen = Turtle()
pen.speed(0)
pen.color('black')
pen.hideturtle()

# Read U.S. States from csv
csv = pd.read_csv('50_states.csv')
all_states = csv["state"].to_list()
print(all_states)
guessed_states = []

while True:
    answer = screen.textinput("Guess the State", "What's another state's name?")
    if answer == 'Exit':
        break
    state_data = csv[csv['state'] == answer]

    if state_data.empty:
        continue

    state_name = state_data.state.item()
    guessed_states.append(state_name)

    pen.penup()
    pen.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
    pen.write(state_name, align='center', font=('Arial', 7, 'bold'))


# Store missing state to learn into csv
missing_states = [state for state in all_states if state not in guessed_states]
export_df = pd.DataFrame(missing_states)
export_df.to_csv('missing_states.csv')

