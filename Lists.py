if __name__ == '__main__':
    N = int(input())
    entry = []
    for t in range(N):
        args = input().split(" ")
        if args[0] == "append":
            entry.append(int(args[1]))
        elif args[0] == "insert":
            entry.insert(int(args[1]), int(args[2]))
        elif args[0] == "remove":
            entry.remove(int(args[1]))
        elif args[0] == "pop":
            entry.pop()
        elif args[0] == "sort":
            entry.sort()
        elif args[0] == "reverse":
            entry.reverse()
        elif args[0] == "print":
            print (entry)