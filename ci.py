import os
import json

class ShellStep():
  def __init__(self, name, cmd, target):
    self.name = name
    self.cmd = cmd
    self.type = "target"
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
x = {
    "jobs" : [
        {
        "target" : "pc_job_spown",
        "wait" : "False",
        "name" : "job to do on pc 1",
        "steps" : [
            {
                "name" : "Print current path",
                "cmd" : "pwd",
                "type" : "shell"
            },
            {
                "name" : "Print current path 2",
                "cmd" : "pwd",
                "type" : "shell"
            },
        ]
        },
        {
            "target" : "pc_job_spown",
            "wait" : "False",
            "name" : "job to do on pc 2",
            "steps" : [
                {
                    "name" : "Print current path",
                    "cmd" : "pwd",
                    "type" : "shell"
                },
                {
                    "name" : "Print current path 2",
                    "cmd" : "pwd",
                    "type" : "shell"
                },
            ]
        }
    ]
}

#print(Job())
s1 = ShellStep("Print current path", "pwd", "pc")
print(json.dumps(x))






