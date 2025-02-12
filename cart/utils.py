def calculate_cart_total(cart, movies_in_cart):
    total = 0
    for movie in movies_in_cart:
        quantity = cart[str(movie.id)]
        total += movie.price * int(quantity)
    return total

def get_quantities(cart, movies_in_cart):
    quantities = {}
    for movie in movies_in_cart:
        quantity = cart[str(movie.id)]
        quantities[movie.id] = int(quantity) 
    return quantities