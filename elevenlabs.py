from elevenlabslib import ElevenLabsUser

'''
This function uses Elevenlabs' AI to generate speech from text input
Input:
- text: string
Output:
- 'tts.wav': the path to the generated .wav audio file
- speech: the audio data in bytes type. You probably do not need the audio in bytes form. Playing the .wav file should be sufficient
'''
def text_to_speech(text):
    user = ElevenLabsUser('c90279917ab85ed77a6dbcd04df749c7')
    voice = user.get_voices_by_name('Emma')[0]

    speech = voice.generate_audio_bytes(text, stability=0.4)

    with open('tts.wav', mode='bx') as f:
        f.write(speech)
    
    return 'tts.wav', speech

if __name__  == '__main__':
    text_to_speech('The relationship between what people want to buy and the price of the item is that people tend to buy more of something when the price is lower, and they tend to buy less of it when the price is higher.')
