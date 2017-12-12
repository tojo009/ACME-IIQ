from subprocess import check_output


currentCommitSHA = check_output("git rev-parse HEAD",shell=True)
#masterSHA        = check_output("git rev-parse orgin/master",shell=True)
print(currentCommitSHA)
#print(masterSHA)
command = "git diff --name-only fd07f332b27dccff04ecbb69c7c40a0b6fb5bd0a master~0"
print(check_output(command,shell=True))
