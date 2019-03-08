# AWS Kubernetes demo part

## create EKS infrastructure
```
eksctl create cluster --name=eks-summit --nodes-min=2 --nodes-max=10 --node-type=t2.medium --asg-access --ssh-access
```


## install kubernetes-dashboard
```
kubectl apply -f kubernetes-dashboard/
```

get into dashboard
```
kubectl proxy
```
dashboard should be available at: http://127.0.0.1:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/

get token to auth
```
kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}')
```

## install demo-app
```
kubectl apply -f demo-app/
```
when app will be installed in kubernetes You will be able to see endpoint in kubernetes-dashboard to access app


## install metrics-server
```
kubectl apply -f metrics-server/
```


## install autoscaler
```
kubectl apply -f autoscaler/
```


links:
https://eksctl.io

https://github.com/kubernetes/kubectl

https://github.com/kubernetes/dashboard

https://github.com/kubernetes-incubator/metrics-server

https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler
