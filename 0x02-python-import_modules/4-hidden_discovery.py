#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for loop in sorted(dir(hidden_4)):
        if "__" not in loop:
            print(loop)
