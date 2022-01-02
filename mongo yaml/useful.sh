# secret 加密
echo root | base64

# create secret
kubectl create -f ./my-secret.yaml

# before read secondary
rs.secondaryOk()

# show all document in collection
db.collectionName.find()

# insert
db.col.insert({'name' : 'test'})

https://medium.com/geekculture/installing-mongodb-on-kubernetes-with-replica-sets-and-no-mongodb-operator-ed8d7f3bb2d1