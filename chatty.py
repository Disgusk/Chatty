from pronunciation import pron_check_and_read_from_file
from chat_buddy import setup_chat, chat_with_gpt
from elevenlabs import text_to_speech

'''
This is the function that returns everything
'''
def respond_to_user(chat_history, path_to_audio):
    user_sentence, pron_json = pron_check_and_read_from_file(path_to_audio)
    pron_score = []
    
    #  pronunciation score is stored as a list of tuple: [('Word1', score1), ('Word2', score2), ...]
    for word in pron_json['NBest'][0]['Words']:
        text = word['Word']
        score = word['PronunciationAssessment']['AccuracyScore']
        pron_score.append((text, score))
    
    # let ChatGPT respond to user's input
    chat_history, gpt_msg, cost = chat_with_gpt(chat_history, user_sentence)

    # generate AI voiceover
    text_to_speech(gpt_msg)

    response = {
        'chat': chat_history,   # this will be a list of dictionaries, check https://platform.openai.com/docs/guides/chat/introduction
        'score': pron_score,    # this will be a list of tuple: [('Word1', score1), ('Word2', score2), ...]
        'user_txt': user_sentence,  # this will be string
        'gpt_txt': gpt_msg,     # this will be string
        'ai_speech': 'tts.wav'      # the path to AI generated voice
    }
    
    return response

    
if __name__ == '__main__':
    chat_history = setup_chat(1)

    respond_to_user(chat_history)