import time

bacteria = 1

# for generation in range(0, 10):
#     bacteria = bacteria * 2
#     print(bacteria)
#     time.sleep(0.5)


actors = [
    "Nathan",
    "Gina",
    "Alan",
    "Morena"
]

roles = [
    "Captain",
    "Zoe",
    "Hoban",
    "Inara"
]
for index in range(0,len(actors)):
    print(actors[index], "as", roles[index])