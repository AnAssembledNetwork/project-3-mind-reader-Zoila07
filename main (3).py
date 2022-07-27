     # """
#  *****************************************************************************
#    FILE:        guess.py
#
#    AUTHOR:      {Zoila-Lee Harris}
#
#    ASSIGNMENT:  Mind Reader
#
#    DATE:        June 23, 2022
#
#    DESCRIPTION: {Your Description Here}
#
#  *****************************************************************************
# randrange(1000,10000) : Gives a random four digit numbers.
import random


def guessing_game(num):
  #print(num)
  guess_number = input("Guess the four digit number: ")
  print()
  
  # while guess_number!=num:
  str_ran_num = str(num)

  correct_num = 0
  output = ""
  total_guess = 1
    
  if guess_number == str_ran_num:
    print(f"Good job you have done it!")
    print()

    playing = input("Do you want to keep playing? (yes/no) ")
    if playing == 'yes':
      main()
    else:
      print()
      print("Thank you for playing this game")


  elif guess_number != str_ran_num:
    while guess_number != str_ran_num and correct_num <= 4:
      total_guess+=1
      for i in range(4):
        if guess_number[i] == str_ran_num[i]:
          correct_num+=1
          output+=guess_number[i]
        else:
          output+="x"
        print(f"Not quite number, but you did get {correct_num} digit correct! These were the numbers in your input that were correct.\n{output}")
        correct_num = 0 
        output = ""
        print()
        

        guess_number = input("Enter your next choice of numbers: ")
        if guess_number == str_ran_num:
          print(f"Thats not a match\nIt took you only {total_guess} tries.")
          print()



          again_keep_playing = input("Do you want to keep playing? (yes/no) ")
          if again_keep_playing == 'yes':
            print()
            main()

          else:
            print()
            print("Thank you for playing this game")
        

  
# Define your function guessing_game below. All of your logic/code for playing the game should be written
# in your function guessing_game.



def main():
    num = random.randrange(1000,10000)
    guessing_game(num)
  
# Generate your random number below and pass it as an argument to your function guessing_game
    


##################DO NOT EDIT BELOW THIS LINE################
# This invokes the main function.  It is always included in our
# python programs. 
if __name__ == "__main__":
    main()