from urllib.request import urlopen, Request


def get_one_page(index):
    url = 'http://maoyan.com/board/4?offset={}'.format(index * 10)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Cookie': '__mta=49772185.1609052065037.1609052489289.1609052526863.11; uuid_n_v=v1; uuid=5A219900481011EB82084F456C94A28EA6941CCD72044C/'
                  'FA946DFA10CD8FBF2B; _csrf=636f654f158aed7d53a7db9c7bca9a42851b626961ebc141c43ad15d90187c97; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1608460926,/'
                  '1608461081,1608820275,1609052065; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1762d363da3c8-0b38bbfee66fbe-c791039-144000-1762d363da3bd;/'
                  ' _lxsdk=5A219900481011EB82084F456C94A28EA6941CCD72044CFA946DFA10CD8FBF2B; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; __mta=49772185.1609052065037.1609052065037/'
                  '.1609052068641.2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1609052527; _lxsdk_s=176a2fa0c00-707-980-e01%7C%7C24'
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read().decode('utf-8')


if __name__ == '__main__':
    print(get_one_page(0))

