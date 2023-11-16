from collections import defaultdict

logs = [["08:00:13 From Alex Johnson: hello to everyone"],
        ["08:00:21 From Emily Smith: hello"],
        ["08:00:29 From Chris Brown: hello"],
        ["08:00:34 From Chris Brown: hi again everyone!"]]

chatlog = defaultdict(list)

for line in logs:
    chatlog[line[0].split(" ")[2] + " " + line[0].split(" ")[3].strip(":")].append(
        line[0].split(" ")[0] + line[0].split(":")[3])

name = input("Enter Name To Search\n")
message = []

for key, value in chatlog.items():
    if name.casefold() == str(key).casefold():
        message = value

for x, y in enumerate(message):
    print("[" + str(x+1) + "] " + y)
