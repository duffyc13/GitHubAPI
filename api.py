from github import Github

access_token = "e501cf8d657ff88bee4e3092442b86ac122db544"

g = Github(access_token)

current_user = g.get_user()

print(current_user.name)
print(current_user.bio)
