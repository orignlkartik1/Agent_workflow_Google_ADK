# Agent Workflow

This project is a small Google ADK agent workflow. It defines two agents in
`my_agent/agent.py`:

- `generate_fruit_agent`: understands the user's fruit-related query and gives
  brief fruit details.
- `generate_benefit_agent`: adds a health benefit for the specified fruit.

The `root_agent` is a `Workflow` that runs both agents as part of the same
agent workflow.

## Project Structure

```text
Agent_workflow/
+-- my_agent/
|   +-- agent.py        # Agent and workflow definitions
|   +-- __init__.py     # Python package marker
|   +-- .env            # Local environment variables, not committed
|   +-- .adk/           # Local ADK session data, not committed
+-- pyproject.toml      # Python project metadata
+-- README.md
```

## Requirements

- Python 3.14 or newer, based on `pyproject.toml`
- Google ADK
- A Google API key that can access the configured Gemini model

The agents currently use the `gemini-2.5-flash` model.

## Setup

From the project root:

```powershell
cd C:\Users\karti\PycharmProjects\Agent_workflow
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the Google ADK package:

```powershell
pip install google-adk
```

If PowerShell blocks virtual environment activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Environment Variables

Create or update `my_agent/.env` with:

```env
GOOGLE_GENAI_USE_ENTERPRISE=false
GOOGLE_API_KEY=your_google_api_key_here
```

Do not commit `.env` to version control. It is already ignored by
`my_agent/.gitignore`.

## Run From Terminal

Run the agent in interactive mode:

```powershell
adk run my_agent
```

Run the agent with one message:

```powershell
adk run my_agent "Tell me about mango"
```

You can also call the ADK executable from the local virtual environment:

```powershell
.\.venv\Scripts\adk.exe run my_agent "Tell me about apple"
```

## Run With ADK Web UI

Start the local web interface:

```powershell
adk web .
```

Or use a specific port:

```powershell
adk web --port 8000 .
```

Then open the local URL shown in the terminal, usually:

```text
http://127.0.0.1:8000
```

## Main File

The workflow is defined in `my_agent/agent.py`:

```python
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
```

## Notes

- `.adk/` stores local ADK session data.
- `__pycache__/` contains generated Python cache files and can be ignored.
- If `adk` is not recognized, make sure the virtual environment is activated or
  run `.\.venv\Scripts\adk.exe` directly.
