.PHONY: clean
clean:
	@echo "Removing images"
	@sudo docker image rm semantikadocker.vdu.lt/hatespeech:latest

.PHONY: build
build:
	@echo "Building images"
	@sudo docker build . -t semantikadocker.vdu.lt/hatespeech:latest

.PHONY: push
push:
	@echo "Pushing images"
	@sudo docker push semantikadocker.vdu.lt/hatespeech:latest

.PHONY: update-kubernetes
update-kubernetes:
	@echo "Kubernetes deleting"
	@kubectl delete deploy hatespeech
	@sleep 60
	@echo "Kubernetes apply"
	@kubectl apply -f devops/hs-deployment.yaml

.PHONY: redeploy
redeploy: build push update-kubernetes
	@echo "Done"

.PHONY: logs
logs:
	@echo "Kubernetes logs"
	POD=$$(kubectl get pods --no-headers -o custom-columns=":metadata.name" | grep hatespeech); \
	kubectl logs $${POD}

#.PHONY: init
#init:
#create new venv
#clone https://github.com/facebookresearch/fastText.git
#source env
#pip install /fastText/.