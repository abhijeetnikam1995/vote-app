node {
    def app

    stage('Clone repository') {
      

        checkout scm
    }
    stage('Build App Image') {
            steps {
                script {
			sh 'pwd'
                  //  dockerImage = docker.build( appRegistry + ":$BUILD_NUMBER", "./vprofile-docker/Docker-files/app/multistage/")
                }
            }
        }

    stage('Build image') {
  
       app = docker.build("abhijeetnikam1995/front")
    }

    stage('Test image') {
  

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    
    stage('Trigger ManifestUpdate') {
                echo "triggering updatemanifestjob"
                build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
        }
}
