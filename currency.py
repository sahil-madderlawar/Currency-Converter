import requests

def convert_currency(amount, from_currency, to_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][to_currency]
        result = amount * rate
        return round(result, 2)
    except:
        return "Error: Invalid currency codes"

amount = float(input("Amount: "))
from_curr = input("From: ").upper()
to_curr = input("To: ").upper()
result = convert_currency(amount, from_curr, to_curr)
print(f"{amount} {from_curr} = {result} {to_curr}")