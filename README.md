# pyspark-flatten-file

A PySpark utility to pivot and flatten vertically structured (long-format) CSV data into a clean, wide-format table.

---

## What It Does

This script reads a CSV file where each person's attributes (first name, last name, address, phone) are stored as separate rows with an indicator column (`ind`). It uses PySpark `when` / `otherwise` logic and `groupBy` + `agg` to pivot the data into one flat row per person.

**Input format (long/vertical):**

| id | ind | fname | lname | apartment | street |
|---|---|---|---|---|---|
| 1 | FN | John | | | |
| 1 | LN | | Doe | | |
| 1 | AD | | | 10A | Main St |
| 1 | PH | 9999999999 | | | |

**Output format (wide/flat):**

| id | fname | lname | apartment | street | city | country | phone |
|---|---|---|---|---|---|---|---|
| 1 | John | Doe | 10A | Main St | ... | ... | 9999999999 |

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| PySpark | Distributed data processing |
| Spark SQL Functions | `when`, `otherwise`, `concat_ws`, `split`, `groupBy`, `agg` |
| SparkSession | Entry point for Spark application |

---

## Key PySpark Concepts Used

- `f.when(condition, value).otherwise(default)` — conditional column logic
- `f.concat_ws(separator, *cols)` — concatenate columns into address string
- `groupBy("id").agg(f.min(...))` — collapse multiple rows per person into one
- `f.split(col, delimiter).getItem(index)` — parse address string into fields
- Filtering null/placeholder rows with `f.col(...) != f.lit("null")`

---

## Files

| File | Description |
|---|---|
| `flatten.py` | Main PySpark transformation script |
| `flatten.csv` | Sample input dataset (long format) |
| `README.md` | Documentation |

---

## How to Run

```bash
# Submit via spark-submit
spark-submit flatten.py

# Or run locally in a PySpark-enabled environment (Databricks, local Spark, etc.)
python flatten.py
```

> Update the file path in `flatten.py` to point to your local `flatten.csv` before running.

---

## Skills Demonstrated

- Data transformation with PySpark DataFrame API
- Pivot/unpivot patterns using conditional aggregation
- Working with structured CSV data in distributed compute environments
- Applicable to real-world ETL pipelines (e.g., normalising CRM or ERP flat files)

---

*Part of a broader data engineering portfolio — [view more](https://ar2029.github.io/prasoon-portfolio/)*
