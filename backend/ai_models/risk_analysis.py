import random

def assess_project_risk(project):
    """Assess project risk based on budget, timeline, and complexity."""
    budget_factor = 1 if project.budget > 5_000_000 else 0.7
    timeline_factor = 1 if project.status == "On Track" else 0.6
    complexity_factor = random.uniform(0.5, 1.0)

    risk_score = round((budget_factor * timeline_factor * complexity_factor) * 100, 2)

    return risk_score
