# recap-nlp

Building a NLP engine to quiz you on material from a textbook pdf

## Main Tasks

1. Given a chunk(s) of text, generate a question and answer pair based on important concepts
	- **Current Approach**
   		 - Supervised learning might be a good method here, because "important" is a fuzzy word and it would make better sense to use lets say pdf textbooks and the end of the chapter questions and their answers as train, test, validate data
    	    - Use summarization techniques from nlp to filter down inputs https://www.machinelearningplus.com/nlp/text-summarization-approaches-nlp-example/
			- Given this approach, we think the bigger task would be to extract questions and answers from a textbook using NLP to generate our dataset. 
2. Generate similar, but not obvious false answers (or, would make it short answer and some how check validity to correct answer)
	- **Current Approach**
		- Again, data can be extracted from textbooks if they have multiple choice in the textbook questions and answers

### Model
- Outline:
   - **Input:** chapter's worth of text
   - **Output:** List of question and answer pairs

- Potential options:
   - BERT seemed interesting as it has a semi-supervised approach and is very popular
   - Make a custom transformer model
   - Use OpenAI GPT-3 somehow

## Feedback

If you've came across this repo and think that our approach/implementation is doomed to fail, we'd greatly appreciate if you can open up an issue and tell us what we're doing wrong.
