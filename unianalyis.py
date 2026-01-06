import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1400)
pd.set_option('display.colheader_justify', 'left')

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

print(df.head(10))

# Extract numeric part of the '2025 Rank' for sorting
df['Rank_numeric'] = (
    df['2025 Rank']
    .astype(str)
    .str.extract(r'^(\d+)')   # take the first number only
    .astype(float)
)
# Sort by the numeric rank and get top 10 universities in france
france_unis = df[df['Location Full'] == "France"]
france_unis = france_unis.sort_values(by='Rank_numeric', ascending=True).head(10)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print("Top 10 universities in France in 2025:")
print(france_unis[['Institution Name', '2025 Rank', 'QS Overall Score']])

netherlands_unis = (
    df[df['Location Full'] == 'Netherlands']
    .sort_values('Rank_numeric', ascending=True)
)

print("\nTop 10 universities in the Netherlands in 2025:")
print(netherlands_unis[['Institution Name', '2025 Rank', 'QS Overall Score']].head(10))