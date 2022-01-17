"""Cookiecutter pypackage template post_gen_project hook."""
import os
import shutil


def remove(paths):
    """Remove directories and files provided in paths list.

    Args:
        paths(list): List of relative paths to remove.

    """
    pwd = os.getcwd()

    for path in paths:
        path = os.path.join(pwd, path)

        if path and os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)


def set_gh_actions():
    """Remove GitHub actions if not enabled."""
    if "{{ cookiecutter.github_actions }}" != "yes":
        remove([".github"])


if __name__ == "__main__":
    set_gh_actions()
