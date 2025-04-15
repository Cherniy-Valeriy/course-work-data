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
                    // Включаем Docker BuildKit перед сборкой
                    sh 'DOCKER_BUILDKIT=1 docker build -f /home/valera/course-work-data/Dockerfile -t $DOCKER_IMAGE:$DOCKER_TAG .'
			}
		}
	}

	stage('Run Tests') {
            steps {
                script {
                    // Запуск тестов внутри контейнера
                    sh 'docker run --rm -v "$PWD":/app -w /app $DOCKER_IMAGE:$DOCKER_TAG pytest -v'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Деплой на сервер, если тесты прошли успешно
                script {
                    // Запуск контейнера с маппингом портов
                    // Контейнер использует порт 5000 для Flask
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
