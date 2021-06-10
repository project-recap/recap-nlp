# recap-nlp

Building a NLP engine to quiz you on material from a textbook pdf

## Tasks 

1. Given a chunk(s) of text, generate a multiple choice and/or short answer questions based on important concepts 

2. Answer validation 
  - Multiple choice: Generate incorrect multiple choice options 
  - Short answer: Evaluate the correctness of inputted answer

## Approaches for tasks
Warning: I really know nothing about NLP, so a lot of this might not work.

### Task 1

1. Supervised learning. Many textbooks have chapter questions at the end of each chapter with answers which can be used as training data. Use BERT or variation on HuggingFace

- Pros
  - Less feature engineering, as the model can infer which parts of the chapter and details are important and which are not.
- Cons
  - For this to scale, it requires a data OCR pipeline that takes PDFs, converts to images, and scans them for the question and answer portions 

2. GPT-3?

### Task 2

#### Multiple choice
Might not be feasible. Humans are pretty good at detecting BS, and I'm not a PhD ML student, so I don't know if its feasbile for us to build a good MC option generator.

#### Short Answer
1. Create a similarity algorithm that determines if the inputted answer is correct. Could be as simple as if input contains a certain number of keywords, then it is correct.
2. NLP model that can determine if an answer is correct or not. Dunno how to do this well, needs some more thinking. User to provide +/- labels to improve the model?

## Feedback

If you've came across this repo and think that our approach/implementation is doomed to fail, we'd greatly appreciate if you can open up an issue and tell us what we're doing wrong.
