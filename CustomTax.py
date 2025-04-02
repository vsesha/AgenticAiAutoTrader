import asyncio
from agents import function_tool

@function_tool
async def calculate_tax(order_total: float, tax_rate: float) -> str:
    print(f"[debug] calculating tax function called for the amount:{order_total} ")
    """Calculates the tax for a given order total based on the input amount (float) and tax rate (float).
    Args:
        order_total: The total amount of the order before tax.
        location: The location of the order. Defaults to Los Angeles, CA.
    """
    tax_rate = 9  
    print("tax-rate now - ",tax_rate)
    tax_amount = order_total * tax_rate
    total_with_tax = order_total + tax_amount
    return f"The tax on your sale is ${tax_amount:.2f}. Your total with tax is ${total_with_tax:.2f}."