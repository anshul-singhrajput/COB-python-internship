import random
# Define  set of questions and answers
questions = [
    {
         "question": "What is the capital of India?",
         "answer": "New Delhi"
    }
    ,
    {
        "question": "What is the capital of Chhattisgarh?",
        "answer": "Raipur"
    },
    {
        "question": "What is 2 + 2?",
        "answer": "4"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars"
    },
    {
        "question": "Who made the famous painting Mona Lisa?",
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "Name of the largest country in the world?",
        "answer": "Russia"
    },
    {
        "question": "What is the name of longest river of world?",
        "answer": "Nile"
    },
    {
        "question": "What is the name of nearest star to the earth?",
        "answer": "The Sun"
    },
    {
        "question": "Which animal is called as the 'Ship pf the Desert'?",
        "answer": "Camel"
    },
    {
        "question": "Hpw many Consonants are in the English alphabet'?",
        "answer": "21"
    },
    {
        "question": "What are primary colors?",
        "answer": "Three (Red,Yellow,Blue)"
    },
    {
        "question": "What is the name of house made of ice ?",
        "answer": "Igloo"
    },
    {
        "question": "What is the name of bird lays the largest eggs ?",
        "answer": "Ostrich"
    },
    {
        "question": "Which festival is called as the 'Fwstival of flowers' ?",
        "answer": "Onam"
    },
    {
        "question": "Which day is celebrated World Literacy Day ?",
        "answer": "September 8"
    },
    {
        "question": "What does USB stand for ?",
        "answer": "Universal Serial bus"
    },
    {
        "question": "What is a female donkey called ?",
        "answer": "A jenny"
    },
    {
        "question": "Mycology is the study of what ?",
        "answer": "Fungi"
    },
    {
        "question": "In Greek Mythology , Who was the father of Zeus?",
        "answer": "Kronos"
    },
    {
        "question": "In the TV show 'Friends' , what doesn't joey share?",
        "answer": "Food"
    },
    {
        "question": "Alastair Cook belongs to which sport?",
        "answer": "Cricket"
    },
    {
        "question": "Who founded Amazon?",
        "answer": "Jeff Bezos"
    },
    {
        "question": "MODEM is used for?",
        "answer": "A/D and D/A conversions"
    },
    {
        "question": "Indian robot namely 'Vyom mitra' was developed by which organization?",
        "answer": "I.S.R.O"
    },
    {
        "question": "Ceremony of crowning a king?",
        "answer": "Coronation"
    },
    {
        "question": "One who does not believe in the existance of god?",
        "answer": "Atheist"
    },
    {
        "question": "A lover of good food?",
        "answer": "Gourmand"
    },
    {
        "question": "One Who does not express himself freely?",
        "answer": "Introvert"
    },
    {
        "question": "One who is unable to pay his debts?",
        "answer": "Insolvent"
    },
    {
        "question": "The Killing of a large group of people?",
        "answer": "Genocide"
    },   
]

# Function to select a random question
def get_random_question():
    if questions:
        question = random.choice(questions)
        questions.remove(question)
        return question
    else:
        return None

# Function to play the quiz
def play_quiz():
    score = 0
    for i in range(5):  # Change 5 to the number of questions you want to ask
        question = get_random_question()
        if question:
             print(question["question"])
             user_answer = input("Your answer: ")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
             print("Wrong! The correct answer is:" + question['answer'] + "\n")

    print("You got " + str(score) + " out of 5 questions correct.")

if __name__ == "__main__":
    print("Welcome to the Random Quiz!")
    play_quiz()
