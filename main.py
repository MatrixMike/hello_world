#!/bin/python3
from typing import Protocol
from bs4 import BeautifulSoup


class Message(Protocol):
    def __str__(self) -> str:
        ...


class Inputer(Protocol):
    def read_input(self) -> Message:
        ...


class Outputer(Protocol):
    def write_output(self, message: Message) -> None:
        ...


class TextMessage():
    def __init__(self, msg: str) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return self.msg


class XmlInputer():
    def __init__(self, xml: str) -> None:
        self.soup = BeautifulSoup(xml, features="html.parser")

    def read_input(self) -> Message:
        p = self.soup.p
        if p is None:
            raise RuntimeError("Error reading message")
        return TextMessage(p.string)


class ConsoleOutputer():
    def write_output(self, message: Message) -> None:
        print(str(message) + "\n")


def do_work(inputer: Inputer, outputer: Outputer) -> None:
    text = inputer.read_input()
    outputer.write_output(text)


def main() -> None:
    inputer = XmlInputer("<p>Hello world!</p>")
    outputer = ConsoleOutputer()
    do_work(inputer, outputer)


if __name__ == "__main__":
    main()
