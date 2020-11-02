from abc import ABCMeta, abstractmethod
import time


class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
                time.sleep(1)
            except KeyboardInterrupt:
                break

        self.stop()


class MyWindow(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行...")

    def stop(self):
        print("窗口停止运行...")

    def repaint(self):
        print(self.msg)


if __name__ == '__main__':
    MyWindow("Hello, world:)").run()

