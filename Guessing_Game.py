import csv
import os
import random

# File to store user credentials
database_file = "users_db.csv"

# Function to initialize the CSV file if it doesn't exist
def initialize_db():
    if not os.path.exists(database_file):
        with open(database_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])  # Header row

# Function to register a new user
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if username_exists(username):
        print("Username already exists!")
    else:
        with open(database_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        print("User registered successfully!")

# Function to check if a username exists
def username_exists(username):
    with open(database_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            if row[0] == username:
                return True
    return False

# Function to login a user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open(database_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            if row[0] == username and row[1] == password:
                print("Login successful!")
                return True
    print("Invalid username or password!")
    return False

# Function to play the guessing game
def play_game():
    number_to_guess = random.randint(1, 100)
    print("Welcome to the guessing game!")
    print("I have chosen a number between 1 and 100.")
    
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Higher...")
            elif guess > number_to_guess:
                print("Lower...")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

# Main function
def main():
    initialize_db()  # Ensure the CSV exists

    while True:
        choice = input("\n1. Register\n2. Login\n3. Exit\nChoose an option: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                play_game()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
