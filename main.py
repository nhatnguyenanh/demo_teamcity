import os

if __name__ == '__main__':
    check_env = os.getenv("CI_CD")
    branch = os.getenv("branch")
    if check_env:
        print(f"hello {check_env} with branch {branch} ")
    else:
        print("hello teamcity master")