from langchain_openai import ChatOpenAI,OpenAI

from dotenv import load_dotenv
load_dotenv()


llm=ChatOpenAI(
    model="gpt-5.4-mini",
    temperature=1
)


llm2=OpenAI(
    model='gpt-5.4-mini',
    temperature=1
)



response1=llm.invoke("who is prime minister of india?")
response2=llm2.invoke("who is prime minister of india?")


print(response1.text)
print(response2)