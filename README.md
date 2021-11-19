<p align="center">
  <img alt="Cat Gif" src="https://i.imgur.com/9z4r02l.png">
</p>

# Action Cats

> <h3> I'm trying to replicate [ruairidhwm/action-cats](https://github.com/ruairidhwm/action-cats) in python.
>  
> All credits goes to [ruairidhwm](https://github.com/ruairidhwm) and other contributers in the original repo </h3>

This is a simple Github Action which comments on your PRs with a cat gif as a reward for pushing some code.

This is just a novelty action, but feel free to use it. If you'd like to contribute then just open a PR.

## Usage

```yaml          
name: Cats 😺

on:
  pull_request_target:
    types:
      - opened
      - reopened

jobs:
  aCatForCreatingThePullRequest:
    name: A cat for your effort!
    runs-on: ubuntu-latest
    steps:
      - uses: lem0n4id/python-container-action-cats@main
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
