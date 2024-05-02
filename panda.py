import pandas as pd

# df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
# print(df.head(3))
# print(df['Popularity'].describe())
# print(df.info())
# print(df['Length'].describe())
# df = df.drop(0)

# 1
def filter_movies_by_year(year):
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    filtered_movies = df[df['Year'] == year]
    return filtered_movies
print(filter_movies_by_year(1990))

# 2
def average_movie_length():
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    df['Length'] = pd.to_numeric(df['Length'], errors='coerce')
    average_length = df.groupby('Director')['Length'].mean()
    return average_length
print(average_movie_length())

# 3
def create_filtered_csv(output_file):
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    filtered_df = df[['Title', 'Director', 'Popularity']]
    filtered_df.to_csv(output_file, index=False)
create_filtered_csv('filtered_movies.csv')

# 4
def calculate_award_percentage():
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    df['Awards'] = df['Awards'].replace({'No': False, 'Yes': True})
    films_with_awards = df[df['Awards'] == True]
    award_percentage = (len(films_with_awards) / len(df)) * 100
    return award_percentage
print(calculate_award_percentage())

# 5
def movies_by_director(director_name):
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    df = df.dropna(subset=['Director'])
    movies = df[df['Director'].str.contains(director_name, case=False)]
    return movies
print(movies_by_director("Kubrick"))

# 6
def sum_popularity_of_genre(genre):
    df = pd.read_csv('movies.csv', sep=';', encoding="ISO-8859-1")
    df = df.dropna(subset=['Subject', 'Popularity'])
    comedy_movies = df[df['Subject'].str.contains(genre, case=False)]
    total_popularity = comedy_movies['Popularity'].sum()
    return total_popularity
print(sum_popularity_of_genre("comedy"))
























