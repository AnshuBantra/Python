original_price: float = 75.00
discount_rate: float = 15.00

discount: float = original_price * (discount_rate / 100)
final_price: float = original_price - discount

print(f'The final price after discount is: ${final_price:.2f}')