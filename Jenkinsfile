pipeline {
    agent any
    
    stages {
        stage('Run Shell Script') {
            steps {
                // Path to your shell script file
                script {
                    // Specify the path to your shell script file
                    def scriptFilePath = "./scripts/trigger.sh"
                    
                    // Make sure the script file exists
                    if (fileExists(scriptFilePath)) {
                        // Execute the shell script
                        sh "chmod +x ${scriptFilePath}" // Make the script executable
                        sh "./${scriptFilePath}" // Run the script
                    } else {
                        error "Script file not found at ${scriptFilePath}"
                    }
                }
            }
        }
    }
}
