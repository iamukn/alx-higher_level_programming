#!/usr/bin/python3
# Author IAM_UKN
if __name__ == "__main__":
    import sys
    k = 0
    i = len(sys.argv) - 1
    for j in range(1, i + 1):
            k = k + int(sys.argv[j])
    print("{}".format(k))
