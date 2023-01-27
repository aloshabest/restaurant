def add_list(submenus):
    result_submenu = []

    for submenu in submenus:
        dishes_count = len(submenu.dish)
        submenu.dishes_count = dishes_count
        result_submenu.append(submenu)

    return result_submenu


def add(submenu):
    submenu.dishes_count = len(submenu.dish)

    return submenu
