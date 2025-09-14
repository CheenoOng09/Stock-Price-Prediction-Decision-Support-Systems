import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import matplotlib.pyplot as plt
import re


def load_csv():
    """Load a CSV file and populate the dropdown with column names."""
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        global df, date_column, stock_column, risk_column
        df = pd.read_csv(file_path)
        # Clean column names
        try:
            date_column = df.columns[1]  # Assuming the second column contains dates
            stock_column = df.columns[0]  # Assuming the first column contains stock names
            risk_column = "Classification" # Assuming this is the column name
            df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
            if df[date_column].isnull().all():
                status_label.config(text="Error: Second column could not be parsed as dates.")
                return
        except Exception as e:
            status_label.config(text=f"Date parsing failed: {e}")
            return

        unique_risks = df[risk_column].dropna().unique().tolist()
        risk_drop_down["values"] = ["All Stocks"] + unique_risks
        risk_drop_down.current(0)  # Select the first risk by default

        drop_down_stock1["values"] = df[stock_column].unique().tolist()
        drop_down_stock2["values"] = df[stock_column].unique().tolist()
        drop_down_stock1.current(0)
        drop_down_stock2.current(0)

        drop_down_attribute1["values"] = [col.strip() for col in df.columns[2:7]]
        drop_down_attribute2["values"] = [col.strip() for col in df.columns[2:7]]
        update_stock_dropdown()
        status_label.config(text=f"Loaded: {file_path.split('/')[-1]}")


def update_stock_dropdown():
    """Update the stock dropdown based on the selected risk classification."""
    selected_risk = risk_drop_down.get().strip()
    if selected_risk == "All Stocks":  # If "All Stocks" is selected
        # Include all stocks
        filtered_stocks = df[stock_column].unique()
    elif selected_risk:  # If a specific risk classification is selected
        # Filter stocks by the selected risk classification
        filtered_stocks = df[df[risk_column] == selected_risk][stock_column].unique()
    else:  # No valid risk classification selected
        filtered_stocks = []

    drop_down_stock1["values"] = filtered_stocks.tolist()
    drop_down_stock2["values"] = filtered_stocks.tolist()
    if filtered_stocks.size > 0:
        drop_down_stock1.current(0)  # Select the first stock by default
        drop_down_stock2.current(0)
    else:
        drop_down_stock1.set("")  # Clear selection if no stocks found
        drop_down_stock2.set("")


def plot_graph():
    """Plot selected column as a line graph."""
    selected_column1 = drop_down_attribute1.get().strip()
    selected_column2 = drop_down_attribute2.get().strip() # Strip whitespace from selection
    selected_stock1 = drop_down_stock1.get().strip()
    selected_stock2 = drop_down_stock2.get().strip()
    if selected_stock1 and selected_column1 and selected_column1 and selected_stock2 and selected_column2 and selected_column2 in df.columns:
        filtered_data1 = df[df[stock_column] == selected_stock1]
        filtered_data2 = df[df[stock_column] == selected_stock2]

        plt.figure(figsize=(10, 6))
        plt.plot(filtered_data1[date_column], filtered_data1[selected_column1], label=selected_stock1)
        plt.plot(filtered_data2[date_column], filtered_data2[selected_column1], label=selected_stock2)
        plt.title(f"{selected_stock1} and {selected_stock2}: Predictions for {selected_column1}")
        plt.xlabel("Date")
        plt.ylabel(selected_column1)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        status_label.config(text="Error: Invalid stock or column selected!")


# Initialize the main application window
root = tk.Tk()
root.title("CSV Line Graph Plotter")

# Load CSV Button
load_button = tk.Button(root, text="Load CSV File", command=load_csv)
load_button.pack(pady=10)

risk_label = tk.Label(root, text="Select Risk Classification:", font=("Arial", 12))
risk_label.pack(pady=(10, 0))
risk_drop_down = ttk.Combobox(root, state="readonly", width=30)
risk_drop_down.pack(pady=(0, 10))

risk_drop_down.bind("<<ComboboxSelected>>", lambda e: update_stock_dropdown())

# Drop-down to select stocks
stock_label = tk.Label(root, text="Select Stock:", font=("Arial", 12))
stock_label.pack(pady=(10, 0))  # Add some padding above the dropdown
drop_down_stock1 = ttk.Combobox(root, state="readonly", width=30)
drop_down_stock1.pack(pady=10)


# Drop-down to select Prices or Volume
column_label = tk.Label(root, text="Select Data Column:", font=("Arial", 12))
column_label.pack(pady=(10, 0))  # Add some padding above the dropdown
drop_down_attribute1 = ttk.Combobox(root, state="readonly")
drop_down_attribute1.pack(pady=10)


# Drop-down to select stocks
stock_label = tk.Label(root, text="Select Stock:", font=("Arial", 12))
stock_label.pack(pady=(10, 0))  # Add some padding above the dropdown
drop_down_stock2 = ttk.Combobox(root, state="readonly", width=30)
drop_down_stock2.pack(pady=10)

# Drop-down to select Prices or Volume
column_label = tk.Label(root, text="Select Data Column:", font=("Arial", 12))
column_label.pack(pady=(10, 0))  # Add some padding above the dropdown
drop_down_attribute2 = ttk.Combobox(root, state="readonly")
drop_down_attribute2.pack(pady=10)

# Plot Button
plot_button = tk.Button(root, text="Show Predictions", command=plot_graph)
plot_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Load a CSV file to begin.", fg="green")
status_label.pack(pady=10)

# Global DataFrame Variable
df = None
date_column = None
stock_column = None
risk_column = None

# Run the application
root.mainloop()
