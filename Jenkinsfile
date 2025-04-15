pipeline {
    agent any  // Использовать любой доступный агент для выполнения

    environment {
        DOCKER_IMAGE = 'flask'
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
        	script {
			sh 'DOCKER_BUILDKIT=1 docker build -f /home/valera/course-work-data/app/Dockerfile -t $DOCKER_IMAGE:$DOCKER_TAG .'
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
                    sh 'docker run -d -p 80:5000 $DOCKER_IMAGE:$DOCKER_TAG'
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
