from github import Github

access_token = "access code"

g = Github(access_token)

current_user = g.get_user()

print(current_user.name)
print(current_user.bio)
