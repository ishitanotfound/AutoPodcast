from .custom_tool import gemini_voice_tool
import os
os.environ["RUN_DIR"] = r"C:\Z\Tech\Projects\AutoPodcast\outputs\test"

with open(
    r"C:\Z\Tech\Projects\AutoPodcast\outputs\run-11102026-041522\script.md",
    "r",
    encoding="utf-8"
) as f:
    script = f.read()

result = gemini_voice_tool.run(script)

print(result)