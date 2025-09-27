import random

questions_file = "questions.txt"

# Read all questions and save as a list
with open(questions_file, encoding="utf8") as f:
    questions = f.readlines()

# In a loop, randomly choose a question, print it, and remove it from the list
while len(questions) > 0:
    # Choose a random index (starting from 0, ending 1 less than list length)
    index = random.randint(0, len(questions) - 1)
    # Remove and return the question at [index]
    question = questions.pop(index)
    # Print the chosen question
    print(question.strip())
    # Wait for an 'Enter' press to continue:
    input()
