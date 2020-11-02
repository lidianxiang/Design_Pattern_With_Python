from abc import abstractmethod, ABCMeta


class Observer(metaclass=ABCMeta):   # 抽象订阅者
    @abstractmethod
    def update(self, notice):  # notice是一个Notice类的对象
        pass


# 抽象发布者
class Notice:
    def __init__(self):
        # 订阅者列表
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):  # 推送给所有的观察者
        for obs in self.observers:
            # 这里的obs是Oberser类的实例（对象）,self是Notice实例对象
            obs.update(self)


# 具体发布者
class StaffNotice(Notice):
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()   # 推送


# 具体订阅者（观察者）
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):  # 更新推送
        self.company_info = notice.company_info


if __name__ == '__main__':
    notice = StaffNotice("初始公司信息")
    s1 = Staff()
    s2 = Staff()
    notice.attach(s1)
    notice.attach(s2)
    notice.company_info = "公司今年业绩非常好，给大家发奖金！！！"
    print(s1.company_info)
    print(s2.company_info)
    print("*" * 30)
    notice.detach(s1)
    notice.company_info = "公司明天放假！！！"
    print(s1.company_info)
    print(s2.company_info)
