def season(number: int) -> str:
    d = {1: "Зима", 2: "Зима", 12: "Зима",
         4: "Весна", 5: "Весна", 3: "Весна",
         6: "Лето", 7: "Лето", 8: "Лето",
         9: "Осень", 10: "Осень", 11: "Осень"}

    return d[number]