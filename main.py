result = []

def divider(a, b):
    try:
        if a < b or b == 0 or b > 100:
            raise ValueError("Invalid values for a and/or b")
        return a / b
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key, value in data.items():
    res = divider(key, value)
    if res is not None:
        result.append(res)

print(result)
