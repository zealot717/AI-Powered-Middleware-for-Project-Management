'''import random

def optimize_project_resources(project):
    """Optimize resource allocation for a given project."""
    available_resources = project.allocated_resources

    if not available_resources:
        return {"ProjectID": project.id, "OptimizedResources": []}

    optimized_allocation = [
        {"ResourceID": res["ResourceID"], "Efficiency": random.uniform(0.7, 1.0)}
        for res in available_resources
    ]

    return {"ProjectID": project.id, "OptimizedResources": optimized_allocation}'''

import random
import numpy as np
from deap import base, creator, tools, algorithms
from sqlalchemy.orm import Session
from backend.models.models import Resource, Task

# Define the Genetic Algorithm structure
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

def evaluate(individual, resources, tasks):
    """Fitness function to maximize efficiency based on AI-based criteria."""
    total_efficiency = 0
    for task_idx, resource_idx in enumerate(individual):
        resource = resources[resource_idx]
        task = tasks[task_idx]
        efficiency = random.uniform(0.7, 1.0)  # AI-based simulated efficiency
        total_efficiency += efficiency / (1 + task.complexity)  # Adjusted for task complexity
    return (total_efficiency,)

def optimize_project_resources(db: Session):
    """AI-driven resource allocation using Genetic Algorithm, aligned with the existing service structure."""
    resources = db.query(Resource).all()
    tasks = db.query(Task).all()
    
    if not resources or not tasks:
        return {"message": "No resources or tasks available for optimization."}

    num_tasks = len(tasks)
    num_resources = len(resources)

    toolbox = base.Toolbox()
    toolbox.register("indices", random.sample, range(num_resources), num_tasks)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", evaluate, resources=resources, tasks=tasks)

    pop = toolbox.population(n=50)
    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=30, verbose=False)

    best_individual = tools.selBest(pop, 1)[0]
    allocation = [{"TaskID": tasks[i].task_id, "AssignedResource": resources[best_individual[i]].resource_id} for i in range(num_tasks)]
    
    return {"OptimizedResources": allocation}