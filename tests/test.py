from subprocess import check_output
from lxml import etree

currentCommitSHA  = check_output("git rev-parse HEAD",shell=True).decode(encoding='UTF-8').rstrip()
print(currentCommitSHA)
dtd = etree.DTD("/home/circleci/project/tests/sailpoint.dtd")

command           = "git diff --name-only "+ currentCommitSHA +" origin/master~0"
filesCheckResult  = check_output(command,shell=True)
modifiedFiles     = filesCheckResult.decode(encoding='UTF-8').split("\n")
for file in modifiedFiles:
   if file.endswith(".xml"):
      print("Validating -" + file)
      with open(file, 'r') as myfile:
       data=myfile.read().replace('\n', '')
      root = etree.XML(data)
      print(dtd.validate(root))
  
print(modifiedFiles)
