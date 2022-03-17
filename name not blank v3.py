def check_name(question):
    while True:
        answer = input(question)
        if not answer.isalpha():
         print("you can't levave this blank")
        else:
         return answer

question = check_name("what's your name")
