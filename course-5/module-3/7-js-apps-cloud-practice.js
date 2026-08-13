function classify_deployment_strategy(uses_serverless, uses_containers, requires_stateful_storage) {
    // TODO: Implement the decision logic based on the arguments:
    // - uses_serverless (boolean)
    // - uses_containers (boolean)
    // - requires_stateful_storage (boolean)
    // The function should return one of the following strings:
    //   "serverless-stateless"
    //   "serverless-with-external-storage"
    //   "containerized-stateful"
    //   "containerized-stateless"
    //   "basic-app-service"
    // according to the rules described in the prompt.

    // Write your implementation below.
    if (uses_serverless) {
        if (requires_stateful_storage) {
            return "serverless-with-external-storage";
        } else {
            return "serverless-stateless";
        }
    }
}

function classify_deployment_strategy(uses_serverless, uses_containers, requires_stateful_storage) {
    // TODO: Implement the decision logic based on the arguments:
    // - uses_serverless (boolean)
    // - uses_containers (boolean)
    // - requires_stateful_storage (boolean)
    // The function should return one of the following strings:
    //   "serverless-stateless"
    //   "serverless-with-external-storage"
    //   "containerized-stateful"
    //   "containerized-stateless"
    //   "basic-app-service"
    // according to the rules described in the prompt.

    // Write your implementation below.
    if (uses_serverless) {
        if (requires_stateful_storage) {
            return "serverless-with-external-storage";
        } else {
            return "serverless-stateless";
        }
    } else if (uses_containers) {
        if (requires_stateful_storage) {
            return "containerized-stateful";
        } else {
            return "containerized-stateless";
        }
    } else {
        return "basic-app-service";
    }
}