pipeline {
    agent any  // Использовать любой доступный агент для выполнения

    environment {
        DOCKER_IMAGE = 'my-flask-app'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Клонируем репозиторий из Git
                git 'https://github.com/Cherniy-Valeriy/course-work-data'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Собираем Docker-образ
                script {
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Запуск тестов внутри контейнера
                script {
                    sh 'docker run --rm $DOCKER_IMAGE:$DOCKER_TAG pytest tests'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Деплой на сервер, если тесты прошли успешно
                script {
                    sh 'docker run -d -p 80:80 $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }
        success {
            echo 'Build and deploy successful!'
        }
        failure {
            echo 'Build or deploy failed!'
        }
    }
}
