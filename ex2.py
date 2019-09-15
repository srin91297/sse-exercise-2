import numpy as np
import pandas as pd
import os

import git
from git import RemoteProgress

from git import Repo
import sys
#import matplotlib.pyplot as plt
#import seaborn as sns

#INPUTS [[remote link, local_link, fixing commit], ......, .......] 
repo_details =  [
    [
        "https://github.com/apache/poi",
        "repo/poi",
        "c7db66a30dfb6cbbd5812ff3ae4c90ed2d9b9a27"      
    ],
    [
        "https://github.com/sebfz1/wicket-jquery-ui",
        "repo/wicket-jquery-ui",
        "fa0ce80f8e92c28c801773ed7c28621ae98e872"
    ],
    [
        "https://github.com/apache/httpcomponents-client",
        "repo/httpcomponents-client",
        "d954cd287dfcdad8f153e61181e20d253175ca8c"
    ]
]

#colours
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#helper function
class Progress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(self._cur_line)

#cloning repos
for i in repo_details:
    print(color.BOLD + i[1] + color.END)
    Repo.clone_from(i[0], i[1], progress=Progress())
    repo = Repo(i[1])
    data = repo.git.show("-s", i[2]).splitlines()
    # a. What was the message and title of the fixing commit? Was there any mention of fixing a bug or vulnerability? Hint: git diff or git show
    print('Part A:')
    for line in data:
        print(line)
    # b. How many total files were affected in the fixing commit? Hint: git diff or git show
    # # d. How many total lines of code (including comments and blank lines) were deleted? Hint: git diff or git show
    # # e. How many total lines of code (including comments and blank lines) were added? Hint: git diff or git show
    # print('Part e:')
    # print('Part d:')
    print('Part B, D, E:')
    print(repo.git.diff("--stat", i[2] + "^", i[2]))
    # # c. How many total directories were affected in the fixing commit? For example, if a file path is: abc/def/File.java, then its directory is abc/def. Hint: git diff or git show
    # print('Part c:')
    print('Part C:')
    print(repo.git.diff("--dirstat", i[2] + "^", i[2]))
    # # f. How many total lines of code (excluding comments and blank lines) were deleted? Hint: git diff or git show
    # print('Part f:')
    # # g. How many total lines of code (excluding comments and blank lines) were added? Hint: git diff or git show
    # print('Part g:')
    # print('Part F, G:')
    # print(repo.git.diff("--stat", "--regexp-ignore-case", i[2] + "^", i[2]))
    print("")

# # h. How many days were between the current fixing commit and the previous commit of each affected file? Hint: git log
# print('Part h:')
# # i. How many time has each affected file of the current fixing commit been modified in the past since their creation (including rename of the file)? Hint: git log
# print('Part i:')
# # j. Which developers have modified each affected file since its creation? Hint: git log
# print('Part j:')
# # k. For each developer identified, how many commits have each of them submitted? From your observation, are the involving developers experienced (with many commits) or new ones (with few commits) or both? Hint: git log or git shortlog
# print('Part k:')