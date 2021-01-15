import random

randint = random.randint(0, 8)
responses = ["Yes", "Absolutely", "Without a doubt", "It is destined", "Of course!", "No", "Absolutely not", "Maybe", "It's possible"]
input("Ask the magic 8 ball anything: ")
print(responses[randint])
