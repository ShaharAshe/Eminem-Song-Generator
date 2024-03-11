# Nlp final project

1. Yaniv Gabay - 205745615 - yanivga@edu.hac.ac.il
2. Shahar Asher - 209305408 - shaharas@edu.hac.ac.il
3. Hadar Liel Harush - 211721568 - hadarhar@edu.hac.ac.il

Eminem song generator

This project will compare different models, all trained on the legendary hip-hop artist Eminem lyrics. We will train these models on an Eminem lyrics dataset. Then, we'll have each model generate a song for us. We're still debating whether to give each model a "prompt" for the song or to have them generate songs from scratch.


we will want to judge the quality, in three ways:
1.preplexity 
2. manual "human" check - logic,rhymes,references,creativeness
3. send the results to chatGpt and ask him

We do want to get a response already formatted in a song, so there will be some challenges there.
For example:
`<verse>`
lyrics
`<chorus>`
lyrics
`<verse>`
lyrics

## Actual steps:







1. **Obtain the Eminem dataset (probably from Hugging Face).**
   - We need to decide on the type of lyrical dataset to use. We've identified two options: one including <verse> and <chorus>, and another with lyrics already stripped and containing only the lyrical content.
   - This choice will affect the preprocessing stage.

2. **Preprocess the Dataset**
   - Careful consideration is needed as lyrics may contain slang, dialectical expressions, or intentionally misspelled words to convey rhythm, rhyme, or emphasis.
   - Lemmatization is likely not suitable due to the creative use of language in lyrics.
   - The choice of dataset will determine which tags to retain. Tags like `<verse>`, `<chorus>`, `<newline>`, `<intro>`, `<interlude>`, and `<outro>` can be crucial for understanding song structure and rhyme schemes.
   - Some databases mark background vocals with `(lyrics)`. Deciding whether to include these will depend on the desired complexity of the generated songs.
   - References such as "D-R-E" or "N.W.A" or instances where letters are spelled out in songs should be carefully considered. The decision to teach the network these references depends on the goal of maintaining authentic stylistic elements.
   - Additional challenges are expected to arise during preprocessing and will need to be addressed accordingly.
   - we want to check phonetic libraries and maybe embeed that aswell
3. **Tokenization:**
   - Tokenization will be changed/affected depending on the preprocessing part.
   - Implement subword-level tokenization, considering Byte Pair Encoding (BPE) or WordPiece.

   
4. **Embeddings**
   - Experiment with GPT API, ELMo, and Flair embeddings.
   - Each embedding will be used with a separate Bi-LSTM model for comparison.
5. **Model Training**
   - Train three Bi-LSTM models, one for each type of embedding.
   - Fine-tune GPT-2 and T5 models on the Eminem lyrics dataset.
6. **Evaluation:**
   - Perform perplexity calculations for each model.
   - Conduct manual human checks by categories and implement some form of grading system.
   - Send the results via the ChatGPT API (or manually) and inquire about whether the results are identified as an Eminem hip-hop song.

7. **Analysis and Documentation:**

   - Evaluate the performance of each model
   - Comparison of Model Performances
   - Conclusion and Best Result
    
   


