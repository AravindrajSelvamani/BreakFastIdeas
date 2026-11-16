# Healthy Breakfast Ideas

A Python command-line app that uses LangChain and OpenAI to suggest five healthy South Indian breakfast ideas. Each idea is requested in one or two sentences, and the response is printed in the terminal.

## Requirements

- Python and pip
- An OpenAI API key
- An internet connection

## Setup

From the repository root, open PowerShell and run:

```powershell
cd Day10_Breakfast
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install langchain-openai python-dotenv
```

Create a `.env` file in this folder containing:

```dotenv
OPENAI_API_KEY=your_openai_api_key_here
```

Keep your API key private and exclude `.env` from version control.

## Run

With the virtual environment active, run:

```powershell
python breakfast.py
```

The script loads environment variables, sends its breakfast prompt to OpenAI's `gpt-4o-mini` model through LangChain, and prints the response. API usage may incur charges.

## Customize

Edit the `prompt` string in [breakfast.py](breakfast.py) to change the cuisine, number of suggestions, dietary preferences, or response length. The script sends a fixed prompt; it does not ask for input while running.

## Project files

| File | Purpose |
| --- | --- |
| `breakfast.py` | Sends the prompt and prints breakfast suggestions. |
| `.env` | Stores your local API key. |
| `README.md` | Setup and usage instructions. |

## Troubleshooting

- **Missing module:** Activate the virtual environment and rerun the package installation command.
- **Missing or invalid API key:** Check `OPENAI_API_KEY` in this folder's `.env` file.
- **Connection or quota error:** Check your internet connection and OpenAI API account quota.
