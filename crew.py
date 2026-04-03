import os
from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from dotenv import load_dotenv

load_dotenv()
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ContentCreation():
    """ContentCreation crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config ="config/agents.yaml"
    tasks_config ="config/tasks.yaml"

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def content_idea_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['content_idea_agent'], # type: ignore[index]
            llm=LLM(model="gemini-2.5-flash",base_url="https://generativelanguage.googleapis.com/v1beta/openai/",api_key=os.getenv("GEMINI_API_KEY")),
            verbose=True
        )

    @agent
    def seo_optimizer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_optimizer_agent'], # type: ignore[index]
            llm=LLM(model="gemini-2.5-flash",base_url="https://generativelanguage.googleapis.com/v1beta/openai/",api_key=os.getenv("GEMINI_API_KEY")),
            verbose=True
        )


    @agent
    def content_editor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['content_editor_agent'], # type: ignore[index]
            llm=LLM(model="gemini-2.5-flash",base_url="https://generativelanguage.googleapis.com/v1beta/openai/",api_key=os.getenv("GEMINI_API_KEY")),
            verbose=True
        )
    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def idea_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['idea_generation_task'], # type: ignore[index]
        )

    @task
    def seo_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config['seo_optimization_task'],
            context=[self.idea_generation_task()]
        
        )
    
    @task
    def content_editing_task(self) -> Task:
        return Task (
            config=self.tasks_config['content_editing_task'],
            context=[self.seo_optimization_task()],
            output_file="./article.md"
         ) # type: ignore[index]
        

    @crew
    def crew(self) -> Crew:
        """Creates the ContentCreation crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            llm=LLM(model="gemini-2.5-flash",base_url="https://generativelanguage.googleapis.com/v1beta/openai/",api_key='AIzaSyDjfuev6EimdTUzgz3TbHYng7RDPhX5o4k'),
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
