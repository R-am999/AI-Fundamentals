customers = [
    {
        "customer_id": 1001,
        "name": "Alice Smith",
        "email": "alice@example.com",
        "addresses": [
            {
                "house_add": {
                    "street": "123 Maple St", "city": "Los Angeles", "zip": "90001"
                }
            },
            {
                "work_add": {
                    "street": "789 Corporate Blvd", "city": "San Francisco", "zip": "94105"
                }
            }
        ]
    },
    {
        "customer_id": 1002,
        "name": "Bob Jones",
        "email": "bob@example.com",
        "addresses": [
            {
                "house_add": {
                    "street": "456 Oak Rd", "city": "Austin", "zip": "73301"
                },
                "work_add": {
                    "street": "999 Finance Way", "city": "New York", "zip": "10001"
                }
            }
        ]
    }
]

print(customers[1]['addresses'][0])