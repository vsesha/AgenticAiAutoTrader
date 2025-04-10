import asyncio
from agents import function_tool

@function_tool
async def calculate_tax(order_total: float, tax_rate: float) -> str:
    print(f"calculating tax function called for the amount:{order_total} ")
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


@function_tool
async def calculate_tariff(order_total: float, origin_country_of_car: str) -> str:
    """
    Calculates the tariff for a given car based on the country of its origin.
    This function will be invoked by LLM (GPT in this case) with appropriate Args.
    This tariff is a sample exercise for function calling.
    Args:
        order_total (float): Total order value before tariff.
        origin_country_of_car (str): Country of origin (e.g., USA, China, Germany, Japan).
    """
    print(f"calculate_tariff called for origin: {origin_country_of_car}, order total: {order_total}")

    # Default tariff rate
    tariff_rate = 0
    # Normalize country name (optional)
    origin = origin_country_of_car.strip().lower()
    if origin in ["usa","us","united states","united states of america","america"]:
        tariff_rate = 0
    elif origin in ["japan","jp"]:
        tariff_rate = 30
    elif origin in ["eu", "europe", "germany", "france", "italy", "de", "se", "gb", "uk"]:
        tariff_rate = 40
    elif origin in ["china","cn"]:
        tariff_rate = 104
    print("Tariff rate: ", tariff_rate)
    tariff_amount = order_total * (tariff_rate / 100)
    total_with_tariff = order_total + tariff_amount
    
    response = "The tariff amount on your car originated from ${origin} is ${tariff_amount:.2f}. " \
    "Your total with tax is ${total_with_tariff:.2f}."
    
    return response
