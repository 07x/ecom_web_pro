# INITIAL 
. docker-compose up (BUILD & RUN )
. docker exec -it docker_test /bin/bash


# RUN , STOP , REMOVE  
. Starting a Stopped Container
    docker start [container_name or container_id]

. Stopping a Container 
    - docker stop [container_name or container_id]

.Removing a Container:
    - docker rm [container_name or container_id]

# CONTAINER
.Show All Container
    - docker ps -a
.Show Running Containers
    - docker ps
