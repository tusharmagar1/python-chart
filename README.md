# 📊 Student Marks Bar Chart using Python

A simple Python project that reads student data from a CSV file and visualizes student marks using a bar chart with **Pandas** and **Matplotlib**.

## 📌 Features

- Reads student data from a CSV file
- Checks whether the CSV file exists before loading
- Displays a bar chart of student marks
- Uses Pandas for data handling
- Uses Matplotlib for data visualization

---

## 📂 Project Structure

```
Student-Marks-Chart/
│
├── students.csv
├── main.py
└── README.md
```

---

## 📄 Sample CSV (students.csv)

| Name | Marks | Department | Attendance |
|------|------:|------------|-----------:|
| Amit | 78 | CS | 80 |
| Riya | 65 | IT | 90 |
| Rahul | 85 | CS | 76 |
| Sneha | 72 | CS | 70 |
| Kunal | 90 | ECE | 88 |

---

## 🛠 Requirements

Install the required Python libraries:

```bash
pip install pandas matplotlib
```

---

## ▶️ How to Run

1. Place `students.csv` in the specified directory.
2. Update the file path if necessary:

```python
csv_path = r"C:\Users\aqwa\Documents\PY\students.csv"
```

3. Run the program:

```bash
python main.py
```

---

## 📜 Code Overview

The program performs the following steps:

1. Imports required libraries.
2. Checks if the CSV file exists.
3. Reads the CSV using Pandas.
4. Creates a bar chart of student marks.
5. Displays the chart.

---

## 📊 Output

The program generates a **bar chart** showing:

- **X-axis:** Student Names
- **Y-axis:** Marks

Example:

```
Marks
90 |                     █
85 |              █      █
80 | █            █      █
75 | █            █      █
70 | █      █     █      █
65 | █      █     █      █
    --------------------------------
     Amit  Riya Rahul Sneha Kunal
```

---

## 📚 Libraries Used

- **Pandas** – Reading and handling CSV data
- **Matplotlib** – Creating bar charts
- **OS** – Checking file existence

---

## 💡 Future Improvements

- Add different chart types (Pie, Line, Histogram)
- Display attendance analysis
- Compare department-wise average marks
- Save charts as PNG images
- Add user input for CSV file selection
- Use Seaborn for enhanced visualizations

---

## 👨‍💻 Author

**Tushar Magar**

Learning Python Data Analysis and Data Visualization using Pandas and Matplotlib.

---

## 📜 License

This project is open-source and available for educational purposes.
