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