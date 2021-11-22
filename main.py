import os

GITHUB_ACTION = os.environ["GITHUB_ACTION"]

if __name__ == "__main__":
    print(GITHUB_ACTION)