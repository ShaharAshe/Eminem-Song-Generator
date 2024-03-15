
import pandas as pd
import re



def export_data_to_csv(data, stage, debug_mode=False):
    """
    Exports DataFrame to a CSV file. Used for debugging purposes.

    Parameters:
    - data (DataFrame): The pandas DataFrame to export.
    - stage (str): Descriptive name for the export stage to include in the file name.
    - debug_mode (bool, optional): Flag to control the export functionality. Default is False.

    Returns:
    - None
    """
    if not debug_mode:
        return
    try:
        data.to_csv(f'data_{stage}.csv')
    except Exception as e:
        print(f"Error exporting the csv file for {stage}: {e}")

def import_data_from_location(location):
    """
    Imports data from the given location, trying multiple encodings.

    Parameters:
    - location (str): The file path or URL to import data from.

    Returns:
    - DataFrame: The imported data as a pandas DataFrame.
    """
    try_encodings = ['utf-8', 'latin1', 'utf-16', 'cp1252', 'ISO-8859-1', 'windows-1252']
    for encoding in try_encodings:
        try:
            df = pd.read_csv(location, encoding=encoding, delimiter='\t')
            print(f"Success with encoding: {encoding}")
            return df
        except Exception as e:
            print(f"Error with encoding {encoding}: {e}")

def remove_non_ascii_characters(text):
    """
    Removes non-ASCII characters from the text and prints them.

    Parameters:
    - text (str): The text to clean.

    Returns:
    - str: The cleaned text with only ASCII characters.
    """
    cleaned_text = "".join(char for char in text if ord(char) < 128)
    removed_chars = set(text) - set(cleaned_text)
    if removed_chars:
        print(f"Removed non-ASCII characters: {''.join(removed_chars)}")
    return cleaned_text

def remove_tags(lyrics):
    """
    Removes text within square brackets, often used to remove metadata or annotations within lyrics.

    Parameters:
    - lyrics (str): The lyrics text to clean.

    Returns:
    - str: The cleaned lyrics without square bracket tags.
    """
    pattern = re.compile(r'\[[^\]]*\]')
    return re.sub(pattern, '', lyrics)

import re

def handle_special_characters(lyrics):
    """
    Cleans the lyrics by handling various special characters. Specific characters are
    removed or replaced with spaces or appropriate substitutes to simplify the text and
    potentially improve the model's learning efficiency.

    Parameters:
    - lyrics (str): The lyrics text to be cleaned.

    Returns:
    - str: The cleaned lyrics with special characters handled.
    """

    #print("Original Lyrics:", lyrics)
    replacements = {
        r"[\(\)]": '',  # Remove parentheses
        r"[']": '',  # Remove apostrophes
        r"[\-?!]": ' ',  # Replace hyphens, question marks, and exclamation marks with spaces
        r"[\{\}]": ' ',  # Replace curly braces with spaces
        r"[*]": ' ',  # Replace asterisks with spaces
        r"[\"]": ' ',  # Replace double quotes with spaces
        r"[:;]": ' ',  # Replace colons and semicolons with spaces
        r"[_]": ' ',  # Replace underscores with spaces
        r"[&]": ' and ',  # Replace '&' with 'and'
        r"[\n]": ' ',  # Replace newlines with spaces
    
      
    }
    for pattern, replacement in replacements.items():
        lyrics = re.sub(pattern, replacement, lyrics)

    # Remove extra spaces that might have been introduced by the replacements
    lyrics = re.sub(r'\s+', ' ', lyrics)
    #print("Processed Lyrics:", lyrics) 
    return lyrics.strip()





contractions_dict = {
    "im": "i am",
    "youre": "you are",
    "hes": "he is",
    "shes": "she is",
    "its": "it is",
    "were": "we are",
    "theyre": "they are",
    "ive": "i have",
    "youve": "you have",
    "weve": "we have",
    "theyve": "they have",
    "isnt": "is not",
    "arent": "are not",
    "wasnt": "was not",
    "werent": "were not",
    "havent": "have not",
    "hasnt": "has not",
    "hadnt": "had not",
    "wont": "will not",
    "wouldnt": "would not",
    "dont": "do not",
    "doesnt": "does not",
    "didnt": "did not",
    "cant": "cannot",
    "couldnt": "could not",
    "shouldnt": "should not",
    # Add more contractions and their expansions as needed
}

test_string = "This is a testwith the character."
cleaned_string = remove_non_ascii_characters(test_string)
print("Cleaned String:", cleaned_string)

def expand_contractions(text, contractions_dict=contractions_dict):
    """
    Expands contractions in the given text based on a contractions dictionary.

    Parameters:
    - text (str): The text with contractions to expand.
    - contractions_dict (dict, optional): A dictionary mapping contractions to their expanded forms. Default is the predefined contractions_dict.

    Returns:
    - str: The text with contractions expanded.
    """
    # Function to expand a single contraction
    def expand_match(contraction):
        match = contraction.group(0)
        first_word, rest = re.match(r"(\w+)(.*)", match, re.IGNORECASE).groups()
        expanded_contraction = contractions_dict.get(first_word.lower(), first_word + rest)
        return expanded_contraction

    # Compile a regular expression pattern with all contractions
    contractions_pattern = re.compile(r'\b({})\b'.format('|'.join(contractions_dict.keys())), flags=re.IGNORECASE)
    
    # Expand contractions in the text
    expanded_text = contractions_pattern.sub(expand_match, text)
    return expanded_text




# ####Tests######
'''
test_cases = [
    "Hello, world!",  # Test punctuation removal
    "Rock & Roll",  # Test ampersand replacement
    "High-____quality",  # Test hyphen removal
    "It's a test",  # Test apostrophe removal
    "(This is in parentheses)",  # Test parentheses removal
    "Multi\nLine\nText",  # Test newline replacement
    "{Curly} [Brackets] *Asterisk*",  # Test various symbols removal
]

# Run tests and display results
test_results = [(test, handle_special(test)) for test in test_cases]
print(test_results)
'''