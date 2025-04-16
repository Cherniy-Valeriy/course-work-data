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
                git branch: 'main', url: 'https://github.com/Cherniy-Valeriy/course-work-data.git'
		sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
		    sh 'pwd'
   		    sh 'ls -la'
                    // Включаем Docker BuildKit перед сборкой
                    sh 'DOCKER_BUILDKIT=1 docker build -f /home/valera/course-work-data/Dockerfile -t $DOCKER_IMAGE:$DOCKER_TAG .'
			}
		}
	}

	stage('Run Tests') {
            steps {
                script {
		    sh 'ls -la'
                    // Запуск тестов внутри контейнера
                    sh 'docker run --rm $DOCKER_IMAGE:$DOCKER_TAG pytest app/tests'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Деплой на сервер, если тесты прошли успешно
                script {
		    sh 'docker rm -f flask_app || true' 
                    // Запуск контейнера с маппингом портов
                    // Контейнер использует порт 5000 для Flask
                    sh 'docker run -d -p 80:5000 --name flask_app $DOCKER_IMAGE:$DOCKER_TAG'
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
