numbers = [1, 2, 3]
new_list = []
# Add 1 to each item and print list.
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
print(new_list)


# LIST COMPREHENSION METHOD TO DO THIS SAME:-
# new_list = [new_item for item in list]
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Angela"
new_list = [letter for letter in name]
print(new_list[::-1])  # Reverse string
print(new_list)

range_list = [n*2 for n in range(1, 5)]
print(range_list)

# CONDITIONAL LIST COMPREHENSION:-
# new_list = ['new_item' 'for' item 'in' list 'if' test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_list = [name for name in names if len(name) < 5]
print(new_list)
new = [name.upper() for name in names if len(name) > 5]
print(new)


# In USA program we can append the exit code as :-
# missing_state = [state for state in all_states if state not in guessed_state]
