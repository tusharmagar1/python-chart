import pandas as pd
import matplotlib.pyplot as plt
import os

# Correct absolute path to CSV
csv_path = r"C:\Users\aqwa\Documents\PY\students.csv"

# Check if file exists (for safety)
print("CSV exists:", os.path.exists(csv_path))

# Read CSV
data = pd.read_csv(csv_path)

# Create bar chart
plt.bar(data["Name"], data["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()
