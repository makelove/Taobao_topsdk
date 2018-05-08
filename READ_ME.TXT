python sdk 目前还处于起步阶段，希望大家一起来完善它

Version 1.1

设计背景：本SDK参考了facebook和twitter的pythonSDK的组织结构，同时结合top的SDK自动生成的机制，系统生成。

使用方法：

拷贝依赖包top到你的工程下，同时引入到PYTHONPATH中，具体怎么搞，就看你自己的系统啦。
总之一句话，让执行器可以找到top这个依赖包就OK拉。

调用方式，请参考
test.py

注意事项：

SDK在设计的时候，每次请求都让传入appkey和secret，但是一定不要把appkey和secret写的满项目都是，这还蛮坑爹的。
请大家像爱护自己密码一样爱护secret

希望大家一起来完善它。TKS。

