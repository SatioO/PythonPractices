from config import configuration
from one import file1

if __name__ == "__main__":
    print(configuration["db"])
    s = file1.method1()
    print(s)
    print(configuration["db"])
