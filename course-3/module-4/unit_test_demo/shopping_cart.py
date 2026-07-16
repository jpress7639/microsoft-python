def calculate_discount(price, discount_percentage):
    """Calculates the discounted price"""
    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount
