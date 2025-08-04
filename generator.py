<<<<<<< HEAD
# #generator.py



# import random

# def generate_flashcards(chunks, num=10, complexity="Basic", question_type="Q&A"):
#     flashcards = []
#     used_chunks = set()

#     for _ in range(min(num, len(chunks))):
#         chunk = random.choice([c for c in chunks if c not in used_chunks])
#         used_chunks.add(chunk)

#         if question_type == "Q&A":
#             question = f"What is the main idea of: {chunk[:100]}...?"
#             answer = chunk

#         elif question_type == "Fill in the Blanks":
#             words = chunk.split()
#             if len(words) > 8:
#                 blank_index = random.randint(5, len(words) - 1)
#                 answer = words[blank_index]
#                 words[blank_index] = "_____"
#                 question = " ".join(words)
#             else:
#                 question = chunk
#                 answer = "N/A"

#         elif question_type == "True/False":
#             question = f"True or False: {chunk}"
#             answer = "True"  # Simplified

#         elif question_type == "MCQ":
#             question = f"What fits best here: {chunk[:80]}...?"
#             answer = "Correct Answer"
#             # You can also add options in a future upgrade

#         else:
#             question = chunk
#             answer = "Answer not available"

#         flashcards.append((question.strip(), answer.strip()))

#     return flashcards



# 2

# import random
# from transformers import T5ForConditionalGeneration, T5Tokenizer

# # Load T5 model and tokenizer
# def load_question_generator():
#     model_name = "t5-small"  # You can change to "t5-base" for better quality
#     tokenizer = T5Tokenizer.from_pretrained(model_name)
#     model = T5ForConditionalGeneration.from_pretrained(model_name)
#     return model, tokenizer

# # Generate flashcards using T5 model
# def generate_flashcards(chunks, num=10, complexity="Basic", question_type="Q&A", model_tokenizer=None):
#     flashcards = []
#     used_chunks = set()

#     model, tokenizer = model_tokenizer if model_tokenizer else (None, None)

#     for _ in range(min(num, len(chunks))):
#         chunk = random.choice([c for c in chunks if c not in used_chunks])
#         used_chunks.add(chunk)

#         if question_type == "Q&A" and model:
#             input_text = f"generate question: {chunk.strip()}"
#             inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
#             outputs = model.generate(inputs, max_length=64, num_beams=4, early_stopping=True)
#             question = tokenizer.decode(outputs[0], skip_special_tokens=True)

#             # Use the same chunk as answer or generate answer
#             answer = chunk.strip()

#         elif question_type == "Fill in the Blanks":
#             words = chunk.split()
#             if len(words) > 8:
#                 blank_index = random.randint(5, len(words) - 1)
#                 answer = words[blank_index]
#                 words[blank_index] = "_____"
#                 question = " ".join(words)
#             else:
#                 question = chunk
#                 answer = "N/A"

#         elif question_type == "True/False":
#             question = f"True or False: {chunk}"
#             answer = "True"

#         elif question_type == "MCQ":
#             question = f"What fits best here: {chunk[:80]}...?"
#             answer = "Correct Answer"

#         else:
#             question = chunk
#             answer = "Answer not available"

#         flashcards.append((question.strip(), answer.strip()))

#     return flashcards



#3

import random


def generate_flashcards(chunks, num=10, complexity="Basic", question_type="Q&A", model_tokenizer=None):
    flashcards = []
    used_chunks = set()

    for _ in range(min(num, len(chunks))):
        chunk = random.choice([c for c in chunks if c not in used_chunks])
        used_chunks.add(chunk)

        if model_tokenizer and question_type in ["Q&A", "MCQ"]:
            tokenizer, model = model_tokenizer
            input_text = f"generate question: {chunk}"
            input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
            output = model.generate(input_ids, max_length=64, num_return_sequences=1)
            generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

            if question_type == "Q&A":
                question = generated_text
                answer = chunk  # or run another prompt to extract answer
            elif question_type == "MCQ":
                question = generated_text
                # Simulate options
                answer = "Option B"
                options = ["Option A", "Option B", "Option C", "Option D"]
                question += f"\n\nA. {options[0]}\nB. {options[1]}\nC. {options[2]}\nD. {options[3]}"

        elif question_type == "Fill in the Blanks":
            words = chunk.split()
            if len(words) > 8:
                blank_index = random.randint(5, len(words) - 1)
                answer = words[blank_index]
                words[blank_index] = "_____"
                question = " ".join(words)
            else:
                question = chunk
                answer = "N/A"

        elif question_type == "True/False":
            question = f"True or False: {chunk}"
            answer = "True"

        else:
            question = f"What is the main idea of: {chunk[:100]}...?"
            answer = chunk

        flashcards.append((question.strip(), answer.strip()))

    return flashcards






# import random
# from transformers import T5Tokenizer, T5ForConditionalGeneration

# def load_question_generator(model_name="t5-small"):
#     tokenizer = T5Tokenizer.from_pretrained(model_name)
#     model = T5ForConditionalGeneration.from_pretrained(model_name)
#     return tokenizer, model

# def generate_flashcards(chunks, num=10, complexity="Basic", question_type="Q&A", model_tokenizer=None):
#     flashcards = []
#     used_chunks = set()

#     for _ in range(min(num, len(chunks))):
#         chunk = random.choice([c for c in chunks if c not in used_chunks])
#         used_chunks.add(chunk)

#         if model_tokenizer and question_type in ["Q&A", "MCQ"]:
#             tokenizer, model = model_tokenizer
#             input_text = f"generate question: {chunk}"
#             input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
#             output = model.generate(input_ids, max_length=64, num_return_sequences=1)
#             generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

#             if question_type == "Q&A":
#                 question = generated_text
#                 answer = chunk  # Optional: Use another prompt to extract answer
#             elif question_type == "MCQ":
#                 question = generated_text
#                 answer = "Correct Answer"  # Placeholder for now

#         else:
#             if question_type == "Q&A":
#                 question = f"What is the main idea of: {chunk[:100]}...?"
#                 answer = chunk
#             elif question_type == "Fill in the Blanks":
#                 words = chunk.split()
#                 if len(words) > 8:
#                     blank_index = random.randint(5, len(words) - 1)
#                     answer = words[blank_index]
#                     words[blank_index] = "_____"
#                     question = " ".join(words)
#                 else:
#                     question = chunk
#                     answer = "N/A"
#             elif question_type == "True/False":
#                 question = f"True or False: {chunk}"
#                 answer = "True"
#             else:
#                 question = chunk
#                 answer = "Answer not available"

#         flashcards.append((question.strip(), answer.strip()))

#     return flashcards





=======
# #generator.py



# import random

# def generate_flashcards(chunks, num=10, complexity="Basic", question_type="Q&A"):
#     flashcards = []
#     used_chunks = set()

#     for _ in range(min(num, len(chunks))):
#         chunk = random.choice([c for c in chunks if c not in used_chunks])
#         used_chunks.add(chunk)

#         if question_type == "Q&A":
#             question = f"What is the main idea of: {chunk[:100]}...?"
#             answer = chunk

#         elif question_type == "Fill in the Blanks":
#             words = chunk.split()
#             if len(words) > 8:
#                 blank_index = random.randint(5, len(words) - 1)
#                 answer = words[blank_index]
#                 words[blank_index] = "_____"
#                 question = " ".join(words)
#             else:
#                 question = chunk
#                 answer = "N/A"

#         elif question_type == "True/False":
#             question = f"True or False: {chunk}"
#             answer = "True"  # Simplified

#         elif question_type == "MCQ":
#             question = f"What fits best here: {chunk[:80]}...?"
#             answer = "Correct Answer"
#             # You can also add options in a future upgrade

#         else:
#             question = chunk
#             answer = "Answer not available"

#         flashcards.append((question.strip(), answer.strip()))

#     return flashcards



# 2

# import random
# from transformers import T5ForConditionalGeneration, T5Tokenizer

# # Load T5 model and tokenizer
# def load_question_generator():
#     model_name = "t5-small"  # You can change to "t5-base" for better quality
#     tokenizer = T5Tokenizer.from_pretrained(model_name)
#     model = T5ForConditionalGeneration.from_pretrained(model_name)
#     return model, tokenizer

# # Generate flashcards using T5 model
# def generate_flashcards(chunks, num=10, complexity="Basic", question_type="Q&A", model_tokenizer=None):
#     flashcards = []
#     used_chunks = set()

#     model, tokenizer = model_tokenizer if model_tokenizer else (None, None)

#     for _ in range(min(num, len(chunks))):
#         chunk = random.choice([c for c in chunks if c not in used_chunks])
#         used_chunks.add(chunk)

#         if question_type == "Q&A" and model:
#             input_text = f"generate question: {chunk.strip()}"
#             inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
#             outputs = model.generate(inputs, max_length=64, num_beams=4, early_stopping=True)
#             question = tokenizer.decode(outputs[0], skip_special_tokens=True)

#             # Use the same chunk as answer or generate answer
#             answer = chunk.strip()

#         elif question_type == "Fill in the Blanks":
#             words = chunk.split()
#             if len(words) > 8:
#                 blank_index = random.randint(5, len(words) - 1)
#                 answer = words[blank_index]
#                 words[blank_index] = "_____"
#                 question = " ".join(words)
#             else:
#                 question = chunk
#                 answer = "N/A"

#         elif question_type == "True/False":
#             question = f"True or False: {chunk}"
#             answer = "True"

#         elif question_type == "MCQ":
#             question = f"What fits best here: {chunk[:80]}...?"
#             answer = "Correct Answer"

#         else:
#             question = chunk
#             answer = "Answer not available"

#         flashcards.append((question.strip(), answer.strip()))

#     return flashcards



#3

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





# import random
# from transformers import T5Tokenizer, T5ForConditionalGeneration

# def load_question_generator(model_name="t5-small"):
#     tokenizer = T5Tokenizer.from_pretrained(model_name)
#     model = T5ForConditionalGeneration.from_pretrained(model_name)
#     return tokenizer, model

# def generate_flashcards(chunks, num=10, complexity="Basic", question_type="Q&A", model_tokenizer=None):
#     flashcards = []
#     used_chunks = set()

#     for _ in range(min(num, len(chunks))):
#         chunk = random.choice([c for c in chunks if c not in used_chunks])
#         used_chunks.add(chunk)

#         if model_tokenizer and question_type in ["Q&A", "MCQ"]:
#             tokenizer, model = model_tokenizer
#             input_text = f"generate question: {chunk}"
#             input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
#             output = model.generate(input_ids, max_length=64, num_return_sequences=1)
#             generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

#             if question_type == "Q&A":
#                 question = generated_text
#                 answer = chunk  # Optional: Use another prompt to extract answer
#             elif question_type == "MCQ":
#                 question = generated_text
#                 answer = "Correct Answer"  # Placeholder for now

#         else:
#             if question_type == "Q&A":
#                 question = f"What is the main idea of: {chunk[:100]}...?"
#                 answer = chunk
#             elif question_type == "Fill in the Blanks":
#                 words = chunk.split()
#                 if len(words) > 8:
#                     blank_index = random.randint(5, len(words) - 1)
#                     answer = words[blank_index]
#                     words[blank_index] = "_____"
#                     question = " ".join(words)
#                 else:
#                     question = chunk
#                     answer = "N/A"
#             elif question_type == "True/False":
#                 question = f"True or False: {chunk}"
#                 answer = "True"
#             else:
#                 question = chunk
#                 answer = "Answer not available"

#         flashcards.append((question.strip(), answer.strip()))

#     return flashcards






>>>>>>> 9da00c47a0e236eff71f07160e26ce4a92aeb826
