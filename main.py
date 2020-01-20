from string import Template
import random

testy = 3

naglowek = Template(
    "Imie i nazwisko:\n\nData:\n\nSemest:\n\n\t\t\t\tStolice - sprawdzian(Formularz $version)\n"
)

pytanie = Template("\n$number. Jaką stolicę ma państwo $country?\n")

opcje = Template("\tA. $A\n\tB. $B\n\tC. $C\n\tD. $D\n")

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
    test = open(f"spr{i}.txt", "w")
    key = open(f"odp{i}.txt", "w")

    test.write(naglowek.substitute(version=i))

    random.shuffle(countries)

    for j in enumerate(countries):
        test.write(pytanie.substitute(number=j[0] + 1, country=j[1]))
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

        test.write(opcje.substitute(questionAnswers))

        for dictKey in questionAnswers:
            if questionAnswers[dictKey] == testAnswer:
                key.write(f"{j[0] + 1}.{dictKey}\n")

    test.close()
    key.close()
