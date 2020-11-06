 # -*- coding: utf-8 -*-

import requests, json
import uuid

base = 'http://127.0.0.1:8080/'

store_url = base + 'store_text'
retrieve_url = base + 'retrieve'
retrieve_summ_url = base + 'retrieve_summ'


def store_text(text):
	""" Store a large english text (stored as a local file in server)
	Args:
		text: the english text 
	Returns:
		document_id: the ID for the saved text
	"""
	data = {'text':text}
	response = requests.post(store_url,data=data)
	document_id = response.text
	return document_id


def retrieve_text(document_id):
	""" Retrieve a large english text with the given document_id
	Args:
		document_id: the document_id of the english text 
	Returns:
		text: the full text
	"""
	data = {'document_id':document_id}
	response = requests.post(retrieve_url,data=data)
	text = response.text
	return text

def retrieve_summ(document_id):
	""" Retrieve the summarization of a large english text
	Args:
		text: the ID of the English text
	Returns:
		summ_text: the summarization text for the full text 
	"""
	data = {'document_id':document_id}
	response = requests.post(retrieve_summ_url,data=data)
	text = response.text
	return text


if __name__ == '__main__':
	
	text = 'large english text test.'

	# 3 tese cases
	print('===[Test of Store]===\n', store_text(text))
	print('===[Test of Retrieve]===\n', retrieve_text('568e4f61-3e39-46e2-9185-3febb18bf644'))
	print('===[Test of Summarization]===\n', retrieve_summ('568e4f61-3e39-46e2-9185-3febb18bf644'))

