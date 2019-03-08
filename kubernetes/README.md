# AWS Kubernetes demo part


## create EKS infrastructure
```
eksctl create cluster --name=eks-summit --nodes-min=2 --nodes-max=10 --node-type=t2.small --asg-access
```




## install metrics-server
```
kubectl create -f metrics-server/deploy/1.8+/
```
