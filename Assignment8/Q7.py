
import numpy as np
def guessing_game(matrix_size):
    matrix = np.random.randint(1, 101, size=(matrix_size, matrix_size))
    trials = []

    for i in range(matrix_size):
        hidden_number = np.random.choice(matrix[i])
        count = 0
        guessed = False

        while not guessed:
            guess = int(input(f"Guess the hidden number for row {i + 1}: "))
            count += 1
            if guess == hidden_number:
                guessed = True
                print(f"Correct! The hidden number was {hidden_number}.")
            else:
                print("Incorrect guess. Try again.")

        trials.append(count)

    return trials
matrix_size = int(input("Enter the size of the matrix: "))
trials_taken = guessing_game(matrix_size)
print("Number of trials taken for each row to guess the correct number:", trials_taken)
