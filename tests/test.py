from subprocess import check_output


currentCommitSHA = check_output("git rev-parse HEAD",shell=True).strip('\n')
#masterSHA        = check_output("git rev-parse orgin/master",shell=True)
print(currentCommitSHA)
#print(masterSHA)
command = "git diff --name-only"+ currentCommitSHA +"master~0"
print(check_output(command,shell=True))
