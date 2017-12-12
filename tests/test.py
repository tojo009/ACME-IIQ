from subprocess import check_output

print(check_output("git status",shell=True))
