import json


def test_get_menu(client, filled_menu, filled_submenu, filled_dish):
    response = client.get(f"/api/v1/menus/")
    assert response.status_code == 200, (
            f'Ожидается код 200, получен: {response.status_code}/'
        )

    response = client.get(f"/api/v1/menus/{filled_menu['id']}")
    assert response.status_code == 200, (
            f'Ожидается код 200, получен: {response.status_code}/'
        )

    response_data = response.json()
    assert response_data["id"] == filled_menu["id_"], (
            f'id не соответствует id filled_menu'
        )

    assert response_data["title"] == filled_menu["title"], (
            f'Заголовок не соответствует заголовку filled_menu'
        )

    assert response_data["description"] == filled_menu["description"], (
            f'Описание не соответствует описаниб filled_menu'
        )

    assert response_data["submenus_count"] == 0, (
            f'Количество подменю не верное у данного меню'
        )

    assert response_data["dishes_count"] == 0, (
            f'Количество блюд не верное у данного меню'
        )


def test_create_menu(client):
    data = {"title": "test", "description": "test description"}
    response = client.post("/api/v1/menus/", data=json.dumps(data))
    response_data = response.json()
    assert response.status_code == 201, (
            f'Ожидается код 201, получен: {response.status_code}/'
        )

    assert response_data["title"] == data["title"], (
            f'Заголовок не соответствует отправленному'
        )

    assert response_data["description"] == data["description"], (
            f'Описание не соответствует отправленному'
        )

    assert response_data["submenus_count"] == 0, (
            f'Количество подменю не верное у данного меню'
        )

    assert response_data["dishes_count"] == 0, (
            f'Количество блюд не верное у данного меню'
        )