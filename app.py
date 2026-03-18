import streamlit as st

# We need to import the function that gets the answer.
# This assumes that `app.py` and `main.py` are in the same folder.
# If they are not, this line might need to be changed.
from main import get_answer

# --- 1. Set up the title of the page ---
# This line creates the main heading for your web app.
st.title("My Simple RAG Chatbot")

# This is a short description to tell the user what to do.
st.write("Enter your question below and I will find the answer for you.")

# --- 2. Get the user's question ---
# This creates a simple text box where the user can type their question.
# The user's question is saved in a variable called `user_question`.
user_question = st.text_input("Please enter your question here:")

# --- 3. Create a button to submit the question ---
# This creates a button that the user can click.
# The code inside the `if` statement will only run when the button is clicked.
if st.button("Get Answer"):
    # First, we check if the user actually typed something.
    if user_question:
        # If they did, we show a loading message while we wait for the answer.
        st.info("Finding your answer...")
        
        # Now, we call the `get_answer` function from your `main.py` file.
        # We pass the user's question to it.
        # The answer it returns is saved in the `answer` variable.
        answer = get_answer(user_question)
        
        # Finally, we display the answer in a special box.
        st.success("Here is the answer:")
        st.write(answer)
    else:
        # If the user clicks the button without typing anything,
        # we show a warning message.
        st.warning("Please type a question first!")
