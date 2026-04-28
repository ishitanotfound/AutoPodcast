# 🎙️ AutoPodcast — Multi-AI Podcast Generator

> Drop a topic. Get a podcast. Multi-agent AI that researches, scripts, and voices episodes automatically.

VoxCrew is a multi-agent AI pipeline built with CrewAI and Google Gemini. Give it any topic, and it autonomously researches the latest information, writes a full report, crafts an engaging two-host podcast script, and generates a real audio file — all without any human intervention.

## ✨ What it does

1. 🔍 **Researches** the topic using web search
2. 📝 **Writes** a detailed report from the findings
3. 🎭 **Scripts** a fun, natural two-host podcast episode
4. 🎙️ **Generates** real AI voice audio using Gemini TTS

## 🛠️ Tech Stack

- [CrewAI](https://crewai.com/) — Multi-agent orchestration
- [Google Gemini](https://aistudio.google.com/) — LLM + Text-to-Speech
- [Serper](https://serper.dev/) — Web search
- Python 3.10+

## ⚡ Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/voxcrew.git
cd voxcrew
```

### 2. Install dependencies
```bash
pip install uv
crewai install
```

### 3. Set up environment variables

Create a `.env` file in the root folder:
```
MODEL=gemini/gemini-2.5-flash
GEMINI_API_KEY=your-gemini-key-here
SERPER_API_KEY=your-serper-key-here
```

Get your free API keys:
- **Gemini** → [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
- **Serper** → [serper.dev](https://serper.dev)

### 4. Run it
```bash
crewai run
```

Your outputs will appear in the `outputs/` folder:
- `report-[timestamp].md` — Research report
- `script-[timestamp].md` — Podcast script
- `podcast-[timestamp].wav` — Audio file 🎧

## 🎯 Customize

Want to change the topic? Open `src/podcaster/main.py` and edit:
```python
inputs = {
    'topic': 'Your Topic Here',  # ← change this
}
```

Want to change the agents or tasks? Edit:
- `src/podcaster/config/agents.yaml` — Agent roles and personalities
- `src/podcaster/config/tasks.yaml` — Task instructions

## 📁 Project Structure

```
voxcrew/  
├── src/podcaster/  
│   ├── config/  
│   │   ├── agents.yaml      # Agent definitions  
│   │   └── tasks.yaml       # Task definitions  
│   ├── tools/  
│   │   └── custom_tool.py   # Search, file, and voice tools  
│   ├── crew.py              # Crew setup  
│   └── main.py              # Entry point  
├── outputs/                 # Generated files land here  
└── .env                     # Your API keys (never commit this!)  
```

## 🔑 Notes

- All API keys used are **free tier** — no credit card needed
- Never commit your `.env` file — it's already in `.gitignore`
- The podcast audio is generated using Gemini's multi-speaker TTS with two distinct voices

