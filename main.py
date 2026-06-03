'''users = [
    {
        'name': '',
        'role': '',
        'join_date': ''
    }
]

users[0]['name'] = input("Enter name: ")
users[0]['role'] = input("Role: ")
users[0]['join_date'] = input("Start date: ")

print(f"""Joining Letter Confirmation

Dear {users[0]['name']}, 

We are delighted to officially confirm your selection for the role of {users[0]['role']} Intern at Bluestock Fintech. 
To proceed with the onboarding process, please complete the joining formalities by submitting the joining letter at the link below. This step is essential to validate your acceptance of the internship offer.

We are confident that your journey with Bluestock will be an enriching and valuable experience. Our team looks forward to working with you and supporting your professional growth.
If you have any queries or require assistance, feel free to contact us at any time. You can start by {users[0]['join_date']}.

Best Regards,
HR Department
Bluestock Company""")'''

names = (
    ('A', 1),
    ('B', 2),
    ('C', 3),
    ('D', 4)
)

for name, grade in names:
    print(name, grade)