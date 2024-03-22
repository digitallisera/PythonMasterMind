import random       # to get random numbers
import os           # to clear screen

#
# Mastermind
#
# 1) Spelet slumpar fram 4st tecken av tecken från A - H. Resultatet är hemligt för spelaren.
# 2) Spelet ber spelaren gissa vilka 4 tecken det är och i vilken ordning.
# 3) Spelet kontrollerar svaret och berättar för spelaren hur många tecken som var rätt OCH på rätt plats. Och vilka tecken som var rätt men på fel plats.
# 4) Spelet ber återigen spelaren att gissa. 
# 5) Spelaren får gissa tills alla tecknen är rätt, max omgångar (20) har uppnåtts eller spelaren väljer att avbryta spelet.
#
# Antalet omgångar, antalet tecken att gissa på och antalet tecken som är gissningsbara är konfigurerbara via variabler initialt i koden nedan.
# En cheat mode kan användas under utvecklingen för att se vad det korrekta svaret är, detta styrs genom variabeln "cheat_mode".
#
#

        
#
# Config/setup
#

# Setup values
num_of_char_to_guess_on = 4                     # number of characters to guess on
num_of_char_to_guess_from = 8                   # number of characters to guess from 
possible_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    # Characters to play with
num_of_max_rounds = 20                          # maximum number of rounds for guessing
cheat_mode = False                              # when this is sat to True, the answer is displayed in the header when playing the game.

# Text colors, etc
text_reset = '\033[0m'
text_bold = '\033[01m'
text_underline = '\033[04m'
text_green = '\033[32m'
text_orange = '\033[33m'
text_red = '\033[31m'
text_black = '\033[30m'


# 
# Get the list with random characters (the answer in the game).
#
def get_right_answer(num_of_random_char,num_of_char_to_random_from, char_string):
    answer_list = []                                    # List for answers
    for i in range(0,num_of_random_char):
        # get a random number between 0 (zero) and upper limit, translate it to a character and append the character as an element to the list
        answer_list.append(char_string[random.randint(0,num_of_char_to_random_from-1)])
    return answer_list


#
# Display the game rules.
#
def output_game_rules(num_of_random_char,num_of_char_to_random_from,char_string):
    os.system('cls')
    print(text_green+text_bold+"Welcome to play MasterMind!"+text_reset)
    print()
    print(f"{text_underline}Game rules{text_reset}")
    print()
    print(f"I will select {num_of_random_char} number of characters from the characters {char_string[0:num_of_char_to_random_from]}")
    print("Your job is to find out the characters and place them in the right order.")
    print("A character could exist multiple times.")
    print("For every game round I will display how many characters which is right and on the RIGHT position. They will have a green symbol ("+text_green+"☻"+text_reset+").")
    print("And also how many characters which are right but on the WRONG position. They will have a yellow symbol ("+text_orange+"☻"+text_reset+").")
    print()
    print("Ready? Good luck - you will need it! ;)")
    print()
    print("Press [ENTER] to start the game")
    print("Type 'Q' to Quit")
    print()


#
# Display the information about previous rounds during the game.
#
def output_ongoing_game(num_of_random_char,num_of_char_to_random_from,char_string,player_round_list,right_answer_list):
    # convert right answer list to string, for debug output...
    if cheat_mode: 
        answer_str = " (" + "-".join(str(element) for element in right_answer_list) + ")"
    else:
        answer_str = ""
    os.system('cls')
    print(text_green+text_bold+"Playing MasterMind!"+text_black+answer_str+text_reset)
    print()
    print(f"Type {num_of_random_char} of the characters ({char_string[0:num_of_char_to_random_from]}) in right order and finish with ENTER/RETURN.")
    print("A character can appear several times.")
    print()
    
    # Go through the previous round results and display them to help the player found the right answer
    # But only if any previous round exist.
    if len(player_round_list) > 0:
        print("This is your answers and result on previous rounds.")
        print(text_green+" ☻ "+text_reset+"means you got one right character on the right place.")
        print(text_orange+" ☻ "+text_reset+"means you got one right character but on the WRONG place.")
        print("----------------------------------------------------------------------------------------------")
        
        for i in player_round_list:
            output_row = "| "
            # display characters
            for j in i["answer"]:
                output_row = output_row + j + " | "    
            # display how many characters are right AND on the right position
            for j in range(0,i["num_of_right_char_and_pos"]):
                output_row = output_row + text_green + "☻" + text_reset + " "     
            # display how many characters are right but NOT on the right position       
            for j in range(0,i["num_of_right_char_not_pos"]):
                output_row = output_row + text_orange + "☻" + text_reset + " "
            print(output_row)
            print("----------------------------------------------------------------------------------------------")
        print()

    print("Type 'Q' if you give up!")
    print()


#
# Get the input from the player during the game.
#
def get_player_round_input(num_of_random_char,num_of_char_to_guess_from,possible_char):
    input_valid = False
    while not input_valid:        
        input_char = input(">> ")     # \r to clear console line before input
        if len(input_char)!=num_of_random_char and input_char!="Q" and input_char!="q":
            print(f"You must enter {num_of_random_char} of this uppercase characters: {possible_char[0:num_of_char_to_guess_from]}. Try again.")
            input_valid = False
        else:
            input_valid = True
    return input_char.upper()


#
# Check the answer from the player and compare it with facit.
# And produce information to the player how many characters that was right and on the right place - and wrong place...
#
def calc_round_result(facit,answer):

    # Find right char on right positions
    num_of_right_char_and_pos = 0
    index = 0
    rest_answer = ""
    rest_facit = ""
    # Loop facit list
    for i in facit:     
        # right answer   
        if i == answer[index]: 
            num_of_right_char_and_pos += 1             
        # wrong answer
        else:
            rest_answer = rest_answer + answer[index]
            rest_facit = rest_facit + i                 # build up a string with the characters from facit which was not right in the answer from the player      
        index += 1

    # Find right chars on wrong positions
    num_of_right_char_not_pos = 0
    new_rest_answer = ""
    # Loop the rest of the facit list, which was not right in the answer from the player
    for i in rest_facit:
        char_is_found = False
        # Loop the rest of the answer list, which was not right in the answer from the player 
        for j in rest_answer:
            # char is equal (and no previous equal)
            if i == j and not char_is_found:
                num_of_right_char_not_pos += 1
                char_is_found = True
            # char is not equal
            else:
                new_rest_answer = new_rest_answer + j       # build up a string with the characters from rest_answer which was not found compared to the current char from facit string
        rest_answer = new_rest_answer                       # prepare to loop the rest of the characters again with next character from the facit string 
    
    # Set dictionary with the return values
    round_dict = {
        "answer": answer,
        "num_of_right_char_and_pos": num_of_right_char_and_pos,
        "num_of_right_char_not_pos": num_of_right_char_not_pos
    }

    return round_dict


#
# Main function
#
def main():

    player_menu_input = ""
    best_game_rounds = 20       # Keep track on best game result

    # Continue the play until player input "q" to quit
    while player_menu_input != "Q" and player_menu_input != "q":    

        # Output info about the game rules
        output_game_rules(num_of_char_to_guess_on,num_of_char_to_guess_from,possible_char)

        player_menu_input = input(">> ")   

        # new game is selected
        if player_menu_input != "Q" and player_menu_input != "q" :

            num_of_rounds = 0           # counter for the rounds
            player_round_list = []      # list with dictionaries holding the answer, num of char on right position and num of char on wrong positions
            exit_reason = ""            # reason exiting the round loop (Q=quiting, V=Victory, M=Max rounds)
            next_round = True           # flag for round loop

            # Get a list with 4 random characters from A to H
            random_answer = get_right_answer(num_of_char_to_guess_on,num_of_char_to_guess_from,possible_char)

            while next_round == True:

                # Output the previous rounds and result
                output_ongoing_game(num_of_char_to_guess_on,num_of_char_to_guess_from,possible_char,player_round_list,random_answer)
                # Get the player input and validate the answer
                player_round_input = get_player_round_input(num_of_char_to_guess_on,num_of_char_to_guess_from,possible_char)
                # Count the rounds
                num_of_rounds += 1                

                # Find out if the game is over and the reason
                if player_round_input[0] == "Q" or player_round_input[0] == "q" : exit_reason = "Q"
                elif num_of_rounds > num_of_max_rounds: exit_reason = "M"

                # Set flag to continue the game or not
                next_round = exit_reason == ""

                # Calc the round result and add it to list of rounds
                if next_round:
                    # compare the quess with the facit
                    round_result = calc_round_result(random_answer,player_round_input)
                    # append result dict to the list
                    player_round_list.append(round_result)                    
                    # check if the right answer is given and keep reason and abort input
                    if num_of_char_to_guess_on == int(round_result["num_of_right_char_and_pos"]): 
                        exit_reason = "V"
                        next_round = False

            # Take action and display different info depending on reason the game was ended
            if exit_reason == "V":
                print(f"\n{text_red}{text_bold}Congrats!!!{text_reset}\nYou have entered the correct answer after {num_of_rounds} rounds.")
                if best_game_rounds > num_of_rounds:
                    print(f"And even better, you have beaten the previous record which was {best_game_rounds} rounds!")
                    best_game_rounds = num_of_rounds
            elif exit_reason == "Q":
                print(f"\n{text_red}{text_bold}Quiting{text_reset}\nYou have choosen to quit the game. Try a new round!")
                print(f"The right answer is: {text_green}" + "-".join(str(element) for element in random_answer) + text_reset)
            elif exit_reason == "M":
                print(f"\n{text_red}{text_bold}Sorry!{text_reset}\nYou have reached {num_of_max_rounds} rounds, which is the maximum.")
                print(f"The right answer is: {text_green}" + "-".join(str(element) for element in random_answer) + text_reset)

            # Go back to menu 
            input("\nPress [ENTER] for the menu. ")

            # Reset input string
            player_menu_input = ""     

    print("\nThanks for playing!\n")



main()






