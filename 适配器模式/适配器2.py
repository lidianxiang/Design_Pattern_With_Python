from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    def pay(self, money):
        print("支付宝支付%d元." % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)


class Bankpay:
    def cost(self, money):
        print("银联支付%d元." % money)


class ApplyPay:
    def cost(self, money):
        print("苹果支付%d元." % money)


# 类适配器
class NewBankPay(Payment, Bankpay):
    def pay(self, money):
        self.cost(money)


# 对象适配器
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


if __name__ == '__main__':
    # p = AliPay()
    # p.pay(100)   # 支付宝支付100元

    # p = NewBankPay()
    # p.pay(100)   # 银联支付100元.

    p = PaymentAdapter(ApplyPay())
    p.pay(200)  # 苹果支付200元.
