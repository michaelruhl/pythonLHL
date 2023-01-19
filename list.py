people = [
    "Mike",
    "Angela",
    "Beebs",
    "Kian",
    "Steph",
    "Jake",
    "Elle"
]

emptylist = []

print(people)

foosballers = [
  "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca",
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"
]
print(int(len(foosballers)))
median1 = (int(len(foosballers))/ 2) + .5
print(median1)
print(foosballers[7:12])
foosballers.insert(10, "Average Player")
foosballers[10] = "AVERAGE PLAYER"
print(foosballers)
badballers = [
    "badballer1",
    "badballer2",
    "badballer3",
    "badballer4",
    "badballer5",
]
totalballers = foosballers + badballers
print(totalballers)
foosballers.insert(13, "AVERAGE PLAYER")
del foosballers[10]
foosballers.insert(7, "Lacy")
foosballers.insert(-10, "Omar")
foosballers.insert(7, "Otto")
foosballers.insert(-9, "Chauncey")
print(foosballers)
