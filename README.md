### Python设计模式

#### 1. 定义

每个模式描述了一个在我们周围不断重复发生的问题，以及该问题的解决方案的核心。这样你就能一次又一次地使用该方案而不必做重复劳动。



#### 2. 解决思路

+ 分解
    + 面对复杂问题的常用思路是分而治之，即将大的问题分解成小的问题，将复杂的问题分解为多个简单的问题的思路
+ 抽象
    + 由于不能掌握全部复杂的对象，可以考虑忽视它的非本质细节，而去处理泛化和理想化的对象模式。

#### 3. 面向对象设计原则

1. 依赖倒置原则（DIP）
    + 高层模块不应该依赖于底层模块，二者都应该依赖于抽象
    + 抽象不应该依赖于实现细节，实现细节应该依赖于抽象。
2. 开放闭合原则（OCP）
    + 对扩展开放，对更改封闭。
    + 类模块应该是可扩展的，但是不可以修改。
3. 单一职责原则（SRP）
    + 一个类应该仅有一个引起它变化的原因
    + 变化的方向隐含着类的责任
4. Liskov替换原则（LSP）
    + 子类必须能够替换它们的基类
    + 继承表达类型抽象
5. 接口隔离原则（ISP）
    + 不应该强迫客户程序依赖他们不用的方法
    + 接口应该小而完备
6. 优先使用对象组合，而不是类继承
    + 类继承通常为“白箱复用”，对象组合通常为“黑箱复用”。
    + 继承在某种程度上破坏了封装性，子类父类耦合度高。
    + 而对象组合则只要求被组合的对象具有良好定义的接口，耦合度低。
7. 封装变化点
    + 使用封装来创建对象之间的分界层，让设计者可以在分界层的一侧进行修改，而不会对另一侧产生不良的影响，从而实现层次间的松耦合。
8. 针对接口编程，而不是针对实现编程
    + 客户程序无需获知对象的具体类型，只需要知道对象所具有的接口
    + 减少系统中各部分的依赖关系，从而实现“高内聚，松耦合”的类型设计方案。



#### 4. 设计模式分类

1. 创建型模式
    + [工厂方法模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F/%E5%B7%A5%E5%8E%82%E7%B1%BB%E7%9B%B8%E5%85%B3%E6%A8%A1%E5%BC%8F.md)
    + [抽象工厂模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E5%B7%A5%E5%8E%82%E6%A8%A1%E5%BC%8F/%E5%B7%A5%E5%8E%82%E7%B1%BB%E7%9B%B8%E5%85%B3%E6%A8%A1%E5%BC%8F.md)
    + [创建者模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E5%BB%BA%E9%80%A0%E8%80%85%E6%A8%A1%E5%BC%8F/%E5%BB%BA%E9%80%A0%E8%80%85%E6%A8%A1%E5%BC%8F.md)
    + 原型模式
    + [单例模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F/%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F.md)
2. 结构型模式
    + [适配器模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E9%80%82%E9%85%8D%E5%99%A8%E6%A8%A1%E5%BC%8F/%E9%80%82%E9%85%8D%E5%99%A8.md)
    + [桥模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E6%A1%A5%E6%A8%A1%E5%BC%8F/%E6%A1%A5%E6%A8%A1%E5%BC%8F.md)
    + [组合模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E7%BB%84%E5%90%88%E6%A8%A1%E5%BC%8F/%E7%BB%84%E5%90%88%E6%A8%A1%E5%BC%8F.md)
    + 装饰模式
    + [外观模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E5%A4%96%E8%A7%82%E6%A8%A1%E5%BC%8F/%E5%A4%96%E8%A7%82%E6%A8%A1%E5%BC%8F.md)
    + 享元模式
    + [代理模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E4%BB%A3%E7%90%86%E6%A8%A1%E5%BC%8F/%E4%BB%A3%E7%90%86%E6%A8%A1%E5%BC%8F.md)
3. 行为型模式
    + 解释器模式
    + [责任链模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E8%B4%A3%E4%BB%BB%E9%93%BE%E6%A8%A1%E5%BC%8F/%E8%B4%A3%E4%BB%BB%E9%93%BE%E6%A8%A1%E5%BC%8F.md)
    + 命令模式
    + 迭代器模式
    + 中介者模式
    + 备忘录模式
    + [观察者模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E8%A7%82%E5%AF%9F%E8%80%85%E6%A8%A1%E5%BC%8F/%E8%A7%82%E5%AF%9F%E8%80%85%E6%A8%A1%E5%BC%8F.md)
    + 状态模式
    + [策略模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E7%AD%96%E7%95%A5%E6%A8%A1%E5%BC%8F/%E7%AD%96%E7%95%A5%E6%A8%A1%E5%BC%8F.md)
    + 访问者模式
    + [模版方法模式](https://github.com/lidianxiang/Design_Pattern_With_Python/blob/master/%E6%A8%A1%E7%89%88%E6%96%B9%E6%B3%95%E6%A8%A1%E5%BC%8F/%E6%A8%A1%E7%89%88%E6%96%B9%E6%B3%95%E6%A8%A1%E5%BC%8F.md)



#### 5. 参考资料

《设计模式：可复用面向对象软件的基础》

