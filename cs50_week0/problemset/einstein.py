"""
Calculates energy given mass with the Special Relativity Equation E = m*c^2
"""

# In meters per second
light_speed = 3 * pow(10, 8)

def main() -> None:
    mass = int(input("m: "))
    energy = mass * pow(light_speed, 2)
    print("E:",energy)


main()
