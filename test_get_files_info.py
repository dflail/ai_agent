# This is a test file for the get_files_info function.

from functions.get_files_info import get_files_info



def test() -> None:

    result = get_files_info("calculator", ".")
    print(result)

    result = get_files_info("calculator", "pkg")
    print(result)

    result = get_files_info("calculator", "/bin")
    print(result)

    result = get_files_info("calculator", "../")
    print(result)



if __name__ == "__main__":
    test()

