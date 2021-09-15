from parsing import Parsing


def run():
    parsing: Parsing = Parsing("JavaFile.java")


if __name__ == "__main__":
    print("Все комментарии в файле:")
    run()
