import random

def coin_toss():
    print("Let's have a coin toss.")
    call = ["head", "tail"]
    my_call = input("What is your call? Head or Tail: ").strip().lower()
    
    if my_call not in call:
        print("Invalid input. Please choose 'head' or 'tail'.")
        return
    
    appears = random.choice(call)
    
    print(f"You chose {my_call}.")
    print(f"It appears {appears}.")

    if my_call == appears:
        print("Congratulations! You won the toss.")
    else:
        print("Sorry, the opponent won the toss.")

coin_toss()
