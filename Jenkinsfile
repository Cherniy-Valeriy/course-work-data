pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/твой-репо.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-app .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run --rm my-app pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 80:80 my-app'
            }
        }
    }
}
....
