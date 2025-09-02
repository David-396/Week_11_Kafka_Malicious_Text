 docker run -d -p 27017:27017 --name mongo_project -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=example mongo:6.0



oc apply -f ..\infra\retriever_infra\secret.yaml
oc apply -f ..\infra\retriever_infra\deployment.yaml
oc apply -f ..\infra\retriever_infra\svc.yaml

oc apply -f ..\infra\preprocessor_infra\secret.yaml
oc apply -f ..\infra\preprocessor_infra\deployment.yaml
oc apply -f ..\infra\preprocessor_infra\svc.yaml

oc apply -f ..\infra\enricher_infra\secret.yaml
oc apply -f ..\infra\enricher_infra\deployment.yaml
oc apply -f ..\infra\enricher_infra\svc.yaml

oc apply -f ..\infra\presister_infra\secret.yaml
oc apply -f ..\infra\presister_infra\deployment.yaml
oc apply -f ..\infra\presister_infra\svc.yaml

oc apply -f ..\infra\data_retrieval_infra\secret.yaml
oc apply -f ..\infra\data_retrieval_infra\deployment.yaml
oc apply -f ..\infra\data_retrieval_infra\svc.yaml
oc apply -f ..\infra\data_retrieval_infra\route.yaml