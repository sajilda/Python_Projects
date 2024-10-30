import random 
list = ['rock','paper','scissor']
print("****************rokc,paper and scissor******************")
comp_choice = random.choice(list)
def output_for_user_choice(user_value):
        if comp_choice == "rock" and user_value == 'scissor' or comp_choice == 'paper' and user_value == 'rock':
            print('comp wins')
        elif user_value == "rock" and comp_choice == 'scissor' or user_value == 'paper' and comp_choice == 'rock':
            print('user wins')
        else:
            if comp_choice == user_value:
                print('its draw')
            else:
                print('Only rock,paper and scissor string are valid')



user_choice = input("What is you choice:")
print(f"The computer choice is:{comp_choice}")
final_output = output_for_user_choice(user_choice)


