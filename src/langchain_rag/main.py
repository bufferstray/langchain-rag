from importlib.metadata import version
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

def main() -> None:
    llm = ChatAnthropic(model="claude-haiku-4-5-20251001")
    response = llm.invoke("What is the only prime number that is even?")
    print(response)


if __name__ == "__main__":
    main()