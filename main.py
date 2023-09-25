from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.agents.agent_toolkits import create_python_agent, create_csv_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool, Tool

load_dotenv()


def main():
    print("Start ...")

    python_agent_executor = create_python_agent(
        llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        tool=PythonREPLTool(),
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        agent_executor_kwargs={"handle_parsing_errors": True},
    )

    python_agent_executor.run(
        """generate and save in current working directory 5 qr codes that point to http://www.timschmelmer.com/,
        use the qrcode python packge which you have installed already"""
    )

    csv_agent_executor = create_csv_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        "episode_info.csv",
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )

    csv_agent_executor.run("how many columns are there in episode_info.csv?")
    csv_agent_executor.run("Which writer wrote the most episodes, and how many episodes did they write?")
    csv_agent_executor.run(
        "According to episode_info.csv, which season has the most episodes?"
    )

    # grand_agent_executor = initialize_agent(
    #     tools=[
    #         Tool(
    #             name="PythonAgent",
    #             func=python_agent_executor.run,
    #             description="""useful when you need to transform natural language and write from it python and execute the python code,
    #                         returning the results of the code execution,
    #                         DO NOT SEND PYTHON CODE TO THIS TOOL""",
    #         ),
    #         Tool(
    #             name="CSVAgent",
    #             func=csv_agent_executor.run,
    #             description="""useful when you need to answer question over episode_info.csv file,
    #                          takes an input the entire question and returns the answer after running pandas calculations""",
    #         ),
    #     ],
    #     llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo"),
    #     agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    #     verbose=True,
    # )
    #
    # grand_agent_executor.run(
    #     """generate and save in current working directory 5 qr codes that point to http://www.timschmelmer.com/ and have a size of 100x100 pixels,"
    #     you have qrcode package installed already"""
    # )
    #
    # grand_agent_executor.run(
    #     "print seasons ascending order of the number of episodes they have"
    # )


if __name__ == "__main__":
    main()
