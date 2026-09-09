from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class StockBriefing():
    """StockBriefing crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def stock_data_collector(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_data_collector'], # type: ignore[index]
            verbose=True
        )
    
    @task
    def stock_data_collection_task(self) -> Task:
        return Task(
            config=self.tasks_config['stock_data_collection_task'], # type: ignore[index]
        )

    @agent
    def stock_data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_data_analyst'], # type: ignore[index]
            verbose=True
        )
    @task
    def stock_data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['stock_data_analysis_task'], # type: ignore[index]
        )
    @agent
    def stock_risk_assessor(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_risk_assessor'], # type: ignore[index]
            verbose=True
        )
    @task
    def stock_risk_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['stock_risk_assessment_task'], # type: ignore[index]
        )

    @agent
    def stock_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['stock_reporter'], # type: ignore[index]
            verbose=True
        )
    @task
    def stock_reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['stock_reporting_task'], # type: ignore[index]
        )
    @task
    def stock_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['stock_summary_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the StockBriefing crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
