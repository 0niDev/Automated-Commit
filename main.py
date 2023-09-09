import os


def main():
    path = os.getcwd()
    print(path)
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    for i in range(100):
        with open(rf"{path}/commit.txt", "w") as f:
            f.write(f'"commit": {i}')
            f.close()
        os.system("git add .")
        os.system('git commit -m " This is a automated commit."')
        os.system("git push")


if __name__ == "__main__":
    main()
