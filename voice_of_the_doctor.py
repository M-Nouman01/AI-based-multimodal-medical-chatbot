from dotenv import load_dotenv
load_dotenv()


# #Step1a: Setup Text to Speech–TTS–model with gTTS
from gtts import gTTS

# def text_to_speech_with_gtts_old(input_text, output_filepath):
#     language="en"

#     audioobj= gTTS(
#         text=input_text,
#         lang=language,
#         slow=False
#     )
#     audioobj.save(output_filepath)

# # input_text="Hi My name is nouman what guidance you want from me ?"
# # text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# #Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# import os
# import elevenlabs
# from elevenlabs.client import ElevenLabs

# ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

# def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio=client.text_to_speech.convert(
#         text= input_text,
#         voice_id= "QeKcckTBICc3UuWL7ETc",
#         output_format= "mp3_22050_32",
#         model_id= "eleven_turbo_v2"
#     )
#     # client.save(audio, output_filepath)

#     audio_bytes = b"".join(audio)
#     with open(output_filepath, "wb") as f:
#         f.write(audio_bytes)

# # text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 





#Step2: Use Model for Text output to Voice

#Step1a: Setup Text to Speech–TTS–model with gTTS

import subprocess
import platform


def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


    subprocess.Popen(
        [
            r"C:\ffmpeg\bin\ffplay.exe",
            "-nodisp",
            "-autoexit",
            output_filepath
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
 

# input_text="Hi My name is nouman what guidance you want from me . Its new version "
# text_to_speech_with_gtts(input_text=input_text , output_filepath="gtts_testing_autoplay.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs

import os
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text= input_text,
        voice_id= "QeKcckTBICc3UuWL7ETc",
        output_format= "mp3_22050_32",
        model_id= "eleven_turbo_v2"
    )
    # client.save(audio, output_filepath)

    audio_bytes = b"".join(audio)
    with open(output_filepath, "wb") as f:
        f.write(audio_bytes)

    subprocess.Popen(
        [
            r"C:\ffmpeg\bin\ffplay.exe",
            "-nodisp",
            "-autoexit",
            output_filepath
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


# text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3") 
