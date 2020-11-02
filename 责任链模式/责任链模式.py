from abc import abstractmethod, ABCMeta


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handler_leave(self, days):
        pass


class GeneralManager(Handler):
    def handler_leave(self, days):
        if days <= 10:
            print("总经理准假%d天" % days)
        else:
            print("你还是辞职吧...")


class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handler_leave(self, days):
        if days <= 5:
            print("部门经理准假%d天" % days)
        else:
            print("部门经理职权不足")
            self.next.handler_leave(days)


class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handler_leave(self, day):
        if days <= 3:
            print("项目主管准假%d天" % days)
        else:
            print("项目主管职权不足")
            self.next.handler_leave(days)


if __name__ == '__main__':
    days = 15
    h = ProjectDirector()
    h.handler_leave(days)
