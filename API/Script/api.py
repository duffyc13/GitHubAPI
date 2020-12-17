from github import Github, RateLimitExceededException, BadCredentialsException, BadAttributeException, \
    GithubException, UnknownObjectException, BadUserAgentException
import pandas as pd
import requests
import time
access_token = "49ece144bbb5d272645163af3a62b73bdf2340ee"

project_list = ['Hextris/hextris', 'bni/orbium', 'dart-lang/sample-pop_pop_win']

def extract_project_info():
    df_project = pd.DataFrame()
    
    while True:
        try:
            for project in project_list:
                g = Github(access_token)
                repo = g.get_repo(project)
                PRs = repo.get_pulls(state = 'all')
        
                df_project = df_project.append({
                'Project_ID' : repo.id,
                'Name' : repo.name,
                'Full_Name' : repo.full_name,
                'Language' : repo.language,
                'Forks' : repo.forks_count,
                'Stars' : repo.stargazers_count,
                'PRs_count' : PRs.totalCount,
                'Watchers' : repo.subscribers_count,
                }, ignore_index = True)
        except RateLimitExceededException as e:
            print(e.status)
            print('Rate limit exceeded')
            time.sleep(300)
            continue
        except BadCredentialsException as e:
            print(e.status)
            print('Bad credentials exception')
            break
        except UnknownObjectException as e:
            print(e.status)
            print('Unknown object exception')
            break
        except GithubException as e:
            print(e.status)
            print('General exception')
            break
        except requests.exceptions.ConnectionError as e:
            print('Retries limit exceeded')
            print(str(e))
            time.sleep(10)
            continue
        except requests.exceptions.Timeout as e:
            print(str(e))
            print('Time out exception')
            time.sleep(10)
            continue
        break
    df_project.to_csv(r'Dataset\dataset.csv', sep=',', encoding = 'utf-8', index = True)
    
if __name__ == "__main__":
    extract_project_info()
        
