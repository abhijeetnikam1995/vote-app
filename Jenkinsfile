

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
	      AWS_ACCESS_KEY_ID="AKIAXJ7BTGHPNC77FZVV"
  AWS_SECRET_ACCESS_KEY="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"
    }

    stages {
    
       

        
        stage('Build App Image') {
            steps {
                script {
			sh 'pwd'
                    dockerImage = docker.build( appRegistry + ":$BUILD_NUMBER", "./")
                }
            }
        }
        
        stage('Upload App Image') {
          steps{
            script {
              docker.withRegistry( vprofileRegistry, registryCredential ) {
                dockerImage.push("$BUILD_NUMBER")
                dockerImage.push('latest')
              }
            }
          }
        }

        stage('Deploy to ECS staging') {
            steps {
		     script {
              //  withAWS(credentials: 'awscreds', region: 'us-east-1') {
                    sh 'aws ecs update-service --region ${region} --cluster ${cluster} --service ${service} --force-new-deployment'
		//}
                } 
            }
        }
	    
	    
	    
    }

}


