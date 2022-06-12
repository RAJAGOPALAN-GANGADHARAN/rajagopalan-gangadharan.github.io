from github import Github, RateLimitExceededException
import time
import calendar
from pathlib import Path

filepath = Path(__file__).resolve().parent
print("Running script in directory: " + str(filepath))

g = Github("") # Enter token make it run biweekly

basic_details = open(f'{filepath}/basic_details.csv','w')

repos = [repo for repo in g.get_user().get_repos()]
with open(f'{filepath}/repos.txt','w') as f:
    for repo in repos:
        f.write(repo.full_name+'\n')

for repo in g.get_user().get_repos():
    for branch in repo.get_branches():
        for commit in repo.get_commits(sha=branch.name, author="Rajagopalan-Gangadharan"):
            try:
                basic_details.write(f'{repo.full_name},{branch.name},{commit.commit.author.date},{commit.html_url}\n')
            except RateLimitExceededException:
                search_rate_limit = g.get_rate_limit().search
                print('search remaining: {}'.format(search_rate_limit.remaining))
                reset_timestamp = calendar.timegm(search_rate_limit.reset.timetuple())
                # add 10 seconds to be sure the rate limit has been reset
                sleep_time = reset_timestamp - calendar.timegm(time.gmtime()) + 10
                time.sleep(sleep_time)
                continue

basic_details.close()
