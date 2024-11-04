import random

# Vocabulary words in English with translations
vocabulary = {
    "apple": "manzana",
    "book": "libro",
    "cat": "gato",
    "dog": "perro",
    "house": "casa"
}

# Function to quiz user on vocabulary
def vocabulary_quiz():
    word, translation = random.choice(list(vocabulary.items()))
    user_answer = input(f"What is the Spanish word for '{word}'? ")
    if user_answer.lower() == translation:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is '{translation}'.")

# Start quiz
print("Vocabulary Quiz")
vocabulary_quiz()
