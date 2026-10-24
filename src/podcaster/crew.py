import os
from typing import List
from datetime import datetime

from crewai import LLM, Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew, before_kickoff #decorators and other fns
from .tools.custom_tool import search_tool, file_writer_tool, file_read_tool, gemini_voice_tool
from crewai.agents.agent_builder.base_agent import BaseAgent

llm=LLM(model="gemini/gemini-3.8-flash")

@CrewBase
class Podcaster():
    """Podcaster crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            # "Get the value associated with the key 'reporting_analyst' from the agents_config dictionary.
            config=self.agents_config['researcher'],
            llm=llm,
            tools=[search_tool],
            verbose=True, 
            max_iter=2         
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            llm=llm,
            verbose=True,   
            max_iter=2         
        )

    @agent
    def scriptwriter(self) -> Agent:
        return Agent(
            config=self.agents_config['scriptwriter'],
            llm=llm,
            tools=[file_writer_tool, file_read_tool],
            verbose=True, 
            max_iter=2           
        )

    @before_kickoff
    def _ensure_outputs_dir(self, inputs):
        return inputs

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file="outputs/report.md",
        )

    @task
    def scripting_task(self) -> Task:
        return Task(
            config=self.tasks_config['scripting_task'],
            output_file="outputs/script.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Podcaster crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )