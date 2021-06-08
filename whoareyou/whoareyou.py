#simple who.is script to indentify the organizations that own the email domains on the dataset
#the dataset does not give me an exact number of organizations involved, so maybe this will give me a more accurate answer
import whois
import pandas as pd

# data = pd.read_csv('forkchecker//enterprise_projects.txt',  sep = '\t', header = None)
# data.columns = ['url', 'project_id', 'sdtc', 'mcpc', 'mcve', 'star_number', 'commit_count', 'files', 'lines', 'pull_requests', 'github_repo_creation', 'earliest_commit', 'most_recent_commit', 'commiter_count', 'author_count', 'dominant_domain', 'dominant_domain_committer_commits', 'dominant_domain_author_commits', 'dominant_domain_committers','dominant_domain_authors', 'cik', 'fg500', 'sec10k', 'sec20f', 'project_name', 'owner_login', 'company_name', 'owner_company', 'license']

# determinant = data.dominant_domain
# cabecinha = determinant.head(10)

data = pd.read_csv('emaildomainlist.txt', sep =',', header=None)
data.columns = ['domain', 'frequency']

determinant = data.domain
cabecinha = determinant

file = open('output2.txt', 'w')

for i in cabecinha:
    print(i)
    try:
        w = whois.whois(i)
        print(w["org"])
        x = w['org']
        str(x)
        file.write('{}\t{}\n'.format(i, x))
    except KeyError:
        print("Domínio não tem organização declarada")
        file.write("{}\tDomínio não tem organização declarada\n".format(i))

# w = whois.whois('10up.com')
# print(w)
file.close()