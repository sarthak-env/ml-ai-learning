# Learn Pandas

Welcome! This notebook is your complete, hands-on guide to **Pandas** — the library that turns raw, messy data into something you can actually understand and work with. By the time you're done, you'll be able to load, clean, explore, and manipulate real datasets with confidence — the exact skills every data science job expects on day one.

---

## What You'll Learn:

By the end of this notebook, you'll be able to:

- ✅ Build and navigate **Series** and **DataFrames** — the two data structures that power all of Pandas
- ✅ Load real datasets from CSV files and immediately understand what's in them
- ✅ Select, filter, and slice data with precision — no loops, no guesswork
- ✅ Group and aggregate data to find patterns that aren't visible row-by-row
- ✅ Clean dirty, real-world data — handle missing values, fix dtypes, and transform columns
- ✅ Visualize data directly from a DataFrame with just one line of code

---

## Prerequisites:

Before jumping in, make sure you're comfortable with:

- Python basics (lists, dictionaries, functions)
- Nothing else — seriously, that's it!

---

## Installation:

```bash
# Using pip
pip install pandas matplotlib

# Using conda
conda install pandas matplotlib
```

Then open the notebook and run the first cell:

```python
import pandas as pd
```

You're ready. Let's go!

---

## What's Inside:

### 1. Introduction to Pandas
What is Pandas, why does it exist, and why is it the first tool every data scientist reaches for? We start by understanding what Pandas is built on (NumPy), what problems it solves, and why it's non-negotiable for anyone working with data.

### 2. Core Data Structures
Everything in Pandas is built on two structures — understand these and everything else clicks:
- **Series** — a single labeled column of data. Create one from a list, a dictionary, or a custom index. Think of it as a smarter Python list
- **DataFrame** — a full table with rows and columns. Create one from a dictionary, a list of dicts, or a CSV file. Think of it as a spreadsheet you can program

### 3. Describing Data
Before you touch any data, you need to understand it. We cover the attributes and methods that give you an instant X-ray of any dataset:
- **Attributes:** `dtypes`, `columns`, `index`, `shape` — know what you're working with before you start
- **Methods:** `.info()`, `.describe()`, `.mean()`, `.sum()` — summarize thousands of rows in one call
- *Gotcha:* `.describe()` silently skips non-numeric columns — we show you exactly why and what to do about it

### 4. Viewing & Selecting Data
This is where most beginners get confused. We cut through it cleanly:
- `.head()` and `.tail()` — the first thing you run on any new dataset
- `.loc[]` vs `.iloc[]` — label-based vs position-based selection, and why mixing them up causes silent bugs
- **Column selection** — bracket notation vs dot notation, and when dot notation will betray you
- **Boolean filtering** — extract exactly the rows you want from thousands of records in one line, no loop needed
- `pd.crosstab()` — see how two categorical columns relate to each other instantly
- `.groupby()` — split your data into groups, apply a function, get answers. The most powerful pattern in Pandas

### 5. Plotting
Real insight requires visualization. Pandas has matplotlib built in, so you never need to leave the notebook:
- **Line plot** via `.plot()` — watch trends across your data in one line
- **Histogram** via `.hist()` — understand the distribution of any column instantly
- *Gotcha:* plotting fails silently if your column is stored as a string — we show you how to catch and fix it

### 6. Data Types
Every column in a DataFrame has a dtype, and getting it wrong breaks everything downstream — your math, your plots, your models. We cover:
- Checking a column's dtype with `.dtype`
- Why numeric columns sometimes get stored as strings (and why `.mean()` then explodes)
- Converting dtypes with `.astype()` and cleaning messy string values with `.str.replace()` before converting

### 7. Manipulating Data
Raw data is never clean. This section is where you build the skills to fix it:
- **String operations** — `.str.lower()` and the `.str` accessor that applies any string method to an entire column at once
- **Missing data** — real datasets always have gaps. Learn `.fillna()` and why filling with the column mean is the standard starting move
- **Adding columns** — four different ways: from a Series, a Python list, another column, or a single scalar value
- **Removing columns** — `.drop()` with `axis=1`, and why you need `axis` in the first place
- **Sampling & shuffling** — `.sample(frac=1)` to shuffle, `.sample(frac=0.2)` to grab a random 20% — essential for ML prep
- **Resetting the index** — after filtering or shuffling, your index is a mess. `.reset_index(drop=True)` fixes it cleanly
- **Applying custom functions** — `.apply()` with a lambda runs any transformation across an entire column instantly. Your replacement for every loop you used to write

---

## Dataset

`orders.csv` is a mock e-commerce dataset built with Indian products and INR pricing — so the examples feel grounded and familiar, not abstract. It has 15 rows and 5 columns:

| Column | Type | Description |
|--------|------|-------------|
| `order_id` | int | Unique order identifier |
| `product` | str | Product name (Phone, Laptop, Rice, etc.) |
| `category` | str | Product category — Electronics, Clothing, or Grocery |
| `price` | float | Price in INR |
| `delivered` | str | Delivery status (Yes / No) |

We also generate two exported versions — `indexed-exported-orders.csv` and `unindexed-exported-orders.csv` — so you can see exactly what `index=False` does and why you'll use it almost every time you export data.

---

## Key Takeaway:

Pandas is not just about tables — it's about **asking questions of data and getting answers fast**. The moment you stop writing loops to process rows and start thinking in Series and DataFrames, you'll write cleaner code, find bugs faster, and do in one line what used to take twenty. That shift in thinking is what this notebook is here to build.

---

## Notebook Structure:

```
ml-ai-learning/
└── fundamentals/
    └── pandas/
        ├── learning_pandas.ipynb   ← You are here
        ├── orders.csv              ← Raw dataset
        ├── indexed-exported-orders.csv
        └── unindexed-exported-orders.csv
```

---

## How to Run:

```bash
git clone https://github.com/sarthak-env/ml-ai-learning.git
cd ml-ai-learning/fundamentals/pandas
jupyter notebook learning_pandas.ipynb
```

---

*Part of the **ml-ai-learning** series — a step-by-step journey through the fundamentals of Machine Learning and AI. Keep going, you're doing great!*
