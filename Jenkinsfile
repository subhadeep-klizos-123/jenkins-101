pipeline {
    agent {
        node {
            label 'dind-slave-agent'
        }
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', changelog: false, poll: false, url: 'https://github.com/subhadeep-klizos-123/jenkins-101.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m pip install pytest
                python3 -m pytest --version
                '''
            }
        }
        
        stage('Test') {
            steps {
                sh "python3 -m pytest -q test_main.py"
            }
        }
        
        stage('Run') {
            steps {
                sh "python3 main.py"
            }
        }
        
        stage('Docker Build & Push') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'docker-credentails') {
                        sh """
                            docker build -t jenkins-101:latest .
                            docker tag jenkins-101:latest iammatrix999/jenkins-101:latest
                            docker push iammatrix999/jenkins-101:latest
                        """
                    }
                }
            }
        }
    }
}
