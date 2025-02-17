import os
import json

class ShellStep():
  def __init__(self, name, cmd, target):
    self.name = name
    self.cmd = cmd
    self.type = "shell"
    self.target = target
  def __str__(self):
     return json.dumps(self.__dict__) 

class Job():
    
  def __init__(self):
     self.target = "pc"

     self.steps = [
        ShellStep("Print current path", "pwd", self.target),
        ShellStep("print ci file", "cat ci.py", self.target),
     ]
    
  def __str__(self):
    res = ""
    for step in self.steps:
      res = res + str(step) + "\n"
    return res
      
#print(Job())
s1 = ShellStep("Print current path", "pwd", "pc")
print(s1)

