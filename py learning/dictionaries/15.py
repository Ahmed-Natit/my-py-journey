#!/bin/python3


month_conversion = {
    "jan": "january",
    "feb": "fenruary",
    "mar": "march",
    "apr": "apri",
    "may": "may",
    "jun": "june",
    "july": "july",
    "aug": "august",
    "sept": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december",
}

print(month_conversion.get("sept"))
print(month_conversion.get("snow"))
print(month_conversion.get("snow", "not a valid key"))