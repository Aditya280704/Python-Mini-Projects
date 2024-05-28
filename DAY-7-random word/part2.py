import random
word_list = ["advark","baboon","camel"]
random_choice = random.randint(0,len(word_list))
chosen_word = word_list[random_choice]
guess = input(("Guess a Letter : "))
lowername = guess.lower()
for letter in chosen_word: #if chosen word is camel then letter gets replaced by c then a then m then e then l... and the
    #checks the condition..
    if letter == lowername:
        print("Match")
    else:
        print("Wrong")

#video 73 - how to replace every letter of chosen word in blank space 
display = [] #empty list.....
for letter in chosen_word:
    display += "_"
print(display)    

#2nd method using range 
for letter in range(len(chosen_word)):
    display += "_"
print(display)    


# Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter 
print(display)        


# letter = chosen_word[position]
# Inside the loop, this line retrieves the character at the
# current position within the chosen_word and assigns it to the variable letter.
# The position variable holds the index value obtained from the loop iteration.        
        

    