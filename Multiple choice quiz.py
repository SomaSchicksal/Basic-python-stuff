question_prompts= [
    "What color are apples?\n 1) red\n 2) blue\n 3) yellow\n\n",
    "What color are bananas? \n 1) red\n 2) blue\n 3) yellow\n\n",
    "What color are strawberries? \n 1) red\n 2) blue\n 3) yellow\n\n",
] # the questions we are gonna ask
# so a question is made of a question and an answer, and to represent that i will create a question class
class Question:
    def __init__(self, prompt, answer):
        self.prompt=prompt
        self.answer=answer

# we will then make another array and call the question class with the customised parameters
questions= [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
]

# we now creat a function
def run_test(questions):
    score=0
    for question in questions: #for each question in questions i want to store the answer, and we will store it in a variable
        answer=input(question.prompt)
        if answer==question.answer:
            score +=1

    print( "u got:"+ str(score) +"/"+ str(len(questions)) +"correct")

run_test(questions)