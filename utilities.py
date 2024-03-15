
import pandas as pd
import re
def export_data(data,stage,debug_mode):
    if(not debug_mode):
        return
    try:
        data.to_csv('data_'+stage+'.csv')
    except Exception as e:
        print("Error exporting the csv file:", e)
#basic import
def import_data(location):
    df = read_data(location)
    return df

def read_data(location):
    try_encodings = ['utf-8', 'latin1', 'utf-16', 'cp1252', 'ISO-8859-1', 'windows-1252']
    for encoding in try_encodings:
        try:
            df = pd.read_csv(location ,encoding=encoding,delimiter='\t')
            print(f"Success with encoding: {encoding}")
            print(df.head())
            return df
            break
        except Exception as e:
            print(f"Error with encoding {encoding}: {e}")

def remove_non_ascii_and_print(text):
    cleaned_text = []
    removed_chars = []
    for char in text:
        if ord(char) < 128:
            cleaned_text.append(char)
        else:
            removed_chars.append(char)
    if removed_chars:
        print(f"Removed characters: {''.join(removed_chars)}")
    return ''.join(cleaned_text)

def remove_remaining_tags(lyrics):
    # Pattern to match any text within square brackets
    pattern = re.compile(r'\[[^\]]*\]')
    cleaned_lyrics = re.sub(pattern, '', lyrics)
    return cleaned_lyrics

def handle_special(lyrics):
    # Replace ' and - and ? and ! with a space
    output_string = re.sub(r"['\-?!]", ' ', lyrics)
    #replace { and } with a space
    output_string = re.sub(r'[\{\}]', ' ', output_string)
    # Replace * with a space
    output_string = re.sub(r'[*]', ' ', output_string)
    # Replace " with a space
    output_string = re.sub(r'["]', ' ', output_string)
    # Replace : and ; with a space
    output_string = re.sub(r'[:;]', ' ', output_string)
    # Replace _ with a space
    output_string = re.sub(r'[_]', ' ', output_string)

    # Replace & with a space
    output_string = re.sub(r'[&]', ' and ', output_string)
    # Replace . with a space
    output_string = re.sub(r'[.]', ' ', output_string)
    # Replace [ and ] with a space
    output_string = re.sub(r'[\[\]]', ' ', output_string)
    # Remove ( ) and replace \n with a space
    output_string = re.sub(r"[\(\)]", ' ', output_string)
    output_string = re.sub(r"\n", ' ', output_string)
    # Additional step to remove extra spaces created by the substitutions
    output_string = re.sub(r'\s+', ' ', output_string).strip()
    return output_string

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
import re

def expand_contractions(text, contractions_dict):
    def expand_match(contraction):
        match = contraction.group(0)
        first_word, rest = re.match(r"(\w+)(.*)", match, re.IGNORECASE).groups()
        expanded_contraction = contractions_dict.get(first_word.lower(), first_word.lower()) + rest
        return expanded_contraction

    contractions_pattern = re.compile(r'\b({})\b'.format('|'.join(contractions_dict.keys())), flags=re.IGNORECASE)
    expanded_text = contractions_pattern.sub(expand_match, text)
    return expanded_text
import re

def handle_special(lyrics):
    # Create a dictionary of replacement rules
    replacements = {
        r"[']": '' ,
        r"[\-_?!]": ' ',  # Replace apostrophes, hyphens, question and exclamation marks with a space
        r'["*:;_\{\}\[\]()]': ' ',  # Replace other punctuations with a space
        r'[&]': ' and ',  # Replace ampersand with 'and'
        r'[.]': ' ',  # Replace period with a space
        r'\n': ' ',  # Replace newlines with a space
    }

    # Apply all replacements
    for pattern, replacement in replacements.items():
        lyrics = re.sub(pattern, replacement, lyrics)

    # Remove extra spaces
    lyrics = re.sub(r'\s+', ' ', lyrics).strip()

    return lyrics

# Tests
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
