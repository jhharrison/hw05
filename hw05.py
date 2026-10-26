"""
Name: Jae Harrison
Peers: none
References: online textbook
"""
#My biggest problem overall was incorrect formatting
#For example
#Typing the error printouts correctly
#Having the return function be inside the same loop as the other functions

def get_letter():
    """ Use input to ask for and return a valid uppercase letter character. """
    while True:
        letter = input("Give me a single uppercase letter: ")
        
        if len(letter) != 1:
            print("Error: it needs to be a single character.")
            continue
        
        if letter != "A" and letter != "B" and letter != "C":
            print("Error: You provided the wrong character.")
            continue       
    
        return letter

def get_digit():
    """ Ask for and return a valid digit character. """
    while True:
        digit = input("Give me a single number character: ")
        
        if not digit.isdigit():
            print("Error: your input should be only digits.")
            continue
        
        if digit != "1" and digit != "2" and digit != "3":
            print("Error: a single digit needs to be in [1,3].")
            continue
    
        return digit


def check_pattern(letter, digit, lst):
    """ Print each string containing a letter before a digit. """
    print("Strings with the pattern: ")
    
    for word in lst:
        found = False
        
        for i in range(len(word)):
            if word[i] == letter:
                for j in range(i + 1, len(word)):
                    if word[j] == digit:
                        found = True
                        break
            if found:
                break
        if found:
            print(word, end=" ") 
#this was difficult to figure out interms of how to communicate the conditions, but I got there through trial and error    
    print()

#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ Get a letter-digit pair and search inside a provided list for matches."""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]      
    # -------------------------------------------------

    #Repeat the search until the user chooses to stop
    while True:
        letter = get_letter()
        digit = get_digit()
        
        check_pattern(letter, digit, st_list)
        again = input("Try Again? (y/n): ")
        
        if again != "y":
            break

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()