from openai import OpenAI
from dotenv import load_dotenv
# .env 파일에서 환경 변수 로드
load_dotenv()
# API 키는 환경 변수(`OPENAI_API_KEY`)에서 자동으로 로드됩니다.
client = OpenAI()
def chat_completions():
    try:
        # Chat Completions API 호출
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            # 'messages' 배열에 사용자의 질문을 담아 전달
            messages=[
                {"role": "user", "content": "한국의 수도는 어디인가요?"}
            ]
        )
        # 응답에서 메시지 내용 추출 및 출력
        message_content = response.choices[0].message.content
        print(message_content)
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# chat_completions 출력값
# 한국의 수도는 서울입니다.

def chat_streaming():
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "한국에 대해서 설명해주세요"}], #"한국에 대해서 설명해주세요"
            #max_tokens = 100,
            stream=True
        )
        for chunk in response:
            print(chunk.choices[0].delta.content or "", end="", flush=True)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
if __name__ == "__main__":
    chat_completions()

# chat_streaming 출력값
# 한국, 정식 명칭은 대한민국(남한)과 조선민주주의인민공화국(북한)으로 나뉘어 있는 동아시아의 나라입니다. 한반도에 위치하고 있으며, 주변에는 일본, 중국이 있습니다. 

# ### 역사
# 한국의 역사는 고대부터 시작되어 삼국시대(고구려, 백제, 신라), 고려, 조선으로 이어집니다. 20세기 초반, 일본 제국의 식민지로 겪은 고통은 한국 역사에서 중요한 전환점이 되었고, 1945년 제2차 세계대전 종전 후, 남북이 각각 독립 국가로 분단되었습니다. 1950년부


# ### 문화
# 한국은 풍부한 문화유산과 전통을 가지고 있습니다. 한복, 김치, 한글(고유의 문자), 한국의 전통 음악과 춤 등은 한국 문화를 대표하는 요소들입니다. 현대에는 K-pop, K-drama 등으로 대표되는 대중 문화도 세계적으로 큰 인기를 끌고 있습니다.

# ### 언어
# 한국어는 공식 언어이며, 한글이라는 독창적인 문자 체계를 사용합니다. 한글은 세종대왕에 의해 15세기 초에 창제되었습니다.
# ### 자연
# 한반도는 사계절이 뚜렷하며, 아름다운 자연 경관을 자랑합니다. 산과 바다, 사막과 하천 등 다양한 지형이 존재합니다. 대표적인 관광지로는 경주, 서울, 부산, 제주도 등이 있습니다.

# 한국은 전통과 현대가 조화롭게 어우러진 나라로, 역사, 문화, 경제 등이 복합적으로 얽혀 있는 매력적인 국가입니다.