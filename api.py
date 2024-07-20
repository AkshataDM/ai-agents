
from fastapi import FastAPI, HTTPException, WebSocket
from contextlib import asynccontextmanager
from pydantic import BaseModel
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema import StrOutputParser
import os 
from fastapi.middleware.cors import CORSMiddleware
from crewai import Crew, Process
from tasks import PreparationTasks
from agents import PreparationAgents


class ResearchModel(BaseModel):
    company: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    openai_api_key = os.environ["OPENAI_API_KEY"]
    yield


api = FastAPI(lifespan=lifespan)

api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@api.post("/research/")
async def ask(research_model: ResearchModel):
    try:

        tasks = PreparationTasks()
        agents = PreparationAgents()
        company = research_model.company
        # Create Agents
        researcher_agent = agents.research_agent()
        recommender_strategy_agent = agents.recommender_strategy_agent()

        # Create Tasks
        research = tasks.research_task(researcher_agent, company)
        recommender_strategy = tasks.recommender_strategy_task(recommender_strategy_agent, company)

        crew = Crew(
                agents=[
                    researcher_agent,
                    recommender_strategy_agent
                ],
                tasks=[
                    research,
                    recommender_strategy
                
                ],
                process=Process.sequential
            )

        result = crew.kickoff()

        return {"response": f"Research result for {research_model.company} {result}"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
