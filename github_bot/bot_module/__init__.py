# -*- coding: utf-8 -*-
from github import Github
import re


class Bot (object):
    """
    Bot class that interacts with GitHub

    :param api_token API Token from Github
    :return GitHub Bot instance
    """

    is_configured = False
    bot_re = r'@bot\s*(\S+)'

    def __init__(self, api_token):
        self.g = Github(api_token)
        self.is_configured = True

    def parse_issue_comment_webhook(self, payload):
        """
        Parses Github comment webhook

        :param payload: Webhook payload
        """
        print('Parsing issue_comment webhook')
        matches = re.search(self.bot_re, str(payload['comment']['body']))
        if matches:
            command = matches.group(1)
            print('Command received: ', command)
            command_dict = {
                'say-hello': self.say_hello,
                'say-goodbye': self.say_goodbye
            }

            try:
                return command_dict[command](payload)
            except KeyError:
                print('Unknown command')
                return False
        else:
            print('No action from bot needed')
            return 'No action from bot needed'

    def say_hello(self, payload):
        """
        Action that sends a comment from bot to the original issue (PR)

        :return Whether or not action was successfully completed
        :rtype: bool
        """
        r = self.g.get_repo(payload['repository']['id'])
        try:
            pr = r.get_pull(payload['issue']['number'])
            pr.create_issue_comment('Hello world')
            #  Do here some interesting stuff with code, or any automation process
            # ...
            return True
        except:
            print('No PR found with the given number')
            return False

    def say_goodbye(self, payload):
        """
        Action that sends a comment from bot to the original issue (PR)

        :return Whether or not action was successfully completed
        :rtype: bool
        """
        r = self.g.get_repo(payload['repository']['id'])
        try:
            pr = r.get_pull(payload['issue']['number'])
            pr.create_issue_comment('Goodbye')
            #  Do here some interesting stuff with code, or any automation process
            # ...
            return True
        except:
            print('No PR found with the given number')
            return False
