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
                {
                    "name" : "print readme",
                    "cmd" : "cat README.md",
                    "type" : "shell"
                },
            ]
        }
    ]
}

print(json.dumps(x))
