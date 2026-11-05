def make_pizzas(size, *pizzas):
    """概述要制作的pizzas"""
    print(f"\n Making a {size}-inch pizza with the followings toppings:")
    for pizza in pizzas:
        print(f"- {pizza}")
