import allure
import jsonschema
import pytest
import requests
from .schemas.store_schema import STORE_SCHEMA

BASE_URL = "http://5.181.109.28:9090/api/v3"

@allure.feature("Store")
class TestStore:
    @allure.description("Размещение заказа")
    def test_place_order(self):
        with allure.step("Подготовка данных для создания заказа"):
            payload = {
                "id": 1,
                "petId": 1,
                "quantity": 1,
                "status": "placed",
                "complete": True
            }
        with allure.step("Отправка запроса на размещение заказа"):
            response = requests.post(f"{BASE_URL}/store/order", json=payload)
            response_json = response.json()

        with allure.step("Проверка статуса ответа и валидация json-схемы"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
            jsonschema.validate(response_json, STORE_SCHEMA)
            assert payload["id"] == response_json.get("id")
            assert payload["petId"] == response_json.get("petId")
            assert payload["quantity"] == response_json.get("quantity")
            assert payload["status"] == response_json.get("status")
            assert payload["complete"] == response_json.get("complete")
