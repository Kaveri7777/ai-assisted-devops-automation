pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Code already checked out from GitHub'
            }
        }

        stage('Build') {
            steps {
                bat 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                echo 'Tests completed successfully'pipeline {
    agent any

    tools {
        maven 'Maven'
    }

    environment {
        SONARQUBE_ENV = 'SonarQube-Local'
    }

    stages {

        stage('Build') {
            steps {
                bat 'mvn clean package'
            }
        }

        stage('AI Code Analysis') {
            steps {
                withSonarQubeEnv('SonarQube-Local') {
                    bat """
                    mvn sonar:sonar ^
                    -Dsonar.projectKey=ai-devops-java-app ^
                    -Dsonar.projectName=AI-DevOps-Java-App ^
                    -Dsonar.host.url=http://localhost:9000
                    """
                }
            }
        }
    }
}
