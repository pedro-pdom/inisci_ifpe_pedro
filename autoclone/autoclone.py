import os
import pandas as pd

data = pd.read_csv('enterprise_projects.txt',  sep = '\t', header = None) #Dataset principal, com 29 colunas.
data.columns = ['url', 'project_id', 'sdtc', 'mcpc', 'mcve', 'star_number', 'commit_count', 'files', 'lines', 'pull_requests', 'github_repo_creation', 'earliest_commit', 'most_recent_commit', 'commiter_count', 'author_count', 'dominant_domain', 'dominant_domain_committer_commits', 'dominant_domain_author_commits', 'dominant_domain_committers', 'cik', 'fg500', 'sec10k', 'sec20f', 'nan', 'project_name', 'owner_login', 'company_name', 'owner_company', 'license']

# first_10 = data.url.head(1000) #O valor é o número de repositórios a serem clonados nesta execução
# name = data.project_name.head(1000) #msm de cima

first_10 = data.url
name = data.project_name 
#Comentar aqueles de cima e descomentar esse para clonar TODOS os repositórios

for x, i in zip(first_10, name):
    # os.system('git clone {} D:\gitrepo\{}'.format(x,i))
    print('git clone {} D:\gitrepo\{}'.format(x,tamanho)) # para testar output 
