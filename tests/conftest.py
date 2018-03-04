import pytest
import json
from .utils import get_fixture_data


@pytest.fixture
def github_webhook_new_issue_comment_payload():
    return json.loads(get_fixture_data('gh_webhook_create_issue_comment'))


@pytest.fixture
def github_webhook_delete_issue_comment_payload():
    return json.loads(get_fixture_data('gh_webhook_delete_issue_comment'))


@pytest.fixture(scope='module', params=['create', 'delete'])
def github_webhook_issue_comment_payload_param(request):
    action = request.param
    return json.loads(get_fixture_data('gh_webhook_%s_issue_comment' % action))
