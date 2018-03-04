# -*- coding: utf-8 -*-

import pytest
from pytest import raises
from github_bot import metadata
from github_bot.main import *

parametrize = pytest.mark.parametrize


def test_bot_is_working():
    result = bot_is_working()
    assert result == "Bot is working"


def test_on_issue_comment(github_webhook_new_issue_comment_payload):
    result = on_issue_comment(github_webhook_new_issue_comment_payload)
    assert result is True


@parametrize('versionarg', ['-V', '--version'])
def test_version(versionarg, capsys):
    with raises(SystemExit) as exc_info:
        main(['progname', versionarg])
    out, err = capsys.readouterr()
    # Should print out version.
    assert err == '{0} {1}\n'.format(metadata.project, metadata.version)
    # Should exit with zero return code.
    assert exc_info.value.code == 0


@parametrize('helparg', ['-h', '--help'])
def test_help(helparg, capsys):
    with raises(SystemExit) as exc_info:
        main(['progname', helparg])
    out, err = capsys.readouterr()
    # Should have printed some sort of usage message. We don't
    # need to explicitly test the content of the message.
    assert 'usage' in out
    # Should have used the program name from the argument
    # vector.
    assert 'progname' in out
    # Should exit with zero return code.
    assert exc_info.value.code == 0
