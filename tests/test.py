from subprocess import check_output


currentCommitSHA = check_output("git rev-parse HEAD",shell=True)
#masterSHA        = check_output("git rev-parse orgin/master",shell=True)
print(currentCommitSHA)
#print(masterSHA)

command = "git diff --name-only "+ currentCommitSHA.decode(encoding='UTF-8').rstrip() +" origin/master~0"
print(check_output(command,shell=True))
