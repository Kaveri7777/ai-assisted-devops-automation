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
                echo 'Tests completed successfully'
            }
        }
    }
}
