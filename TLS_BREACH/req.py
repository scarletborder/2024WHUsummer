import requests
import json
import aiohttp

URL = "http://10.201.133.248/api/app/sendMsg"


def Request(msg) -> tuple[bool, str]:

    payload = '{"login":"20223021000","message":"' + str(msg) + '","courseType":"TLS"}'

    headers = {
        "Content-Type": "application/json",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,zh-HK;q=0.4",
        "Content-Type": "application/json",
        "Cookie": "pass-admin=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMDIiLCJpYXQiOjE3MjExNzkzMjAsImV4cCI6MTcyMTc4NDEyMH0.APQWvq8DHeX7MjLqiNWqrP0ZC-rXvridz-sxrJFQrWGzJQ_Xn4WV4yvfULl8QjFHj6OVR6HYwLLQKnFjCEavqg",
        "Origin": "http://10.201.132.132",
        "Pragma": "no-cache",
        "Referer": "http://10.201.132.132/welcome/studentAns?topic=TLS&num=1",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMDIiLCJpYXQiOjE3MjExNzkzMjAsImV4cCI6MTcyMTc4NDEyMH0.APQWvq8DHeX7MjLqiNWqrP0ZC-rXvridz-sxrJFQrWGzJQ_Xn4WV4yvfULl8QjFHj6OVR6HYwLLQKnFjCEavqg",
    }

    response = requests.request("POST", URL, headers=headers, data=payload)

    resp: dict = json.loads(response.text)
    retmsg: str = resp.get("msg", "：nocontent")
    all = retmsg.split("：")

    return (
        resp.get("code") == "200" and all[-1] != "请输入符合16进制标准待加密数据！",
        all[-1],
    )


# print(Request("1234"))
# print(Request("2248"))
# print(Request("akfk"))


async def ARequest(msg) -> tuple[bool, str]:
    payload = json.dumps(
        {"login": "20223021000", "message": str(msg), "courseType": "TLS"}
    )

    headers = {
        "Content-Type": "application/json",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,zh-HK;q=0.4",
        "Cookie": "pass-admin=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMDIiLCJpYXQiOjE3MjExOTY0MzYsImV4cCI6MTcyMTgwMTIzNn0.QFWdVnYcJzHIuH74sgmqiGPOGEI66FmzbXWhs8ZmRpxIzDVybdQ1nGvl30YOEJ4kumLDY1_wc0gXRNy_OUiE5g",
        "Origin": "http://10.201.133.248",
        "Pragma": "no-cache",
        "Referer": "http://10.201.133.248/welcome/studentAns?topic=TLS&num=1",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMDIiLCJpYXQiOjE3MjExOTY0MzYsImV4cCI6MTcyMTgwMTIzNn0.QFWdVnYcJzHIuH74sgmqiGPOGEI66FmzbXWhs8ZmRpxIzDVybdQ1nGvl30YOEJ4kumLDY1_wc0gXRNy_OUiE5g",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(URL, headers=headers, data=payload) as response:
            resp = await response.json()
            retmsg = resp.get("msg", "：nocontent")
            all = retmsg.split("：")

            return (
                resp.get("code") == "200"
                and all[-1] != "请输入符合16进制标准待加密数据！",
                all[-1],
            )
