import math
import matplotlib.pyplot as plt

def ask_function_type():
    print("Choose a function to plot:")
    print("1) Linear: y = a*x + b")
    print("2) Quadratic: y = ax^2 + bx + c")
    print("3) Sine: y = A * sin(Bx +C)")
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in {"1", "2", "3"}:
            return choice
        print("Invalid choice, try again.")

def ask_float(prompt, default=None):
    while True:
        raw = input(f"{prompt}" + (f" [default {default}]: " if default is not None else ": ")).strip()
        if raw == "" and default is not None:
            return default
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")

def ask_range():
    print("\nDefine x-range for the plot.")
    x_min = ask_float("x min", -10.0)
    x_max = ask_float("x max", 10.0)
    while x_max <= x_min:
        print("x max must be greater than x min.")
        x_max = ask_float("x max", 10.0)
    num_points = int(ask_float("Number of points", 400))
    return x_min, x_max, num_points

def generate_x_values(x_min, x_max, num_points):
    step = (x_max - x_min)/(num_points - 1)
    return [x_min + i * step for i in range(num_points)]

def compute_y_values(choice, x_values):
    if choice == "1":
        print("\nLinear function: y = a*x + b")
        a = ask_float("a", 1.0)
        b = ask_float("b", 0.0)
        y_values = [a * x + b for x in x_values]
        title = f"Linear: y = {a}*x + {b}"
        return y_values, title
    elif choice == "2":
        print("\nQuadratic function: y = a*x^2 + b*x + c")
        a = ask_float("a", 1.0)
        b = ask_float("b", 0.0)
        c = ask_float("c", 0.0)
        y_values = [a * x**2 + b * x + c for x in x_values]
        title = f"Quadratic: y = {a}*x^2 + {b}*x + {c}"
        return y_values, title
    else:
        print("\nSine function: y = A * sin(B*x + C)")
        A = ask_float("A (amplitude)", 1.0)
        B = ask_float("B (frequency)", 1.0)
        C = ask_float("C (phase shift)", 0.0)
        y_values = [A * math.sin(B * x + C) for x in x_values]
        title = f"Sine: y = {A} * sin({B}*x + {C})"
        return y_values, title
    
def plot_function(x_values, y_values, title):
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, label=title)
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    print("=== Function Grapher ===")
    choice = ask_function_type()
    x_min, x_max, num_points = ask_range()
    x_values = generate_x_values(x_min, x_max, num_points)
    y_values, title = compute_y_values(choice, x_values)
    plot_function(x_values, y_values, title)

if __name__ == "__main__":
    main()

