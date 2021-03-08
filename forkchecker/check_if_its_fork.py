import requests
import json
import pandas as pd
import time

#This script makes requests to the Github API to check if the github repositories in this dataset are forks.
#Then, it generates 3 outputs. The first is a .txt file containing the json strings. It's not really necessary but can be nice for individual analysis.
#The second output is a .txt in pandas dataframe format to be analysed as a dataset, containing information already present in Spinellis' dataset and a boolean column telling me if the repository in that row is a fork or not.
#An added benefit of this dataset is that it only contains currently existing repositories, as the original had over 1000 dead links.
#The third and last output is a file listing all forks and telling me the name and owner of it's parent.

#The dataset. Please ensure the file is in the same folder as the script, but you can always edit the path of the pd.read_csv
data = pd.read_csv('enterprise_projects.txt',  sep = '\t', header = None)
data.columns = ['url', 'project_id', 'sdtc', 'mcpc', 'mcve', 'star_number', 'commit_count', 'files', 'lines', 'pull_requests', 'github_repo_creation', 'earliest_commit', 'most_recent_commit', 'commiter_count', 'author_count', 'dominant_domain', 'dominant_domain_committer_commits', 'dominant_domain_author_commits', 'dominant_domain_committers','dominant_domain_authors', 'cik', 'fg500', 'sec10k', 'sec20f', 'project_name', 'owner_login', 'company_name', 'owner_company', 'license']
#
#your github username and auth token goes here
#if you don't authenticate your request rate goes down considerably
username = ''
token = ''
#

#function for countdown timer
#i think it's nice because just a sleep(3700) would make me uneasy. Is the script really running or is it stuck? 
def contagemreg(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

t = 3700 #default value is 1h + little more than a minute just to be safe
         #the requests must be made with at least 1h interval or else github API will start blocking the requests

#data for the columns that i want. The projectname and ownerlogin it's for requests.get iteration.
#the projecturl and dominantdomain are just there because i thought it would be convenient.
ownerlogin = data.owner_login 
projectname = data.project_name
projecturl = data.url
ddomain = data.dominant_domain

forkrepo = open("Fork Checker//datasetfork.txt", "a")#the variable for the dataset file.
forksandparents = open("Fork Checker//forks_and_parents.txt", "a")#the variable for the file that shows me the parents and etc
counter = 0

for x, i, z, d in zip(ownerlogin, projectname, projecturl, ddomain):#using zip to iterate over all columns at the same time
    print("Analisando o repositório {}".format(z))
    r = requests.get("https://api.github.com/repos/{}/{}".format(x, i), auth = (username, token))
    jason = r.json()#transforming the data from github into json objects, behave like dictionaries
    #this next line is for writing the data into a txt file. it can be useful for analysis, but it can also clutter the folder.
    #It's disabled by default.
    #with open('Fork Checker//{}.txt'.format(i), 'w') as outfile:
        #json.dump(jason, outfile)
    
    #everytime the script comes across a repository that does not exist, it returns "KeyError" and interrupts the program. 
    try: #Didn't specify the error because sometimes the repositories give me weird json that python couldn't parse correctly, so there's that.
        isfork = jason['fork']
        if isfork == True:
            parentname = jason['parent']['name']
            parentowner = jason['parent']['owner']['login']
            print("Esse repositório é um fork. {} é o nome do repositório parente e {} é o login do dono.".format(parentname, parentowner))
            forksandparents.write("O repositório {} é fork. {} é o repositório parente e {} é o login do dono.\n".format(z, parentname, parentowner))
            forkrepo.write("{}\t{}\t{}\t{}\tt\n".format(z,x,i,d))
        else:
            print("Não é fork.")
            forkrepo.write("{}\t{}\t{}\t{}\tf\n".format(z,x,i,d))
    except:
        print("Repositório inválido ou não existe.")
    counter+=1
    print("Essa é a {} vez que o loop roda. Legal!".format(counter))
    if counter == 4500 or counter == 9000 or counter == 13500: #the github api gives you 5000 requests every 1h. I wanted to be safe so i stopped the script every 4500 requests.
        print("O programa irá agora parar por pouco mais que 1 hora.")
        print("Isso é necessário para evitar problemas com o API do github.")
        print("Now waiting.")
        contagemreg(t)
        print("Voltando à programação normal!")
