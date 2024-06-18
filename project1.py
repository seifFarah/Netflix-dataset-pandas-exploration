import pandas as pd
import matplotlib.pyplot as plt

# THIS PROJECT IS AN INITIAL EXPLORATION OF THE FEATURES OF PANDA INCLUDING AN INVESTIGATION OF A POTENTIAL RELATIONSHIP BETWEEN NUMBER OF VOTES ON IMDB AND AVERAGE RATING.
# Load the dataset
movies = pd.read_csv(r"C:\Users\seiff\Desktop\Python in data\First project\Netflix TV Shows and Movies.csv")

# Remove duplicates
no_dupes = movies.drop_duplicates()

# Inspect the first few rows of the dataset to identify relevant columns
print(no_dupes.head())

# Check for missing values in the relevant columns
print(no_dupes[['imdb_votes', 'imdb_score']].isnull().sum())

# Drop rows with missing values in the relevant columns
clean_data = no_dupes.dropna(subset=['imdb_votes', 'imdb_score'])

# Calculate the correlation coefficient
correlation = clean_data['imdb_votes'].corr(clean_data['imdb_score'])

# There is no relationship between the number of votes and the rating score of IMDB
print("Correlation between number of votes and average score:", correlation)

# Let's see how it looks like as a scatter plot.
plt.figure(figsize=(10, 6))
plt.scatter(clean_data['imdb_score'], clean_data['imdb_votes'], alpha=0.5)
plt.title('Scatter Plot of Number of Votes vs. Average Score')
plt.ylabel('Number of Votes')
plt.xlabel('Average Score')
plt.grid(True)
plt.show()

# There is no relationship between the number of ratings and the avearage rating.