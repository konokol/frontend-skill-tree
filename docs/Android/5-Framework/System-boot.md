## 启动流程图

## 启动流程

1. Bootloader启动，启动内核，做一些初始化工作；
2. Init进程启动，这是第一个用户进程。  
    - Init进程中会解析rc文件，初始化属性服务，启动zygote和ServiceManager
3. Init进程fork出Zygote进程  
    - 最初这个进程叫app_process，之后改名叫zygote；   
    - 启动AndroidRuntime，这是AppRuntime的子类    
    - 启动Java虚拟机，设置启动类为ZygoteInit，设置jvm的启动参数，早期的Jvm最大堆内存为64MB
    - 注册JNI函数 
    - 运行ZygoteInit类，开始进入Java虚拟机中  
4. Java中，Zygote主要干了以下几件事  
    - 开始socket连接，等待处理消息
    - 预加载类和资源，这个阶段特别耗时
    - fork出system_server进程，在system_server进程中，清理掉socket等资源
    - 运行runSelectLoop，等待处理请求
   
