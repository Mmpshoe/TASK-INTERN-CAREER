import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset into a Pandas DataFrame
# For this example, let's assume you have a CSV file named 'data.csv'
df = pd.read_csv('youtubers_df.csv')
"""
# Display the first few rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head())"""

# Basic statistics summary of the DataFrame
print("\nSummary statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Data visualization using Matplotlib and Seaborn
# Histogram of a suscribers classified by categories
plt.figure(figsize=(8, 6))
sns.histplot(df['Suscribers'], bins=30, kde=True, color='blue')
plt.title('Histogram of suscribers')
plt.xlabel('Category')
plt.ylabel('Suscribers')
plt.show()

# Box plot to visualize the distribution of a numerical column
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Links'], y=df['Suscribers'])
plt.title('Box Plot of suscribers Grouped by links')
plt.xlabel('Links')
plt.ylabel('# of suscribers')
plt.show()

# Scatter plot to visualize the relationship between two numerical columns
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Comments'], y=df['Likes'], hue=df['Country'], palette='viridis')
plt.title('Scatter Plot of comments vs likes')
plt.xlabel('Comments')
plt.ylabel('Likes ')
plt.legend(title='Country')
plt.show()

# Calculate average values
average_subscribers = df['Suscribers'].mean()
average_visits = df['Visits'].mean()
average_likes = df['Likes'].mean()
average_comments = df['Comments'].mean()

# Visualize average values on a bar chart
metrics = ['Subscribers', 'Visits', 'Likes', 'Comments']
average_values = [average_subscribers, average_visits, average_likes, average_comments]

plt.figure(figsize=(10, 6))
plt.bar(metrics, average_values, color='skyblue')
plt.title('Average Metrics')
plt.xlabel('Metrics')
plt.ylabel('Average Values')
plt.show()