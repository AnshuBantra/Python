# %%
import re

def rearrange_name(name):
    try:
        result = re.search(r"^([\w .]*), ([\w .]*)$", name)
        return "{} {}".format(result[2], result[1])
    except:
        return name

# %%

def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True