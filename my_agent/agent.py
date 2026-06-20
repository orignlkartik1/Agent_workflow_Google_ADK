from google.adk import Agent, Workflow

generate_fruit_agent = Agent(
    name="generate_fruit_agent",
    model="gemini-2.5-flash",
    instruction="Understand the user query and give brief details about the fruit ",
)

generate_benefit_agent = Agent(
    name="generate_benefit_agent",
    model="gemini-2.5-flash",
    instruction="Tell me a health benefit about the specified fruit.",
)

root_agent = Workflow(
    name="root_agent",
    edges=[("START", generate_fruit_agent, generate_benefit_agent)],
)