import subprocess

def get_git_revision():
    return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
