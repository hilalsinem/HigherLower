from art import logo, vs
from game_data import data
import random

#Step 1: Print the logo
print(logo)


#Step 2: Define a function to randomize celebrities
def randomize():
    famous = random.choice(data)

    return famous

#Step 3: Define a function to compare the followers of the famous people
def compare(fame1, fame2):
    """Take celebrities as inputs"""
    follower_1 = fame1['follower_count']
    follower_2 = fame2['follower_count']
    print(follower_1)
    print(follower_2)
    if follower_1 > follower_2:
        winner = fame1
        return winner
    elif follower_2 > follower_1:
        winner = fame2
        return winner
score =0
end_of_game = False
famous1 = randomize()
famous2 =randomize()
#Step 4: After function select someone, they should not be in the list to be selected anymore
while famous2 == famous1:
    famous2 = randomize()

while not end_of_game:
    print(f"Compare A: {famous1['name']}, {famous1['description']}, {famous1['country']}")
    print(vs)
    print(f"Against B: {famous2['name']}, {famous2['description']}, {famous2['country']}")
    print(compare(famous1,famous2))
    answer = input("Who has more follower ? Type A or B")
    if answer == "A":
        if compare(famous1,famous2) == famous1:
            print("*****CORRECT*****")
            score += 1
            next_famous = famous1
            data.remove(famous2)
            famous2 = randomize()
            while next_famous == famous2:
                famous2 = randomize()
        else:
            print("*****WRONG*****")
            print(f"Your score: {score}")
            end_of_game = True
    if answer == "B":
        if compare(famous1,famous2) == famous2:
            print("*****CORRECT*****")
            score += 1
            famous1 = famous2
            next_famous = famous1
            data.remove(famous2)
            famous2 = randomize()
            while next_famous == famous2:
                famous2 = randomize()
        else:
            print("*****WRONG*****")
            print(f"Your score: {score}")
            end_of_game = True
