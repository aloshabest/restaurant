def add_list(menus):
    result_menu = []

    for menu in menus:
        submenus_count = len(menu.submenu)
        dishes_count = sum([len(submenu.dish) for submenu in menu.submenu])
        menu.submenus_count = submenus_count
        menu.dishes_count = dishes_count
        result_menu.append(menu)

    return result_menu


def add(menu):
    submenus_count = len(menu.submenu)
    dishes_count = sum([len(submenu.dish) for submenu in menu.submenu])
    menu.submenus_count = submenus_count
    menu.dishes_count = dishes_count

    return menu