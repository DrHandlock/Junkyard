# By Jerry Halflin

# Iteration 1.00 of reddit bot: "Account-Detective"

#Note to future user, this code has not been proved to work, it theoritically could work, this is because by the time the account_tracking has finished we will have been dead, and so would the solar system

print("Now starting program >>> Version 1.00 of Account-Detectve")


import praw
from prawcore.exceptions import NotFound
import itertools
from datetime import datetime
import os

# Authentication
reddit = praw.Reddit(
    client_id=('client_id'),
    client_secret=('client_secret'),
    user_agent='user_agent',
    username=('username'),
    password=('password')
)
print("praw Authentication")



# Variables / Lists
request_taken = False  # This will determine if the requested username to check for similars exists
request_within = 0  # This is for how many accounts have the requested username in the username
conclusion = ""  # This will be what the bot will conclude with

reddit_characters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '-', '_', ''
]

accounts = []
criteria = []  # This will store the keywords
crit_list = []  # This will store the count of how many fall into the amount of keywords listed

print("Variables Set")

def terminal():
    terminal_response = input("A terminal function has been called, respond with [y/n] to (dis)allow the action to follow: ")
    terminal_response = terminal_response.upper()
    
    if terminal_response == "Y":
        print("allowing commmand")
        input()
        return True
        
    elif terminal_response == "N":
        print("disallowing command")
        input()
        return False






# Functions
def verify(username):
    
    print("verify booting up")
    
    print(f"{username} =================== Verifying")
          
    try:
        
        reddit.redditor(username)
        print(f"{username} =================== Accepted")
        return True
        
    except NotFound:
        print(f"{username} =================== Denied")
        return False

    
    print("verify finishing")




def account_tracking():
    print("account_tracking booting up")
    
    global reddit_characters
    global accounts
    global start_tracking
    global end_tracking

    start_tracking = datetime.now()  # This will be used to clear out any confusion for any accounts created during tracking
    itertooled = itertools.product(reddit_characters, repeat=20)

    for comb in itertooled:
        result = ''.join(comb)
        print(f"{comb} ================== Unpacking")
        if result not in accounts and verify(result):
            accounts.append(result)
            print(f"{comb} ================= Appended")

    
    end_tracking = datetime.now()
    print("account_tracking finishing")



def account_finding(request_username):
    print(f"account_finding booting up with reguested {request_username}")
    
    global criteria
    global crit_list
    global request_taken
    global request_within

    crit_list = [0] * (len(criteria) + 1)  # Resetting crit_list

    for username in accounts:
        print(f"{username} ===================== Analyzing")
        crit_ammount = 0
        
        if username == request_username:
            print(f"{username} ===================== exist")
            request_taken = True

        if request_username in username:
            print(f"{username} ===================== used request username")
            request_within += 1

        for keyword in criteria:
            print(f"scanning {username} for {keyword}")
            if keyword in username:
                
                crit_ammount += 1
                print(f"{keyword} found in {username}")
        
        crit_list[crit_ammount] += 1
        print(f"{username}'s count of keywords have been appended")

    print("account_finding finishing")



def concluding(request_username):
    print("concluding booting up")
    
    global conclusion
    global crit_list
    global request_taken
    global request_within
    global start_tracking
    global end_tracking

    conclusion = f"Here are the results for finding similar/parody accounts to the requested account of {request_username}: \n\nThere was "

    if not request_taken:
        conclusion += "NOT "

    conclusion += f"an account by the name of {request_username}.\n\nThere were {request_within} usernames that had {request_username} within their username.\n"

    for percent in range(len(crit_list)):
        conclusion += f"\nThere were {crit_list[percent]} usernames that matched at least {percent} keywords.\n"

    conclusion += f"\nCase Closed\n\n^(This is only an estimate, and may be incorrect. Only accounts created between {start_tracking} and {end_tracking} were investigated. Accounts created in between these times may not be counted.)\n\nVersion 1.00"

    print("concluding finishing")
    
# ==========================Main Loop System====================================================

print("entering >>> Main Loop System")
account_tracking()  # It will start by collecting usernames across Reddit
while True:
    for message in reddit.inbox.unread(limit=None):
        print("inbox readable")
        
        if message.body.upper() == "U/ACCOUNT-DETECTIVE":
            print("Bot Account Requested For Action")
            
            message.reply(
                "Hello! I am a bot designed to find similar/parody accounts.\n"
                "Please input a username for me to check.\n"
                "Hint: It would really help me if you separated multiple words in the account with hyphens (-). Example: NO: ExampleUsername, YES: Example-Username."
            )

        # resetting account_tracking to allow knowledge
        elif message.body.upper() == "ACCOUNT_TRACKING_RESET[CODE:9997Q] TRUE" and message.author.name == "DrHandlock":
            if terminal():
                account_tracking()

        elif message.body.upper() == "PROGRAM_BREAK_MAIN_LOOP[CODE:JARI3] TRUE 10" and message.authro.name == "Drhandlock":
            if terminal():
                break
        
        else:
            print("request found")
            for_message = message.body.upper()
            criteria = for_message.split("-")
            account_finding(for_message)
            concluding(for_message)
            message.reply(conclusion)
            print("request resolved")


print("Account-Detective_v100 has ended")
