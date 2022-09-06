from questionC import Question

test = [
    "1+3=?\n(a)2\n(b)3\n(c)4\n\n",
    "5+3=?\n(a)8\n(b)3\n(c)4\n\n",
    "确认按钮是哪个？\n(a)回车\n(b)control\n(c)fn\n\n"
]

questions = [
    Question(test[0],"c"),
    Question(test[1],"a"),
    Question(test[2],"a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1
    
    print("您得到了 " + str(score) + "分，共 " + str(len(questions)) + "题")

run_test(questions)
