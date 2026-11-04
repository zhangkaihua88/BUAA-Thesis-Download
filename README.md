# 北航学位论文下载工具
<p align="center">
  <a href="https://github.com/zhangkaihua88" alt="开发者">
    <img src="https://img.shields.io/badge/开发者-幻华-blue?logo=github">
  </a>
  <a href="https://github.com/zhangkaihua88/BUAA-Thesis-Download/" alt="version">
    <img src="https://img.shields.io/github/v/release/zhangkaihua88/BUAA-Thesis-Download?label=ver.">
  </a>
  <a href="https://github.com/zhangkaihua88/BUAA-Thesis-Download/" alt="使用人数">
    <img src="https://img.shields.io/github/downloads/zhangkaihua88/BUAA-Thesis-Download/total?color=success">

  </a>
</p>

## 用途
本工具可以：
1. 下载[北京航空航天大学](https://paper.lib.buaa.edu.cn/index.action)学位论文库中可查看的论文。
2. 调整论文清晰度。

本工具不能：
1. 下载未公开的论文。
2. 为无访问权限的用户提供权限。
3. 将论文转化为可选中/编辑的格式。


**[北京航空航天大学](https://paper.lib.buaa.edu.cn/index.action)学位论文库在校园网环境下, 只可预览前16页**

**如果您需要查看全文, 请使用[校内图书馆的指定终端](https://paper.lib.buaa.edu.cn/newlist.action?encid=37)**

**本脚本仅作为学术工具使用, 下载的文件如果泄露, 可能会被追究法律责任, 本人不承担使用此脚本的一切后果.**

## 使用方法
### 软件版
1. 下载打包后的[软件](https://github.com/zhangkaihua88/BUAA-Thesis-Download/releases/download/0.1.0/BUAAThesisDowload.zip)
2. 从所需要下载的论文的详情页复制关键信息
   - `fid`: 论文的id，从浏览论文的网址中可以找到, 例如`https://copyright.lib.buaa.edu.cn/pdfindex.jsp?fid=ee8eb9b94f66990ace67414e01b5ea8c`中的`123456`
   - `cookie`: 从浏览器中复制cookie，点击F12, 进入网络控制台, 获取网页Cookie, 例如`Hm_lvt_xxx=xxx,xxx; _ga=GA1.3.xxx.xxx; UM_distinctid=xxx-xxx-xxx-xxx-xx; JSESSIONID=xxx`
   - `name`: 为输出pdf的名字
   - `max_pages`: 为论文的总页数
   - `scale`: 为清晰度, 原始预览清晰度为`2`, 为了提高清晰度, 可以设置为`5`或`10`, 但是会导致下载速度变慢, pdf文件增大
3. 点击下载(校内终端快速传递文件可以使用[北航云盘](https://bhpan.buaa.edu.cn/#/))
### 插件版
1. 安装[Tampermonkey](https://www.tampermonkey.net/index.php?ext=dhdg), [Tampermokey使用教程](https://zhuanlan.zhihu.com/p/128453110)
2. 安装此[脚本](https://greasyfork.org/zh-CN/scripts/457168-buaa-thesis-download).
3. 打开某篇论文在线阅读, 在左侧列表可以调整清晰度, 下载文件, 根据需要点击即可. （由于域名更新了，脚本目前测试是没法使用的，请参考greasyfork中的反馈中的代码自行更新脚本代码）
### 直接粘贴js代码到地址栏
1. 打开论文详览页，进入全文阅读页：`/read/pdfindex1.jsp?fid=...`
2. 打开 `BUAA-Thesis-Download.bookmarklet.txt` 文件，复制全部内容。
3. 粘贴到浏览器地址栏并回车。若浏览器删除了 javascript:，先手动输入 javascript:，再粘贴后面的内容。
4. 脚本会自动读取页面、下载图片并保存 PDF。
脚本默认使用 2f 清晰度；如需更高清，可在源码中将 DEFAULT_RESOLUTION = "2f" 改为 "3f" 或 "5f"。
**使用风险与责任提示：** 本工具通过读取论文阅读页面并抓取页面内容生成 PDF。使用前，请确认你有权访问、下载和处理相关内容，并遵守论文平台的使用规则、学校或单位的网络与信息安全规定，以及适用的著作权、保密等法律法规。未经授权抓取、保存、传播或以其他不当方式使用内容，可能导致账号或访问权限受限、违反学校或单位规定，或引发版权、保密及其他法律争议；具体后果取决于实际行为和适用规定。请勿使用本工具绕过访问控制、批量获取或传播受限内容。本工具仅提供页面抓取技术，不代表相关内容已获授权，也不对具体使用方式的合法性作出判断；用户应自行评估并承担使用本工具及其获取内容所产生的风险和责任。
## 原理
- 脚本会首先请求所有pdf图片链接
- 随后请求图片，
- 最后调用 MuPDF 渲染 pdf 文件并导出

## 我想获得可编辑的文本, 怎么办？
- 如果为了获得整篇文章文本, 可以考虑使用 OCR 工具. 如Adobe Acrobat等进行扫描.
- 如果为了获得某一段落或部分文本, 考虑使用如`白描`, `Bob`, `天若`, `微信`等工具进行小段落内容识别。

## 更新日志
- 2022-10-28
  - 添加软件版(v0.1.0)
- 2022-12-26
  - 添加油猴插件版(v0.1.0)
## 参考
- [北大论文平台下载工具](https://github.com/xiaotianxt/PKU-Thesis-Download)