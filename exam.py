import requests, json, os

print("Welcome to the Scripting Exam 😄")
print("Lets start simple~")
name = input("Whats your name?: ")

readiness = input(name +" are you ready for this exam? (y/n): ")
if readiness in ["y", "Y", "Yes", "yes", "yea"]:
    print("Great! I'm sure you'll do great!")
else:
    print("Eh! Wrong Answer")


scripts = int(input("How many scripts have you written?: "))
if scripts > 10:
    print("Okay! You couldn've written more but it exceptable.")
else:
    print("Bad answer already 😕")


score = 0
questions = [
    "Bash is a programming language. [ True/False ]: ",
    "'$?' a built-in bash function that tells you the status code of previously run command [ True/False ]:  ",
    "API stands for Application Programming Internet [ True/False ]: ",
    "Python is only used for Software Development [ True/False ]: ",
    "for_loop loops infinitely until condition is met [ True/False ]: ",
    "As of today 25 scripts are due as task [ True/False ]: ",
    "In python scripting when you start if statement, you must close the statement for it to work [ True/False ]: ",
    "Is the following syntax correct? `for i in $(cat /etc/passwd | grep awk '{print $1}'); do echo $i; done` [ True/False ]: ",
    "API error code 401 is server side error. [ True/False ]: ",
    "API headers are used to provide information about the api [ True/False ]: "
]
answers = [
    "false",
    "true",
    "false",
    "false",
    "false",
    "true",
    "false",
    "false",
    "false",
    "true"
]

print("Lets start the exam, good luck!")
for question, answer in zip(questions, answers):
    user_input = input(question).lower()
    if user_input == answer:
        score += 1
        print("Correct!")
    elif user_input not in ['True', 'true', 'False', 'false']:
        print("Please enter True or False")
    else:
        print("Eh Wrong!")

if score > 7: 
    res = "passed"
else: 
    res = "failed"

print("Score is", score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%", "You have", res)

response = requests.post('https://hooks.slack.com/services/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', 
    headers={"Content-type": "application/json"}, 
    json={
        "text": "User %s got score of %s which means %s" % (name, score, res)
        }
    )