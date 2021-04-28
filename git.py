import subprocess

def set_remote():
    print("\nYou will be asked for the user first and then the repository name\n")

    user = input("User: ")
    __user__ = user
    repo = input("Repository: ")
    __repo__ = repo

    link = "https://github.com/{}/{}.git".format(__user__, __repo__)

    subprocess.call(["git", "init"])
    subprocess.call(["git", "add", "*"])
    subprocess.call(["git", "commit", "-m", "default commit"])
    subprocess.call(["git", "branch", "-M", "main"])
    subprocess.call(['git', 'remote', 'add', 'origin' "https://github.com/{}.git".format(link)])
    subprocess.call(["git", "push", "-u", "origin", "main"])


def local_commit():
    message = input("\nType in your commit message: ")
    commit_message = f'{message}'

    subprocess.call(["git", "add", "*"])
    subprocess.call(["git", "commit", "-m", commit_message])


def remote_commit():
    message = input("\nType in your commit message: ")
    commit_message = f'{message}'

    subprocess.call(["git", "add", "*"])
    subprocess.call(["git", "commit", "-m", commit_message])
    subprocess.call(["git", "push", "-u", "origin", "main"])


def main():

    choices = 'set remote, local commit, remote commit'
    print("\nCommands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "set remote":
        set_remote()

    elif choose_command == "local commit":
        local_commit()

    elif choose_command == "remote commit":
        remote_commit()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)


main()