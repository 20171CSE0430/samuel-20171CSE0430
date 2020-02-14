n = int(input())
result = []
for i in range(0, n):
    s = input()
    commands = s.split()
    command = commands[0]

    if command == 'insert':
        i = int(commands[1])
        e = int(commands[2])
        result.insert(i, e)
    elif command == 'print':
        print(result)
    elif command == 'remove':
        try:
            e = int(commands[1])
            result.remove(e)
        except:
            pass
    elif command == 'append':
        e = int(commands[1])
        result.append(e)
    elif command == 'sort':
        result.sort(reverse=True)
    elif command == 'pop':
        try:
            result.pop()
        except:
            pass
    elif command == 'reverse':
        result.reverse
