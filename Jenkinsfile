pipeline{
  agent any
  stages{
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
