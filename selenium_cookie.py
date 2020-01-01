

def cookie_use(cookie):
    cookies = '; '.join(item for item in [item["name"] + "=" + item["value"] for item in cookie])
    return cookies



def cooie_super(cookieh):  # 传入selenium get_cookies()获取的值后，函数返回的值可以直接给requests使用。
    cookies = {}
    # 获取cookie中的name和value,转化成requests可以使用的形式
    for cookie in cookieh:
        cookies[cookie['name']] = cookie['value']
    return cookies