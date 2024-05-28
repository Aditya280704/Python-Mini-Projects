# ERRORS
try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["ssdff"])
# As there is no exception mentioned in except so the dictionary error will also not be caught..
# except:
#     # below code creates a file and writes inside it
#     file = open("a_file.txt", "w")
#     file.write("something")

# This code will catch dictionary error
except FileNotFoundError:
    # below code creates a file and writes inside it
    file = open("a_file.txt", "w")
    file.write("something")

else:
    content = file.read()
    print(content)

finally:
    raise TypeError("this is an error i made up")

