# num1 = float(input("Enter number: "))
# op = input("+ - * /: ")
# num2 = float(input("Enter number: "))
#
# if op == "+":
#     print(num1+num2)
# elif op == "-":
#     print(num1-num2)
# elif op == "*":
#     print(num1*num2)
# elif op == "/":
#     print(num1/num2)
# else:
#     print("Invalid Input")


# secret = "Hello"
# guess = ""
# count = 0
# guessLeft = True
# while guess != secret and guessLeft:
#     if count < 3:
#         guess = input("Enter guess: ")
#         count += 1
#     else:
#         guessLeft = False
# if guessLeft == False:
#     print("You lose")
# else:
#     print("You win")


p1 = "Which one is a ? \na = a\nb = b\nc = c"
p2 = "Which one is b ? \na = a\nb = b\nc = c"

class Question:
    def __init__(self, promp, answer):
        self.promp = promp
        self.answer = answer


example1 = Question(p1, "a")
example2 = Question(p2, "b")

questions = [example1, example2]

def run_test(questions):
    score = 0
    for question in questions:
        print(question.promp)
        user = input("Enter the pick: ")
        if user == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))

run_test(questions)











