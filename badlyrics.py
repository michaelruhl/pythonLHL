journey = """Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere"""

correctlyrics = journey.replace("""Just a small tone girl
Leaving in a lonely whirl
She took the midnight tray going anywhere
Just a seedy boy
Bored and raised in South Detroit or something
He took the midnight tray going anywhere""", "Just a small town girl\nliving in a lonely world\n she took the midnight train going anywhere\njust a city boy born and raised in south detroit\nhe took the midnight train going anywhere")

print(correctlyrics)
print(journey)

name = input("Please type in your name and press Enter ->") 
print("Hello, " + name + ", it's very nice to meet you.")