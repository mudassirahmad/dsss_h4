import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('census_income_dataset.csv')  # Replace 'your_dataset.csv' with the actual file path

# a) Age distribution of respondents
plt.figure(figsize=(8, 6))
plt.boxplot(df['AGE'], vert=False, patch_artist=True, boxprops=dict(facecolor='skyblue', color='black'), medianprops=dict(color='black'))
plt.title('Box Plot of Age Distribution')
plt.xlabel('Age')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.savefig('age_distribution.svg', format='svg', bbox_inches='tight')
plt.show()

# b) How often does each relationship status occur?
plt.figure(figsize=(12, 6))
relationship_counts = df['RELATIONSHIP'].value_counts()
plt.pie(relationship_counts, labels=relationship_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Relationship Status')
plt.savefig('relationship_distribution.svg', format='svg', bbox_inches='tight')
plt.show()


# c) Salary distribution within each educational level
plt.figure(figsize=(12, 6))
sns.countplot(x='EDUCATION', hue='SALARY', data=df, palette=['#1f77b4', '#ff7f0e'])
plt.title('Salary Distribution Within Each Educational Level')
plt.xlabel('Educational Level')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='Salary', labels=['<=50K', '>50K'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('salary_distribution.svg', format='svg', bbox_inches='tight')
plt.show()