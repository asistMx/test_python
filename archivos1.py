with open("hello.txt", "r") as file:
    print(file.read())
    file.seek(0)
    print(file.read())
    file.seek(0)
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line)
        for letter in line:
            print(letter)

    file.seek(0)
    print(file.writable())
