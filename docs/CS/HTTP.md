# HTTP协议详解



## HTTP的发展历史

### HTTP/0.9

- 通过TCP/IP（或者类似的面向连接的服务）与服务器和端口（可选，默认80）建立连接；
- 客户端发送一行ASCII文本，包括GET、文档地址（无空格）、回车符（可选）和换行符；
- 服务端使用HTML格式的消息响应，该消息被定义为“ASCII字符的字节流”；
- 通过服务器关闭连接来终止消息；
- 错误响应以可读的文本显示，使用HTML语法，除了文本内容，无法区分错误响应和正确响应；
- 请求时幂等的；
- 服务器不需要在断开连接之后存储任何请求的信息；

### HTTP/1.0

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

### HTTP/1.1

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