"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
import json

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message(""" 
Create a trivia game with 7 questions about "A Song of Ice and Fire". 
Please provide the output in the following format:
{
  "questions": [
    {
      "question": "What is the name of Jon Snow's direwolf?",
      "answer": "Ghost",
      "fact": "Ghost is the only white direwolf in the Stark family."
    },
    {
      "question": "Who is known as the 'Kingslayer'?",
      "answer": "Jaime Lannister",
      "fact": "Jaime earned this nickname after killing King Aerys II during Robert's Rebellion."
    }
  ]
} 
""")



def get_questions_and_answers(response):
    results = []
    #print(response.text)
    trivia_data = json.loads(response.text)
    for question in trivia_data["questions"]:
        results_dict = {
            "question": question["question"],
            "answer": question["answer"],
            "fact": question["fact"] 
            }
        results.append(results_dict)
    
    return results
