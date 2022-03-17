def check_name(question):
    name = ""
    while not name:
        answer = input(question)
        if not answer:
         print("you can't levave this blank")
        else:
         return answer

question = check_name("what's your name")

