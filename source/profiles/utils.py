import uuid

def get_random_code():
    """
    This method generates the random code.

    :return: returns the code
    """
    code = str(uuid.uuid4())[:8].replace('-', '').lower()
    return code