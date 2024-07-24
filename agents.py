from textwrap import dedent
from crewai import Agent, Process
from langchain.llms import Ollama

# from tools.ExaSearchTool import ExaSearchTool
from langchain_community.tools import DuckDuckGoSearchRun

ollama_model = Ollama(model="llama3")
search_tool = DuckDuckGoSearchRun(backend="news") 

class PreparationAgents():
	def research_agent(self):
		return Agent(
			role='Research Agent',
			goal='Gather the latest financial news about the company.',
			backstory='You are a private equity research agent. You are great at doing background research on the company and finding the latest updates and news.',
			tools=[search_tool],
			verbose=True,
			memory=True
		)

	def summarizer_agent(self):
		return Agent(
				role='Summarizer Agent',
				goal='Generate key points about the research.',
				backstory='Expert in summarizing and generating comprehensive notes.',
				llm=ollama_model,
				verbose=True,
				memory=True,
				allow_delegation=False
			)
	def recommender_agent(self):
		return Agent(
				role='Recommender Agent',
				goal='Generate recommendation based on summary.',
				backstory='Expert in providing a recommendation to invest in the company or not.',
				llm=ollama_model,
				verbose=True,
				memory=True,
				allow_delegation=False
			)