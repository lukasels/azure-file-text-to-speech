import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig


# Replace with possible voices (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#text-to-speech)
# (e.g., voice = "en-US-AriaRUS")
voice = "voice_name"

# Replace with your own subscription key and service region (e.g., "westus")
# Side note: some regions do not support text-to-speech
speech_key, service_region = "subscription_key", "service_region"

# Replace with input file name and format
input_file = open("input_file.txt", "r")
text = input_file.read()

# Replace desired output file name and format
output_file = "output_file.mp3"


# Creates an instance of a speech config with a specified subscription key and service region
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Inputs the selected voice
speech_config.speech_synthesis_voice_name = voice

# Creates a speech synthesizer that stores the audio output in the output_file
audio_config = AudioOutputConfig(filename=output_file)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Synthesizes the received text to speech
result = speech_synthesizer.speak_text_async(text).get()

# Checks the result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized to speaker for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
    print("Did you update the subscription info?")
# </code>

input_file.close()