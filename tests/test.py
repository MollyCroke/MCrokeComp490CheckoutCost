import main
from dataclasses import dataclass

def test_checkout():
    @dataclass
    class item:
        object_name: str
        object_type: str
        object_cost: int
    purchases = item("sneakers","clothing",10)
    main.calculate_checkout("Massachusetts",purchases)
