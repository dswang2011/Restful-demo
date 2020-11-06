# -*- coding: utf-8 -*-

from gensim.summarization.summarizer import summarize
import string
from heapq import nlargest
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

def get_summ_from_gensim(text):
	"""return the summary of a text by gensim lib"""
	return summarize(text)	# we can set word_count=50. or ratio = 0.3 et. as well


def get_summ_manually_spacy(text):
	""" Get summarization with manual implementation with spacy tool
	"""
	stopwords = list(STOP_WORDS)
	nlp = spacy.load('en')	# 
	punctuation = string.punctuation + '\n'

	doc = nlp(text)
	# word frequency -> we can use TF-IDF as well
	word_freq = {}
	for word in doc:
		if word.text.lower() not in stopwords and word.text.lower() not in punctuation: 
			if word.text not in word_freq.keys():
				word_freq[word.text] = 1
			else:
				word_freq[word.text] +=1 
	max_val = max(word_freq.values())
	#normalized
	for word in word_freq.keys():
		word_freq[word] = word_freq[word]/max_val
	# sent score
	sent_list = [sent for sent in doc.sents]
	sent_score = {}
	for sent in sent_list:
		for word in sent:
			if word.text.lower() in word_freq.keys():
				if sent not in sent_score.keys():
					sent_score[sent] = word_freq[word.text.lower()]
				else:
					sent_score[sent] += word_freq[word.text.lower()]
	select_length = int(len(sent_list)*0.3)	# 30 percent of sentences, or we can fix sent num
	summarized_sentences = nlargest(select_length, sent_score, key = sent_score.get)
	# combine sentences
	final_summary = [word.text for word in summarized_sentences]
	summary = ' '.join(final_summary)
	return summary



# from other better versions (RNN, Attention-based)
# ... to be discussed or developed



