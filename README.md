# BUAA-Thesis-Download
## 用途
本工具可以：
1. 下载[北京航空航天大学](https://paper.lib.buaa.edu.cn/index.action)学位论文库中可查看的论文。
2. 调整论文清晰度。

本工具不能：
1. 下载未公开的论文。
2. 为无访问权限的用户提供权限。
3. 将论文转化为可选中/编辑的格式。

**本脚本仅作为学术工具使用，下载的文件如果泄露，可能会被追究法律责任，本人不承担使用此脚本的一切后果。**

## 使用方法
1. 下载打包后的软件
2. 从所需要下载的论文的详情页复制关键信息
   - `fid`: 论文的id，从浏览论文的网址中可以找到, 例如`https://copyright.lib.buaa.edu.cn/pdfindex.jsp?fid=ee8eb9b94f66990ace67414e01b5ea8c`中的`123456`
   - `cookie`: 从浏览器中复制cookie，点击F12, 进入网络控制台, 获取网页Cookie, 例如`Hm_lvt_xxx=xxx,xxx; _ga=GA1.3.xxx.xxx; UM_distinctid=xxx-xxx-xxx-xxx-xx; JSESSIONID=xxx`
   - `name`: 为输出pdf的名字
   - `max_pages`: 为论文的总页数
   - `scale`: 为清晰度, 原始预览清晰度为`2`, 为了提高清晰度, 可以设置为`5`或`10`, 但是会导致下载速度变慢, pdf文件增大

## 原理
- 脚本会首先请求所有pdf图片链接
- 随后请求图片，
- 最后调用 MuPDF 渲染 pdf 文件并导出

## 我想获得可编辑的文本，怎么办？
- 如果为了获得整篇文章文本, 可以考虑使用 OCR 工具. 如Adobe Acrobat等进行扫描.
- 如果为了获得某一段落或部分文本, 考虑使用如`白描`, `Bob`, `天若`, `微信`等工具进行小段落内容识别。

## 参考
- [北大论文平台下载工具](https://github.com/xiaotianxt/PKU-Thesis-Download)