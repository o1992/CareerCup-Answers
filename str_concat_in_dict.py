dictionary = {'world': '', 'hello': '', 'super': '', "hell": ''}


def isValidConcatination(string):
    if len(string) == 0:
        return True
    for i in range(len(string) + 1):
        if string[:i] in dictionary:
            if isValidConcatination(string[i:]):
                return True
    return False

print(isValidConcatination("worldjworld"))
# You're given a dictionary of strings, and a key. Check if the key is composed of an arbitrary number of concatenations of strings from the dictionary. For example:
#
# dictionary: "world", "hello", "super", "hell"
# key: "helloworld" --> return true
# key: "superman" --> return false
# key: "hellohello" --> return true
#
# - davelee71047 October 25, 2014 in United States | Report Duplicate | Flag
# Facebook Software Engineer Intern Algorithm
