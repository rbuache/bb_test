import os
import json

class ShellStep():
  def __init__(self, name, cmd):
    self.name = name
    self.cmd = cmd
    self.type = "shell"
  def __str__(self):
     return json.dumps(self.__dict__) 
s1 = ShellStep("Print current path", "pwd")
s2 = ShellStep("print ci file", "cat ci.py")

print(s1)
print(s2)
