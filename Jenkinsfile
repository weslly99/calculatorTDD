pipeline{
    agent none
    stages {
        stage('Test'){
            agent {
                docker{
                    image: 'qnib/pytest'
                }
            }
            steps {
                sh 'pytest --verbose'
            }
        }
    }
}