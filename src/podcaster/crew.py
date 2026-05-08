import os
from typing import List
from datetime import datetime

from crewai import LLM, Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew, before_kickoff
from .tools import search_tool, gemini_voice_tool, file_writer_tool, file_read_tool
from crewai.agents.agent_builder.base_agent import BaseAgent

@CrewBase
class Podcaster():
    """Podcaster crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            llm=LLM(model="gemini/gemini-2.5-flash"),
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True,
            llm=LLM(model="gemini/gemini-2.5-flash"),
        )

    @agent
    def scriptwriter(self) -> Agent:
        return Agent(
            config=self.agents_config['scriptwriter'],
            verbose=True,
            llm=LLM(model="gemini/gemini-2.5-flash"),
            tools=[file_writer_tool, file_read_tool, gemini_voice_tool],
        )

    @before_kickoff
    def _ensure_outputs_dir(self, inputs):
        os.makedirs(os.path.join(os.getcwd(), 'outputs'), exist_ok=True)
        return inputs

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        report_path = os.path.join('outputs', f'report-{timestamp}.md')
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file=report_path,
        )

    @task
    def scripting_task(self) -> Task:
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        script_path = os.path.join('outputs', f'script-{timestamp}.md')
        return Task(
            config=self.tasks_config['scripting_task'],
            output_file=script_path,
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