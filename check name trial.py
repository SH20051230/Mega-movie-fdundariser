def check_name():
    name = ""
    while not name:
        answer = input("what's your name: ")
    if not answer:
        print("you can't levave this blank")
    else:
        return answer

blank = check_name()

