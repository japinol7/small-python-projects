from collections.abc import Sequence
import requests

from tools.logger import logger
from tools.logger.logger import log
from config import GITHUB_API_BASE_URI, GITHUB_API_VERSION, GITHUB_API_PER_PAGE

VOTE_COUNT_MIN = 5
POPULARITY_COUNT_MIN = 2


class GithubError(Exception):
    pass


class GithubResponse:
    def __init__(self):
        self.id = None
        self.text = None
        self.json = None
        self.status_code = None
        self.err = None
        self.resource_name = None
        self.items_len = 0

    def clear(self):
        self.id = None
        self.text = None
        self.json = None
        self.status_code = None
        self.err = None
        self.resource_name = None
        self.items_len = 0

    def set_state(self, response):
        self.text = response.text
        self.json = response.json()
        self.status_code = response.status_code
        self.items_len = len(self.json) if isinstance(self.json, Sequence) else 0

    def __str__(self):
        return (f"Id: {self.id}\n"
                f"Id: {self.id}\n"
                )


class GithubClient:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_uri = f"{GITHUB_API_BASE_URI}"
        self.per_page = GITHUB_API_PER_PAGE
        self.page = 1
        self.url = None
        self.headers = None
        self.response = GithubResponse()

        self._init()

    def _init(self):
        self.headers = {
            'Authorization': f"Bearer {self.api_token}",
            'Content-Type': 'application/vnd.github+json',
            'X-GitHub-Api-Version': GITHUB_API_VERSION,
            }

    def _get_response(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            self.response.set_state(response)
            return self.response
        except Exception as e:
            raise GithubError(f"Error getting Github answer! Msg: {e}")

    def get_resource_info(self, resource):
        self.response.clear()
        self.response.resource_name = resource

        self.url += (f"?page={self.page}"
                     f"&per_page={self.per_page}")

        log.info(f"Request GET {self.url}")
        return self._get_response()

    def get_commits(self, repo, owner):
        log.info(f"Get commits. Repo: {repo}  Owner: {owner}")
        self.url = f"{self.base_uri}/repos/{owner}/{repo}/{'commits'}"
        return self.get_resource_info('commits')

    def get_repos_for_org(self, org):
        log.info(f"Get repos for organization: {org}")
        self.url = f"{self.base_uri}/orgs/{org}/repos"
        return self.get_resource_info('repos')

    def get_repos_public_for_user(self, user):
        log.info(f"Get public repos for user: {user}")
        self.url = f"{self.base_uri}/users/{user}/repos"
        return self.get_resource_info('repos')


def example_of_usage():
    from config import GITHUB_API_TOKEN
    from tools.utils import utils

    logger.add_stdout_handler(logger_format=logger.LOGGER_FORMAT_NO_DATE)
    logger.add_file_handler(multiple_log_files=False, logger_format=logger.LOGGER_FORMAT_NO_DATE)

    def get_commits(page, count_start=1):
        client.page = page
        client.get_commits(repo=repo, owner=owner)

        if client.response.items_len == 0:
            return count_start

        count_start = count_start + 1 if count_start > 1 else 1
        i = count_start
        for i, item in enumerate(client.response.json, start=count_start):
            com = item['commit']
            com_msg = com['message'][:170].replace('\n', ' ')
            log.info(f"{i:3} {com['author']['name'][:18]:18} "
                     f"{com['author']['date']}  "
                     f"{com_msg}")
        log.info('------\n')
        return i

    def get_repos_not_forked(page, count_start=1):
        client.page = page
        client.get_repos_public_for_user(user=owner)

        if client.response.items_len == 0:
            return count_start

        i = count_start
        for item in client.response.json:
            if item['fork']:
                continue
            log.info(f"{i:3} {item['owner']['login']}  "
                     f"{item['name']}  ")
            i += 1
        log.info('------\n')
        return i

    def get_pages(*, func, max_pages=1):
        count = 1
        for page in range(1, max_pages + 1):
            count = func(page=page, count_start=count)
            if client.response.items_len == 0:
                break

    owner = 'nasa'
    repo = 'OnAIR'

    client = GithubClient(api_token=utils.read_file_as_string(GITHUB_API_TOKEN))
    client.per_page = 75

    get_pages(func=get_commits, max_pages=2)
    get_pages(func=get_repos_not_forked, max_pages=4)

    log.info("EOF")


if __name__ == '__main__':
    example_of_usage()
