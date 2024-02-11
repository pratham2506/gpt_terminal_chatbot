#make necessary imports
import openai

#api key
openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.4-turbo",
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