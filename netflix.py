import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg') 
import seaborn as sns


df = pd.read_csv(r"C:\Users\MEGHAV MITTAL\OneDrive\Desktop\PROJECTS\NetFlix.csv")


# Display the first few rows of the DataFrame
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.shape)
# Check for missing values
print(df.isnull().sum())
print(df.describe())
df.dropna(inplace=True)
print("Shape after dropping nulls:", df.shape)  # Drop rows with missing values



# Movies vs TV Shows Analysis pie chart 
plt.figure(figsize=(8, 6))
labels = df['type'].value_counts().index
sizes = df['type'].value_counts().values
colors = ["#7f1e1e","#24384d"]
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Movies vs TV Shows on Netflix')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular
plt.show()


# Top 10 Directors with the most content on Netflix
top_directors = df['director'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_directors.values, y=top_directors.index, palette="viridis")
plt.title('Top 10 Directors with the Most Content on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.show()

# Top 10 Genres on Netflix
top_genres = df['genres'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette="magma")
plt.title('Top 10 Genres on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.show()

# Distribution of Content Ratings on Netflix
plt.figure(figsize=(10, 6))  #figure size first is for width and second is for height 
sns.countplot(data=df, x='rating', order=df['rating'].value_counts().index, palette="Set2")
plt.title('Distribution of Content Ratings on Netflix')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Distribution of Release Years on Netflix
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='release_year', bins=30, kde=True, color='red')
plt.title('Distribution of Release Years ')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()


# Correlation between Duration and Release Year
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='release_year', y='duration', hue='type', palette="coolwarm")
plt.title('Correlation between Duration and Release Year')
plt.xlabel('Release Year')
plt.ylabel('Duration (minutes)')
plt.legend(title='Type')
plt.show()



# Top 10 Countries with the Most Content on Netflix
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(8,8))
colors = ["#000000", "#1a0000", "#330000", "#660000",
          "#990000", "#b30000", "#cc0000", "#e60000",
          "#ff0000", "#ff1a1a"]
plt.bar(top_countries.index,
        top_countries.values,
        color=colors)
plt.title('Top 10 Countries with the Most Content on Netflix', fontweight='bold')
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Distribution of Content Types by Country
plt.figure(figsize=(12, 6)) 
sns.countplot(data=df, x='country', hue='type', palette="Set1", order=df['country'].value_counts().index[:10])  #  .index[:10] to show only top 10 countries
plt.title('Distribution of Content Types by Country')
plt.xlabel('Country')
plt.ylabel('Count')
plt.xticks(rotation=25)
plt.legend(title='Type')
plt.tight_layout()
plt.show()

# Distribution of Content Types by Genre
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='genres', hue='type', palette="Set3", order=df['genres'].value_counts().index[:10])  # Show only top 10 genres
plt.title('Distribution of Content Types by Genre')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=25)
plt.legend(title='Type')
plt.show()

# Distribution of Content Types by Rating
plt.figure(figsize=(12, 6)) 
sns.countplot(data=df, x='rating', hue='type', palette="Set2", order=df['rating'].value_counts().index)  # Show all ratings
plt.title('Distribution of Content Types by Rating')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=25)
plt.legend(title='Type')
plt.tight_layout()
plt.show()




# Content Added Over Years
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='release_year', y=df.index, hue='type', palette="Set1")  # Set1 is a color palette
plt.title('Content Added Over Years')
plt.xlabel('Release Year')
plt.ylabel('Cumulative Count of Titles')
plt.legend(title='Type')
plt.show()

# Ratings Analysis (TV-MA, PG, etc.)
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='rating', palette="Set2", order=df['rating'].value_counts().index)
plt.title('Distribution of Content Ratings on Netflix') 
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Duration Analysis
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='duration', bins=30, kde=True, color='blue')   # kde = true means kernel density estimation, which adds a smooth curve to the histogram to show the distribution of the data more clearly.
plt.title('Distribution of Content Duration on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Count')
plt.show()

# Correlation between Duration and Release Year
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='release_year', y='duration', hue='type', palette="coolwarm")
plt.title('Correlation between Duration and Release Year')
plt.xlabel('Release Year')
plt.ylabel('Duration (minutes)')
plt.legend(title='Type')
plt.show()

# Country-wise Growth Trend
country_year = pd.crosstab(df['date_added'], df['country'])
plt.figure(figsize=(12, 6))
country_year.plot(kind='line', marker='o')
plt.title('Country-wise Growth Trend of Netflix Content')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles Added')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()  # tight layout is used for adjusting the spacing between subplots to prevent overlap
plt.show()


# Genre-wise Growth Trend
genre_year = pd.crosstab(df['date_added'], df['genres'])
plt.figure(figsize=(12, 6))
genre_year.plot(kind='line', marker='o')
plt.title('Genre-wise Growth Trend of Netflix Content')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles Added')
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Rating-wise Growth Trend
rating_year = pd.crosstab(df['date_added'], df['rating'])
plt.figure(figsize=(12, 6))
rating_year.plot(kind='line', marker='o')
plt.title('Rating-wise Growth Trend of Netflix Content')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles Added')
plt.legend(title='Rating', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Duration vs Rating
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='rating', y="duration", palette="Set3", order=df['rating'].value_counts().index) #boxplot is used to show the distribution of duration for each rating category, and it can help identify any outliers or differences in duration across ratings.
plt.title('Duration vs Rating on Netflix')  
plt.xlabel('Rating')
plt.ylabel('Duration (minutes)')
plt.xticks(rotation=45)
plt.show()




         #Advanced Analysis Ideas 
# Movies vs TV Shows Trend Over Time
type_year  = pd.crosstab(df["date_added"], df["type"])
plt.figure(figsize =(12, 6))
plt.scatter(type_year.index, type_year["Movie"], color="#D1A269", label='Movies')
plt.scatter(type_year.index, type_year["TV Show"], color="#f0c7c7", label='TV Shows')
plt.title('Movies vs TV Shows Trend Over Time')
plt.xlabel('Year Added')
plt.ylabel('Number of Titles Added')
plt.legend()
plt.show()


from wordcloud import WordCloud #Word Cloud is used for the text inside the shape like circle , rectangle , square 
text = " ".join(df['genres'].dropna())
wordcloud = WordCloud(background_color="black").generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

