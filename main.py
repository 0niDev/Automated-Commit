import json
import os


def main():
    path = os.getcwd()
    print(path)
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    for i in range(10):
        with open(rf"{path}/commit.json", "w") as f:
            f.write('"commit": {i}')
            f.close()
        os.system("git add .")
        os.system('git commit -m " This is a automated commit."')
        os.system("git push")


if __name__ == "__main__":
    main()
