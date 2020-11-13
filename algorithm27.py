def search(maze,start,end):
    wait = []
    done = set()

    wait.append(start)
    done.add(start)

    while wait:
        checkroot = wait.pop(0)
        current = checkroot[-1]

        if current == end:
            return checkroot

        for i in maze[current]:
            if i not in done:
                wait.append(checkroot + i)
                done.add(i)
        
    return "?"


maze = {
    'a' : ['d'],
    'b' : ['c'],
    'c' : ['b','f'],
    'd' : ['a','g','e'],
    'e' : ['d','f'],
    'f' : ['e','c','i'],
    'g' : ['d'],
    'h' : ['i'],
    'i' : ['f','h']
}

print(search(maze,'a','b'))
