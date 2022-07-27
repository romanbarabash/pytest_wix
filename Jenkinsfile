pipeline {
    agent {
        node {
            label "pytest_wix"
        }
        dockerfile true
     }
    environment {
        HOST = credentials('pytest_wix_host')
        USER_EMAIL = credentials('user_email')
        USER_PASSWORD = credentials('user_password')
        DEBUG = "true"
    }
    stages {
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
//        stage('Build'){
//            steps {
//                dir('pytest_wix') {
//                    sh 'pip install -r requirements.txt'
//                }
//            }
//        }
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