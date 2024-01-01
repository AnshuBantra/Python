def main():
    yell_1('This', 'is', 'CS50')
    yell_2('This', 'is', 'CS50')
    yell_3('This', 'is', 'CS50')

def yell_1(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

def yell_2(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

def yell_3(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == '__main__':
    main()