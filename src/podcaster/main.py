import sys
import warnings

from datetime import datetime

from .crew import Podcaster

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd") #Python Sentence Boundary Disambiguation

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_month': str(datetime.now().month),
        'current_year': str(datetime.now().year)
    }
    
    try:
        Podcaster().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception("An error occurred while running the crew: ",e)


#This is CrewAI's mechanism for improving agent performance through iterative refinement.Creates a trained model saved to say my_model.pkl
def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_month': str(datetime.now().month),
        'current_year': str(datetime.now().year)
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
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Podcaster().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
