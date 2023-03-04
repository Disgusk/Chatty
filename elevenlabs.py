from elevenlabslib import ElevenLabsUser
import os

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

    speech = voice.generate_audio_bytes(text, stability=0)

    try:
        os.remove('tts.wav')
    except OSError:
        pass            

    with open('tts.wav', mode='bx') as f:
        f.write(speech)       


    return 'tts.wav', speech

if __name__  == '__main__':
    text_to_speech('Oh man, that\'s rough. I\'m sorry to hear that you\'re dealing with a difficult professor. What\'s been going on? Is it just their personality or have they been acting inappropriately?')
