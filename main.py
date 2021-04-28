"""
Massachusetts:
Clothing*6.25
WIC food none
Everything else * 6.25
New Hampshire
No sales tax
Maine:
Clothing*5.5
WIC food none
Everything else *5.5

from dataclasses import dataclass


@dataclass
class item:
    object_name: str
    object_type: str
    object_cost: int
"""


class item:
    def __init__(self, object_name, object_type, object_cost):
        self.object_name = object_name
        self.object_type = object_type
        self.object_cost = object_cost


grocery_list = []
grocery_list.append(item('shoes', "clothing", 20))
grocery_list.append(item('carrot', "WIC", 40))
grocery_list.append(item('shirt', "clothing", 200))


def calculate_checkout(state, items):
    amount = 0
    revenue = 0
    for x in items:
        if state == "Massachusetts":
            if x.object_type == "clothing":
                if x.object_cost > 175:
                    j = (x.object_cost * .0625) + x.object_cost
                else:
                    j = x.object_cost
            elif x.object_type == "WIC":
                j = x.object_cost
            else:
                j = (x.object_cost * .0625) + x.object_cost
        elif state == "New Hampshire":
            j = x.object_cost
        elif state == "Maine":
            if x.object_type == "clothing":
                j = (x.object_cost * .055) + x.object_cost
            elif x.object_type == "WIC":
                j = x.object_cost
            else:
                j = (x.object_cost * .055) + x.object_cost
        else:
            print("Incorrect state")
            exit()
        amount = j
        revenue = revenue + amount
    print(revenue)
    return revenue


if __name__ == '__main__':
    purchase = item("sneakers", "clothing", 200)
    calculate_checkout("Massachusetts", grocery_list)
