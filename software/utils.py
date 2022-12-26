import requests
import json
import copy
import os
import fitz


def get_page(page, fid, cookie, name, scale, output_path):
    header = {
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,sq;q=0.7",
        'connection': "keep-alive",
        'cookie': cookie,
        'host': "copyright.lib.buaa.edu.cn",
        'referer': f"https://copyright.lib.buaa.edu.cn/pdfindex.jsp?fid={fid}",
        'sec-ch-ua': "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Windows\"",
        'sec-fetch-site': "same-origin",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
    }
    jump_headers = copy.deepcopy(header)
    jump_headers.update({
        'accept': "*/*",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
    })

    page_headers = copy.deepcopy(header)
    page_headers.update({
        'accept': "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        'sec-fetch-dest': "image",
        'sec-fetch-mode': "no-cors",
    })

    jumpServlet_url = f"https://copyright.lib.buaa.edu.cn/jumpServlet?page={page}&fid={fid}"

    response = requests.get(jumpServlet_url, headers=jump_headers).text

    response = json.loads(response)["list"]
    for item in response:
        if item["id"] == str(page):
            page_url = item["src"]
    page_url = page_url.split("scale")[0]
    page_url = f"{page_url}scale={scale}f"

    response = requests.get(page_url, headers=page_headers)
    with open(os.path.join(output_path, f"{name}_{page}.jpg"), "wb") as f:
        f.write(response.content)


# [get_page(item) for item in tqdm(range(MAX_PAGE))]

def pic2pdf(name, output_path):
    print(f"正在合成{name}的pdf")
    img_list = [item_path for item_path in os.listdir(output_path) if name in item_path]
    img_list.sort(key = lambda x: int(x.split("_")[-1].split(".")[0])) ##文件名按数字排序

    # print(img_list)
    doc = fitz.open()
    for img in img_list:  # 读取图片，确保按文件名排序
        imgdoc = fitz.open(os.path.join(output_path, img))                 # 打开图片
        pdfbytes = imgdoc.convert_to_pdf()        # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insert_pdf(imgpdf)                   # 将当前页插入文档
        os.remove(os.path.join(output_path, img))
    if os.path.exists(f"{name}.pdf"):
        os.remove(f"{name}.pdf")
    doc.save(f"{name}.pdf")                   # 保存pdf文件
    doc.close()


# if __name__ == '__main__':
#     pic2pdf("abcd", "output/")