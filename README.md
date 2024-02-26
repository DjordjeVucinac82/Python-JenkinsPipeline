# Python-JenkinsPipeline
test repo for Python in Jenkinsfile Pipeline ec2 RHEL 8.4

aws configure --profile djole

aws cloudformation create-stack --stack-name jenkins --template-body file://CloudFormation.yml --profile djole \
aws cloudformation delete-stack --stack-name jenkins --profile djole

ssh -i /home/djole/repos/private/Python-JenkinsPipeline/*****.pem ec2-user@54.196.198.114

coverage run -m unittest discover -p "test_*.py"
python -m unittest test_example.py