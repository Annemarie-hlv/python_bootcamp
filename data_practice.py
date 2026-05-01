import pandas as pd

#Create a dataframe manually using a dictionary
data = {
    'Student': ['Annemarie', 'Kostas', 'Margarita', 'Yixin'],
    'Score': [85, 90, 78, 92],
    'Status': ['Completed', 'In Progress', 'Completed', 'Completed']
}

#Turn the dictionary into a DataFrame
df = pd.DataFrame(data)

#look at the Dataframe
print("Full table:")
print(df)

print("\nJust the Score column:")
print(df['Score'])

print(f"\nAverage Score: {df['Score'].mean()}")
