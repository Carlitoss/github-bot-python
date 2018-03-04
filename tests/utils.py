import json
import os


def get_fixture_data(data_name):
    resources = {
        'gh_webhook_create_issue_comment': 'gh/gh_webhook_create_issue_comment.json',
        'gh_webhook_delete_issue_comment': 'gh/gh_webhook_delete_issue_comment.json'
    }
    fixture_folder_path = os.path.join(os.path.dirname(__file__), "fixtures/")
    return open(fixture_folder_path + resources[data_name]).read()
