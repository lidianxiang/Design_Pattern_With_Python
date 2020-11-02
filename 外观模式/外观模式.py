# 子系统类
class CPU:
    def run(self):
        print("CPU开始运行...")

    def stop(self):
        print("CPU停止运行...")


# 子系统类
class Disk:
    def run(self):
        print("硬盘开始工作...")

    def stop(self):
        print("硬盘停止工作...")


# 子系统类
class Memory:
    def run(self):
        print("内存通电...")

    def stop(self):
        print("内存断电...")


# 外观facade
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


if __name__ == '__main__':
    computer = Computer()
    computer.run()
    print('*' * 15)
    computer.stop()
