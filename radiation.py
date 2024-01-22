import numpy as np

def calculate_nuclear_radiation(activity_initial, time, half_life):
    return activity_initial * (0.5 ** (time / half_life))

def main():
    activity_initial = float(input("Enter initial activity (Bq): "))
    time = float(input("Enter time (seconds): "))
    half_life = float(input("Enter half-life (seconds): "))

    radiation_activity = calculate_nuclear_radiation(activity_initial, time, half_life)

    print(f"Nuclear radiation activity after {time} seconds: {radiation_activity} Bq")

if __name__ == "__main__":
    main()
