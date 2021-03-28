swagger_config = {
    'openapi': '3.0.2',
    'doc_dir': './docs'
}

swagger_template = {
    "info": {
        "description": "Bowling Account API",
        "version": "0.1"
    },
    "tags": [{
        "name": "user",
        "description": "Operation about account"
    }],
    "components": {
        "schemas": {
            "account": {
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "string",
                        "example": "001"
                    },
                    "password": {
                        "type": "string",
                        "example": "Kcnet00!@#$"
                    },
                    "user_name": {
                        "type": "string",
                        "example": "홍길동"
                    },
                    "email": {
                        "type": "string",
                        "example": "test@example.com"
                    },
                    "mobile_number": {
                        "type": "string",
                        "example": "01012341234"
                    }
                }
            },
            "api_response": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "success"
                    },
                    "status": {
                        "type": "string",
                        "example": "ok"
                    }
                }
            }
        }
    }
}
