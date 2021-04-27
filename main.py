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
"""
from dataclasses import dataclass


@dataclass
class item:
    object_name: str
    object_type: str
    object_cost: int


def calculate_checkout(state, items):
    amount = 0
    if state == "Massachusetts":
        if items.object_type == "clothing":
            if items.object_cost > 175:
                x = (items.object_cost * .0625) + items.object_cost
            else:
                x = items.object_cost
        elif items.object_type == "WIC":
            x = items.object_cost
        else:
            x = (items.object_cost * .0625) + items.object_cost
    elif state == "New Hampshire":
        x = items.object_cost
    else:
        if items.object_type == "clothing":
            x = (items.object_cost * .055) + items.object_cost
        elif items.object_type == "WIC":
            x = items.object_cost
        else:
            x = (items.object_cost * .055) + items.object_cost
    revenue = x
    amount = revenue + amount
    print(amount)
    return amount



if __name__ == '__main__':
    purchase = item("sneakers", "clothing", 200)
    print(type(calculate_checkout("Massachusetts", purchase)))
