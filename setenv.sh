grep -v '^#' .local-secrets
export $(grep -v '^#' .local-secrets | xargs)