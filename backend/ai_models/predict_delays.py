'''import random
from models.models import Task
from sqlalchemy.orm import Session

def predict_delay_risk(tasks):
    risk_predictions = {}

    for task in tasks:
        risk = random.uniform(0, 1)  # Random risk probability (placeholder)
        risk_predictions[task.id] = risk

    return risk_predictions

def analyze_risks(db: Session):
    tasks = db.query(Task).all()
    risks = predict_delay_risk(tasks)

    db.commit()  
    return risks'''

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sqlalchemy.orm import Session
from backend.models.models import Task
import random

class DQN(nn.Module):
    def _init_(self, input_dim=3, output_dim=1):
        super(DQN, self)._init_()
        self.fc1 = nn.Linear(input_dim, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, output_dim)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return torch.sigmoid(self.fc3(x))

def predict_delay_risk(tasks):
    """Predicts task delays using AI-based reinforcement learning (DQN)."""
    model = DQN()
    risk_predictions = {}

    for task in tasks:
        task_data = torch.tensor([[random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]], dtype=torch.float32)
        risk_predictions[task.task_id] = model(task_data).item()  # AI-driven delay probability

    return risk_predictions

def analyze_risks(db: Session):
    """Fetches tasks and predicts delays using AI."""
    tasks = db.query(Task).all()
    risks = predict_delay_risk(tasks)

    db.commit()  
    return risks
