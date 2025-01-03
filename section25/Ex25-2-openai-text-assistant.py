'''
파일명: Ex25-2-openai-text-assistant.py

대화형 AI 구현하기
    이전 대화 내용을 요약하고 문맥을 이해하여 대화를 이어나가는 방법
'''


from openai import OpenAI, api_key
from pyexpat.errors import messages

client = OpenAI(api_key=api_key)

# 대화 기록을 저장할 messages 리스트
messages = [
    {'role': 'system', 'content': 'You are a helpful assistant'},
    {'role': 'user', 'content': '이순신의 업적 5가지'}
]

# 첫 번째 API 호출
completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=messages
)

# 첫 번째 응답
first_response = completion.choices[0].message.content
print('첫 번째 응답:', first_response)

# assistant의 응답을 message에 추가
messages.append({'role':'assistant', 'content':first_response})
# 두 번째 질문 추가
messages.append({'role':'assistant', 'content':'그 중에 가장 위대한 업적은 뭐야?'})



# 두 번째 API 호출
completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=messages
)

# 두 번째 응답
print('첫 번째 응답:', completion.choices[1].message.content)


