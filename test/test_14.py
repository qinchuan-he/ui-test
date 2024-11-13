

import requests



def test_delete():
    url = 'https://testapp.fir.ai/api/recycle/delete/'
    cookie = {'fir_session_id':'3P1MIsonKqdBle5bzVXfCraGT2m7v6Sj'}
    date_s = {'src_list':'[{"id":140684,"type":"info"}]'}

    result = requests.post(url=url,data=date_s,cookies=cookie)
    print(result.text)

    print("---")


def ac():
    url = "https://2023.ip138.com/"

    payload = ""
    headers = {
        'User-Agent': "PostmanRuntime/7.11.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "55e7be78-cf66-4180-990f-d34b60ad2805,5232b4fd-a299-4eca-b0b0-28c711211734",
        'Host': "2023.ip138.com",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, data=payload, headers=headers)
    ip = response.text.split('<title>',2)[1].split('</title>',2)[0]
    print(ip)



if  __name__=="__main__":
    # test_delete()
    ac()




