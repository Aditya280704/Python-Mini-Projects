# ERRORS
try:  # Something that my cause an exception
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["ssdff"])
# As there is no exception mentioned in except so the dictionary error will also not be caught..
# except:
#     # below code creates a file and writes inside it
#     file = open("a_file.txt", "w")
#     file.write("something")

# This code will catch dictionary error
except FileNotFoundError:  # Do this if there was an exception
    # below code creates a file and writes inside it
    file = open("a_file.txt", "w")
    file.write("something")

else:  # Do this if there are no exceptions
    content = file.read()
    print(content)

finally:  # Do this no matter what happens
    file.close()
    print("File was closed")



