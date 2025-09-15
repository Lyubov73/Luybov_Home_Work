import pytest
from api_client import create_project, update_project, get_project

def test_create_project_empty_name():
    response = create_project("")
    assert response.status_code == 400  # или другой ожидаемый код

def test_update_project_invalid_id():
    response = update_project("invalid_id", "New Name")
    assert response.status_code == 404

def test_get_project_nonexistent():
    response = get_project("00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404
