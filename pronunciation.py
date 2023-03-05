import os
import azure.cognitiveservices.speech as speechsdk
import json

def pron_check_and_read_from_file(audio_path='sample.wav'):
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    audio_config = speechsdk.AudioConfig(filename=audio_path)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    result = speech_recognizer.recognize_once_async().get()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    ref_text = result.text # Speech to text
    speech_recognizer2 =  speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    pronunciation_assessment_config = speechsdk.PronunciationAssessmentConfig(json_string="{\"referenceText\":\"%s\",\"gradingSystem\":\"HundredMark\",\"granularity\":\"Phoneme\"}" %ref_text)
    pronunciation_assessment_config.apply_to(speech_recognizer2)
    result2 = speech_recognizer2.recognize_once()
    pronunciation_assessment_result_json = result2.properties.get(speechsdk.PropertyId.SpeechServiceResponse_JsonResult)
    json_results_pron = json.loads(pronunciation_assessment_result_json) #json version of Pronunciation check results.
    # print(json.dumps(json_results_pron, indent =4))

    return ref_text, json_results_pron
    
def pron_check_from_microphone():
        pronunciation_assessment_config = speechsdk.PronunciationAssessmentConfig(json_string="{\"ReferenceText\":\"Hello my name is George\",\"gradingSystem\":\"HundredMark\",\"granularity\":\"Phoneme\"}")
        speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
        speech_config.speech_recognition_language="en-US"
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        #pronunciation_assessment_config.apply_to(speech_recognizer)
        print("speak into the microphone:")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()
        print(speech_recognition_result.text)
        # The pronunciation assessment result as a JSON string
        pronunciation_assessment_result_json = speech_recognition_result.properties.get(speechsdk.PropertyId.SpeechServiceResponse_JsonResult)
        print(pronunciation_assessment_result_json)

if __name__ == '__main__':
    pron_check_and_read_from_file()
