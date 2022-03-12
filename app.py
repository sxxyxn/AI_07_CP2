#!/usr/bin/python
# -*- coding: utf-8 -*

# from crypt import methods
# import json
# import re
from flask import Flask, render_template, request, jsonify
# import jpype
# from nltk.util import bigrams

import search
app = Flask(__name__, static_url_path='')

# app.INTENT_STATUS = 0


# def check_intent(message):
#     bigram = bigrams(message)

#     bigram_tokens = []
#     for item in bigram:
#         bigram_tokens.append(''.join(item))

#     if( "검색" in bigram_tokens):
#         app.INTENT_STATUS = 1


@app.route('/', methods=['GET', 'POST'])
def index():
    # jpype.attachThreadToJVM()
    return render_template('index.html')


@app.route('/chatting', methods=['GET', 'POST'])
def chatting():
    # jpype.attachThreadToJVM()
    message = request.json['message']

    # check_intent(message)

    # if(app.INTENT_STATUS == 1):
        # message = "검색어를 말해주세요."
        # app.INTENT_STATUS = 2

    # elif(app.INTENT_STATUS is 2):
    messages = search.search_engine(message)
    # message = " ".join(messages)
        # app.INTENT_STATUS = 0

    return jsonify({'message': messages})

@app.route('/mic', methods=['GET', 'POST'])
def mic():
    msg = request.json['message']
    msgs = search.search_engine(msg)
    return jsonify({'message': msgs})

if __name__ == '__main__':
    app.run(debug=True)