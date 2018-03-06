import pytest
import json
from .utils import get_fixture_data


@pytest.fixture
def create_issue_comment_payload():
    return json.loads(get_fixture_data('gh_webhook_create_issue_comment'))


@pytest.fixture
def delete_issue_comment_payload():
    return json.loads(get_fixture_data('gh_webhook_delete_issue_comment'))


@pytest.fixture
def create_issue_comment_bot_say_hello_payload():
    return json.loads(get_fixture_data('gh_webhook_create_issue_comment_bot_say_hello'))


@pytest.fixture
def create_issue_comment_bot_say_goodbye_payload():
    return json.loads(get_fixture_data('gh_webhook_delete_issue_comment_bot_say_goodbye'))
