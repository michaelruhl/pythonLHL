questions = [
    [2, 2],
    [2, 2],
    [2, 2],
    [2, 4],
    [2, 2],
    [2, 6],
    [2, 2],
    [7, 2],
    [2, 2],
    [9, 2],
]

answers = [
    4,4,4,6,5,8,4,9,4,11
]
counter = 0
for index in range(0,10):
    response = int(input("yo tell me what " +  str(questions[index][0]) + " + "  + str(questions[index][1]) + " is m8-> "))
    # print("this is a", a)
    # print("this is b", b)
    # print(answers[a])
    # print(counter)
    if response == answers[index]: 
      counter = counter + 1
if counter <= 5:
    print("you fuckin suck")
elif counter <= 8:
 print("you pass")
else:
    print("congrats dud")
