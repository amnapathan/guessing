# secret_number = 7
# guess = int(input("Guess a number between 1 and 10> "))
# if guess == secret_number:
#     print(f"Right You guess the number {guess}")
# elif guess > secret_number:
#     print("Too high Try a smaller number")
# else:
import streamlit as st
import random

# Set up the page
st.title("🎯 Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess what it is?")

# Initialize session state variables
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Input from user
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    if st.session_state.game_over:
        st.warning("The game is over. Click 'Restart Game' to play again.")
    else:
        st.session_state.attempts += 1
        if guess < st.session_state.secret_number:
            st.info("🔼 Too low!")
        elif guess > st.session_state.secret_number:
            st.info("🔽 Too high!")
        else:
            st.success(f"🎉 Correct! The number was {st.session_state.secret_number}.")
            st.balloons()
            st.session_state.game_over = True
            st.write(f"You guessed it in {st.session_state.attempts} tries.")

# Restart the game
if st.button("Restart Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False



