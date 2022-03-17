def check_name(question, error_message):
    name = ""
    while not name:
        answer = input(question)
        if not answer:
         print(error_message)
        else:
         return answer

question = check_name("what's your name?:","you can't levave this blank")
