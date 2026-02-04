pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat 'mvn clean package'
            }
        }

        stage('AI Code Analysis') {
            steps {
                withSonarQubeEnv('SonarQube-Local') {
                    bat 'mvn sonar:sonar -Dsonar.projectKey=ai-devops-java-app -Dsonar.projectName=AI-DevOps-Java-App'
                }
            }
        }
    }
}
