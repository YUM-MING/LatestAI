# # 4) 구조화 출력(JSON)로 정보추출
# import ollama
# import json
# import os
# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError
# from dotenv import load_dotenv
# # .env 파일에서 환경 변수를 로드합니다.
# load_dotenv()

# text = """
# 주문 3건:
# 1) 상품: 무선마우스, 수량 2, 가격 25,000원
# 2) 상품: 기계식 키보드, 수량 1, 가격 89,000원
# 3) 상품: USB-C 케이블, 수량 3, 가격 9,900원
# 총 배송지는 서울시 강남구 테헤란로 1
# """

# prompt = f"""
# 아래 텍스트에서 주문 항목을 JSON으로 추출해.
# 스키마:
# {{
#   "orders":[{{"item":str,"qty":int,"price_krw":int}}],
#   "shipping_address": str,
#   "total_price_krw": int
# }}
# 텍스트:
# {text}
# 반드시 JSON만 출력.
# """

# resp = ollama.chat(
#     model='gemma3:4b',
#     messages=[{"role": "user", "content": prompt}],
#     format='json',  # JSON 모드
#     options={"temperature": 0}
# )

# data = json.loads(resp['message']['content'])

# slack_token = os.getenv("SLACK_BOT_TOKEN")
# if not slack_token:
#     print("오류: .env 파일에 SLACK_BOT_TOKEN이 설정되지 않았습니다.")
#     exit(1)
# # WebClient 인스턴스 생성
# client = WebClient(token=slack_token)
# # 2. 메시지를 보낼 채널 ID 또는 채널 이름을 입력합니다.
# channel_name = "C09KBK07GUF" # 예: "#general", "#random" 등

# try:
# # chat_postMessage API 호출
#     response = client.chat_postMessage(
#     channel=channel_name,
#     text=json.dumps(data, indent=2, ensure_ascii=False)
#     )
#     print("메시지가 성공적으로 전송되었습니다.")
# except SlackApiError as e:
# # API 호출 실패 시 에러 코드를 확인합니다.
# # 에러 원인: 토큰이 유효하지 않거나, 봇이 채널에 없거나, 권한이 부족한 경우 등
#     print(f"메시지 전송에 실패했습니다: {e.response['error']}")

# # ============================================================================
# #  영화 리뷰 분석 - 복잡한 JSON 구조 추출 연습
# # ============================================================================
# """
# [미션]
# 영화 리뷰 텍스트에서 다음 정보를 JSON으로 추출하는 코드를 작성하세요:
# - 영화 제목 (title), 감독 (director), 장르 (genre)
# - 평점 (rating) - 5점 만점의 숫자
# - 장점 리스트 (pros) - 문자열 배열
# - 단점 리스트 (cons) - 문자열 배열
# - 추션: 다른 영화 리뷰로 테스트해보세요!
# # ============================================================================
# """
# 💡 연습 과제:
# 1. 위 코드를 참고하여 좋아하는 영화의 가상 리뷰를 작성하고 JSON 추출을 테스트해보세요.
# 2. 여러 개의 리뷰를 처리하는 반복문을 만들어보세요.
# 3. 추출된 JSON 데이터를 파일로 저장해보세요 (json.dump() 사용).
# 4. 평점이 4.0 이상이고 추천하는 영화만 필터링해보세요.

# 예시 리뷰 텍스트 (테스트용):
# - "봉준호 감독의 '기생충'은 블랙 코미디 스릴러로, 계급 갈등을 예리하게 그려냈다..."
# - "제임스 카메론의 '아바타'는 판타지 액션 영화로, 3D 기술이 혁신적이다..."
# """

# 미션

# 4) 구조화 출력(JSON)로 정보추출
import ollama
import json
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()

text = """
리뷰 3건:
1) 감독: 봉준호, 영화: 기생충, 장르: 블랙 코미디 스릴러, 평점: 4.7점
   장점: 사회적 메시지가 강렬하다, 연출력이 뛰어나다, 배우들의 연기가 훌륭하다
   단점: 다소 불편한 장면이 있다

2) 감독: 제임스 카메론, 영화: 아바타, 장르: 판타지 액션, 평점: 4.5점
   장점: 화려한 비주얼, 독창적인 세계관
   단점: 긴 러닝타임

3) 감독: 크리스토퍼 놀란, 영화: 인셉션, 장르: SF 스릴러, 평점: 4.8점
   장점: 독창적인 스토리, 압도적인 연출, 배우들의 명연기
   단점: 난해한 전개로 일부 관객은 이해가 어려움
총 리뷰 수: 3
"""

prompt = f"""
아래 텍스트에서 리뷰 항목을 JSON으로 추출해.
스키마:
{{
  "reviews":[{{
    "title": str,
    "director": str,
    "genre": str,
    "rating": float,
    "pros": [str],
    "cons": [str]
  }}],
  "total_reviews": int
}}
텍스트:
{text}
반드시 JSON만 출력.
"""

resp = ollama.chat(
    model='gemma3:4b',
    messages=[{"role": "user", "content": prompt}],
    format='json',  # JSON 모드
    options={"temperature": 0}
)

data = json.loads(resp['message']['content'])

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
    text=json.dumps(data, indent=2, ensure_ascii=False)
    )
    print("메시지가 성공적으로 전송되었습니다.")
except SlackApiError as e:
# API 호출 실패 시 에러 코드를 확인합니다.
# 에러 원인: 토큰이 유효하지 않거나, 봇이 채널에 없거나, 권한이 부족한 경우 등
    print(f"메시지 전송에 실패했습니다: {e.response['error']}")