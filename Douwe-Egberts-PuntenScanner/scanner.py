import tkinter as tk

# Function to calculate the total points
def calculate_total():
    try:
        # Get the input values from the entry fields
        hundred_points = int(hundred_entry.get()) if hundred_entry.get() else 0
        twenty_points = int(twenty_entry.get()) if twenty_entry.get() else 0
        ten_points = int(ten_entry.get()) if ten_entry.get() else 0
        four_points = int(four_entry.get()) if four_entry.get() else 0
        five_points = int(five_entry.get()) if five_entry.get() else 0
        eight_points = int(eight_entry.get()) if eight_entry.get() else 0

        total_points = (hundred_points * 100) + (twenty_points * 20) + (ten_points * 10) + (eight_points * 8) + (five_points * 5) + (four_points * 4) 

        total_euros = total_points / 200


        # Update the result label to display the total points
        result_label.config(text=f"Total Points: {total_points}\nValued at: €{total_euros:.3f}")
    except ValueError:
        result_label.config(text="Please enter valid or whole numbers.")

# Set up the GUI window
root = tk.Tk()
root.title("Douwe Egberts Points Calculator")
root.geometry("500x500")

# Labels and entry fields for each point type
tk.Label(root, text="Enter the quantity of points:").pack(pady=10)

tk.Label(root, text="100 Points:").pack()
hundred_entry = tk.Entry(root)
hundred_entry.pack(pady=5)

tk.Label(root, text="20 Points:").pack()
twenty_entry = tk.Entry(root)
twenty_entry.pack(pady=5)

tk.Label(root, text="10 Points:").pack()
ten_entry = tk.Entry(root)
ten_entry.pack(pady=5)

tk.Label(root, text="8 Points:").pack()
eight_entry = tk.Entry(root)
eight_entry.pack(pady=5)


tk.Label(root, text="5 Points:").pack()
five_entry = tk.Entry(root)
five_entry.pack(pady=5)


tk.Label(root, text="4 Points:").pack()
four_entry = tk.Entry(root)
four_entry.pack(pady=5)

# Button to calculate the total points
calculate_btn = tk.Button(root, text="Calculate Total", command=calculate_total)
calculate_btn.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="Total Points: 0", font=("Helvetica", 14))
result_label.pack(pady=20)


# Run the Tkinter loop
root.mainloop()
