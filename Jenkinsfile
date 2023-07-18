pipeline {
    agent {
        node {
            label 'docker-agent-python'
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
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing Code"
                sh '''pytest'''
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