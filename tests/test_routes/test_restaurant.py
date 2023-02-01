from dataclasses import dataclass


@dataclass
class MenuData:
    id: str
    title: str
    description: str
    submenus_count: int
    dishes_count: int


@dataclass
class SubmenuData:
    id: str
    title: str
    description: str
    dishes_count: int


@dataclass
class DishData:
    id: str
    title: str
    description: str
    price: str


class TestMenu:
    def test_menu_get_empty(self, client):
        """Checking for an empty menu list"""
        response = client.get('/api/v1/menus/')
        assert response.status_code == 200, (
            f'Ожидается код 200, получен: {response.status_code}/'
        )

        assert response.json() == [], (
            'Ожидается пустой список'
        )

    def test_menu_post_and_get(self, client):
        """Checking sending and receiving menus"""
        data_menu = {
            'title': 'My test menu 1',
            'description': 'My test menu description 1',
        }
        menu_post = client.post('/api/v1/menus/', json=data_menu)
        assert menu_post.status_code == 201, (
            f'Ожидается код 201, получен: {menu_post.status_code}/'
        )

        response_menu_post = menu_post.json()
        MenuData.id = response_menu_post['id']
        MenuData.title = response_menu_post['title']
        MenuData.description = response_menu_post['description']
        MenuData.submenus_count = response_menu_post['submenus_count']
        MenuData.dishes_count = response_menu_post['dishes_count']

        menu_response = client.get(f'/api/v1/menus/{MenuData.id}')
        assert menu_response.status_code == 200, (
            f'Ожидается код 200, получен: {menu_response.status_code}'
        )

        menu_response_data = menu_response.json()
        assert menu_response_data['id'] == response_menu_post['id'], (
            'id не соответствует id data_menu'
        )

        assert menu_response_data['title'] == response_menu_post['title'], (
            'Заголовок не соответствует заголовку data_menu'
        )

        assert menu_response_data['description'] == response_menu_post['description'], (
            'Описание не соответствует описаниб data_menu'
        )

        assert menu_response_data['submenus_count'] == 0, (
            'Количество подменю не верное у данного меню'
        )

        assert menu_response_data['dishes_count'] == 0, (
            'Количество блюд не верное у данного меню'
        )

    def test_menu_delete_and_get(self, client):
        """Checking deleting and receiving menus"""
        menu_delete_response = client.delete(f'/api/v1/menus/{MenuData.id}')
        assert menu_delete_response.status_code == 200, (
            f'Ожидается код 200, получен: {menu_delete_response.status_code}/'
        )

        response = client.get('/api/v1/menus/')
        assert response.status_code == 200, (
            f'Ожидается код 200, получен: {response.status_code}/'
        )

        assert response.json() == [], (
            'Ожидается пустой список'
        )

    def test_menu_post_and_patch(self, client):
        """Checking sending and updating menus"""
        data_menu = {
            'title': 'My test menu 1',
            'description': 'My test menu description 1',
        }
        menu_post = client.post('/api/v1/menus/', json=data_menu).json()
        MenuData.id = menu_post['id']

        data_patch = {
            'title': 'My update test menu 1',
            'description': 'My update test menu description 1',
        }
        menu_patch = client.patch(
            f'/api/v1/menus/{MenuData.id}', json=data_patch,
        )
        assert menu_patch.status_code == 200, (
            f'Ожидается код 201, получен: {menu_patch.status_code}/'
        )

        response_menu_patch = menu_patch.json()
        MenuData.title = response_menu_patch['title']
        MenuData.description = response_menu_patch['description']

        menu_response = client.get(
            f"/api/v1/menus/{response_menu_patch['id']}",
        )
        assert menu_response.status_code == 200, (
            f'Ожидается код 200, получен: {menu_response.status_code}/'
        )

        menu_response_data = menu_response.json()
        assert menu_response_data['id'] == response_menu_patch['id'], (
            'id не соответствует id data_patch'
        )

        assert menu_response_data['title'] == response_menu_patch['title'], (
            'Заголовок не соответствует заголовку data_patch'
        )

        assert menu_response_data['description'] == response_menu_patch['description'], (
            'Описание не соответствует описаниб data_patch'
        )


class TestSubmenu:
    def test_submenu_get_empty(self, client):
        """Checking for an empty submenu list"""
        response = client.get(f'/api/v1/menus/{MenuData.id}/submenus')
        assert response.status_code == 200, (
            f'Ожидается код 200, получен: {response.status_code}/'
        )

        assert response.json() == [], (
            'Ожидается пустой список'
        )

    def test_submenu_post_and_get(self, client):
        """Checking sending and receiving submenus"""
        data_submenu = {
            'menu_id': MenuData.id, 'title': 'My test submenu',
            'description': 'My test submenu description',
        }
        submenu_post = client.post(
            f'/api/v1/menus/{MenuData.id}/submenus', json=data_submenu,
        )
        assert submenu_post.status_code == 201, (
            f'Ожидается код 201, получен: {submenu_post.status_code}/'
        )

        response_submenu_post = submenu_post.json()
        SubmenuData.id = response_submenu_post['id']
        SubmenuData.title = response_submenu_post['title']
        SubmenuData.description = response_submenu_post['description']
        SubmenuData.dishes_count = response_submenu_post['dishes_count']

        submenu_response = client.get(
            f"/api/v1/menus/{MenuData.id}/submenus/{response_submenu_post['id']}",
        )
        assert submenu_response.status_code == 200, (
            f'Ожидается код 200, получен: {submenu_response.status_code}/'
        )

        submenu_response_data = submenu_response.json()
        assert submenu_response_data['id'] == response_submenu_post['id'], (
            'id не соответствует id data_submenu'
        )

        assert submenu_response_data['title'] == response_submenu_post['title'], (
            'Заголовок не соответствует заголовку data_submenu'
        )

        assert submenu_response_data['description'] == response_submenu_post['description'], (
            'Описание не соответствует описаниб data_submenu'
        )

        assert submenu_response_data['dishes_count'] == 0, (
            'Количество блюд не верное у данного меню'
        )

        menu_response = client.get(f'/api/v1/menus/{MenuData.id}')
        menu_response_data = menu_response.json()
        assert menu_response_data['submenus_count'] == 1, (
            'Количество подменю не верное у данного меню'
        )

    def test_submenu_delete_and_get(self, client):
        """Checking deleting and receiving submenus"""
        submenu_delete_response = client.delete(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}',
        )
        assert submenu_delete_response.status_code == 200, (
            f'Ожидается код 200, получен: {submenu_delete_response.status_code}/'
        )

        response = client.get(f'/api/v1/menus/{MenuData.id}/submenus/')
        assert response.status_code == 200, (
            f'Ожидается код 200, получен: {response.status_code}/'
        )

        assert response.json() == [], (
            'Ожидается пустой список'
        )

    def test_submenu_post_and_patch(self, client):
        """Checking sending and updating submenus"""
        data_submenu = {
            'menu_id': MenuData.id, 'title': 'My test submenu',
            'description': 'My test submenu description',
        }
        submenu_post = client.post(
            f'/api/v1/menus/{MenuData.id}/submenus', json=data_submenu,
        ).json()
        SubmenuData.id = submenu_post['id']

        data_patch = {
            'title': 'My update test submenu 1',
            'description': 'My update test submenu description 1',
        }
        submenu_patch = client.patch(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}',
            json=data_patch,
        )
        assert submenu_patch.status_code == 200, (
            f'Ожидается код 201, получен: {submenu_patch.status_code}/'
        )

        response_submenu_patch = submenu_patch.json()
        SubmenuData.title = response_submenu_patch['title']
        SubmenuData.description = response_submenu_patch['description']

        submenu_response = client.get(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}',
        )
        assert submenu_response.status_code == 200, (
            f'Ожидается код 200, получен: {submenu_response.status_code}/'
        )

        submenu_response_data = submenu_response.json()
        assert submenu_response_data['id'] == response_submenu_patch['id'], (
            'id не соответствует id data_patch'
        )

        assert submenu_response_data['title'] == response_submenu_patch['title'], (
            'Заголовок не соответствует заголовку data_patch'
        )

        assert submenu_response_data['description'] == response_submenu_patch['description'], (
            'Описание не соответствует описаниб data_patch'
        )


class TestDish:
    def test_dish_get_empty(self, client):
        """Checking for an empty dish list"""
        response = client.get(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}/dishes',
        )
        assert response.status_code == 200, (
            f'Ожидается код 200, получен: {response.status_code}/'
        )

        assert response.json() == [], (
            'Ожидается пустой список'
        )

    def test_dish_post_and_get(self, client):
        """Checking sending and receiving dishes"""
        data_dish = {
            'submenu_id': SubmenuData.id, 'title': 'My test dish',
            'description': 'My test dish description', 'price': 11.11,
        }
        dish_post = client.post(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}/dishes', json=data_dish,
        )
        assert dish_post.status_code == 201, (
            f'Ожидается код 201, получен: {dish_post.status_code}/'
        )

        response_dish_post = dish_post.json()
        DishData.id = response_dish_post['id']
        DishData.title = response_dish_post['title']
        DishData.description = response_dish_post['description']
        DishData.price = response_dish_post['price']

        dish_response = client.get(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}/dishes/{DishData.id}',
        )
        assert dish_response.status_code == 200, (
            f'Ожидается код 200, получен: {dish_response.status_code}/'
        )

        dish_response_data = dish_response.json()
        assert dish_response_data['id'] == response_dish_post['id'], (
            'id не соответствует id data_dish'
        )

        assert dish_response_data['title'] == response_dish_post['title'], (
            'Заголовок не соответствует заголовку data_dish'
        )

        assert dish_response_data['description'] == response_dish_post['description'], (
            'Описание не соответствует описаниб data_dish'
        )

        submenu_response = client.get(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}',
        )
        submenu_response_data = submenu_response.json()
        assert submenu_response_data['dishes_count'] == 1, (
            'Количество блюд не верное у данного подменю'
        )

    def test_dish_delete_and_get(self, client):
        """Checking deleting and receiving dishes"""
        dish_delete_response = client.delete(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}/dishes/{DishData.id}',
        )
        assert dish_delete_response.status_code == 200, (
            f'Ожидается код 200, получен: {dish_delete_response.status_code}/'
        )

        response = client.get(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}/dishes',
        )
        assert response.status_code == 200, (
            f'Ожидается код 200, получен: {response.status_code}/'
        )

        assert response.json() == [], (
            'Ожидается пустой список'
        )

    def test_dish_post_and_patch(self, client):
        """Checking sending and updating dishes"""
        data_dish = {
            'submenu_id': SubmenuData.id, 'title': 'My test dish',
            'description': 'My test dish description', 'price': 11.11,
        }
        dish_post = client.post(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}/dishes', json=data_dish,
        ).json()
        DishData.id = dish_post['id']

        data_patch = {
            'title': 'My update test dish 1', 'description': 'My update test dish description 1',
            'price': 15.22,
        }
        dish_patch = client.patch(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}/dishes/{DishData.id}',
            json=data_patch,
        )
        assert dish_patch.status_code == 200, (
            f'Ожидается код 201, получен: {dish_patch.status_code}/'
        )

        response_dish_patch = dish_patch.json()
        dish_response = client.get(
            f'/api/v1/menus/{MenuData.id}/submenus/{SubmenuData.id}/dishes/{DishData.id}',
        )
        assert dish_response.status_code == 200, (
            f'Ожидается код 200, получен: {dish_response.status_code}/'
        )

        dish_response_data = dish_response.json()
        assert dish_response_data['id'] == response_dish_patch['id'], (
            'id не соответствует id data_patch'
        )

        assert dish_response_data['title'] == response_dish_patch['title'], (
            'Заголовок не соответствует заголовку data_patch'
        )

        assert dish_response_data['description'] == response_dish_patch['description'], (
            'Описание не соответствует описаниб data_patch'
        )
