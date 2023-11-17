from collections import defaultdict

logs = [["08:00:13 From Jack Johnson: hello to everyone"],
        ["08:00:21 From Emily Smith: hello"],
        ["08:00:29 From Chris Brown: hello"],
        ["08:00:34 From Chris Brown: hi again everyone!"]]

chatlog = defaultdict(list)
message = []


def parse_chat():
    for line in logs:
        chatlog[line[0].split(" ")[2].casefold() + " " + line[0].split(" ")[3].casefold().strip(":")].append(
            line[0].split(" ")[0] + line[0].split(":")[3])


def display_chats(name):
    global message
    message = []
    for key, value in chatlog.items():
        if name.casefold() == str(key).casefold():
            message = value
    if len(message) == 0:
        print("Invalid Name, Not Found")
        return
    for x, y in enumerate(message):
        print("[" + str(x + 1) + "] " + y)
    parse_grade(name)


def parse_grade(name):
    print((len(chatlog.get(name.casefold())) / len(logs)) * 100, "%")


def main():
    display_chats(input("Enter Name To Search\n"))


if __name__ == '__main__':
    parse_chat()
    main()
