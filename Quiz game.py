Questions=[ [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "React", 4
  ],
  [
    "Which language is written by c++?", "Python", "French", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which is the most demanding language in 2024?", "Python", "French", "JavaScript",
    "Php", "None", 2
  ],
  [
    "Which language is known as a mother language of programming?", "Python", "C", "JavaScript",
    "Php", "None", 1
  ],
  [
    "Which language is used in the field of ml?", "Js", "French", "Python",
    "C", "None", 2
  ],
  [
    "Which language was used to create telegram?", "Python", "French", "JavaScript",
    "Php", "C", 4
  ],
  [
    "Laravel is the frsmework of ___", "Python", "French", "JavaScript",
    "Php", "None", 3
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "What is the base language to learn web dev?", "Python", "French", "JavaScript",
    "Php", "None", 2
  ]
]
levels=[1000,3000,5000,7500,10000,20000,50000,75000,90000,100000]
money=0
for i in range(0,len(Questions)):
    Questions=Questions[i]
    print(f"\n Your question for {levels[i]}")
    print(f"a. {Questions[1]}          b. {Questions[2]} ")
    print(f"c. {Questions[3]}          d. {Questions[4]} ")
    answer=int(input("Enter your answer in this format(1-4) or 0 to quit:"))
    if (answer == 0):
        money = levels[i - 1]
        break
    if (answer== Questions[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 6:
            money = 500000
        elif i == 9:
            money = 100000
    else:
        print("Wrong answer!")
        break

    print(f"Your take home money is {money}")
