#make necessary imports
import openai
from openai import ChatCompletion

#api key
openai.api_key = "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"

def chat_with_gpt(prompt):
    response = ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{'role':'user','content':prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == '__main__':
    while True:
        user_input = input("You : ")
        if user_input.lower() in ['quit','exit','bye']:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot : ",response)