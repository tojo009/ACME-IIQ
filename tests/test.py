from subprocess import check_output


currentCommitSHA = check_output("git rev-parse HEAD",shell=True)
print(currentCommitSHA)
command = "git diff --name-only" + currentCommitSHA + "master"
print(check_output(command,shell=True))
