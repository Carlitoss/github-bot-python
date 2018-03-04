#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program entry point"""

from __future__ import print_function
import argparse
import os

from helpers.github_webhook.webhook import Webhook
from flask import Flask

from bot_module import Bot

# Get GitHub API token
github_api_token = os.environ.get('GITHUB_API_TOKEN')

# Get GitHub API token
github_webhook_secret = os.environ.get('GITHUB_WEBHOOK_SECRET')

# Create bot and configure  it
py_bot = Bot(github_api_token)

# Standard Flask app
app = Flask(__name__)

# Defines '/webhooks' endpoint
webhook = Webhook(app, secret=github_webhook_secret)


# Standard Flask endpoint
@app.route('/')
def bot_is_working():
    return "Bot is working"


# Defines a handler for event 'ping'
@webhook.hook('ping')
def on_push(data):
    print('Got ping from Github')


# Defines a handler for event 'issue_comment' and others
@webhook.hook('issue_comment')
def on_issue_comment(data):
    if data['action'] == 'created' or 'edited':
        py_bot.parse_issue_comment_webhook(data)
        return True
    else:
        print('No action needed, discarding webhook')
        return False


def main(argv):
    """Program entry point.

    :param argv: command-line arguments
    :type argv: :class:`list`
    """
    from github_bot import metadata

    author_strings = []
    for name, email in zip(metadata.authors, metadata.emails):
        author_strings.append('Author: {0} <{1}>'.format(name, email))

    epilog = '''
{project} {version}

{authors}
URL: <{url}>
'''.format(
        project=metadata.project,
        version=metadata.version,
        authors='\n'.join(author_strings),
        url=metadata.url)

    arg_parser = argparse.ArgumentParser(
        prog=argv[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=metadata.description,
        epilog=epilog)
    arg_parser.add_argument(
        '-V', '--version',
        action='version',
        version='{0} {1}'.format(metadata.project, metadata.version))

    arg_parser.parse_args(args=argv[1:])

    print(epilog)

    return 0


def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    app.run(host="0.0.0.0", port=4567, debug=True)


if __name__ == '__main__':
    entry_point()
