1. Docker Image Used: `iammatrix999/jenkins-jdk11-py-dind:latest`  
2. Agent Name: `dind-slave-agent`  
3. Root File system: `/home/jenkins`  
4. Container Settings -> Mounts: `type=bind,source=/var/run/docker.sock,destination=/var/run/docker.sock`  