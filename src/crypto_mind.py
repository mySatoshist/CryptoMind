import os
from dotenv import load_dotenv
from datetime import datetime
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
#from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from bot_prompts import *
from bot_tools import *
from cachetools import cached, TTLCache
from random import choice

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY", "")
cache   = TTLCache(maxsize=100, ttl=15)
models  = ["gemini-2.0-flash-lite", "gemini-2.0-flash", "gemini-2.0-flash-thinking-exp-01-21"]

@cached(cache)
def crypto_mind_analysis():
    actual_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    llm = ChatGoogleGenerativeAI(
        model           = choice(models),
        google_api_key  = api_key
    )
    #llm = init_chat_model(model="",provider="",api_key=api_key)

    # 创建提示模板
    prompt = ChatPromptTemplate.from_template(cripto_bot_prompt)

    # 使用管道(|)链接组件定义Chain
    chain = prompt | llm | StrOutputParser()

    info_to_analyse = data_to_analyse(ticker="BTC-USD", periodo="6mo")
    #print(info_to_analyse)

    response = chain.invoke({
        "data_to_analyse" : info_to_analyse,
        "actual_datetime" : actual_datetime
    })

    # 显示回答
    return response.replace("*", "")

#print(crypto_mind_analysis())
