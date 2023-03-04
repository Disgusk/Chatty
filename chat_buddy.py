import openai
import sys

# save your OpenAI API key to this file
openai.api_key_path ='.Renviron'

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
    suffix_phrase = ' Answer me using one sentence.'

    chat_history.append({'role': 'user', 'content': user_input + suffix_phrase})

    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=chat_history,
        temperature = 0.2
    )
    chat_history[-1] = {'role': 'user', 'content': user_input}

    gpt_msg = response['choices'][0]['message']['content']
    chat_history.append({'role': 'system', 'content': gpt_msg})

    if print_conversation:
        print(f'User:\n{user_input}')
        print(f'ChatGPT:\n{gpt_msg}')

    return chat_history, gpt_msg, response['usage']['total_tokens']

'''
This function will setup the beginning of a chat scenario
Input:
- scenario_idx: int
Output:
- a list of dictionary (in this case, there is only one element in the list). The list contains the chat history. This chat history should be fed into the chat_with_gpt function
'''
def setup_chat(scenario_idx=0):
    scenarios = [
        'You will be my Economy professor. I am in your office hour.',
        'You are my roommate. We are doing grocery shopping in Trader Joe\'s.',
        'You are my boyfriend. We are having a date in a restaurant.'
        ]
    
    return [{'role': 'user', 'content':scenarios[scenario_idx]}]

'''
This function corrects the grammar mistake using GPT3
Input:
- content: the sentence that wants to be checked
Output:
- the sentence with correct grammar
'''
def grammar_check(content):
    prefix_phrase = 'Correct the following sentence\'s grammar: ' 

    response = openai.Completion.create(
        model = 'text-curie-001',
        prompt = prefix_phrase + content,
        temperature=0
    )

    return response['choices'][0]['text']

if __name__ == '__main__':
    chat_history = setup_chat(2)
    total_tokens = 0

    while True:
        user_input = input('Enter...')

        if user_input == 'exit()':
            break
        else:
            chat_history, gpt_msg, token_used = chat_with_gpt(chat_history, user_input, print_conversation=True)
            total_tokens += token_used
    
    print(f'Token used in this conversation = {token_used}')
