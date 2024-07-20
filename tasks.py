from textwrap import dedent
from crewai import Task

class PreparationTasks():
	def research_task(self, agent, company):
		return Task(
			description=dedent(f"""\
				Conduct comprehensive research on the company given. Analyze latest financial news about this company
				Company: {company}
				"""),
			expected_output=dedent("""\
				A detailed report summarizing key findings about the company."""),
			async_execution=True,
			agent=agent
		)

	def recommender_strategy_task(self, agent, company):
		return Task(
			    description=dedent(f"""Generate notes with key points about the company {company} financials. 
				Make a recommendation to the user if they should invest in the company {company} or not. If financial
				information is not available, use the information available to you to make a decision."""),
    			expected_output=dedent("""Comprehensive notes with key talking points.
				 Make sure there is no harmful content"""),
    			agent=agent)
