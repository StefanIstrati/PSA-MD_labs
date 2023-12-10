import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict

def separate_text_into_words(text):
    if text:
        words = text.split()
        return words
    else:
        return []

def extract_hashtags(words):
    hashtags = [word for word in words if word.startswith('#')]
    return hashtags

def extract_nouns(text):
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stopwords.words('english')]
    tagged_words = pos_tag(words)
    nouns = [word for word, pos in tagged_words if pos.startswith('N')]
    return nouns

afinn_file_path = 'AFINN-111.txt'
afinn_dict = {}
with open(afinn_file_path, 'r') as afinn_file:
    for line in afinn_file:
        word, score = line.strip().split('\t')
        afinn_dict[word] = int(score)

def calculate_emotional_value(text):
    words = word_tokenize(text.lower())  
    words = [word for word in words if word.isalnum()] 
    words = [word for word in words if word not in stopwords.words('english')] 
    emotional_value = sum(afinn_dict.get(word, 0) for word in words)
    return emotional_value

def print_most_positive_negative_tweets(tweets_data, emotional_values):
    sorted_tweets = sorted(tweets_data, key=lambda tweet: emotional_values.get(tweet['id'], 0), reverse=True)

    print("\nMD 4.3 - Top 10 Most Positive Tweets:")
    for tweet in sorted_tweets[:10]:
        print(f"{tweet['id']}: {emotional_values[tweet['id']]} - {tweet['text']}")

    print("\nMD 4.3 - Top 10 Most Negative Tweets:")
    for tweet in sorted_tweets[-10:]:
        print(f"{tweet['id']}: {emotional_values[tweet['id']]} - {tweet['text']}")

def print_top_nouns(tweets_data):
    nouns_list = []

    for tweet in tweets_data:
        words_in_text = extract_nouns(tweet.get('text', ''))
        nouns_list.extend(words_in_text)

    nouns_counter = Counter(nouns_list)
    top_nouns = nouns_counter.most_common(10)

    print("\nPSA 4.2 - Top 10 Most Frequently Used Nouns:")
    for noun, count in top_nouns:
        print(f"{noun}: {count} occurrences")

def extract_capital_words(text):
    words = word_tokenize(text)
    capital_words = [word for word in words if word.isalpha() and word[0].isupper() and word not in stopwords.words('english')]
    return capital_words

def print_top_proper_nouns(tweets_data):
    capital_words_list = []

    for tweet in tweets_data:
        words_in_text = extract_capital_words(tweet.get('text', ''))
        capital_words_list.extend(words_in_text)

    capital_words_counter = Counter(capital_words_list)
    top_capital_words = capital_words_counter.most_common(10)

    print("\nPSA 4.3 - Top 10 Most Frequently Used Capitalized Words:")
    for word, count in top_capital_words:
        print(f"{word}: {count} occurrences")

def extract_date(tweets_data):
    monthly_counts = []
    for tweet in tweets_data:
        monthly_counts.append(tweet['created_at'][:7])

    return monthly_counts

def count_monthly_occurence(date, word, tweets_data):
    year, month = date.split("-")
    word_count_by_year_month = defaultdict(int)

    for tweet in tweets_data:
        tweet_year, tweet_month = tweet['created_at'][:7].split("-")

        if tweet_year == year and tweet_month == month:
            words_in_text = separate_text_into_words(tweet.get('text', ''))
            word_count_by_year_month[year, month] += words_in_text.count(word)

    return word_count_by_year_month


try:
    with open('tweets.json', 'rb') as fp:
        tweets_data = json.load(fp)
except FileNotFoundError:
    print("Error: File 'tweets.json' not found.")
    tweets_data = []
except json.JSONDecodeError:
    print("Error: Invalid JSON format in the file.")
    tweets_data = []

hashtags_list = []
word_list = []
emotional_values = Counter() 

for tweet in tweets_data:
    tweet_node = {
        'id': tweet.get('id', None),
        'text': tweet.get('text', None),
        'created_at': tweet.get('created_at', None),
        'likes': tweet.get('likes', None),
        'retweets': tweet.get('retweets', None)
    }

    words_in_text = separate_text_into_words(tweet_node['text'])
    word_list.extend(words_in_text)
    hashtags = extract_hashtags(words_in_text)
    if hashtags:
        hashtags_list.extend(hashtags)

    emotional_value = calculate_emotional_value(tweet_node['text'])
    emotional_values[tweet_node['id']] = emotional_value

hashtags_counter = Counter(hashtags_list)
word_counter = Counter(word_list)

top_10_hashtags = hashtags_counter.most_common(10)
top_10_words = word_counter.most_common(10)

print("MD 4.1 - Top 10 Hashtags:")
for hashtag, count in top_10_hashtags:
    print(f"{hashtag}: {count} occurrences")

print("\nPSA 4.1 - Top 10 Words:")
for word, count in top_10_words:
    print(f"{word}: {count} occurrences")

print_most_positive_negative_tweets(tweets_data, emotional_values)
print_top_nouns(tweets_data)
print_top_proper_nouns(tweets_data)

target_word = input("Enter the target word: ")

date = extract_date(tweets_data)
word_counts = 0
x_labels = []
y_values = []

for d in date:
    x = word_counts
    word_counts = count_monthly_occurence(d, target_word, tweets_data)
    if word_counts != x:
        for year_month, count in word_counts.items():
            x_labels.append(f"{year_month[0]}-{year_month[1]}")
            y_values.append(count)

plt.figure(figsize=(10, 6))
plt.bar(range(len(x_labels)), y_values, color='blue')
plt.xlabel('Time Period')
plt.ylabel(f'Occurrences of "{target_word}"')
plt.title(f'Occurrences of "{target_word}" Over Time')
plt.xticks(range(len(x_labels)), x_labels, rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()

