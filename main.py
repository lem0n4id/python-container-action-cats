import os


# github context
GITHUB:object
GITHUB_ACTION:str
GITHUB_ACTION_PATH:str
GITHUB_ACTOR:str
GITHUB_BASE_REF:str
GITHUB_EVENT:object
GITHUB_EVENT_NAME:str
GITHUB_EVENT_PATH:str
GITHUB_HEAD_REF:str
GITHUB_JOB:str
GITHUB_REF:str
GITHUB_REF_NAME:str
GITHUB_REF_PROTECTED:str
GITHUB_REF_TYPE:str
GITHUB_REPOSITORY:str
GITHUB_REPOSITORY_OWNER:str
GITHUB_RUN_ID:str
GITHUB_RUN_NUMBER:int
GITHUB_RUN_ATTEMPT:int
GITHUB_SERVER_URL:str
GITHUB_SHA:str
GITHUB_TOKEN:str
GITHUB_WORKFLOW:str
GITHUB_WORKSPACE:str

# job.container.id
# GITHUB_EVENT = os.environ["GITHUB_EVENT_NAME"]

if __name__ == "__main__":
    # print(GITHUB_EVENT)
    from github import Github
    import os
    from pprint import pprint

    token = os.getenv('GITHUB_TOKEN', '...')
    g = Github(token)
    repo = g.get_repo("lem0n4id/python-container-action-cats")
    issues = repo.get_issues(state="open")
    pprint(issues.get_page(0))