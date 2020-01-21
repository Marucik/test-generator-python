from string import Template
import random

testy = 3

headerT = Template(
    "Imie i nazwisko:\n\nData:\n\nSemest:\n\n\t\t\t\tStolice - sprawdzian(Formularz $version)\n"
)

questionT = Template("\n$number. Jaką stolicę ma państwo $country?\n")

choicesT = Template("\tA. $A\n\tB. $B\n\tC. $C\n\tD. $D\n")

answers = {}

with open("stolice.txt") as file:
    for line in file:
        trailed = line.rstrip()
        split = trailed.split(", ")
        answers[split[0]] = split[1]
countries = []

for x in answers:
    countries.append(x)

questionAnswers = {"A": "", "B": "", "C": "", "D": ""}

for i in range(1, testy + 1):
    with open(f"spr{i}.txt", "w") as test, open(f"odp{i}.txt", "w") as key:

        test.write(headerT.substitute(version=i))

        random.shuffle(countries)

        for j in enumerate(countries):
            test.write(questionT.substitute(number=j[0] + 1, country=j[1]))
            temp = answers.copy()
            questionAnswersTemp = []

            testAnswer = answers.get(j[1])
            questionAnswersTemp.append(testAnswer)

            del temp[j[1]]

            questionAnswersTemp = questionAnswersTemp + random.sample(
                list(temp.values()), 3
            )

            random.shuffle(questionAnswersTemp)

            for item in enumerate(questionAnswers):
                questionAnswers[item[1]] = questionAnswersTemp[item[0]]

            test.write(choicesT.substitute(questionAnswers))

            for dictKey in questionAnswers:
                if questionAnswers[dictKey] == testAnswer:
                    key.write(f"{j[0] + 1}.{dictKey}\n")
