import json
from collections import defaultdict
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def process_text(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)

    nouns = [lemmatizer.lemmatize(word.lower()) for word, pos in pos_tags if pos.startswith('N') and word.lower() not in stop_words]

    return nouns

with open('tweets.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
noun_counts = defaultdict(lambda: {'retweets': 0, 'likes': 0})

for tweet in data:
    nouns = process_text(tweet['text'])
    for noun in set(nouns):
        noun_counts[noun]['retweets'] += tweet['retweets']
        noun_counts[noun]['likes'] += tweet['likes']

popularity = {}

for noun, counts in noun_counts.items():
    norm_retweets = counts['retweets'] / len(data)
    norm_likes = counts['likes'] / len(data)
    frequency = len(noun_counts[noun])

    rating = frequency * (1.4 + norm_retweets) * (1.2 + norm_likes)
    popularity[noun] = rating

sorted_popularity = sorted(popularity.items(), key=lambda x: x[1], reverse=True)[:10]

print("Top 10 Most Popular Nouns:")
for noun, rating in sorted_popularity:
    print(f"{noun}: {rating}")
