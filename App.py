import os
import azure.cognitiveservices.speech as speechsdk
import json

def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    return [speech_recognition_result, speech_recognition_result.text]

def pron_check(reference_text):
    pronunciation_assessment_config = speechsdk.PronunciationAssessmentConfig(json_string="{\"ReferenceText\":\"%r\",\"gradingSystem\":\"HundredMark\",\"granularity\":\"Phoneme\"}" %reference_text[1])
    
    pronunciation_assessment_config.apply_to(reference_text[0])
    print(reference_text[0])
    #speech_recognition_result = reference_text[0].recognize_once()

    # The pronunciation assessment result as a JSON string
    pronunciation_assessment_result_json = speech_recognition_result.properties.get(speechsdk.PropertyId.SpeechServiceResponse_JsonResult)
    print(pronunciation_assessment_result_json)

def pron_check2():
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

pron_check(recognize_from_microphone())
#pron_check2()
