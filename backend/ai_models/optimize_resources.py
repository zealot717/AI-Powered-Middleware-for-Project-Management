import random
import numpy as np
from datetime import datetime
from deap import base, creator, tools, algorithms
from sqlalchemy.orm import Session
from models.models import Resource, Task

# Define the Genetic Algorithm structure
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

def compute_complexity(task):
    """Estimate task complexity based on duration."""
    try:
        start_date = datetime.strptime(task.start_date, "%Y-%m-%d")
        end_date = datetime.strptime(task.end_date, "%Y-%m-%d")
        complexity = (end_date - start_date).days + 1  # Ensure minimum complexity is 1
        return max(complexity, 1)
    except ValueError:
        print(f"Error parsing dates for TaskID {task.task_id}")
        return 1  # Default complexity if date parsing fails

def evaluate(individual, resources, tasks):
    """Fitness function to maximize efficiency based on AI-based criteria."""
    total_efficiency = 0
    for task_idx, resource_idx in enumerate(individual):
        resource = resources[resource_idx]
        task = tasks[task_idx]
        complexity = compute_complexity(task)  # Use computed complexity
        efficiency = random.uniform(0.7, 1.0)  # AI-based simulated efficiency
        total_efficiency += efficiency / (1 + complexity)  # Adjusted for task complexity
    return (total_efficiency,)

def optimize_project_resources(db: Session):
    """AI-driven resource allocation using Genetic Algorithm."""
    try:
        resources = db.query(Resource).all()
        tasks = db.query(Task).all()

        if not resources or not tasks:
            return {"OptimizedResources": [], "RiskPrediction": "No resources or tasks available."}

        num_tasks = len(tasks)
        num_resources = len(resources)

        toolbox = base.Toolbox()

        if num_tasks > num_resources:
            toolbox.register("indices", lambda: random.choices(range(num_resources), k=num_tasks))
        else:
            toolbox.register("indices", lambda: random.sample(range(num_resources), num_tasks))

        toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
        toolbox.register("select", tools.selTournament, tournsize=3)
        toolbox.register("evaluate", evaluate, resources=resources, tasks=tasks)

        pop = toolbox.population(n=50)
        algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=30, verbose=False)

        best_individual = tools.selBest(pop, 1)[0]
        
        allocation = [
            {
                "ProjectID": tasks[i].project_id,  # Added project ID
                "TaskID": tasks[i].task_id,
                "AssignedResource": resources[best_individual[i]].resource_id
            }
            for i in range(num_tasks)
        ]

        return {"OptimizedResources": allocation}

    except Exception as e:
        print(f"Error in optimize_project_resources: {e}")
        return {"OptimizedResources": []}
