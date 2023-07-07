def swap_case(s:str):
    fs="".join([char.upper() if char.islower() else char.lower() for char in s])
    return fs
