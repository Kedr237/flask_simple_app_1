from uuid import NAMESPACE_DNS, uuid5


def generate_uuid(key: str) -> str:
    return str(uuid5(NAMESPACE_DNS, key))


persons_data = [
    {
        'id': generate_uuid('JohnDoe'),
        'first_name': 'John',
        'last_name': 'Doe',
    },
    {
        'id': generate_uuid('JaneSmith'),
        'first_name': 'Jane',
        'last_name': 'Smith',
    },
    {
        'id': generate_uuid('MichaelJohnson'),
        'first_name': 'Michael',
        'last_name': 'Johnson',
    },
    {
        'id': generate_uuid('EmilyWilliams'),
        'first_name': 'Emily',
        'last_name': 'Williams',
    },
    {
        'id': generate_uuid('DavidBrown'),
        'first_name': 'David',
        'last_name': 'Brown',
    },
]
