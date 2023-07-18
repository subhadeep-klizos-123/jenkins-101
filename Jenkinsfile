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
                python3 -m pytest --version
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing Code"
                sh '''
                python3 -m pytest -q test_main.py
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