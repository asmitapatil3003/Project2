#Rock,Paper,Scissor Game
import random
cpu_score=0
player_score=0
game_over=False

while not game_over:
    player_choice=input("Rock,Paper or Scissor").capitalize()
    computer_choice = random.choice(["Rock", "Paper", "Scissor"]).capitalize()

    if player_choice==computer_choice:
        print("It's Tie!!!")


    elif player_choice=="Rock":
        if computer_choice=="Paper":
            print(f"You lose!! ,{computer_choice} covers the {player_choice}")
            cpu_score+=1
        else:
            print(f"You Win!!,{player_choice} smashes {computer_choice}")
            player_score+=1


    elif player_choice=="Paper":
        if computer_choice=="Scissor":
            print(f"You lose!! ,{computer_choice} cuts the {player_choice}")
            cpu_score += 1
        else:
            print(f"You Win!!,{player_choice} covers the {computer_choice}")
            player_score += 1

    elif player_choice=="Scissor":
        if computer_choice=="Rock":
            print(f"You lose!! ,{computer_choice} smashes the {player_choice}")
            cpu_score += 1
        else:
            print(f"You Win!!,{player_choice} cuts the {computer_choice}")
            player_score += 1


    elif player_choice.lower()=="end":
        print("Final scores:")
        print(f"cpu :{cpu_score}")
        print(f"player :{player_score}")
        game_over=True

