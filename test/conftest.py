import jsonschema
import pytest
import requests
from .schemas.pet_schema import PET_SCHEMA

BASE_URL = "http://5.181.109.28:9090/api/v3"

@pytest.fixture(scope="function")
def create_pet():
    payload = {
        "id": 10,
        "name": "Buddy",
        "status": "available"
    }

    response = requests.post(f"{BASE_URL}/pet", json=payload)
    response_json = response.json()

    assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
    jsonschema.validate(response_json, PET_SCHEMA)

    return response_json