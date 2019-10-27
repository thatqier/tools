from flask import Flask, request
import requests
import datetime
import logging
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def xray_webhook():
    vuln = request.json
    #vuln = json.loads(vuln, strict=False)
    content = """
    ## xray 发现了新漏洞

    url: {url}
    
    插件: {plugin}
    
    漏洞类型: {vuln_class}
    
    发现时间: {create_time}
    
    请及时查看和处理
    """.format(url=vuln["target"]["url"], plugin=vuln["plugin"],
               vuln_class=vuln["vuln_class"] or "Default",
               create_time=str(datetime.datetime.fromtimestamp(vuln["create_time"] / 1000)))
    try:
        push_dingding_group(content)
    except Exception as e:
        logging.exception(e)
    return 'ok'


def push_dingding_group(content):
    headers = {"Content-Type": "application/json"}
    # 消息类型和数据格式参照钉钉开发文档
    data = {"msgtype": "markdown","markdown": {"title": "xray 发现了新漏洞"}}
    data['markdown']['text'] = content

    r = requests.post("your api", data=json.dumps(data), headers=headers)
    print(r.text)

if __name__ == '__main__':
    app.run()
