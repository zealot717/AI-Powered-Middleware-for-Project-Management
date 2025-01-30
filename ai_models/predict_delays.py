import numpy as np
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

def predict_delays(project_data):
    model = BayesianModel([("SupplierDelay", "ManufacturingDelay"), 
                           ("ManufacturingDelay", "AssemblyDelay"),
                           ("AssemblyDelay", "ProjectCompletion")])
    
    model.fit(data=project_data, estimator=MaximumLikelihoodEstimator)
    
    inference = VariableElimination(model)
    prediction = inference.map_query(variables=["ProjectCompletion"])
    
    return prediction["ProjectCompletion"]