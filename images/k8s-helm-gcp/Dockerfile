FROM google/cloud-sdk:alpine

# setup kubectl
RUN gcloud components install kubectl

# setup helm
RUN apk add curl openssl
RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 \
    && chmod 700 get_helm.sh \
    && ./get_helm.sh