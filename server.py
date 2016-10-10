"""Slack Slash Command TicTacToe"""

from flask import Flask, request, json

from Model import (Game)

import valid_emojis

import os

app = Flask(__name__)

app.secret_key = os.environ['APP_SECRET_KEY']

slack_token = os.environ['SLACK_TOKEN']

# ___________________________________________________________________________


@app.route('/new_game', methods=['POST'])
def new_game():
    '''Recieves a slash command to start a new game'''

    # This area is commented out because the app is not live, the test data
    # below it for development purposes should be removed before deployment.

    # I think request.data is the right form but http://flask.pocoo.org/docs/0.11/api/#flask.Request
    #  can be consulted for further forms

    token = request.data["token"]
    team_id = request.data["team_id"]
    team_domain = request.data["team_domain"]
    channel_id = request.data["channel_id"]
    channel_name = request.data["channel_name"]
    user_id = request.data["user_id"]
    user_name = request.data["user_name"]
    command = request.data["command"]
    text = request.data["text"]
    response_url = request.data["response_url"]

    # token = "gIkuvaNzQIHg97ATvDxqgjtO"
    # team_id = "T0001"
    # team_domain = "example"
    # channel_id = "C2147483705"
    # channel_name = "test"
    # user_id = "U2147483697"
    # user_name = "Steve"
    # command = "/weather"
    # text = "94070"
    # response_url = "https://hooks.slack.com/commands/1234/5678"

    if token == slack_token:
        # execute the command

        # If you'd like to add HTTP headers to a request, simply pass in a dict to the headers parameter.

        # For example, we didn't specify our user-agent in the previous example:

        # >>> url = 'https://api.github.com/some/endpoint'
        # >>> headers = {'user-agent': 'my-app/0.0.1'}

        # >>> r = requests.get(url, headers=headers)
        # Note: Custom headers are given less precedence than more specific sources of information. For instance:

         # r = requests.post('http://httpbin.org/post', data = {'key':'value'})'

         # http://flask.pocoo.org/docs/0.11/quickstart/#about-responses
         
        pass

    else:
        # error message or pass. The request did not come from Slack.
        # "Additionally, you can verify whether the team_id matches a
        # team that has approved your command for usage.
        # If the token or team are unknown to your application, you should
        # refuse to service the request and return an error instead."
        pass

# ___________________________________________________________________________


if __name__ == "__main__":

    app.debug = True

    app.run(host="0.0.0.0")