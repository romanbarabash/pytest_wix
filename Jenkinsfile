pipeline {
    agent any
    environment {
        HOST = credentials('pytest_wix_host')
        USER_EMAIL = credentials('user_email')
        USER_PASSWORD = credentials('user_password')
        DEBUG = "true"
    }
    stages {
        stage('Build using Dockerfile'){
            agent {
                dockerfile true
                }
            }
        stage('Clean up'){
            steps {
                cleanWs()
            }
        }
        stage('Clone repo'){
            steps {
                sh 'git clone https://github.com/romanbarabash/pytest_wix.git'
            }
        }
        stage('Run Tests'){
            steps {
                dir('pytest_wix') {
                    sh 'pytest --tb=auto tests --alluredir ./allure-results'
                }
            }
        }
    }
    post {
        always {
            script {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'pytest_wix/allure-results']]
                ])
            }
        }
    }
}