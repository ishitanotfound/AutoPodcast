import os
import sys
import warnings
import shutil
from datetime import datetime

from .crew import Podcaster
from .tools.custom_tool import generate_podcast_audio

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd") 
# Ignore only SyntaxWarnings that come from the pysbd module(Python Sentence Boundary Disambiguation-It's an NLP library that splits text into sentences.)

def run():
    """
    Run the crew.
    """
    timestamp = datetime.now().strftime("%d%m%Y-%H%M%S")

    run_dir = os.path.join(
        os.getcwd(),
        "outputs",
        f"run-{timestamp}"
    )

    os.makedirs(run_dir, exist_ok=True)
    os.environ["RUN_DIR"] = run_dir

    inputs = {
        "topic": "Latest develpopments in AI and Technology",
        "current_day": str(datetime.now().day),
        "current_month": str(datetime.now().month),
        "current_year": str(datetime.now().year),
        "run_dir": run_dir
    }

    try:
        result = Podcaster().crew().kickoff(inputs=inputs)

        report_path = os.path.join(run_dir, "report.md")
        script_path = os.path.join(run_dir, "script.md")

        shutil.move(
            "outputs/report.md",
            report_path
        )

        shutil.move(
            "outputs/script.md",
            script_path
        )

        print("\nGenerating audio...\n")

        with open(
            script_path,
            "r",
            encoding="utf-8"
        ) as f:
            script = f.read()

        audio_file = generate_podcast_audio(script)

        print(f"\nAudio saved to: {audio_file}\n")

    except Exception as e:
        raise Exception(
            "An error occurred while running the crew:",
            e
        )


#This is CrewAI's mechanism for improving agent performance through iterative refinement.Creates a trained model saved to say my_model.pkl
def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Latest develpopments in AI and Technology",
        'current_day': str(datetime.now().day),
        'current_month': str(datetime.now().month),
        'current_year': str(datetime.now().year),
    }
    try:
        Podcaster().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """

    try:
        Podcaster().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Latest develpopments in AI and Technology",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Podcaster().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

# if this is the main module, run the crew
if __name__ == "__main__":
    run()
