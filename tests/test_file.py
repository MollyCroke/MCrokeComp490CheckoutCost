import main


class item:
    def __init__(self, object_name, object_type, object_cost):
        self.object_name = object_name
        self.object_type = object_type
        self.object_cost = object_cost


def test_checkout():
    grocery_list = []
    grocery_list.append(item('shoes', "clothing", 20))
    grocery_list.append(item('carrot', "WIC", 40))
    grocery_list.append(item('shirt', "clothing", 200))
    assert main.calculate_checkout("Massachusetts", grocery_list) == 272.5


def test_large_checkout():
    grocery_list = []
    grocery_list.append(item('shoes', "clothing", 45))
    grocery_list.append(item('carrot', "WIC", 10))
    grocery_list.append(item('shirt', "clothing", 200))
    grocery_list.append(item("tv", "other", 600))
    assert main.calculate_checkout("New Hampshire", grocery_list) == 855
