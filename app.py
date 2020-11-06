# -*- coding: utf-8 -*-

from flask import Flask, request
import requests
import uuid
import summary as summ_util

app = Flask(__name__)

def save_to_local(text):
	""" Save a large english text in local place and return a ID
	Args:
		text: the full english text 
	Returns:
		ID: the ID for the saved text (generated with UUID)
	"""
	UU = uuid.uuid4()
	document_id = str(UU)
	with open('files/'+document_id, 'w', encoding='utf8') as fw:
		fw.write(text)
	return document_id

def load_text(document_id):
	""" A private function to retrieve the English text in local place
	Args:
		document_id: the ID for the english text 
	Returns:
		text: the full text
	"""
	with open('files/'+document_id,'r',encoding='utf8') as fr:
		text = fr.read()
	return text

@app.route('/store_text', methods=['POST'])
def store():
	""" Upload text to server
	Args: text
	Retrun: document_id
	"""
	if request.method=='POST':
		text = request.form['text']
		document_id = save_to_local(text)
		return document_id


@app.route('/retrieve', methods=['POST'])
def retrieve():
	""" Retrieve the text file
	Args: document_id
	Retrun: text
	""" 
	if request.method=='POST':
		document_id = request.form['document_id']
		text = load_text(document_id)
		return text

@app.route('/retrieve_summ',methods=['POST'])
def retrieve_summ():
	""" Get summary of text file by a document_id
	Args: document_id
	Returns: the summary of text
	"""
	if request.method=='POST':
		document_id = request.form['document_id']
		text = load_text(document_id)
		return summ_util.get_summ_from_gensim(text)
		# return summ_util.get_summ_manually_spacy(text)

if __name__ == '__main__':
	app.run(debug=True,port=8080)

