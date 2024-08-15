#by Jerry Halflin
import random



stratagy_name = "S P A R C : Sicsor Paper And Rock Calulater"

"""
Simplfied version of what should happen: 
By Jerry Halflin (4/3/24)

(WHILE LOOPED)

input(what the oppoenent played, or whether or not this a new player)

adds the input to a string
↓
RRPPSS < R (Rock/R is added)   

then it checks if this is a similar to a pattern it knows
↓

checking history...

if they have a similar pattern:

  input(RRPPSSR) ~ history(RRPPSSRR)
  ↓
  return paper/P because it will think the opponent will play Rock

  If there is muliple patterns that are similar, then will run a 
  incorperate the likelihood system down below↓




elif they can't reconize the pattern: (likelihood system)

*at the end of player's game, it will record this pattern into 
the .txt file for remembering*

  it will turn the turn # your on and look at how favorable each    option is for that #

  example: 

    4 (turn number)
    R: 120 < most likely
    P: 91
    S: 100

    will return paper

  btw, all these numbers on default will be 100 whenever we    
  reach a turn with no data (except for the first turn, since  
  rock is the most likely, it will be put to 120) and also if 
  there is two or more that most likely due to them sharing the 
  same number, rather than going with random we will go to the 
  "personal likelihood system" which will be similar to 
  "likelihood system" except that this one is only based on the 
  opponent's history, and not the whole history

  example:

    [PLS]
    R: 4
    P: 1
    S: 5 < most likely 

    will return Rock

  if this fails to work, then we will just do random for the 2 or 3 most likely option




"""

#List
strat_mem =  [
    "RPRS",        # First Pattern
    "RRRRRRRRRR",  # Repetitive Rock
    "PPPPPPPPPP",  # Repetitive Paper
    "SSSSSSSSSS",  # Repetitive Scissors
    "RPSRPSRPSR",  # Alternating sequence
    "RSPPSRPRSP",  # Semi-predictable
    "SPRSPRSPRS",  # Semi-predictable reverse
    "RRSPPRRSPP",  # Double tap strategy
    "SSPRRPPRSS",  # Scissors heavy with mixes
    "PPRRSSPPRR",  # Paper and Rock preference
    "RSPRSPPRSR",  # Complex pattern
    "PSRPSRPSRP",  # Complex pattern reverse
    "RRPPSSRRPP",  # Preference for each, in turns
    "PRSPPRSPRS",  # Avoids repeating immediately
    "SPPRRSPSPR",  # Scissors less common
    "RRSPSPRSPS",  # Starts with Rock, complex follow-ups
    "PPRSSPRSPR",  # Starts with Paper, complex follow-ups
    "SSRPRSPRSP",  # Starts with Scissors, complex follow-ups
    "RSPSPSPRSP",  # Favoring no Scissors
    "PRSPRSPRSP",  # No consecutive repeats
    "SRPRSPRSPR",  # Alternating without starting repeat
]
rec_list = [] #recommending the next move based on the
r_list = [
    0, #PLS
    50,  
    45,  
    60,  
    40,  
    55,  
    50,  
    65,  
    35,  
    70,  
    45,  
    55,  
    30,  
    75,  
    50,  
    40,  
    60,  
    45,  
    55,  
    65,  
    50, 
    0 #Overrunning Error
]
p_list = [ 
    0, #PLS
    45,  
    50,   
    40,  
    60,  
    50,  
    55,  
    35,  
    65,  
    40, 
    70,  
    45,  
    55,  
    30,  
    75,  
    50,  
    45,  
    60,  
    40,  
    55,
    65,  
    0 #Overrunning Error
]
s_list = [ 
    0, #PLS
    55,  
    45,  
    50,  
    40,  
    45,  
    60,  
    55,  
    45,  
    60,  
    40,  
    65,  
    70,  
    45, 
    30,  
    55,  
    50,  
    35,  
    65,  
    40,  
    45,  
    0 #Overrunning Error
]


#Variables
turn = 0
opp_play = ""
new_pattern = False
option = "DEFAULT"

opp_score = 0
our_score = 0
our_move = "DEFAULT"
opp_move = "DEFAULT"

#Function
def check_pat(): 
  global rec_list
  global new_pattern
  rec_list = []


  valid = True

  for opt in strat_mem: #pattern
    valid = True

    if len(opt) <= len(opp_play):
      pass #skips if the pattern is too short

    else:
      for char in range(len(opp_play)):
        if opt[char] != opp_play[char]:
          valid = False


      if valid:
        rec_list = opp_create(opt[len(opp_play)])



  if rec_list != []:

    return rec_list
  else: 
    # new_pattern = True
    return ls(True, True, True)


   #==================================================   
def ls(r, p, s): #ls AKA Likelihood System

  global r_list
  global p_list
  global s_list
  global turn
  global our_move

  #print("ls active \n")

# Normal Conditions where their is a more likely option



  if r and r_list[turn] > p_list[turn] and r_list[turn] > s_list[turn]:
    our_move = "P"
    return "P" #Opposite to R

  elif p and p_list[turn] > r_list[turn] and p_list[turn] > s_list[turn]:
    our_move = "S"
    return "S" #Opposite to P

  elif s and s_list[turn] > r_list[turn] and s_list[turn] > p_list[turn]:
    our_move = "R"
    return "R" #Opposite to S

# Conditions where there is a tie between 2 options

  elif r and p and r_list[turn] == p_list[turn] > s_list[turn]:
   return pls(True, True, False)

  elif r and s and r_list[turn] == s_list[turn] > p_list[turn]:
    return pls(True, False, True)

  elif p and s and p_list[turn] == s_list[turn] > r_list[turn]:
    return pls(False, True, True)

# Conditions where there is a tie between 3 options
  elif r and p and s and r_list[turn] == p_list[turn] == s_list:
    return pls(True, True, True)

  else:
    return "ERROR OCCURED"
#============================================================

def pls(r, p, s): #ls AKA Personal Likelihood System

  global r_list
  global p_list
  global s_list
  global turn
  global our_move

  #print("pls active")

  # Normal Conditions where their is a more likely option
  if r and r_list[0] > p_list[0] and r_list[0] > s_list[0]:
    our_move = "P"
    return "P" #Opposite to R

  elif p and p_list[0] > r_list[0] and p_list[0] > s_list[0]:
    our_move = "S"
    return "S" #Opposite to P

  elif s and s_list[0] > r_list[0] and s_list[0] > p_list[0]:
    our_move = "R"
    return "R" #Opposite to S

  # Conditions where there is a tie between 2 options

  elif r and p and r_list[0] == p_list[0] > s_list[0]:
    return last_resort(True, True, False)

  elif r and s and r_list[0] == s_list[0] > p_list[0]:
    return last_resort(True, False, True)

  elif p and s and p_list[0] == s_list[0] > r_list[0]:
    return last_resort(False, True, True)

  # Conditions where there is a tie between 3 options

  elif r and p and s and r_list[0] == p_list[0] == s_list[0]:
    return last_resort(True, True, True)

#==========================================================
def opp_create(og): #creating the opposite of the what the program thinks they will play
  opp_mapping = {"R": "P", "P": "S", "S": "R"}

  return opp_mapping.get(og, "Invalid option")

#============================================================
def last_resort(r, p, s): #last resort, if all else fails, we will just do random


  #print("last_resort active \n")



  finish_result = False 
  #that way if random chooses a number it shouldn't it will do another one

  while not finish_result:
    rand = random.randint(1, 3)


    if r and rand == 1:
      finish_result = True
      return "P" #Opposite of R

    elif p and rand == 2:
      finish_result = True
      return "S" #Opposite of P

    elif s and rand == 3:
      finish_result = True
      return "R" #Opposite of S

#===========================================================
def create_history(): #deleting and rewriting the history file
  #print("create_history active")

  #LIST UPDATING

  if option == "R":
    r_list[turn] += 1 # Likelihood System
    r_list[0] += 1 # Personal Likelihood System
  elif option == "P":
    p_list[turn] += 1 
    p_list[0] += 1 
  elif option == "S":
    s_list[turn] += 1 
    s_list[0] += 1 



  """
  REMEMBER TO DELETE THIS FILE ONCE THE PROGRAM IS DONE AND HAS 
  LEARNED. ONCE THIS IS BEING PUBLISHED TO THE CLASS, WE WILL   
  PUT ALL THE DATA IN THE CORRECT SPOTS↓↓ 




  #FILE HISTORY IMPORTING AND EXPORTING

  open('file.txt', 'w').close() #clear the whole file
  file = open("Team5_History.txt", "a")
  file.write(str(r_list) + "\n" + str(p_list) + "\n" + str(s_list) + "\n" + str(strat_mem))
  """
#===============================================================
"""
  THIS FUNCTION WAS REMOVED DUE TO CONFUSION

  def update_score():

  global our_move
  global option
  global opp_score
  global our_score


  combat = str(option) + str(our_move)

  # 1 is lose, 2 is win
  win_lose = {"RS" : 1, "PR" : 1, "SP" : 1, "RP" : 2, "PS" : 2, "SR" : 2}

  if option == our_move: # TIE

    print("TIE \n")

  elif win_lose.get(combat) == 1:
    print("LOSE \n")
    opp_score += 1

  elif win_lose.get(combat) == 2:
    print("WIN \n")
    our_score += 1

  print("Opponent Score: " + str(opp_score) + "\n")
  print("Our Score: " + str(our_score) + "\n")
"""   
#===============================================================



# Neat Intro; spells out "SPARC"

print(" ###   ####   ####         #####")
print("#      #  #   #  #         #")
print(" ###   ####   ####   ####  #")
print("    #  #      #  #   #     #")
print(" ###   #      #  #   #     ##### \n")

print("#" * 31 + "\n")
print("Siccor Paper And Rock Calulater (S P A R C) \n")




#Tutorial
print("To play this game type R for Rock, P for Paper, and S      for Scissors.\n")
print("If a new player is here, type N.\n")

print("for Debuging purposes, type D \n") #DEBUGGING

print("Once your inputed something, we will reply with the best option \n")

print("Okay, to make this work, you must first play one game without assisance to see what we are up against. \n")

for x in range(20): #only 20 turns


  option = input("What did oppoent play last turn\n")
  option = option.upper()

  if option == "R" or option == "S" or option == "P":

    turn += 1
    opp_play += str(option)

    print(check_pat())
    create_history()


  elif option == "N": #New Player

    if new_pattern:
      strat_mem.append(opp_play)

    turn = 0
    opp_play = ""
    print("New Player Intiated \n")

    r_list[0] = 0
    p_list[0] = 0
    s_list[0] = 0





  #=================== DEBUGGING =====================
  elif option == "D": 

    print("Debug: Check_Pat - 1")
    print("Debug: LS - 2 [NOT USABLE FOR DEBUGGING]")
    print("Debug: PLS - 3 [NOT USABLE FOR DEBUGGING]")
    print("Debug: Opp_Create - 4")
    print("Debug: Last_Resort - 5 [NOT USABLE FOR DEBUGGING]")
    print("Debug: Create_History - 6")
    print("Debug: Update_Score - 7 [REDACTED]")



    option = input("What Debug option do you want to use? ")
    if option == "1":

      option = input("Input Normally")
      print(check_pat())

    elif option == "2":
      turn += 1
      print(ls(bool(input("r")), bool(input("p")), bool(input("s"))))
      turn -= 1

    elif option == "3":
      turn += 1
      print(pls(bool(input("r")), bool(input("p")), bool(input("s"))))
      turn -= 1
    elif option == "4":
      print(opp_create(input("Input")))

    elif option == "5":
      print(bool(input("Input ")))
      print(bool("False"))
      print(bool("True"))
      print(last_resort(bool(input("r")), bool(input("p")), bool(input("s"))))

    elif option == "6":
      create_history()

    elif option == "7":
      option = input("Option Value: ")
      our_move = input("Our Move: ")


# =============== END OF PROGRAM ==========================
print("Thank you for playing! \n")
print("You have hit the limit of 20 turns, this program has finish \n")
print("Scissor Papers Rock Calulater (S P A R C) \n")

