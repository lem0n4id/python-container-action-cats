import os

GITHUB_ACTION = os.environ["GITHUB_ACTOR"]

if __name__ == "__main__":
    print(F"{GITHUB_ACTION} initiated the workflow")