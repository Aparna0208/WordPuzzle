# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Aparna Subramaniam, Maira, Nadia, Matthew
# Section:      461 
# Assignment:   Word Puzzle
# Date:         10/24/2024

import math

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-' * len(puzzle[i]): >16}")

def get_valid_letters(puzzle):
    ''' Return a string of unique letters found in the puzzle. '''
    letters = set()
    for char in puzzle:
        if char.isalpha():  # Check if the character is a letter
            letters.add(char)
    return ''.join(sorted(letters))

def is_valid_guess(valid_letters, guess):
    ''' Check if the user's guess has exactly 10 unique letters. '''
    return len(set(guess)) == 10 and set(guess).issubset(set(valid_letters))

def check_user_guess(dividend, quotient, divisor, remainder):
    ''' Check if the equation holds true: Dividend = Quotient * Divisor + Remainder. '''
    return dividend == quotient * divisor + remainder

def make_number(word, guess):
    ''' Convert a word to an integer based on the guess mapping. '''
    number = 0
    for char in word:
        number = number * 10 + guess.index(char)  # Get index of char in guess
    return number

def make_numbers(puzzle, guess):
    ''' Create a tuple of four integers from the puzzle string based on the guess. '''
    puzzle_parts = puzzle.split(',')
    dividend = make_number(puzzle_parts[1].split('|')[1].strip(), guess)
    quotient = make_number(puzzle_parts[1].strip(), guess)
    divisor = make_number(puzzle_parts[0].strip(), guess)
    remainder = make_number(puzzle_parts[-1].strip(), guess)
    return (dividend, quotient, divisor, remainder)

def main():
    # User input for the puzzle
    ari_puzzle = input("Enter a word arithmetic puzzle:\n")
    print()
    print_puzzle(ari_puzzle)

    # Get valid letters from the puzzle
    valid_letters = get_valid_letters(ari_puzzle)

    # User input for the guess
    user_guess = input("Enter your guess, for example ABCDEFGHIJ: ")

    # Validate guess
    if not is_valid_guess(valid_letters, user_guess):
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
        return

    # Create numbers from the puzzle
    dividend, quotient, divisor, remainder = make_numbers(ari_puzzle, user_guess)

    # Check if the user's guess is correct
    if check_user_guess(dividend, quotient, divisor, remainder):
        print("Good job!")
    else:
        print("Try again!")

if __name__ == '__main__':
    main()