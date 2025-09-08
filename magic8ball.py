import random  

while True:
    question = input("Ask the Magic 8 Ball a question: (type 'quit' to exit)")
    if question == "quit":
        break 
    elif question == "":
        print ("Please ask a question!")
        continue

    answer = random.randint(1,5)

    if answer == 1:
        print ("Yes!")
    elif answer == 2:
        print ("No!")
    elif answer == 3:
        print ("Maybe...")
    elif answer == 4:
        print("Ask again later...")
    else:
        print("Without a doubt!")