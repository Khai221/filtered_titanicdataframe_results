import panda as pd
df = pd.read_csv('titanic.csv')

# Filtering the Dataframe
filtered_df = df.loc[(df['Sex'] == 'female') & (df['Pclass'] == 1) & (df['Survived'] == 1), ['Name', 'Age', 'Sex', 'Pclass', 'Survived']].sort_values(by = 'Name')

# Importing Dataframe results
filtered_df.to_csv('filtered_titanic_results.csv', index = False)