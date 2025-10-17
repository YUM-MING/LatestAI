# 7) 분류(Classification) — 라벨 집합 고정 & 근거 포함
import ollama
import json
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()


reviews = [
    "배송이 빠르고 포장도 안전했어요.",
    "설명과 다른 제품이 왔고 반품 진행이 너무 느렸습니다.",
    "가격은 좋지만 내구성이 아쉽네요."
]

label_set = ["positive", "neutral", "negative"]


slack_token = os.getenv("SLACK_BOT_TOKEN")
if not slack_token:
    print("오류: .env 파일에 SLACK_BOT_TOKEN이 설정되지 않았습니다.")
    exit(1)
# WebClient 인스턴스 생성
client = WebClient(token=slack_token)
# 2. 메시지를 보낼 채널 ID 또는 채널 이름을 입력합니다.
channel_name = "C09KBK07GUF" # 예: "#general", "#random" 등

results = []

for r in reviews:
    prompt = f"""
아래 리뷰를 {label_set} 중 하나로 분류하고, 한 문장 근거를 제시해.
JSON만 출력:
{{"label": <label>, "reason": <string>}}
리뷰: "{r}"
"""
    out = ollama.chat(
        model='gemma3:4b',
        messages=[{"role": "user", "content": prompt}],
        format='json',
        options={"temperature": 0}
    )
    result = json.loads(out['message']['content'])
    results.append({"review": r, **result})

# Slack 전송 (전체 결과)
try:
    response = client.chat_postMessage(
        channel=channel_name,
        text=json.dumps(results, indent=2, ensure_ascii=False)
    )
    print("Slack 전송 완료: 전체 결과")
except SlackApiError as e:
    print(f"Slack 전송 실패: {e.response['error']}")
