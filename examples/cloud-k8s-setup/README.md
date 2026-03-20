# Cloud Kubernetes Setup Examples

Academic, script-first examples for provisioning Kubernetes clusters on major cloud providers.

Scripts are safe-by-default:

- Bash scripts print commands unless `EXECUTE=1`
- Python scripts print commands unless `--execute`

## Providers

- AWS EKS: `aws/create-eks.sh`, `aws/create_eks.py`
- Azure AKS: `azure/create-aks.sh`, `azure/create_aks.py`
- GCP GKE: `gcp/create-gke.sh`, `gcp/create_gke.py`

## Examples

AWS (dry-run):

```bash
./aws/create-eks.sh
python3 aws/create_eks.py
```

Azure (execute):

```bash
EXECUTE=1 ./azure/create-aks.sh
python3 azure/create_aks.py --execute
```

GCP (custom):

```bash
CLUSTER_NAME=demo-gke REGION=us-central1 NODE_COUNT=3 ./gcp/create-gke.sh
python3 gcp/create_gke.py --cluster-name demo-gke --region us-central1 --node-count 3
```

## Test

```bash
python3 -m unittest -v tests/test_cloud_setup.py
```
