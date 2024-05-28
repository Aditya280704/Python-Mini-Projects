import random
word_list = ["advark","baboon","camel"]

len(word_list)
random_choice = random.randint(0,len(word_list))
print(random_choice)
chosen_word = word_list[random_choice]

guess = input(("Guess a Letter : "))
lowername = guess.lower()

for letter in chosen_word: #if chosen word is camel then letter gets replaced by c then a then m then e then l... and the
    #checks the condition..
    if letter == lowername:
        print("Match")
    else:
        print("Wrong")
        
        
        
