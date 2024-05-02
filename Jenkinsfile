pipeline {
    agent any
    
    stages {
        stage('Run Shell Script') {
            steps {
                // Path to your shell script file
                script {
                    // Specify the path to your shell script file
                    sh ./home/ec2-user/trigger.sh
                    
                }
            }
        }
    }
}
