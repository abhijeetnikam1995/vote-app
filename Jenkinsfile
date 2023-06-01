

def COLOR_MAP = [
    'SUCCESS': 'good', 
    'FAILURE': 'danger',
]
pipeline {
    agent any
  
    environment {

        registryCredential = 'ecr:us-east-1:awscreds'
        appRegistry = '502447419870.dkr.ecr.us-east-1.amazonaws.com/dockerdemo'
        vprofileRegistry = "https://502447419870.dkr.ecr.us-east-1.amazonaws.com/dockerdemo"
	cluster = "myapp-cluster"
        service = "testapp-service"
	    region = "us-east-1"
	  
    }

   stages {
        stage('Run Python Script') {
            steps {
                sh 'python3 test.py'
            }
        }
    }
}


