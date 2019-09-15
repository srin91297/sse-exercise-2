import numpy as np
import pandas as pd
import os

import git
from git import RemoteProgress

from git import Repo
#import matplotlib.pyplot as plt
#import seaborn as sns

#helper function
class Progress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print(self._cur_line)

#cloning 3 repo's
#First repo
remote_link = "https://github.com/apache/poi"
local_link = "repo/poi"
fixing_commit_poi = "c7db66a30dfb6cbbd5812ff3ae4c90ed2d9b9a27"
#Repo.clone_from(remote_link, local_link, progress=Progress())
repo_poi = Repo(local_link)
#Second repo
remote_link = "https://github.com/sebfz1/wicket-jquery-ui"
local_link = "repo/wicket-jquery-ui"
fixing_commit_wicket = "fa0ce80f8e92c28c801773ed7c28621ae98e872"
#Repo.clone_from(remote_link, local_link, progress=Progress())
repo_wicket = Repo(local_link)
#Third repo
remote_link = "https://github.com/apache/httpcomponents-client"
local_link = "repo/httpcomponents-client"
fixing_commit_http = "d954cd287dfcdad8f153e61181e20d253175ca8c"
#Repo.clone_from(remote_link, local_link, progress=Progress())
repo_http = Repo(local_link)
#show data of a fixing commit
show_data = repo_poi.git.show("-s", fixing_commit_poi).splitlines()
for line in show_data:
    print(line)