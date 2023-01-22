import json


def test_menu(client):
    data_menu = {"title": "My test menu 1",  "description": "My test menu description 1"}
    response = client.get(f"/api/v1/menus/")
    assert response.status_code == 200, (
            f'Ожидается код 200, получен: {response.status_code}/'
        )

    assert response.json() == [], (
            f'Ожидается пустой список'
        )

    menu_post = client.post("/api/v1/menus/", json=data_menu)
    assert menu_post.status_code == 201, (
        f'Ожидается код 201, получен: {menu_post.status_code}/'
    )

    response_menu_post = menu_post.json()

    menu_response = client.get(f"/api/v1/menus/{response_menu_post['id']}")
    assert menu_response.status_code == 200, (
            f'Ожидается код 200, получен: {menu_response.status_code}'
        )

    menu_response_data = menu_response.json()
    assert menu_response_data["id"] == response_menu_post["id"], (
            f'id не соответствует id data_menu'
        )

    assert menu_response_data["title"] == response_menu_post["title"], (
            f'Заголовок не соответствует заголовку data_menu'
        )

    assert menu_response_data["description"] == response_menu_post["description"], (
            f'Описание не соответствует описаниб data_menu'
        )

    assert menu_response_data["submenus_count"] == 0, (
            f'Количество подменю не верное у данного меню'
        )

    assert menu_response_data["dishes_count"] == 0, (
            f'Количество блюд не верное у данного меню'
        )

    data_patch = {"title": "My update test menu 1",  "description": "My update test menu description 1"}
    menu_patch = client.patch(f"/api/v1/menus/{response_menu_post['id']}", json=data_patch)
    assert menu_patch.status_code == 200, (
        f'Ожидается код 201, получен: {menu_patch.status_code}/'
    )

    response_menu_patch = menu_patch.json()
    menu_response = client.get(f"/api/v1/menus/{response_menu_patch['id']}")
    assert menu_response.status_code == 200, (
        f'Ожидается код 200, получен: {menu_response.status_code}/'
    )

    menu_response_data = menu_response.json()
    assert menu_response_data["id"] == response_menu_patch["id"], (
        f'id не соответствует id data_patch'
    )

    assert menu_response_data["title"] == response_menu_patch["title"], (
        f'Заголовок не соответствует заголовку data_patch'
    )

    assert menu_response_data["description"] == response_menu_patch["description"], (
        f'Описание не соответствует описаниб data_patch'
    )

    menu_delete_response = client.delete(f"/api/v1/menus/{response_menu_patch['id']}")
    assert menu_delete_response.status_code == 200, (
        f'Ожидается код 200, получен: {menu_delete_response.status_code}/'
    )


def test_submenu(client):
    data_menu = {"title": "My test menu", "description": "My test menu description"}

    menu_post = client.post("/api/v1/menus/", json=data_menu)
    assert menu_post.status_code == 201, (
        f'Ожидается код 201, получен: {menu_post.status_code}/'
    )
    response_menu_post = menu_post.json()

    response = client.get(f"/api/v1/menus/{response_menu_post['id']}/submenus")
    assert response.status_code == 200, (
        f'Ожидается код 200, получен: {response.status_code}/'
    )

    assert response.json() == [], (
        f'Ожидается пустой список'
    )

    data_submenu = {"menu_id": response_menu_post['id'], "title": "My test submenu",
                    "description": "My test submenu description"}
    submenu_post = client.post(f"/api/v1/menus/{response_menu_post['id']}/submenus", json=data_submenu)
    assert submenu_post.status_code == 201, (
        f'Ожидается код 201, получен: {submenu_post.status_code}/'
    )

    response_submenu_post = submenu_post.json()

    submenu_response = client.get(f"/api/v1/menus/{response_menu_post['id']}/submenus/{response_submenu_post['id']}")
    assert submenu_response.status_code == 200, (
        f'Ожидается код 200, получен: {submenu_response.status_code}/'
    )

    submenu_response_data = submenu_response.json()
    assert submenu_response_data["id"] == response_submenu_post["id"], (
        f'id не соответствует id data_submenu'
    )

    assert submenu_response_data["title"] == response_submenu_post["title"], (
        f'Заголовок не соответствует заголовку data_submenu'
    )

    assert submenu_response_data["description"] == response_submenu_post["description"], (
        f'Описание не соответствует описаниб data_submenu'
    )

    assert submenu_response_data["dishes_count"] == 0, (
        f'Количество блюд не верное у данного меню'
    )

    menu_response = client.get(f"/api/v1/menus/{response_menu_post['id']}")
    menu_response_data = menu_response.json()
    assert menu_response_data["submenus_count"] == 1, (
        f'Количество подменю не верное у данного меню'
    )

    data_patch = {"title": "My update test submenu 1", "description": "My update test submenu description 1"}
    submenu_patch = client.patch(f"/api/v1/menus/{response_menu_post['id']}/submenus/{response_submenu_post['id']}",
                                 json=data_patch)
    assert submenu_patch.status_code == 200, (
        f'Ожидается код 201, получен: {submenu_patch.status_code}/'
    )

    response_submenu_patch = submenu_patch.json()
    submenu_response = client.get(f"/api/v1/menus/{response_menu_post['id']}/submenus/{response_submenu_post['id']}")
    assert submenu_response.status_code == 200, (
        f'Ожидается код 200, получен: {submenu_response.status_code}/'
    )

    submenu_response_data = submenu_response.json()
    assert submenu_response_data["id"] == response_submenu_patch["id"], (
        f'id не соответствует id data_patch'
    )

    assert submenu_response_data["title"] == response_submenu_patch["title"], (
        f'Заголовок не соответствует заголовку data_patch'
    )

    assert submenu_response_data["description"] == response_submenu_patch["description"], (
        f'Описание не соответствует описаниб data_patch'
    )

    submenu_delete_response = client.delete(f"/api/v1/menus/{response_menu_post['id']}/submenus/{response_submenu_post['id']}")
    assert submenu_delete_response.status_code == 200, (
        f'Ожидается код 200, получен: {submenu_delete_response.status_code}/'
    )


def test_dish(client):
    data_menu = {"title": "My test menu", "description": "My test menu description"}

    menu_post = client.post("/api/v1/menus/", json=data_menu)
    assert menu_post.status_code == 201, (
        f'Ожидается код 201, получен: {menu_post.status_code}/'
    )
    response_menu_post = menu_post.json()

    data_submenu = {"menu_id": response_menu_post['id'], "title": "My test submenu",
                    "description": "My test submenu description"}
    submenu_post = client.post(f"/api/v1/menus/{response_menu_post['id']}/submenus", json=data_submenu)
    assert submenu_post.status_code == 201, (
        f'Ожидается код 201, получен: {submenu_post.status_code}/'
    )
    response_submenu_post = submenu_post.json()

    response = client.get(f"/api/v1/menus/{response_menu_post['id']}/submenus/{response_submenu_post['id']}/dishes")
    assert response.status_code == 200, (
        f'Ожидается код 200, получен: {response.status_code}/'
    )

    assert response.json() == [], (
        f'Ожидается пустой список'
    )

    data_dish = {"submenu_id": response_submenu_post['id'], "title": "My test dish",
                 "description": "My test dish description", "price": 11.11}
    dish_post = client.post(f"/api/v1/menus/{response_menu_post['id']}/submenus/{response_submenu_post['id']}/dishes",
                            json=data_dish)
    assert dish_post.status_code == 201, (
        f'Ожидается код 201, получен: {dish_post.status_code}/'
    )

    response_dish_post = dish_post.json()

    dish_response = client.get(f"/api/v1/menus/{response_menu_post['id']}/submenus/{response_submenu_post['id']}/dishes/{response_dish_post['id']}")
    assert dish_response.status_code == 200, (
        f'Ожидается код 200, получен: {dish_response.status_code}/'
    )

    dish_response_data = dish_response.json()
    assert dish_response_data["id"] == response_dish_post["id"], (
        f'id не соответствует id data_dish'
    )

    assert dish_response_data["title"] == response_dish_post["title"], (
        f'Заголовок не соответствует заголовку data_dish'
    )

    assert dish_response_data["description"] == response_dish_post["description"], (
        f'Описание не соответствует описаниб data_dish'
    )

    submenu_response = client.get(f"/api/v1/menus/{response_menu_post['id']}/submenus/{response_submenu_post['id']}")
    submenu_response_data = submenu_response.json()
    assert submenu_response_data["dishes_count"] == 1, (
        f'Количество блюд не верное у данного подменю'
    )

    data_patch = {"title": "My update test dish 1", "description": "My update test dish description 1", "price": 15.22}
    dish_patch = client.patch(f"/api/v1/menus/{response_menu_post['id']}/submenus/{response_submenu_post['id']}/dishes/{response_dish_post['id']}",
                                 json=data_patch)
    assert dish_patch.status_code == 200, (
        f'Ожидается код 201, получен: {dish_patch.status_code}/'
    )

    response_dish_patch = dish_patch.json()
    dish_response = client.get(f"/api/v1/menus/{response_menu_post['id']}/submenus/{response_submenu_post['id']}/dishes/{response_dish_post['id']}")
    assert dish_response.status_code == 200, (
        f'Ожидается код 200, получен: {dish_response.status_code}/'
    )

    dish_response_data = dish_response.json()
    assert dish_response_data["id"] == response_dish_patch["id"], (
        f'id не соответствует id data_patch'
    )

    assert dish_response_data["title"] == response_dish_patch["title"], (
        f'Заголовок не соответствует заголовку data_patch'
    )

    assert dish_response_data["description"] == response_dish_patch["description"], (
        f'Описание не соответствует описаниб data_patch'
    )

    dish_delete_response = client.delete(
        f"/api/v1/menus/{response_menu_post['id']}/submenus/{response_submenu_post['id']}/dishes/{response_dish_post['id']}")
    assert dish_delete_response.status_code == 200, (
        f'Ожидается код 200, получен: {dish_delete_response.status_code}/'
    )