import tkinter as tk

def calculate_cost():
    try:
        distance = float(entry_distance.get())
        mileage = float(entry_mileage.get())
        price = float(entry_price.get())

        fuel = distance / mileage
        cost = fuel * price

        result.config(text=f"Fuel: {fuel:.2f} L\nCost: ₹{cost:.2f}")
    except:
        result.config(text="Invalid input!")

root = tk.Tk()
root.title("Fuel Cost Estimator")
root.geometry("350x300")

tk.Label(root, text="Fuel Cost Estimator", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Distance (km)").pack()
entry_distance = tk.Entry(root)
entry_distance.pack()

tk.Label(root, text="Mileage (km/l)").pack()
entry_mileage = tk.Entry(root)
entry_mileage.pack()

tk.Label(root, text="Petrol Price (₹/l)").pack()
entry_price = tk.Entry(root)
entry_price.pack()

tk.Button(root, text="Calculate", command=calculate_cost).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack()

root.mainloop()
