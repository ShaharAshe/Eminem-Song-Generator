
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
    # Replace . with a space
    output_string = re.sub(r'[.]', ' ', output_string)
    # Replace [ and ] with a space
    output_string = re.sub(r'[\[\]]', ' ', output_string)
    # Remove ( ) and replace \n with a space
    output_string = re.sub(r"[\(\)]", '', output_string)
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
def expand_contractions(tokens, contractions_dict):
    expanded_tokens = []
    for token in tokens:
        # Check if the token is a contraction and expand it if necessary
        expanded_token = contractions_dict.get(token.lower(), token)
        expanded_tokens.extend(expanded_token.split())  # Split expanded form into individual tokens
    return expanded_tokens