from subprocess import check_output

command = "git diff --name-only HEAD HEAD~3"
print(check_output(command,shell=True))
