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

        stage('Docker Build') {
            steps {
                bat 'docker build -t ai-devops-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker rm -f ai-devops-container || exit 0'
                bat 'docker run -d -p 8082:8081 --name ai-devops-container ai-devops-app'
            }
        }
    }
}
