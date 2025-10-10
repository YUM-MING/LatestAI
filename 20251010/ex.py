from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
# .env 파일에서 환경 변수를 로드합니다.
load_dotenv()
# model
llm = ChatOpenAI(model="gpt-4o-mini")
# chain 실행
print(llm.invoke("지구의 자전 주기는?"))

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("You are an expert in astronomy. Answer the question. <Question>: {input}")
llm = ChatOpenAI(model="gpt-4o-mini")
# chain 연결
chain = prompt | llm
# chain 호출
chain.invoke({"input": "지구의 자전 주기는?"})

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# prompt + model + output parser
prompt = ChatPromptTemplate.from_template("You are an expert in astronomy. Answer the question. <Question>: {input}")
llm = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()
# LCEL chaining
chain = prompt | llm | output_parser
# chain 호출
chain.invoke({"input": "지구의 자전 주기는?"})

prompt1 = ChatPromptTemplate.from_template("translates {korean_word} to English.")
prompt2 = ChatPromptTemplate.from_template("explain {english_word} using oxford dictionary to me in Korean.")
llm = ChatOpenAI(model="gpt-4o-mini")
chain1 = prompt1 | llm | StrOutputParser()
chain1.invoke({"korean_word":"미래"})

chain2 = (
{"english_word": chain1}
| prompt2
| llm
| StrOutputParser()
)

chain2.invoke({"korean_word":"미래"})

#content='지구의 자전 주기는 약 24시간입니다. 이 주기는 지구가 한 번 자전을 완료하는 데 걸리는 시간으로, 보통 "1일"이라고 합니다. 그러나 정확하게 말하자면, 지구가 태양을 한 번 돌아서 같은 위 치에서 다시 보이기 위해 필요한 시간(태양일)은 약 24시간입니다. 한편, 지구가 별을 기준으로 한 자전 주기는 약 23시간 56분 4초로, 이를 \'항성일\'이라고 합니다.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 115, 'prompt_tokens': 15, 'total_tokens': 130, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_51db84afab', 'id': 'chatcmpl-CP2H0evu3NXWmo3m5k94gPjZ3t7hC', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='run--1d252ae0-447d-402c-8918-f568bfdc45ff-0' usage_metadata={'input_tokens': 15, 'output_tokens': 115, 'total_tokens': 130, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
