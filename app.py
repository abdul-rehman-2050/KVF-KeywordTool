from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Function to filter keywords with at least n words and exclude negative words
def filter_keywords(csv_file, min_words, negative_words):
    df = pd.read_csv(csv_file)
    total_keywords = len(df)
    
    # Split negative words into a list
    negative_words_list = negative_words.split(',')
    negative_words_set = set(map(str.strip, negative_words_list))  # Convert to set for efficient exclusion
    
    # Filter keywords based on minimum words and exclude negative words
    filtered_keywords = df[
        df['Keyword'].apply(lambda x: len(x.split()) >= min_words and all(word not in x for word in negative_words_set))
    ]['Keyword']
    
    long_tail_keywords = filtered_keywords.tolist()
    total_long_tail_keywords = len(long_tail_keywords)
    return long_tail_keywords, total_keywords, total_long_tail_keywords

@app.route('/', methods=['GET', 'POST'])
def index():
    total_keywords = 0
    total_long_tail_keywords = 0
    long_tail_keywords = []
    min_words = 1  # Default minimum number of words
    negative_words = ""  # Default empty negative words
    
    if request.method == 'POST':
        file = request.files['file']
        min_words = int(request.form['minWords'])
        negative_words = request.form['negativeWords'].strip()  # Get negative words and remove leading/trailing spaces
        if file:
            long_tail_keywords, total_keywords, total_long_tail_keywords = filter_keywords(file, min_words, negative_words)

    return render_template('index.html', keywords=long_tail_keywords, total_keywords=total_keywords, total_long_tail_keywords=total_long_tail_keywords)

if __name__ == '__main__':
    app.run(debug=True)
