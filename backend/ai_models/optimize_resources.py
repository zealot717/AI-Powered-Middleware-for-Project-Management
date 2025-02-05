import random

def optimize_project_resources(project):
    """Optimize resource allocation for a given project."""
    available_resources = project.allocated_resources

    if not available_resources:
        return {"ProjectID": project.id, "OptimizedResources": []}

    optimized_allocation = [
        {"ResourceID": res["ResourceID"], "Efficiency": random.uniform(0.7, 1.0)}
        for res in available_resources
    ]

    return {"ProjectID": project.id, "OptimizedResources": optimized_allocation}
