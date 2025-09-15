#!/usr/bin/env python3
"""
Amir Digital Twin - CrewAI Implementation
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import click


@CrewBase
class PersonalAssistantCrew:
    """Personal Assistant crew for Amir"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def personal_assistant(self) -> Agent:
        return Agent(config=self.agents_config["personal_assistant"], verbose=True)

    @agent
    def translator(self) -> Agent:
        return Agent(config=self.agents_config["translator"], verbose=True)

    @agent
    def formatter(self) -> Agent:
        return Agent(config=self.agents_config["formatter"], verbose=True)

    @task
    def personal_interaction_task(self) -> Task:
        return Task(
            config=self.tasks_config["personal_interaction_task"],
        )

    @task
    def translator_task(self) -> Task:
        return Task(
            config=self.tasks_config["translator_task"],
        )

    @task
    def format_response_task(self) -> Task:
        return Task(
            config=self.tasks_config["format_response_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Personal Assistant crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )


@click.command()
@click.argument("user_input")
def main(user_input):
    """
    Run the crew with CLI input.

    USER_INPUT: The prompt or question for Amir's digital twin
    """
    inputs = {"user_input": user_input}

    PersonalAssistantCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    main()
