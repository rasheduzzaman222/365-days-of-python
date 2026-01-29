from datetime import datetime

def api_response(success, message, data=None):
    return {
        "success": success,
        "message": message,
        "timestamp": datetime.utcnow().isoformat(),
        "data": data
    }


if __name__ == "__main__":
    response = api_response(True, "Request processed", {"id": 101})
    print(response)
