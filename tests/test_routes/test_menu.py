import json


def test_create_menu(client):
    data = {"title": "test", "description": "test description"}
    response = client.post("/api/v1/menus/", data=json.dumps(data))
    response_data = response.json()
    assert response.status_code == 201
    assert response_data["title"] == data["title"]
    assert response_data["description"] == data["description"]
    assert response_data["submenus_count"] == 0
    assert response_data["dishes_count"] == 0
