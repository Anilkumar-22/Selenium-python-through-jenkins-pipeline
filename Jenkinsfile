pipeline{
  agent any
  stages{
      stage('Checkout') {
            steps {
                echo "Cloning repository..."
                git branch: 'main', url: 'https://github.com/Anilkumar-22/Selenium-python-through-jenkins-pipeline.git'
            }
        }
      stage("packages"){
        steps{
        echo "I am installing packages"
        bat pip install -r requirements.txt
        }
      }
      stage("run test"){
        steps{
        echo "I am running tests"
        bat python test.py
        }
      }
  }
}
