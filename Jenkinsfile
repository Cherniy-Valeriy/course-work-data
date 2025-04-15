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


stage('Check Files') {
            steps {
                script {
                    // Проверяем, что тесты находятся в правильной директории на машине Jenkins
                    sh 'ls -alh /var/lib/jenkins/workspace/proba'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Проверяем содержимое /app в контейнере
                    sh 'docker run --rm -v "$PWD":/app -w /app $DOCKER_IMAGE:$DOCKER_TAG ls -alh'

                    // Запуск тестов внутри контейнера
                    sh 'docker run --rm -v "$PWD":/app -w /app $DOCKER_IMAGE:$DOCKER_TAG pytest -v'
                }
            }
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
