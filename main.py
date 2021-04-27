
#Massachusetts:
    #Clothing*6.25
    #WIC food none
    #Everything else * 6.25
#New Hampshire
    #No sales tax
#Maine
    #Clothing*5.5
    #WIC food none
    #Everything else *5.5
from dataclasses import dataclass



@dataclass
class item:
    object_name: str
    object_type: str
    object_cost: int



def calculate_checkout(state, list):
    amount = 0
    if state == "Massachusetts":
        if list.object_type == "clothing":
            if list.object_cost > 175:
                x = (list.object_cost * .0625)+list.object_cost
            else:
                x = list.object_cost
        elif list.object_type == "WIC":
            x= list.object_cost
        else:
            x = (list.object_cost * .0625)+list.object_cost
    elif list.state == "New Hampshire":
            x = list.object_cost
    else:
        if list.object_type == "clothing":
            x = (list.object_cost * .055) + list.object_cost
        elif list.object_type == "WIC":
            x = list.object_cost
        else:
            x = (list.object_cost * .055) + list.object_cost
    revenue = x
    amount = revenue + amount
    print(amount)




if __name__ == '__main__':
    purchase = item("sneakers", "clothing", 200)
    calculate_checkout("Massachusetts", purchase)
