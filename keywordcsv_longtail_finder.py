import pandas as pd

# Function to filter keywords with at least 4 words using pandas
def filter_keywords(input_file, output_file):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(input_file, sep='\t')

    # Filter keywords with at least 4 words
    filtered_keywords = df[df['Keyword'].apply(lambda x: len(x.split()) >= 4)]['Keyword']

    # Write filtered keywords to a new CSV file
    filtered_keywords.to_csv(output_file, index=False, header=['Filtered Keywords'])

    # Display the first few rows of the filtered keywords
    print("Filtered Keywords (head):")
    print(filtered_keywords.head())

# Example usage
input_csv_file = 'esp8266_shitter.csv'  # Replace with your input CSV file name
output_csv_file = 'filtered_keywords.csv'  # Replace with your output CSV file name

# Read CSV file into a pandas DataFrame with custom delimiter and quoting character
df = pd.read_csv('esp8266_shitter.csv', sep=',', quotechar='"')

