from utils.hash_db import get_all_watch_directories
from git.repo import Repo
from git.exc import InvalidGitRepositoryError, NoSuchPathError


def ensure_git_repo(directory) -> Repo:
    try:
        # Try to load the repo
        return Repo(directory)
    except (InvalidGitRepositoryError, NoSuchPathError):
        # If not a repo, initialize one
        print(f"Initializing new Git repository at {directory}")
        return Repo.init(directory)


# Example usage:
directories = get_all_watch_directories()
repos: dict[str, Repo] = {}

for directory in directories:
    repos[directory] = ensure_git_repo(directory)


def stage_file(repo: Repo, file_path: str):
    """Stage a file in the given Git repository."""
    repo.index.add([file_path])
    print(f"Staged file: {file_path} in repository: {repo.working_tree_dir}")
