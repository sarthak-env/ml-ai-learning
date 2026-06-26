#  Learn NumPy 

Welcome! This notebook is your complete, hands-on guide to **NumPy** the backbone of data science and machine learning in Python. By the time you're done, you'll be fluent in the language that powers Pandas, TensorFlow, and pretty much everything else in the ML world. 

---

## What You'll Learn:

By the end of this notebook, you'll be able to:

- ✅ Create and manipulate N-dimensional arrays with confidence
- ✅ Perform lightning-fast math operations on entire datasets without a single `for` loop
- ✅ Understand **broadcasting** NumPy's superpower that trips up most beginners
- ✅ Reshape, transpose, and multiply matrices like a pro
- ✅ Sort, compare, and search through arrays efficiently
- ✅ Turn real images into NumPy arrays and understand how computers "see"

---

## Prerequisites:

Before jumping in, make sure you're comfortable with:

- Python basics (lists, loops, functions)
- Nothing else, seriously, that's it! 

---

## Installation:

```bash
# Using pip
pip install numpy matplotlib

# Using conda
conda install numpy matplotlib
```

Then just open the notebook and run the first cell:

```python
import numpy as np
```

You're ready. Let's go! 

---

##  What's Inside:

### 1. Introduction to NumPy
What is NumPy, why does it exist, and why should you care? We kick things off by understanding what makes NumPy so essential and why it's the first library every data scientist learns.

### 2. Core Data Structure: ndarray
Everything in NumPy revolves around one thing the `ndarray`. We'll build 1D, 2D, and 3D arrays from scratch and explore the key attributes you'll use constantly: `dtype`, `shape`, `ndim`, and `size`.

### 3. Array Creation Functions
Stop typing out arrays by hand! Learn NumPy's built-in creation tools:
- `np.zeros` and `np.ones` placeholder arrays in seconds
- `np.arange` like Python's `range()`, but better
- `np.random` generate random data for testing and simulation

### 4. Viewing Arrays and Matrices
Learn how to look inside your arrays:
- `np.unique` find distinct values instantly
- **Indexing & Slicing** pull out exactly the rows, columns, or elements you need (works just like Python lists, but with superpowers for 2D!)

### 5. Manipulating & Comparing Arrays
This is where NumPy starts to feel like magic. Apply operations to an entire array in one line:
- Scalar arithmetic multiply every price by 1.18 (GST) in a single line
- Array vs array operations add, subtract, multiply two arrays element by element
- **Universal Functions (ufuncs)** `np.square`, `np.log`, `np.exp` and more
- **Statistical Methods** `mean`, `min`, `max`, `std`, `var`
- *Bonus:* See why `np.sum()` is **~70× faster** than Python's built-in `sum()` 

### 6. Broadcasting
The concept that makes beginners scratch their heads but once it clicks, you'll wonder how you ever lived without it. We cover:
- Adding a scalar to an entire array
- Adding a 1D array across every row of a 2D matrix
- Adding a column vector across every column
- When broadcasting fails and how to debug shape mismatches

### 7. Reshaping & Transposing Arrays
Same data, different shape. Learn to:
- `.reshape()` rearrange elements into any valid shape
- `.transpose()` / `.T` flip rows and columns instantly

### 8. Array Multiplication: Element-wise vs Dot Product
Two completely different operations, one common source of confusion. We break it down clearly:
- `*` for element-wise (Hadamard) multiplication
- `@` and `np.dot()` for matrix multiplication
- Why shape compatibility matters and how to fix it with `.T`

### 9. Comparison Operators
NumPy can compare every element of an array at once and give you back a Boolean array incredibly useful for filtering data. We cover all six operators: `>`, `<`, `>=`, `<=`, `==`, `!=`.

### 10. Sorting Arrays
Four powerful tools for ordering and finding values:
- `np.sort()` sorted copy of an array, rows or columns
- `np.argsort()` the *indices* of sorted values
- `np.argmin()` where the smallest value lives
- `np.argmax()` where the largest value lives (works across axes too!)

### 11. Turning Images into NumPy Arrays
The coolest section and it'll change how you think about images forever. We load a real JPG, convert it to a NumPy array with `imread()`, and inspect exactly how a computer stores pixel data as numbers.

---

## Key Takeaway:

NumPy is not just a library it's a **way of thinking**. The moment you stop reaching for loops and start thinking in arrays, your code gets faster, shorter, and cleaner. That mindset is what this notebook is here to build.

---

## Notebook Structure: 

```
ml-ai-learning/
└── fundamentals/
    ├── learning_numpy.ipynb   ← You are here
    └── images/
        └── tiger.jpg          ← Used in Section 11
```

---

## How to Run:

```bash
git clone https://github.com/sarthak-env/ml-ai-learning.git
cd ml-ai-learning/fundamentals
jupyter notebook learning_numpy.ipynb
```

---

*Part of the **ml-ai-learning** series, a step-by-step journey through the fundamentals of Machine Learning and AI. Keep going, you're doing great!* 
