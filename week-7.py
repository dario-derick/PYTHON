# -----------------------------
# Task: Load, Analyze, Visualize Iris Dataset
# -----------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# -----------------------------
# Task 1: Load and Explore the Dataset
# -----------------------------
try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Explore structure: data types and missing values
print("\nDataset info:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

# No missing values in Iris dataset, but if there were, we could handle them:
# df.fillna(method='ffill', inplace=True)
# or df.dropna(inplace=True)

# -----------------------------
# Task 2: Basic Data Analysis
# -----------------------------
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Group by species and compute mean for each numerical column
species_group = df.groupby('species').mean()
print("\nMean values per species:")
print(species_group)

# -----------------------------
# Task 3: Data Visualization
# -----------------------------
sns.set_style("whitegrid")  # make plots look nicer

# 1. Line chart: Plot sepal length trend for all samples
plt.figure(figsize=(8,5))
plt.plot(df.index, df['sepal length (cm)'], color='blue', label='Sepal Length')
plt.title("Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart: Average petal length per species
plt.figure(figsize=(8,5))
species_group['petal length (cm)'].plot(kind='bar', color=['red','green','blue'])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=10, color='purple', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot: Sepal length vs Petal length, colored by species
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Set1')
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()
