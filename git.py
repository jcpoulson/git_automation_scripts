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

def clone():

    print("\nYou will be asked for the user first and then the repository name\n")

    user = input("User: ")
    __user__ = f'{user}'
    repo = input("Repository: ")
    __repo__ = f'{repo}'

    print("\nChoose the local path for your clone.")
    local = input("Local path: ")
    local_path = f'{local}'

    subprocess.Popen(['git', 'clone', "https://github.com/" + __user__ + "/" + __repo__ + ".git", local_path])

def log():
    subprocess.call(["git", "log"])


def main():

    choices = 'set remote, local commit, remote commit, clone, log'
    print("\nCommands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "set remote":
        set_remote()

    elif choose_command == "local commit":
        local_commit()

    elif choose_command == "remote commit":
        remote_commit()
    
    elif choose_command == "clone":
        clone()

    elif choose_command == "log":
        log()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)


if __name__ == __main__:
    main()
