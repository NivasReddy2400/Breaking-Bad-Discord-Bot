import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there'

    if message == 'roll':
        return str(random.randint(1, 10))
    
    if p_message == 'say my name':
        return 'HEISENBERG'

    if p_message == 'help':
        return 'Figure it out'

    return 'I did not get that one.'
