import requests
from config import BASE_URL, HEADERS

def create_project(name):
    payload = {"name": name}
    response = requests.post(f"{BASE_URL}/projects", json=payload, headers=HEADERS)
    return response

def update_project(project_id, new_name):
    payload = {"name": new_name}
    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=payload, headers=HEADERS)
    return response

def get_project(project_id):
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
    return response
