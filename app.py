#importing the necessary packages
import streamlit as st
import spacy
from textblob import TextBlob

#Function definition to analyze the tokens and lemma from the provided text.
def text_analyzer(my_text):
	nlp =spacy.load('en')
	docx = nlp(my_text)

	tokens = [token.text for token in docx]
	allData = [('"Tokens":{}.\n"Lemma":{}'.format(token.text,token.lemma_)) for token in docx]
	return allData

#Function definition to analyze the entities from the input text
def entity_analyzer(my_text):
	nlp =spacy.load('en')
	docx = nlp(my_text)
	tokens = [token.text for token in docx]
	entities = [(entity.text,entity.label_)for entity in docx.ents]
	allData = ['"Tokens":{},\n"Entities":{}'.format(tokens,entities)]
	return allData

# def sentiment_analyzer(my_text):
# 	nlp.spacy.load('en')
# 	docx = nlp(my_text)
# 	tokens =  	

#main_function 
def main():
	st.title('NLP playground') 
	st.markdown("This is an interface powered by Python library named Streamlit to showcase few of the tasks.")
	st.markdown("*Go ahead...Start Exploring*")
	st.subheader("Natural Language Processing")
	st.markdown('If you would like to have an introduction on NLP, kindly visit the following. :')
	st.markdown('https://nullcast.io/introduction-to-natural-language-processing/')
	#Tokenization
	if st.checkbox("Show tokens and Lemma") and st.markdown("Tokenization is task of chopping down words into pieces often defined to be tokens."):
		st.subheader("Tokenize your text")
		st.subheader("Lemma ")
		message = st.text_area("Enter your text here", "Type-here", key = 0)
		if st.button("Analyze", key = 0):
			nlp_result = text_analyzer(message)
			st.json(nlp_result)
	
	#Named entity
	if st.checkbox("Show Named Entities"):
		st.subheader("Extract entities from the entered text")
		message = st.text_area("Enter your text here", "Type-here", key = 1)
		if st.button("Extract", key = 1):
			nlp_result = entity_analyzer(message)
			st.json(nlp_result) #converting the output to json format for displaying the result.

	#Sentiment analysis
	if st.checkbox("Show Sentiment analysis"):
		st.subheader("Sentiment of your text")
		message = st.text_area("Enter your text", "type-here", key = 2)
		if st.button("Analyze", key = 2):
			# nlp_result = sentiment_analyzer(message)
			# st.json(nlp_result)
			blob = TextBlob(message)
			result_sentiment = blob.sentiment
			st.success(result_sentiment)

if __name__ == '__main__':
	main()	
