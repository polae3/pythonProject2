'''
파일명: Ex25-1-openai-api.py

OpenAI API 사용하기
    Open AI에서 제공하는 AI(ChatGPT, DALL-E 등) 모델을 파이썬에서 활용

'''

from openai import OpenAI, api_key

api_key = ''
client = OpenAI(api_key=api_key)

'''
model: 사용할 AI 모델 지정
role:
    system - AI 지시 또는 역할 부여 (페르소나 지정)
    user - 사용자
'''



completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {
            'role':'user',
            'content':'이순신 업적 5가지'
        }
    ]

)

print(completion.choices[0].message.content)