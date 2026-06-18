# Pandas

Hands-on learning notebook for the Pandas library, covering everything from core data structures to data manipulation and visualization.

## Files

| File | Description |
|------|-------------|
| `learning_pandas.ipynb` | Main notebook — all concepts, examples, and outputs |
| `orders.csv` | Raw dataset used throughout the notebook (e-commerce orders) |
| `indexed-exported-orders.csv` | DataFrame exported with the default Pandas index |
| `unindexed-exported-orders.csv` | DataFrame exported without the index column |

## What's Covered

**1. Introduction**
- What is Pandas and why use it
- Installation and import

**2. Core Data Structures**
- `Series` — creation from lists, dicts, custom indexes, element access
- `DataFrame` — creation from dicts, list of dicts, CSV files, and exporting

**3. Describing Data**
- Attributes: `dtypes`, `columns`, `index`, `shape`
- Methods: `.info()`, `.describe()`, `.mean()`, `.sum()`

**4. Viewing & Selecting Data**
- `.head()`, `.tail()`
- `.loc[]` (label-based) vs `.iloc[]` (position-based)
- Column selection (bracket and dot notation)
- Boolean filtering (single and multiple conditions)
- `pd.crosstab()`, `.groupby()`

**5. Plotting**
- Line plot via `.plot()`
- Histogram via `.hist()`

**6. Data Types**
- Checking and converting column dtypes

**7. Manipulating Data**
- String operations (`.str.lower()`)
- Handling missing data (`.fillna()`)
- Adding columns (from Series, list, another column, scalar)
- Removing columns
- Sampling and shuffling rows
- Resetting the index
- Applying custom functions (`.apply()`)

## Dataset

`orders.csv` is a mock e-commerce dataset with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `order_id` | int | Unique order identifier |
| `product` | str | Product name |
| `category` | str | Product category (Electronics, Clothing, Grocery) |
| `price` | float | Price in INR |
| `delivered` | str | Delivery status (Yes / No) |

## Requirements

```bash
pip install pandas matplotlib
```
