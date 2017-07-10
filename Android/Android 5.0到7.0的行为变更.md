# Android 5.0到7.0的行为变更

## Android 5.0(Lollipop)

[Android 5.0 行为变更](https://developer.android.com/about/versions/android-5.0-changes.html?hl=zh-cn#BehaviorNotifications)

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

1. 电池和内存，移除了一些隐式广播
2. 权限更改，私有文件的安全性，分享私有文件内容的推荐方法是使用 FileProvider。DownloadManager 不再按文件名分享私人存储的文件。Android 框架执行的 StrictMode API 政策禁止在您的应用外部公开 file:// URI。
3. 多窗口支持
4. 配置文件指导的 JIT/AOT 编译，快速的应用安装路径
5. 随时随地低电耗模式...
6. Android 中的 ICU4J API
7. WebView，Chrome 和 WebView 配合使用，多进程，Javascript 在页面加载之前运行
