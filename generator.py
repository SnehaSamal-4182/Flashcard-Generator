

import openai
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generate_flashcards(chunks, num=10, complexity="Basic", question_type="Q&A"):
    flashcards = []
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Secure key loading

    for _ in range(min(num, len(chunks))):
        chunk = random.choice(chunks)
        
        try:
            if question_type == "Q&A":
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{
                        "role": "user", 
                        "content": f"Generate 1 concise question and answer about: {chunk}. Complexity: {complexity}. Format: Q: [question]\nA: [answer]"
                    }],
                    temperature=0.7
                )
                qa = response.choices[0].message['content'].split("\n")
                question = qa[0].replace("Q: ", "").strip()
                answer = qa[1].replace("A: ", "").strip() if len(qa) > 1 else chunk

            elif question_type == "True/False":
                # Randomly decide true/false and modify chunk if false
                is_true = random.choice([True, False])
                if is_true:
                    question = f"True or False: {chunk}"
                    answer = "True"
                else:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{
                            "role": "user",
                            "content": f"Make this statement false by modifying one fact: {chunk}"
                        }],
                        max_tokens=150
                    )
                    false_statement = response.choices[0].message['content'].strip()
                    question = f"True or False: {false_statement}"
                    answer = "False"

            elif question_type == "MCQ":
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{
                        "role": "user",
                        "content": f"Generate a multiple-choice question with 4 options about: {chunk}. Mark the correct answer with (Correct)."
                    }],
                    temperature=0.7
                )
                question = response.choices[0].message['content'].strip()
                answer = "Correct answer: " + question.split("(Correct)")[0].strip()[-1]  # Extract correct option

            else:  # Fallback to Q&A
                question = f"Explain: {chunk[:200]}"
                answer = chunk

            flashcards.append((question, answer))

        except Exception as e:
            print(f"Error generating flashcard: {e}")
            continue

    return flashcards












