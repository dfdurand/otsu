pipeline {
    agent none
    stages {
        stage('Build') {
           
           echo "install libraries"

            steps {
                sh 'python pip install pytest'
            }
        }

       // stage('Build') {
           
        //    echo "install libraries"

        //     steps {
        //         sh 'python pip install pytest'
        //     }
        // }

        stage('Test') {

            echo "run test" 
            steps {
                sh 'pytest-3 test/test_func.py'
            }

        }
        
    }
}