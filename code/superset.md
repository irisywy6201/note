- docker pull amancevice/superset
- docker run --name my_superset -p 8088:8088
- 進入 container
  -    superset db upgrade
  -    superset init
  -    export FLASK_APP=superset
  -    flask fab create-admin
  -    superset load_examples #download example
  - https://blog.csdn.net/nikeylee/article/details/115264818    
  - https://github.com/AlexsJones/kubernetes-mongodb-cluster/blob/master/templates/mongo/statefulset.yaml
  - https://www.youtube.com/watch?v=W-lJX3_uE5I
  - https://github.com/justmeandopensource/kubernetes/blob/master/yamls/mongodb/mongodb-statefulset.yaml
  - https://hub.docker.com/r/starburstdata/superset/dockerfile/
