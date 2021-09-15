import typing


class Parsing:
    def __init__(self, path: str):
        self.__path = path
        self.__lines = self.__get_lines()
        self.__search_for_comment()

    def __get_lines(self) -> typing.List[str]:
        with open(self.__path, 'r') as file_read:
            return file_read.readlines()

    def __search_for_comment(self) -> None:
        search_long_comment: bool = False
        list_long_comment: typing.List[str] = []
        for line in self.__lines:
            if "//" in line and search_long_comment is False:
                comment: str = self.__parse_single_line_comment(line)
                print(comment)
            if "/*" in line and "*/" not in line:
                search_long_comment = True
            elif "/*" not in line and "*/" in line:
                search_long_comment = False
                list_long_comment.append(line)
                long_comment: str = self.__parse_long_comment(list_long_comment)
                print(long_comment)
                list_long_comment.clear()
            elif "/*" in line and "*/" in line:
                comment: str = self.__parse_long_comment_one_line(line)
                print(comment)

            if search_long_comment:
                list_long_comment.append(line)

    @staticmethod
    def __parse_single_line_comment(line: str) -> str:
        number_slash = 0
        comment: str = ""
        for letter in line:
            if number_slash >= 2:
                comment += letter
            if letter == '/':
                number_slash += 1
        comment = comment.replace('\n', '')
        return comment

    def __parse_long_comment(self, lines: typing.List[str]) -> str:
        long_comment: str = self.__parse_long_comment_one_line(lines[0])
        for i in range(1, len(lines) - 1):
            long_comment += lines[i]
        long_comment += self.__parse_long_comment_one_line(lines[len(lines) - 1])
        return long_comment

    @staticmethod
    def __parse_long_comment_one_line(line: str) -> str:
        comment: str = ""
        is_start_comment: bool = False
        for i in range(1, len(line)):
            if is_start_comment:
                comment += line[i]

            if is_start_comment is False and line[i - 2: i] == "/*":
                is_start_comment = True
        return comment.replace("*/", '')
