def allocate_resources(data):
    workers = data["workers"]
    materials = data["materials"]
    deadlines = data["deadlines"]
    
    allocated_workers = min(workers, 100)
    allocated_materials = min(materials, 500)
    
    return {"workers": allocated_workers, "materials": allocated_materials, "deadline_met": deadlines > 30}