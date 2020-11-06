
# Overview
This is a small server and client demo. Server is written in app.py and Client is written in client.py. In addition to that, summary.py is used to get summarization of a text.

# Lib Requirements
pip install flask
pip install spacy
pip install requests
pip install gensim


# How to Run
1. Run the app.py, so that the server will be running
2. Run the client.py, note there are three test cases in main function, including store, retrieve, and retrieve summary


# three use cases
Store: stores a string text into a file on server, and returns a automatically generated ID
Retrieve: retrieves the text based on a given ID
Retrieve summarization: retrieves the text and invoke a summarization function that returns the summarized text

