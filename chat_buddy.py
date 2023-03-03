import openai
import sys

'''
Send in the chat history and user's new input, ChatGPT gives you a response
***Input***:
- chat_history, a list of dictionary. Check https://platform.openai.com/docs/guides/chat
- user_input, a string. User's new input
- print_conversation, bool default to false. If true, print conversation in terminal
***Return***
- chat_history, a list of dictionary. It is extended based on the inputted chat_history, but with user's new input and ChatGPT's new response appended
- gpt_msg, a string, ChatGPT's new response
'''
def chat_with_gpt(chat_history, user_input, print_conversation=False):   
    chat_history.append({'role': 'user', 'content': user_input})

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=chat_history,
        temperature = 0.05
    )

    gpt_msg = response['choices'][0]['message']['content']
    chat_history.append({'role': 'system', 'content': gpt_msg})

    if print_conversation:
        print(f'User:\n{user_input}')
        print(f'ChatGPT:\n{gpt_msg}')

    return chat_history, gpt_msg

if __name__ == '__main__':

    chat_history = []

    while True:
        user_input = input('Enter...')

        if user_input == 'exit()':
            break
        else:
            chat_history, gpt_msg = chat_with_gpt(chat_history, user_input, print_conversation=True)
