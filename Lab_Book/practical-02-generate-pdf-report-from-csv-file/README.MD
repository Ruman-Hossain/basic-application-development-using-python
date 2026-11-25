# 📊 PDF Report Generator (From CSV)

This project reads fruit inventory data from a CSV file and generates a formatted PDF report.

---

## 📁 Features

- Read CSV data
- Format data into table
- Generate PDF report
- Maintain logs

---

## 🧱 Project Structure

- `main.py` → Entry point
- `csv_reader.py` → Reads CSV
- `formatter.py` → Prepares table
- `pdf_generator.py` → Generates PDF
- `logger.py` → Logs actions
- `utils.py` → Validation

---

## ⚙️ Requirements

- Python 3.x

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Project
```bash
python main.py
```
## Precautions
### 📂 Input / Output
- Input: fruits_inventory.csv
- Output: report.pdf
### 📝 Notes
CSV must have columns:
- fruit_name
- unit_price
- quantity
- total_price
