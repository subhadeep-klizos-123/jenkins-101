pipeline {
    agent {
        node {
            label 'docker-agent-alpine'
        }
    }
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Install') {
            steps {
                echo "Installing Dependencies..."
                sh '''
                pip3 install -U pytest
                pytest --version
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing Code"
                sh '''
                pytest -q test_main.py
                '''
            }
        }
        stage('Run') {
            steps {
                echo "Running Code"
                sh '''
                python3 main.py
                '''
            }
        }
    }
}