import os

if __name__ == '__main__':
    check_env = os.getenv("CI/CD")
    if check_env:
        print(f"hello {check_env} teamcity master")
    else:
        print("hello teamcity master")