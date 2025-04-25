pipeline {
    agent any

    stages {
        stage('Preparar entorno') {
            steps {
                echo 'Instalando dependencias...'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                echo 'Ejecutando pruebas...'
                sh 'python -m unittest discover -s . -p "*_test.py"'
            }
        }

        stage('Finalizado') {
            steps {
                echo 'Pipeline completado exitosamente 🎉'
            }
        }
    }

    post {
        failure {
            echo '⚠️ El pipeline falló.'
        }
    }
}
