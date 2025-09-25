# 🤖 Simple Agent

A minimal Python agent that uses Model Context Protocol (MCP) servers to find Airbnb listings, search the web, and write travel plans.

## ⚙️ Prerequisites

- **Python 3.8+**
- **Node.js and npm/npx** (required for MCP servers)
- **OpenAI API Key** (set as `OPENAI_API_KEY` environment variable)

## 📦 Installation

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Ensure npm/npx is available:

   ```bash
   npx --version
   ```

## 🚀 Usage

Run the agent:

```bash
python agent_demo.py
```

The agent will search for Airbnb listings in NYC, find nearby restaurants and attractions, and generate a travel plan in `retreat_plan.md`.

## ✨ What it does

- Uses Airbnb MCP server to find accommodations
- Uses Playwright MCP server for web browsing
- Uses filesystem MCP server to write results
- Generates a comprehensive travel plan with links and images

## 💬 Prompt Used

```text
 Choose a nice place on Airbnb, under $600 usd/night, to stay in NYC
 on the upper east side close to Rockefeller University and Central 
 Park, then use Google to find nearby restaurants and attractions. 
 Write the results in current directory in retreat_plan.md in a nice 
 markdown format, with image links and with a summary at the end.
```
