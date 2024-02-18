# Nlp final project

Eminem song generator

This project will compare different models, all trained on a legendary hip hop artist Eminem.
we will try to train those models on a Eminem lyrics dataset, than make each model generate a song 
for us, what input will he gets? we still debate if to give him a "prompt" for the song, or to just generate songs from
scrath without prompts.

we will want to judge the quality, in three ways:
1.preplexity 
2. manual "human" check - logic,rhymes,references,creativeness
3. send the results to chatGpt and ask him

We do want to get a response already formatted in a song, so there will be some challenges there.

Actual steps:
1. Get the Eminem dataset (probally hugginface)
   1. we have to decide what type of lyrical dateset we choose, we saw 2 options, dataset including <verse> and <chorus> , and ones who are already stripped and are lyrics only.
   2. it will change the preproccessing part depend on choice.
2. Preprocess the dataset - we should be carefull, lyrics may contain slang, dialectical expressions, or intentionally misspelled words to convey rhythm,    rhyme, or emphasis.
   1. do we lemmetize? probally not.
   2. depend on the dataset choosen, which <TAGS> we save, which are helpfull for us, for example, even new line tag, can be possible advatagous to know rhyming wise and struct song wise. of course the <verse X> and <chourus> or <intro> can also be usefull. <Newline>. <interlude>.<outro>.
   3. some databases use (lyrics) - which means background singing, do we want this
   4. D-R-E || N.W.A - what we do with references like this? or letters spelling in the song? do we want the network to learn those?
   5. of course, more challenges will occur to solve.
3. Tokenization 
   1. this will be changed/affected depend on the preproccing part.
   2. we will try to use subword-level tokenization, for example BPE.
       1. several options will be performe depend on time taken from google collab, althourgh the dataset is small. bpe | wordpiece 
   
4. Embeddings
    1. we want to try different embeddings
       1. GPT API
       2. ElMo 
       3. Flair
    2. we will compare them as each one will be an input to a bilstm.
 5. Models and training
    1. 3 bi-lstms for each embedding
    2. gpt-2 fine tuned
    3. T5 fine tuned 
5. Evaluation 
   1. preplexity calculations for each
   2. manual human checks by categories and some kind of grading
   3. send results via chatGpt API (or manually) and ask him about the results or if he idenfiy the results as an eminem hiphop song.
6. Analysis and documention
   1. what each models did better, what wasnt good.
   2. conclusion and best results
   


