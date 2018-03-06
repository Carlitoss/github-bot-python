# -*- coding: utf-8 -*-
import os
import pytest
import vcr

from github_bot.bot_module.bot import Bot
from settings import GITHUB_API_TOKEN

my_vcr = vcr.VCR(record_mode='once')


@pytest.fixture(scope='module')
def bot():
    return Bot(GITHUB_API_TOKEN)


def test_bot_init(bot):
    assert bot.is_configured
    assert set(bot.commands.keys()) == {'say-hello', 'say-goodbye'}


# TODO: Use cassette
def test_bot_get_pr_from_payload(bot, create_issue_comment_payload):
    pr = bot._get_pr_from_payload(payload=create_issue_comment_payload)
    assert pr.id == 172572812


# TODO: Use cassette
def test_bot_get_command_from_comment_no_found(bot, create_issue_comment_payload):
    command = bot.get_command_from_comment(payload=create_issue_comment_payload)
    assert command is None


# TODO: Use cassette
def test_bot_get_command_from_comment_say_hello(bot, create_issue_comment_bot_say_hello_payload):
    command = bot.get_command_from_comment(payload=create_issue_comment_bot_say_hello_payload)
    assert command == 'say-hello'


# TODO: Use cassette
def test_bot_get_command_from_comment_say_goodbye(bot, create_issue_comment_bot_say_goodbye_payload):
    command = bot.get_command_from_comment(payload=create_issue_comment_bot_say_goodbye_payload)
    assert command == 'say-goodbye'


# def test_execute_command_with_payload(mocker, bot, create_issue_comment_payload):
#     import pdb; pdb.set_trace()
#     commands = bot.commands
#     mocked_command = mocker.spy(commands, 'say-hello')
#     bot.commands = mocked_command
#     bot.execute_command_with_payload('say-hello',{})
#     assert mocked_command.assert_called_once_with({})
#
