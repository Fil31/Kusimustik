
import random
#Функция для чтения вопросов и ответов из файла и записи в словарь
def read_questions_answers():
    with open("kusimused_vastused.txt", "r") as file:
        lines = file.readlines()
        questions_answers = {}
        for line in lines:
            question, answer = line.strip().split(":")
            questions_answers[question] = answer
    return questions_answers

#Функция для чтения ответов из файла и записи в два списка
def read_answers():
    with open("kusimused_vastused.txt", "r") as fail:
        mas1=[]
        mas2=[]
        for line in fail:
            n=line.find(",")
            mas1.append(line[0:n].strip())
            mas2.append(int(line[n+1:len(line)].strip()))
    print(mas1)
    print(mas2)
    return mas1, mas2

# Считываем вопросы и ответы из файла
questions_answers = read_questions_answers()

# Задаем количество опрашиваемых
num_of_testers = 3

# Создаем списки успешно и неуспешно прошедших опросник
successful_testers = []
unsuccessful_testers = []

# Опросник
for i in range(num_of_testers):
    name = input("Hi! What's your name?")
    print(f"Nice to meet you, {name}! Let's take a five-question test.")
    random_questions = random.sample(list(questions_answers.keys()), 5)
    correct_answers = 0
    for question in random_questions:
        answer = input(f"{name}, {question}: ")
        if answer == questions_answers[question]:
            print("That's right!")
            correct_answers += 1
        else:
            print(f"Wrong. The correct answer is: {questions_answers[question]}")
    if correct_answers >= 3:
        print(f"Well done, {name}! You successfully completed the questionnaire with the result {correct_answers}/5.\n")
        successful_testers.append((name, correct_answers))
    else:
        print(f"Unfortunately, {name}, you did not pass the test. Your score: {correct_answers}/5.\n")
        unsuccessful_testers.append((name, correct_answers))

# Сортируем списки успешно и неуспешно прошедших опросник
successful_testers.sort(key=lambda x: x[1], reverse=True)
unsuccessful_testers.sort()

# Записываем данные в файлы
with open("oiged.txt", "w") as file:
    for tester in successful_testers:
        file.write(f"{tester[0]}: {tester[1]}\n")

with open("valed.txt", "w") as file:
    for tester in unsuccessful_testers:
        file.write(f"{tester[0]}: {tester[1]}\n")

# Выводим списки успешно прошедших опросник
print("List of those who successfully completed the test:")
for tester in successful_testers:
    print(f"{tester[0]}: {tester[1]}")
print("\nList of those who did not pass the test:")
for tester in unsuccessful_testers:
    print(f"{tester[0]}: {tester[1]}")