# 5) 요약(Summarization) — 길이 제한 & 톤 제어
import ollama
import json
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

def ask(model, task, system="한국어로 간결하고 정확하게 답해줘.", **options):
    return ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": task}
        ],
        options=options or {}
    )['message']['content']


article = """
생성형 AI는 기업의 문서 검색, 고객지원 자동화, 코드 리뷰 등 다양한 영역에 적용되고 있다.
특히 검색결합형(RAG) 방식은 내부 문서를 실시간으로 참조하여 최신 정보를 제공할 수 있어,
많은 기업들이 도입을 검토하고 있다. 로컬 추론 환경에서도 충분히 활용 가능하다.
"""

prompt = f"""
다음 글을 3문장 이내로 요약하고, 마지막에 핵심 키워드 3개를 해시태그로 제시해줘.
글:
{article}
"""

slack_token = os.getenv("SLACK_BOT_TOKEN")
if not slack_token:
    print("오류: .env 파일에 SLACK_BOT_TOKEN이 설정되지 않았습니다.")
    exit(1)
# WebClient 인스턴스 생성
client = WebClient(token=slack_token)
# 2. 메시지를 보낼 채널 ID 또는 채널 이름을 입력합니다.
channel_name = "C09KBK07GUF" # 예: "#general", "#random" 등

try:
# chat_postMessage API 호출
    response = client.chat_postMessage(
    channel=channel_name,
    text=ask('gemma3:4b', prompt, temperature=0.3)
    )
    print("메시지가 성공적으로 전송되었습니다.")
except SlackApiError as e:
# API 호출 실패 시 에러 코드를 확인합니다.
# 에러 원인: 토큰이 유효하지 않거나, 봇이 채널에 없거나, 권한이 부족한 경우 등
    print(f"메시지 전송에 실패했습니다: {e.response['error']}")