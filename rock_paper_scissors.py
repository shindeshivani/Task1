import random
class RPS_game:
   def __init__(self) -> None:
      self.round=1                                     # initatizing varibles for futher use
      self.win=0
      self.draw=0
      self.lose=0
      pass

   def get_input(self):
      given_list=["rock","paper","scissors"]
      user_input= input("Choose one of the following:\nRock, Paper, Scissors : ").lower() #user input
      if user_input in given_list:                       #checking the entered input
         print("Your input : {}\n".format(user_input))
         return user_input                               #indicates valid input
      else:
         print("Enter propre input : ")                   #error message for unvalid input
         self.round-=1
         self.play_again()
         return None                                     # indicates invalid input 
       

   def choose_random(self):                              #generating system's input
      given_list=['rock','paper','scissors']
      sys_input=random.choice(given_list)                #choicing item amoung's the list
      print("System's input : {}\n".format(sys_input))
      return sys_input                                   #returns system generated input
   
   def match(self,user_input,sys_input):                 #conditions to decide the winner
      if (user_input=='rock' and sys_input=='scissors') or\
         (user_input=='scissors' and sys_input=='paper') or\
         (user_input=='paper' and sys_input=='rock'):
         print("You Win!")
         self.win+=1                                        #increasing the win counter
      elif user_input == sys_input :
         self.draw+=1                                       #increasing the draw counter
         print("Match is draw.")    
      else:
         print("You lose!")
         self.lose+=1                                       #increasing the lose counter
      

   def play_again(self):                                 # for playing game multiple times
      play_a=input("Do you want to play again? Y\\N : \n").lower()
      if play_a=='y':
         self.round+=1                                     #increasing the round counter
         print("Round {} starts.\n".format(self.round))
         self.loop()                                       #calling loop function to execute

      elif play_a=='n':
         self.end_game()                                  #calling for termination

      else:
         print("Enter correct input.\n")
         self.play_again()                                #calling to play again

   def end_game(self):                                 #conditions for terminating the game
      if self.win>self.lose:
         print("You won by {} points\n".format(self.win-self.lose))
         
      elif self.win<self.lose:
         print("You lost by {} points\n".format(self.lose-self.win))

      elif self.round==0:
         print("No-one played!")
         
      else:
         print("The match is a draw.\n")
      self.message()


   def message(self):                                   #message for terminating the game
      print("Total matches\t: {}\nDraw matches\t: {}\nYour score\t: {}\nSystem's score\t: {}".format(self.round,self.draw,self.win,self.lose))
      print("See you next time.")
            

   def loop(self):                                       #looping function to repeat every function for multiple rounds
      user_input=self.get_input()
      if user_input is not None:                         #proceeding only if the user input is valid
         sys_input=self.choose_random()
         self.match(user_input,sys_input)
         self.play_again()      

obj=RPS_game()
obj.loop()




         
