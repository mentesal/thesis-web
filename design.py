def design_response(temp):
    if temp == 25:
        return {
            "roof_height": "1m",
            "material": "plastic"
        }
    elif temp > 25:
        return {
            "roof_height": "1.5m",
            "material": "heat-resistant material"
        }
    else:
        return {
            "roof_height": "0.8m",
            "material": "insulated material"
        }


# ask user for input
temp = float(input("Enter temperature: "))

result = design_response(temp)
print("Design response:", result)