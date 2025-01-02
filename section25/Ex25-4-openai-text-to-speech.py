'''
파일명: Ex25-4-openai-text-to-speech.py

OpenAI TTS(text to speech)
    텍스트를 음성으로 변환하는 기술
'''
from http.client import responses

from openai import OpenAI


client = OpenAI(api_key=api_key)

def generate_speech(text, voice='alloy', output_file='speech.mp3'):

    response = client.audio.speech.create(
        model='tts-1',
        voice=voice,    # alloy, echo, fable, onyx, nova, shimmer 목소리 선택
        input=text
    )

    response.stream_to_file(output_file)
    return f'Speech saved to {output_file}'

# 실행코드
text1 = '나는 그곳에 간다'
result1 = generate_speech(text1)
print(result1)