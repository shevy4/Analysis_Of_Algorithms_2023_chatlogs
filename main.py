from collections import defaultdict
import tableprint as tb
import tqdm
from time import sleep

logs = [["08:00:13 From Jack Johnson: hello to everyone"],
        ["08:00:21 From Emily Smith: hello"],
        ["08:00:29 From Chris Brown: hello"],
        ["08:00:34 From Chris Brown: hi again everyone!"]]

# Init of default dictionary, this handles key errors arising from a normal dictionary
chatlog = defaultdict(list)


# This Function returns the average frequency of messages sent by a particular student
def parse_grade(name):
    return str((len(chatlog.get(name.casefold())) / len(logs)) * 100) + "%"


# This function splits the chat-log in reorganizes it by indexing
def parse_chat():
    for line in logs:
        chatlog[line[0].split(" ")[2].casefold() + " " + line[0].split(" ")[3].casefold().strip(":")].append(
            line[0].split(" ")[0] + line[0].split(":")[3])


# Simple loading bar for aesthetics
def loading_animation(length):
    for _ in tqdm.tqdm(range(length), desc="Grading..."):
        sleep(.5)


# This function displays the student name, number of messages and the message sent
def display_chats(name):
    if name.casefold() == "exit":
        exit(0)

    message = []
    data = []
    # Iterates chat-log using O(n) complexity
    for key, value in chatlog.items():
        if name.casefold() == str(key).casefold():
            message = value
            break
    # If the message length is 0 then student name is not found in chat
    if len(message) == 0:
        print("Invalid Name, Not Found")
        return

    # Displays student info in a table
    headers = ["Message Frequency", "Message"]
    for x, y in enumerate(message):
        data.append(["[" + str(x + 1) + "]"] + [y])
    loading_animation(len(logs))
    if str(message).split(" ")[1].replace("'", "").replace("]", "") == "":
        data.append(["Participation Grade : "] + [0])
    else:
        data.append(["Participation Grade : "] + [str(parse_grade(name))])
    tb.banner("Student Name : " + name, 1)
    tb.table(data, headers)
    return


if __name__ == '__main__':
    parse_chat()
    while True:
        display_chats(input("Enter Name To Search or 'exit' to exit\n"))
