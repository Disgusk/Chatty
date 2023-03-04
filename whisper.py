import openai

openai.api_key_path ='.Renviron'

'''
Use this function to do speech to text using whisper.
Input:
- audio: audio file, in mp3, mp4, mpeg, mpga, m4a, wav, or webm file type
Output:
- transcription: string, the generated text
'''
def whisper_transcribe(audio):
    response = openai.Audio.transcribe('whisper-1', audio, language='en', temperature=0)

    return response['text']

if __name__ == '__main__':
    # This is an English sample with VERY HEAVY accent LOL, found on YouTube: https://www.youtube.com/watch?v=LuZV9kkzscg
    audio_file = open('EnglishSample.mp3', 'rb')

    caption = whisper_transcribe(audio_file)

    with open("stt.txt", "w", encoding='utf-8') as text_file:
        text_file.write(caption)