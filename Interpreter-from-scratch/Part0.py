from os import read
import os
import win10toast

#simple notification system
toaster = win10toast.ToastNotifier()

#Assignment 1
#Take a string as an input, and return it with no spaces or uppercase letters
def NoSpaceLowercase(str):
    return str.replace(" ", "").lower()

#Assignment 2
#Take out any comments from the input
def NoComments(str):
    try:
        return NoSpaceLowercase(str[:str.index("//")])
    except ValueError:
        return NoSpaceLowercase(str)

#Assignment 3
#return a line only if there are only letters, otherwise throw an error
def LettersOnly(str):
    if NoComments(str).isalpha():
        return NoComments(str)
    else:
        raise ValueError("Only letters allowed")

#Assignment 4
#takes a file and returns the lines formatted and concatinated
def FileFormatting(file):
    result = []
    with open(file, "r") as f:
        file1 = f.readlines()
    for line in file1:
        try:
            result.append(LettersOnly(line.rstrip("\n")))
        except ValueError:
            continue
    return "".join(result)

if __name__ == "__main__":
    #Assignment 1 tests
    test1 = "Hello World!"
    assert NoSpaceLowercase(test1) == "helloworld!"
    test2 = "this is quite a LONG sentence, is it not?"
    assert NoSpaceLowercase(test2) == "thisisquitealongsentence,isitnot?"

    #Assignment 2 tests
    test1 = "Hello World! //commented out"
    assert NoComments(test1) == "helloworld!"
    test2 = "this is quite a LONG sentence, is it not?"
    assert NoComments(test2) == "thisisquitealongsentence,isitnot?"

    #Assignment 3 tests
    test1 = "Apple Pear Banana // Comment on the morality of fruit as a pizza topping. Or do something else with your time"
    assert LettersOnly(test1) == "applepearbanana"
    test2 = "this is quite a long sentence, // is it not?"
    try:
        LettersOnly(test2)
    except ValueError as error:
        assert error.args[0] == "Only letters allowed"

    #Assignment 4 tests
    #Paste file path below if testing it
    file1 = "program.txt"
    assert FileFormatting(file1) == "avdqvdmavvqmiqiiifvdlfbffiiiflblblfbqviiifbfiiifwdfwwiif"
    
    toaster.show_toast("Part0", "All test cases passed", duration = 5)
