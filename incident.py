
# Simulated service logs
logs = {
    "payment-api": "ERROR: Database connection timeout",
    "user-api": "ERROR: Invalid authentication token",
    "payment-api": "ERROR: connection timeout",
}

# Company's troubleshooting documents
runbooks = [
    {
        "title": "Database connection timeout",
        "solution": "Check database health and connection pool."
    },
    {
        "title": "Invalid authentication token",
        "solution": "Verify token validity and expiry."
    }
]

def get_logs(service_name):
    return logs.get(service_name,"No logs found")

def search_runbooks(error_message):
    results = []
    for document in runbooks:
        if document["title"].lower() in error_message.lower():
            results.append(document)
    return results

error = get_logs("payment-api")
documents = search_runbooks(error)

print("Error:,",error)
print("Relevant-document:",documents)