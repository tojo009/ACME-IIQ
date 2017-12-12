from subprocess import check_output

command = "git diff --name-only HEAD HEAD~3"
currentCommitSHA = check_output("git rev-parse HEAD",shell=True)
print(currentCommitSHA)
print(check_output(command,shell=True))
