import streamlit as st

def answer_riddle(question, answer):
    correct_answers = {
        'What single digit appears most frequently between and including the numbers 1 and 1,000?': '1',
        'My twin lives at the reverse of my house number. The difference between our house numbers ends in two. What are the lowest possible numbers of our house numbers?': '19 and 91',
        'A small number of cards has been lost from a complete pack. If I deal among four people, three cards remain. If I deal among three people, two remain and if I deal among five people, two cards remain. How many cards are there?': '47',
        'What is the smallest whole number that is equal to seven times the sum of its digits?': '21',
        'I am an odd number. Take away one letter and I become even. What number am I?': 'seven',
        'What comes once in a minute, twice in a moment, but never in a thousand years?': ''m''
    }

    if answer == correct_answers.get(question, '').lower():
        return True, None
    else:
        return False, correct_answers[question]

questions = [
    'What single digit appears most frequently between and including the numbers 1 and 1,000?',
    'My twin lives at the reverse of my house number. The difference between our house numbers ends in two. What are the lowest possible numbers of our house numbers?',
    'A small number of cards has been lost from a complete pack. If I deal among four people, three cards remain. If I deal among three people, two remain and if I deal among five people, two cards remain. How many cards are there?',
    'What is the smallest whole number that is equal to seven times the sum of its digits?',
    'I am an odd number. Take away one letter and I become even. What number am I?',
    'What comes once in a minute, twice in a moment, but never in a thousand years?'
    
]

st.title("Arthur's math riddles")

show_correct_answers = st.checkbox("Show correct answers for wrong questions")

for idx, question in enumerate(questions):
    st.subheader(question)
    answer = st.text_input(f'Enter your answer for question {idx+1}: ').lower()
    if st.button(f'Submit for question {idx+1}'):
        result, correct_answer = answer_riddle(question, answer)
        if result:
            st.success('Well done! Right answer')
        else:
            st.error('Wrong answer. Try again!')
            if show_correct_answers:
                st.write(f"The correct answer is: {correct_answer}")
        st.write('------------------')
