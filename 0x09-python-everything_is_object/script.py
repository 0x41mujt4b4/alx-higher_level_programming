import os
with open('answer.txt', 'r') as my_file:
    lines = my_file.readlines()
    for i in range(len(lines)):
        new_file = open(f"{i}-answer.txt", 'w')
        new_file.write(lines[i])
        print(f"created: {i}-answer.txt")
        new_file.close()
