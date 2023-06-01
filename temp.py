import os
login = 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 502447419870.dkr.ecr.us-east-1.amazonaws.com'
build = 'docker build -t 502447419870.dkr.ecr.us-east-1.amazonaws.com/dockerdemo .'
tag = 'docker tag dockerdemo:latest 502447419870.dkr.ecr.us-east-1.amazonaws.com/dockerdemo:latest'
push = 'docker push 502447419870.dkr.ecr.us-east-1.amazonaws.com/dockerdemo:latest'

os.system(login)
os.system(build)
os.system(tag)
os.system(push)
