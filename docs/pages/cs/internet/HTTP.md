# HTTP协议详解

## HTTP的发展历史

### HTTP/0.9 -- 单行协议

HTTP最初没有版本，为了区分后面的版本，第一个版本被命名为v0.9. HTTP/0.9中只支持GET请求，响应也只有文档本身，没有Header，也没有状态码和错误码。

请求：

```text
GET /mypage.html
```

响应：

```text
<html>
  hello
</html>

```

- 通过TCP/IP（或者类似的面向连接的服务）与服务器和端口（可选，默认80）建立连接；
- 客户端发送一行ASCII文本，包括GET、文档地址（无空格）、回车符（可选）和换行符；
- 服务端使用HTML格式的消息响应，该消息被定义为“ASCII字符的字节流”；
- 通过服务器关闭连接来终止消息；
- 错误响应以可读的文本显示，使用HTML语法，除了文本内容，无法区分错误响应和正确响应；
- 请求是幂等的；
- 服务器不需要在断开连接之后存储任何请求的信息；

### HTTP/1.0 -- 构建可扩展性

HTTP/1.0的一个请求
```text
GET /mypage.html HTTP/1.0
User-Agent: NCSA_Mosaic/2.0 (Windows 3.1)

200 OK
Date: Tue, 15 Nov 1994 08:12:31 GMT
Server: CERN/3.0 libwww/2.17
Content-Type: text/html
<HTML>
一个包含图片的页面
  <IMG SRC="/myimage.gif">
</HTML>

```

- 更多请求方法。除了HTTP 0.9中的GET方法，新增了HEAD和POST方法；
- 为所有的消息增加了版本号字段。该字段是可选的，为了向后兼容，默认使用HTTP/0.9；
- HTTP首部，即请求头。可以与请求和响应一起发送，以提供正在执行的请求或发送响应相关的更多信息；
- 一个三位整数的响应状态码。

HTTP/1.0 中的响应码：

| 分类              | 值                             | 描述<img width="150">                                        | 详情                                                         |
| :---------------- | :----------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1xx（信息）       | N/A                            | N/A                                                          | HTTP/1.0中没定义1xx相关的状态码，但是定义了此分类            |
| 2xx（成功）       | 200<br/>201<br/>202<br/>204    | OK<br/>Created<br/>Acepted<br/>No content                    | 请求成功<br/>此状态码应当由POST请求返回<br/>请求正在处理中，还未处理完<br/>已接收请求，正在处理中，但响应无消息体 |
| 3xx（重定向）     | 300<br/>301<br/>302<br/>304    | Multiple choices<br/>Moved permanently<br/>Moved temporarily<br/>Not Modified | 资源在多处可用，响应中提供了的更多信息<br/>响应Header中Location提供资源新地址<br/>响应Header中Location提供资源新地址<br/>条件响应，无需发送正文 |
| 4xx（客户端错误） | 400<br />401<br />403<br />404 | Bad request<br/>Unauthorized<br />Forbidden<br />Not Found   | 服务端无法理解请求或请求参数有误<br/>请求未被授权访问<br />通过授权，但是没有访问资源的权限<br />资源找不到 |
| 5xx（服务端错误） | 500<br />501<br />502<br />503 | Internal server error<br />Not implemented<br />Bad gateway<br />Service unavailable | 服务端内部错误，请求无法完成<br />服务端不识别请求（如未实现的HTTP方法）<br />网关或代理服务收到上游服务错误<br />由于负载过高或者维护，服务端无法完成请求 |

### HTTP/1.1 -- 标准化的协议

- 强制增加Host首部
- 持久连接（Keep-Alive）
- 新的请求方法，如PUT、OPTIONS、CONNECT、TRACE、DELETE
- 更丰富的缓冲方法，比如Cache-Control和HTTP/1.0中的Expires选项更多
- HTTP cookies，允许HTTP维护状态
- 引入字符集，即Header中Charset字段
- 支持代理
- 支持权限验证
- 新的状态码
- 尾随首部

## HTTPS

HTTPS对HTTP的消息添加了三个重要的概念：

- 加密 –––– 传输过程中第三方无法读取信息
- 完整性校验 –––– 消息传输过程中未被更改，因为整个消息已经过数字签名，并且该签名在解密之前已通过加密验证
- 身份验证 –––– 服务器不是伪装的

### SSL、TLS、HTTPS和HTTP

HTTPS使用SSL或者TLS来加密。SSLv1只在Netscape内部发布，1995年发布了SSLv2，1996年发布了更安全的SSLv3。由于SSL由Netscape拥有，因此它不是互联网标准，但由于SSLv3被普遍使用，很长一段时间里其都是事实上的标准。之后SSL被标准化为TLS。在2014年，SSLv3中发现了重大安全漏洞，因此被要求停止使用，浏览器也停止了对其支持。

TLSv1.0和SSL类似，但是它们不兼容。TLS1.1和TLS1.2分别在2006年和2008年推出。TLSv3在2018年被批准为标准。

## HTTPS身份验证流程

1. 客户端向服务端发送一个消息
2. 服务端返回一个数字证书（包含颁布证书的机构CA，证书有效期，公钥，证书所有者， 签名等信息）
3. 客户端读取证书的所有者，有效期，签名等进行验证
4. 客户端获取操作系统中内置的受信任的证书机构（CA），与收到的证书对比，校验证书真实性
5. 找不到证书报错，给出不安全提示
6. 找到证书，用本地CA的公钥对收到的证书的签名解密
7. 客户端用相同的hash算法计算收到证书的hash，与收到的证书中的hash对比

## 参考

![mozilla. HTTP 基础](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP)