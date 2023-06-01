

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
	cluster = "vprostaging"
        service = "vproappstagesvc"
	    
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
                withAWS(credentials: 'awscreds', region: 'us-east-1') {
                    sh 'aws ecs update-service --cluster ${cluster} --service ${service} --force-new-deployment'
                } 
            }
        }
	    
	    
	    
    }
    post {
        always {
            echo 'Slack Notifications.'
            slackSend channel: '#jenkinscicd',
                color: COLOR_MAP[currentBuild.currentResult],
                message: "*${currentBuild.currentResult}:* Job ${env.JOB_NAME} build ${env.BUILD_NUMBER} \n More info at: ${env.BUILD_URL}"
        }
    }
}


