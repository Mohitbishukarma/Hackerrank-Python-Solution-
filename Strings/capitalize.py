# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    cap_s = []
    for i in s:
        cap_s.append(i.capitalize())
    return " ".join(cap_s)