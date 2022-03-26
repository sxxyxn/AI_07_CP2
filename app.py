#!/usr/bin/python
# -*- coding: utf-8 -*

from flask import Flask, render_template, request, jsonify
import chatbot
app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/chatting', methods=['GET', 'POST'])
def chatting():
    message = request.json['message']
    messages = chatbot.chatbot_response(message)
    return jsonify({'message': messages})

@app.route('/mic', methods=['GET', 'POST'])
def mic():
    msg = request.json['message']
    msgs = chatbot.chatbot_response(msg)
    return jsonify({'message': msgs})

if __name__ == '__main__':
    app.run()
