from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool

load_dotenv()


def main():
    print("Start ...")
    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo"),
        tool= PythonREPLTool(),
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    python_agent_executor.run("generate and save in current working directory 5 qr codes that point to http://www.timschmelmer.com/ and have a size of 100x100 pixels")

if __name__ == "__main__":
    main()
