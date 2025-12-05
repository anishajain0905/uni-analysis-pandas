import pandas as pd

'''#loading the csv 2024 from world university rankings
df = pd.read_csv('2024_rankings.csv')
print("Columns in the dataset:", df.columns)


df= df[['name','rank', 'scores_overall','stats_student_staff_ratio','location']]
df = df.dropna(subset=['scores_overall'])

 #sample print to check its loading correctly
print(df.head(10))'''


#loading csv from 2025 qs world rankings
df= pd.read_csv('qs-world-rankings-2025.csv')

print("columns:", df.columns)
df= df[['Institution Name','2025 Rank', '2024 Rank','Location Full', 'Academic Reputation', 'International Students', 'Employment Outcomes', 'QS Overall Score']]

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print(df.head(10))

france_unis = df[df['Location Full'] == "France"]
france_unis = france_unis.sort_values(by='2025 Rank')
print(france_unis[['Institution Name', '2025 Rank', 'QS Overall Score']])
