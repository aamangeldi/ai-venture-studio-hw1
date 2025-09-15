# HW1
Amir's Digital Twin - CrewAI Implementation

A minimal CrewAI "digital twin lite" for Amir, producing short introductions and topic briefs in his authentic tone via terminal interaction.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- [uv](https://docs.astral.sh/uv/guides/install-python/) (dependency management)
- [OpenAI API key](https://platform.openai.com/api-keys) (required for the agents to function)

### Installation

1. Clone or download this example code
2. Install the required dependencies:
   ```bash
   uv pip install .
   ```

3. Create and fill out `.env`:
   ```
   cp .env.template .env
   
   # then follow instructions in .env
   ```

## Usage

Run the main script with a prompt:

```bash
uv run main.py "introduce yourself to the class"
uv run main.py "tell me about your background"
uv run main.py "what are your interests"
```

The system will respond in both English and Russian, representing Amir's voice and personality.

### Help
```bash
uv run main.py --help
```

Optionally, format code:
```bash
uv format
```