# Android 5.0到8.0的行为变更

## Android 5.0(Lollipop)

[Android 5.0 行为变更](https://developer.android.com/about/versions/lollipop/android-5.0-changes.html)  
[Android 5.0 行为变更-中文](https://developer.android.google.cn/about/versions/lollipop/android-5.0-changes?hl=zh-cn)  

1. Android Runtime (ART)替代了Dalvik
2. 通知行为变更
   - Material Design
   - 声音和震动的设置方式变动
   - 锁定屏幕可见性，用户可以选择保护敏感信息不公开，缩减显示的文本
   - 多媒体播放，不建议使用自定义的RemoteView
   - 浮动通知
   - 媒体控件和 RemoteControlClient
3. getRecentTasks()弃用，如果您的应用使用此方法检索它自己的任务，则改用 getAppTasks() 检索该信息。

4. Android NDK 中的 64 位支持
5. 绑定到服务，Context.bindService() 方法现在需要显式 Intent
6. WebView，默认会阻止第三方Cookie和混合内容，系统现在可以智能地选择要绘制的 HTML 文档部分
7. 自定义权限唯一性要求，只有一个应用可以定义给定自定义权限，除非使用与定义权限的其他应用相同的密钥进行签名
8. TLS/SSL 默认配置变更
9. 支持托管配置文件

## Android 6.0(Mushroom)

[Android 6.0行为变更](https://developer.android.com/about/versions/marshmallow/android-6.0-changes.html)  
[Android 6.0行为变更-中文](https://developer.android.google.cn/about/versions/marshmallow/android-6.0-changes.html)

1. 运行时权限
2. 低电耗模式和应用待机模式
3. 取消支持 Apache HTTP 客户端
4. 由OpenSSL转到BoringSSL
5. 硬件标识符访问权
6. 通知
7. 音频管理器变更
8. 文本选择
9. 浏览器书签变更
10. Android 密钥库变更
11. WLAN 和网络连接变更
12. 相机服务变更
13. 运行时
14. APK 验证
15. USB 连接
16. 指纹身份验证
17. 可采用的存储设备，动态返回文件路径

## Andorid 7.0(Nougat)
[Android 7.0 开发者版本](https://developer.android.com/about/versions/nougat/android-7.0-changes.html)  
[Android 7.0 开发者版本-中文](https://developer.android.google.cn/about/versions/nougat/android-7.0-changes.html)  

**行为变更**

1. 电池和内存，移除了一些隐式广播
2. 权限更改，私有文件的安全性，分享私有文件内容的推荐方法是使用 FileProvider。DownloadManager 不再按文件名分享私人存储的文件。Android 框架执行的 StrictMode API 政策禁止在您的应用外部公开 file:// URI。
3. 多窗口支持
4. 配置文件指导的 JIT/AOT 编译，快速的应用安装路径
5. 随时随地低电耗模式...
6. Android 中的 ICU4J API
7. WebView，Chrome 和 WebView 配合使用，多进程，Javascript 在页面加载之前运行

## Android 8.0(Oreo)

[具透 | Android O 突然就来了，首个开发者预览版都有哪些新东西？](https://zhuanlan.zhihu.com/p/25938526)  

**行为变更**

1. 更激进的后台管理策略
2. 支持更高阶的蓝牙音频解码协议
3. 多渠道通知分类, 通知延后功能, 状态标记（应用角标）
4. XML 字体支持
5. 导航栏自定义功能

**适配指南**：

1. 后台位置更新频率下降，依赖后台定位需要适配
2. `net.hostname` 已不再受支持
3. 网络连接，如果之前执行的 connect(InetAddress, int) 方法失败，send(DatagramPacket) 方法会抛出 SocketException
4. 集合API，AbstractCollection.removeAll(null) 和 AbstractCollection.retainAll(null) 现在始终抛出 NullPointerException
5. 国际化，调用 Currency.getDisplayName(null) 会抛出 NullPointerException

升级 targetSdkVersion 之后：

6. 广播接收器，隐式广播接收不到消息，除了个别 API 有例外
7. 不支持使用 net.dns1、net.dns2、net.dns3 或 net.dns4 系统属性
8. 对于 Native 库，强制执行以下规则：数据不应可执行，代码不应可写入
9. Native 库，动态链接器会检查 ELF 标头和节标头中的更多值，如果无效值则会失败
10. 通知栏要求必须设置渠道
11. 集合 API 的变更

## Android 9.0(Pie)

[Android P 行为变更](https://developer.android.google.cn/about/versions/pie/android-9.0-changes-all?hl=zh-cn)

**行为变更**

1. 使用 Wi-Fi RTT 进行室内定位
2. 新增刘海屏支持
3. 通知栏功能增强，即时通讯通知栏设置人物更方便，支持显示图片，通知可以按渠道屏蔽
4. 多摄像头支持和摄像头更新
5. 新增 ImageDecoder 用来做图片解码
6. 新增 AnimatedImageDrawable 用来展示 webp 和 gif 动图
7. HDR VP9 视频、HEIF 图片压缩和媒体 API
8. JobScheduler 中的数据流量费用敏感度
9. Neural Networks API 1.1，机器学习相关的 API 在 Android O中引入，对功能做了增强
10. 自动填充框架的改进
11. 安全增强功能

**适配指南**

1. 针对非 SDK 接口的限制，通过反射访问非开放的 API，会抛异常
2. 移除 Crypto 提供程序，Crypto JCA 提供程序已被移除，调用 SecureRandom.getInstance("SHA1PRNG", "Crypto") 将会抛出 NoSuchProviderException
3. 更严格的 UTF-8 解码器，严格遵循 Unicode 标准
4. 已禁止空闲应用访问摄像头、麦克风和传感器

升级 targetSdkVersion 之后需要适配：

5. 前台服务必须先请求 `FOREGROUND_SERVICE` 权限
6. 移除了对 Build.serial 的直接访问，获取序列号需要申请 `READ_PHONE_STATE` 权限，使用 `Build.getSerial()` 获取
7. 不允许共享 WebView 数据目录，如果存在多进程使用 WebView，CookieManager 或 android.webkit 中的任何其他 API 软件包，第二个进程调用会崩溃
8. SELinux 禁止访问应用的数据目录