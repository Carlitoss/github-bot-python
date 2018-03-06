# -*- coding: utf-8 -*-
import os
import pytest
import vcr

from github_bot.app import App
from settings import GITHUB_API_TOKEN, GITHUB_WEBHOOK_SECRET

parametrize = pytest.mark.parametrize

my_vcr = vcr.VCR(
    record_mode='once'
)


@my_vcr.use_cassette('synopsis.yaml')
def test_on_issue_comment(mocker, create_issue_comment_payload):
    app = App(GITHUB_API_TOKEN, GITHUB_WEBHOOK_SECRET)
    app.bot.handle_comment(create_issue_comment_payload)
