from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import requests
from bs4 import BeautifulSoup
from time import sleep
from PIL import Image
import io
import urllib.request
import random
import configparser
import hashlib
import re
import getpass

# FireFox起動
options = Options()
options.add_argument('--headless')
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
#,chrome_options=options
browser = webdriver.Chrome(executable_path="./chromedriver.exe",chrome_options=options)
#browser.implicitly_wait(3)

#defシリーズ
def MJM(ID,PASS,Play):
    i = browser.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input')
    i.send_keys(ID)
    pas = browser.find_element_by_xpath('//*[@id="loginForm"]/div[4]/input')
    pas.send_keys(PASS)
    if Play == "0":
        elem = browser.find_element_by_xpath('//*[@id="ios"]')
        browser.execute_script("arguments[0].click();", elem)
    elif Play == "1":
        elem = browser.find_element_by_xpath('//*[@id="pc"]')
        browser.execute_script("arguments[0].click();", elem)
    login = browser.find_element_by_xpath('//*[@id="login"]')
    login.click()
    sleep(1)
    try:
        BeautifulSoup(browser.page_source,'html.parser')
        return(BeautifulSoup(browser.page_source,'html.parser'))
    except:
        return('NOLOGIN')
def SEGA(ID,PASS,Ga,Play):
    i = browser.find_element_by_xpath('//*[@id="segaidLoginForm"]/div[2]/input')
    i.send_keys(ID)
    pas = browser.find_element_by_xpath('//*[@id="segaidLoginForm"]/div[4]/input')
    pas.send_keys(PASS)
    g = browser.find_element_by_xpath('//*[@id="option_tag"]/div[3]/input')
    g.send_keys(Ga)
    if Play == "0":
        elem = browser.find_element_by_xpath('//*[@id="ios"]')
        browser.execute_script("arguments[0].click();", elem)
    elif Play == "1":
        elem = browser.find_element_by_xpath('//*[@id="pc"]')
        browser.execute_script("arguments[0].click();", elem)
    login = browser.find_element_by_xpath('//*[@id="segaid_login"]')
    login.click()
    sleep(1)
    try:
        BeautifulSoup(browser.page_source,'html.parser')
        return(BeautifulSoup(browser.page_source,'html.parser'))
    except:
        return('NOLOGIN')
def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)
def History():
    t =""
    A = []
    browser.find_element_by_xpath('//*[@id="v2-contents"]/div/div/div[2]/a[5]').click()
    sleep(0.1)
    soup = BeautifulSoup(browser.page_source,'html.parser')
    a = soup.find_all(class_ = "article")
    for a in a:
        i = a.get("href")
        if type(i) == type(t):
            A.append("https://pl.sega-mj.com"+i)
    return(A)
def ANGOUKA(ID,PASS,W,P):
    config = configparser.ConfigParser()
    A = []
    A_P = []
    All = ""
    All_P = "" 
    koukai = ""
    koukai_P = ""
    AND  = ""
    AND_P = ""
    XOR = ""
    XOR_P= ""
    H = ""
    H_P = ""
    for i in ID:
        #print(ord(i))
        num = ord(i)
        two = format(num,'b')
        #print(two)
        A.append(len(str(two)))
        All = All + str(two)
    for i in PASS:
        #print(ord(i))
        num = ord(i)
        two = format(num,'b')
        #print(two)
        A_P.append(len(str(two)))
        All_P = All_P + str(two)
    #print(A)
    #print("h",All)
    #print(int(All,2))
    for i in range(len(All)):
        a = random.randint(0,1)
        koukai = koukai + str(a)
    for i in range(len(All_P)):
        a = random.randint(0,1)
        koukai_P = koukai_P + str(a)
    #print("k",koukai)
    #print(int(koukai,2))
    #print(bin(int(All,2)& int(koukai,2)))
    for i in range(len(koukai)):
        if All[i] == koukai[i]:
            a = "0"
        else:
            a = "1"
        XOR = XOR + a
    for i in range(len(koukai_P)):
        if All_P[i] == koukai_P[i]:
            a = "0"
        else:
            a = "1"
        XOR_P = XOR_P + a
    #print("X",XOR)
    #print(int(XOR,2))
    config['CONFIG'] = {
        'W':W,
        'P':P}
    config['IDS'] = {
        'lists': A,
        'K': koukai,
        'X': XOR}
    config['PASSS'] = {
        'lists':A_P,
        'K': koukai_P,
        'X': XOR_P}
        
    with open('temporary.ini','w') as config_file:
        config.write(config_file)
    return("保存が完了しました！")
def HUKUGOU():
    config = configparser.ConfigParser()
    config.read('temporary.ini')
    A = config['IDS']['lists']
    koukai = config['IDS']['k']
    XOR = config['IDS']['x']
    A_P = config['PASSS']['lists']
    koukai_P = config['PASSS']['k']
    XOR_P = config['PASSS']['x']
    H = ""
    H_P = ""
    x = 0
    c = 0
    CUL = ""
    CUL_P = ""
    J = []
    J_P = []
    K = []
    K_P = [] 
    ID = ""
    PASS = ""
    A = A.replace("[","").replace("]","").replace(" ","")
    A = A.split(",")
    A_P = A_P.replace("[","").replace("]","").replace(" ","")
    A_P = A_P.split(",")
    for i in range(len(koukai)):
        if XOR[i] == koukai[i]:
            a = "0"
        else:
            a = "1"
        H = H + a
    for i in range(len(koukai_P)):
        if XOR_P[i] == koukai_P[i]:
            a = "0"
        else:
            a = "1"
        H_P = H_P + a
    for i in range(len(koukai)):
        c = c + 1
        CUL = CUL + str(H[i])
        if A[x] == str(c):
            c = 0
            x = (x + 1)%len(A)
            J.append("0b"+CUL)
            CUL = ""
    c = 0
    for i in range(len(koukai_P)):
        c = c + 1
        CUL_P = CUL_P + str(H_P[i])
        if A_P[x] == str(c):
            c = 0
            x = (x + 1)%len(A_P)
            J_P.append("0b"+CUL_P)
            CUL_P = ""
    for i in J:
        K.append(eval(i))
    for i in J_P:
        K_P.append(eval(i))
    for i in K:
        ID  = ID + chr(int(i))
    for i in K_P:
        PASS  = PASS + chr(int(i))

        
    return(ID,PASS)
def URLS(A,shI):
    U = []
    DATE = []
    FL = False
    Sub = []
    config = configparser.ConfigParser()
    config.read('final_date.ini')
    for i in A:
        browser.get(i)
        soup = BeautifulSoup(browser.page_source,'html.parser')
        a = soup.find_all(class_ = "article")
        date = soup.find(class_="date").string
        date = date.strip()
        try:
            AA = config[shI]['final_date']
            FL = True
            A = re.sub(r'\D', '',AA)
            B = re.sub(r'\D', '',date)
            print(A)
            print(B)
            if A < B:
                for a in a:
                    sleep(0.1)
                    u = a.get("href")
                    url= "https://pl.sega-mj.com"+u
                    browser.get(url)
                    browser.find_element_by_xpath('//*[@id="v2-contents"]/div/div/div[3]/div[1]/div[4]/a').click()
                    el = browser.find_element_by_xpath('//*[@id="replay_url"]')
                    U.append(el.text)
                    DATE.append(date)
                    

                #DATE.append(config[shI]['final_date'])
        except:
            for a in a:
                sleep(0.1)
                u = a.get("href")
                url= "https://pl.sega-mj.com"+u
                browser.get(url)
                browser.find_element_by_xpath('//*[@id="v2-contents"]/div/div/div[3]/div[1]/div[4]/a').click()
                el = browser.find_element_by_xpath('//*[@id="replay_url"]')
                U.append(el.text)
                DATE.append(date)
    
    
    write = configparser.ConfigParser()
    if len(DATE) > 0:
        d = DATE[0]
    elif FL == True:
        d = AA
    else:
        d = "0"
        
    try:
        config[shI]
        #print("見つけた")
        for i in config.sections():
            for key in config[i]:
                config[i] = {
                    key:config[i][key]}
        config[shI] = {
            'final_date':d}
        with open('final_date.ini','w') as config_file:
            config.write(config_file)
    except:
        #print("なかった")
        write[shI] = {
            'final_date':d}
        with open('final_date.ini','a') as config_file:
            write.write(config_file)
    return([U,DATE])

    

def LOOP(shI):
    o = ""
    F = False
    URL = ""
    U = []
    DATE = []
    config = configparser.ConfigParser()
    config.read('final_date.ini')
    date = config[shI]['final_date']
    config.read('config.ini')
    sec = config['LOOP']['sec']
    if sec.isnumeric():
        sec = int(sec)
        sleep(sec)
        print("定期実行")
        print("--")
        soup = BeautifulSoup(browser.page_source,'html.parser')
        a = soup.find_all(class_="article")
        if len(a) > 0: 
            print("[+]ページ読み込み開始")
            for i in a:
                if type(i.get("href")) == type(o):
                    a = i.find(class_="date").string
                    a = a.strip()
                    URL = "https://pl.sega-mj.com"+i.get("href")
                    break
            #a = soup.find(class_="article").find(class_="date").string
            print("[+]更新チェック開始")
            print(re.sub(r'\D', '',a))
            print(re.sub(r'\D', '',date))
            if re.sub(r'\D', '',a) > re.sub(r'\D', '',date):
                print("更新があります")
                browser.get(URL)
                soup = BeautifulSoup(browser.page_source,'html.parser')
                config = configparser.ConfigParser()
                config.read('final_date.ini')
                a = soup.find_all(class_ = "article")
                date = soup.find(class_="date").string
                date = date.strip()
                for a in a:
                        sleep(0.1)
                        u = a.get("href")
                        url= "https://pl.sega-mj.com"+u
                        browser.get(url)
                        browser.find_element_by_xpath('//*[@id="v2-contents"]/div/div/div[3]/div[1]/div[4]/a').click()
                        el = browser.find_element_by_xpath('//*[@id="replay_url"]')
                        U.append(el.text)
                        DATE.append(date)
                config[shI]
                d = DATE[0]
                for i in config.sections():
                    for key in config[i]:
                        config[i] = {
                            key:config[i][key]}
                config[shI] = {
                    'final_date':d}
                with open('final_date.ini','w') as config_file:
                    config.write(config_file)
                return([U,DATE])
            
            else:
                print("更新はありません")
                print(a)
                print(date)
        else:
            print("更新はありません")
                    
    else:
        print("config.iniのsecが数字ではありません！")
        print("動作を停止します")
        return("ERROR")

def MJ(U,DATE):
    url = ""
    date = ""
    url = U
    date = DATE
    print(url)
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.action_chains import ActionChains
    import os
    from time import sleep
    from bs4 import BeautifulSoup
    import re
    import csv
    import sys
    from PIL import Image,ImageDraw,ImageFont
    import math
    import configparser
    import qrcode
    import requests

    #tsumoは自分を0
    #sutehaiも同じ
    def CLICK():
        browser.find_element_by_xpath('//*[@id="v2-contents"]/div[1]/div[2]/div[2]').click()
        sleep(0.001)
        browser.find_element_by_xpath('//*[@id="v2-contents"]/div[1]/div[2]/div[1]').click()
        return(BeautifulSoup(browser.page_source,'html.parser'))
    options = Options()
    options.add_argument('--headless')
    #,chrome_options=options
    browser = webdriver.Chrome(executable_path="./chromedriver.exe",chrome_options=options)
    browser.set_window_size(657,657)
    browser.implicitly_wait(3)
    actions = ActionChains(browser)
    # 暗黙的な待機を最大3秒。ドライバの初期化待ち
    names = []
    points = []
    kazes = []
    jun = []
    kaze = ""
    hai=""
    haipai = []
    ki = []
    kaze0 =[]
    kaze1 =[]
    kaze2 =[]
    kaze3 =[]
    kazez =[kaze0,kaze1,kaze2,kaze3]
    naki=[]
    tsumo =[[],[],[],[]]
    who =[]
    what = []
    count = 0
    nakicount = [0,0,0,0]
    kan = [[],[]]
    flag = False
    tsumocount = []
    c = 1
    sainaki = [[],[],[],[]]
    A = 0
    cNull = 0
    tumonum = 1
    tumotumo = 0
    rr = [[],[]]
    flag1 = False
    sutecount=[]
    scount = 0
    sutehai = [[],[],[],[]]
    zure = [[],[]]
    nakinasi = []
    ff = False
    nam = 0
    nakinaki = [[],[],[]]
    agarimun = 0
    tensuu=[[],[]]
    AA = False
    furikomi = 0
    motiten =[[],[],[],[]]
    saisyuu = []
    tsumonaki = []
    tsumogiri = []
    kansute = [[],[]]
    AWA = []
    v = ""
    g = 0
    T = False
    TT =0
    r = 0
    reach = [[],[]]
    agariway = ""
    agariname= ""
    jBa = ""
    agari = False
    agarihai = ""
    kc = 0
    Nhonba = ""
    TSUMO = False
    RON = False
    STOPER = False
    agarihai = ""
    hurihuri = 0
    """
    while True:
        url = input("URLを入力してください:")
        if url.count("https://pl.sega-mj.com/mj_viewer?") == 0:
            print("[-]MJのURLを入力してください！")
        else:
            break
    """
    #url = "https://pl.sega-mj.com/mj_viewer?B=6000&K=12013&V=6&DI=FrMuMj3HV01NPb&T=820_184_46&SA=10&D=b&S=16&H=qkkbvh-caog9z_njtswni1xqp1x_mxjfldthwcc1g&A=1vziw1fzmjfjz9qwdll1ltrmkzb_yrjljzztdju_yxqRoh1a_e_n1vzd_P3ve_a_o_u_yhk_p_9_i_~0dUv&Y=11_0085120_30110010120m20d1bvdabcd-fghkkkqqi0&Z=awpbouimxlmovthfrpig9cryrgbvt9ue&N=%E3%81%8B%E3%81%9A%E3%82%8A%E3%82%85%E3%81%86_%E3%81%88%E3%81%8F%E3%81%99%E3%81%9F%E3%81%97%E3%83%BC_%E3%82%A2%E3%83%86%E3%83%8A"
    #url = "https://pl.sega-mj.com/mj_viewer?B=0002&K=11203&V=6&DI=FrMuMj3HV01NPb&T=350_350_350&SA=10&D=m&S=15&H=vfxa9jr1nwcfr_d1vtaulqewilp_lqqigkolhy9gd&A=z1x91vxwtxrwvxkygxjuct9nctris_y_orP0gez9_P0rhacRhjfw_j_P0fzjt_acuzw_u_vui_-_a_~04&Y=11_208d320_115000d1E1mh411aaa32123rrr21239992123jjj&Z=ikdnxfmghq1mpzbdboppuboykmtbnmhefyz&N=%E3%81%8B%E3%81%9A%E3%82%8A%E3%82%85%E3%81%86_%E3%81%88%E3%81%8F%E3%81%99%E3%81%9F%E3%81%97%E3%83%BC_%E3%82%A2%E3%83%86%E3%83%8A"
    #url = 'https://pl.sega-mj.com/mj_viewer?B=1003&K=10123&V=6&DI=FrMuMj3HV01NPb&T=680_30_340&SA=10&D=p&S=36&H=togrdyyxwhxnf_cvq-jmrlakuuj_1qoapwpc11xml&A=gxP0rdvuwewyaju9_lyP0tuli_t_z_ajzn9R_1A1DsLhcnzb_v_l_a_w_k_d_w_iny_iRp~2dUbUz&Y=11_228480_20110010130d2pbszdcd-jjklmqruuup0&Z=dvbvefrkgtfreogikxqmcbqf9nzotch9pszpbhjm&N=%E3%81%8B%E3%81%9A%E3%82%8A%E3%82%85%E3%81%86_%E3%81%88%E3%81%8F%E3%81%99%E3%81%9F%E3%81%97%E3%83%BC_%E3%82%A2%E3%83%86%E3%83%8A'
    #url = "https://pl.sega-mj.com/mj_viewer?B=2000&K=12013&V=6&DI=FrMuMj3HV01NPb&T=680_110_260&SA=10&D=t&S=33&H=ddajhti1iceaw_uxthcbokhlzlp_m-ivqg1u9zwmv&A=x1gxaqyj9_vmvxyznmj_uykn1wetzklypem_mtbcf1z_P39pvM3DeLbwa1nkbiP0pr_9_gmsRgx_q_w_dudlx_r_w_l_u_r_y_faj_q_9_p_o~2eUqUn&Y=11_1259160_40311010110420c50d2tqenebbhhllsnoppuuo00&Z=ihkofkjft1corentqcyg&N=%E3%81%8B%E3%81%9A%E3%82%8A%E3%82%85%E3%81%86_%E3%81%88%E3%81%8F%E3%81%99%E3%81%9F%E3%81%97%E3%83%BC_%E3%82%A2%E3%83%86%E3%83%8A"
    #url = "https://pl.sega-mj.com/mj_viewer?B=6000&K=12013&V=6&DI=FrMuMj3HV01NPb&T=820_184_46&SA=10&D=b&S=16&H=qkkbvh-caog9z_njtswni1xqp1x_mxjfldthwcc1g&A=1vziw1fzmjfjz9qwdll1ltrmkzb_yrjljzztdju_yxqRoh1a_e_n1vzd_P3ve_a_o_u_yhk_p_9_i_~0dUv&Y=11_0085120_30110010120m20d1bvdabcd-fghkkkqqi0&Z=awpbouimxlmovthfrpig9cryrgbvt9ue&N=%E3%81%8B%E3%81%9A%E3%82%8A%E3%82%85%E3%81%86_%E3%81%88%E3%81%8F%E3%81%99%E3%81%9F%E3%81%97%E3%83%BC_%E3%82%A2%E3%83%86%E3%83%8A"
    #url = "https://pl.sega-mj.com/mj_viewer?B=0003&K=01023&V=6&DI=OfEaMj3HV01NPb&T=350_350_350&SA=20&D=w&S=33&H=rfooc-qezmcad_vimmcv1u9rhrh_w9pkcqlyiyjuu&A=w9gzk9fcbRmg19_r_muP3ih_qra_1_nrb_q_jqg_o_dmz_a_lm9_1_hisfx_theqz_thb_d_pdl_p~0eUd&Y=11_106580_30111010110430d1wdeabccd-efgooqrp00&Z=zekxxpublwn1fyvygixitjaotkwdfjnv&N=%E3%81%8B%E3%81%9A%E3%82%8A%E3%82%85%E3%81%86_%E5%B0%8F%E8%B1%86%E6%B2%A2%E9%80%9A%E3%82%8A_%E3%81%8B%E3%81%8A%E3%82%8B"
    #url = "https://pl.sega-mj.com/mj_viewer?B=0002&K=11203&V=6&DI=FrMuMj3HV01NPb&T=350_350_350&SA=10&D=m&S=15&H=vfxa9jr1nwcfr_d1vtaulqewilp_lqqigkolhy9gd&A=z1x91vxwtxrwvxkygxjuct9nctris_y_orP0gez9_P0rhacRhjfw_j_P0fzjt_acuzw_u_vui_-_a_~04&Y=11_208d320_115000d1E1mh411aaa32123rrr21239992123jjj&Z=ikdnxfmghq1mpzbdboppuboykmtbnmhefyz&N=%E3%81%8B%E3%81%9A%E3%82%8A%E3%82%85%E3%81%86_%E3%81%88%E3%81%8F%E3%81%99%E3%81%9F%E3%81%97%E3%83%BC_%E3%82%A2%E3%83%86%E3%83%8A"
    #url = "https://pl.sega-mj.com/mj_viewer?B=4002&K=11203&V=6&DI=FrMuMj3HV01NPb&T=580_270_200&SA=10&D=m&S=21&H=9tfyuwzq1ahud_hmecwvykfbvi1_krjcypuvvlibo&A=g1nbeqr_tc-zq_fit1bw9fz_cyf9w9lvofj_z_9_j_u_qtyftvi_p_xta_i_o_gyhRdnxnga~0eUx&Y=11_205b240_60411010110310420c30d30v1mxea-ehhttuuwwyya00&Z=crw1blz1q9darljokmmgxpkephxmxsddg&N=%E3%81%8B%E3%81%9A%E3%82%8A%E3%82%85%E3%81%86_%E3%81%88%E3%81%8F%E3%81%99%E3%81%9F%E3%81%97%E3%83%BC_%E3%82%A2%E3%83%86%E3%83%8A"
    #date = "2018-09-13 18:19:57"
    browser.get(url)
    #a = browser.find_element_by_class_name("cName")

    a = browser.find_element_by_xpath('//*[@id="v2-contents"]/div[2]/textarea')
    URL = a
    soup = BeautifulSoup(browser.page_source,'html.parser')
    for i in range(4):
        j = "jKaze"+str(i)
        a = soup.find_all("div",attrs={"id":j})
        for k in a:
            if len(k["class"]) > 1:
                n = k["class"][1]
                if n == "Nan":
                    n = "南"
                elif n == "Sya":
                    n = "西"
                elif n == "Ton":
                    n = "東"
                elif n == "Pei":
                    n = "北"
                kazes.append(n)
            else:
                kazes.append("北")
    for i in range(0,4):
        point = "jTen"+str(i)
        a = browser.find_elements_by_id(point)
        for b in a:
            points.append(b.text)
    a = browser.find_elements_by_id("jBa")
    for a in a:
        #print(a.text)
        Ba = a.text
    a = browser.find_elements_by_id("jHonba")
    for a in a:
        #print(a.text)
        Nhonba = a.text
        Honba = a.text+"本場"
    a = browser.find_elements_by_id("jKyoutaku")
    for a in a:
        print(a.text)
        kyoutaku = "供託"+a.text+"点"
    ton = browser.find_element_by_xpath('//*[@class="cKaze Ton"]')
    for i in range(0,4):
        num = "jKaze"+str(i)
        para = browser.find_element_by_id(num)
        if ton == para:
            kaze = str(i)
            break
    for i in range(0,4):
        name = "jName"+str(i)
        a = browser.find_elements_by_id(name)
        for b in a:
            names.append(b.text)

    if names.count("") == 0:
        print("[+]東風")    
        san = False
    else:
        print("[+]サンマ")
        san = True
    print("[+]親の位置",kaze)
    """
    if kaze == "0":
        kazes = ["東","南","北","西"]
        jun = [0,1,2,3]
        ki = [1,2,3,4]
    elif kaze == "1":
        kazes = ["西","東","北","南"]
        jun = [3,0,1,2]
        ki = [4,1,2,3]
    elif kaze == "2":
        kazes = ["西","北","東","南"]
        jun = [2,3,0,1]
        ki = [3,4,1,2]
    elif kaze == "3":
        kazes = ["南","北","西","東"]
        jun = [1,2,3,0]
        ki = [2,3,4,1]
    """

    print(kazes)
        
    bar = browser.find_element_by_xpath('//*[@id="jSlider_Pinch"]')
    actions.click_and_hold(bar)
    actions.move_by_offset(400, 0)
    actions.perform()
    maxn = browser.find_element_by_id('jSlider_Counter')
    maxn = maxn.text
    actions.click_and_hold(bar)
    actions.move_by_offset(-400, 0)
    actions.perform()
    browser.execute_script('window.scrollTo(310,142)')

    """for a in kazes:
        print(a)
    for a in names:
        print(a)
    for a in points:
        print(a)"""
    """------------------------ここから---------------------------"""
    tsumos = [["" for i in range(2)] for j in range(int(maxn))]
    #配牌
    c = int(kaze)+1
    t = "jTehai"+str(kaze)+"_"+"13"
    n = "jTehai"+str((int(kaze)+1)%4)+"_"+"13"
    sss = "jTehai"+str((int(kaze)+2)%4)+"_"+"13"
    nn =(int(kaze)+1)%4
    sn= (int(kaze)+2)%4
    print("[+]maxn",maxn)
    print("[+]鳴きのチェック")
    for i in range(0,int(maxn)):
        #print("\r{0:d}".format(i), end="")
        #print("/",maxn, end="")
        """sys.stdout.write("\r{}".format(i))
        sys.stdout.flush()"""
        browser.find_element_by_xpath('//*[@id="v2-contents"]/div[1]/div[2]/div[2]').click()
        sleep(0.001)
        browser.find_element_by_xpath('//*[@id="v2-contents"]/div[1]/div[2]/div[1]').click()
        soup = BeautifulSoup(browser.page_source,'html.parser')
        a = soup.find_all(id="jVoice0")
        b = soup.find_all(id="jVoice1")
        c = soup.find_all(id="jVoice2")
        d = soup.find_all(id="jVoice3")
        tumo = soup.find_all("div",attrs={"class":"Tsumo"})
        for k in a:
            if k["class"][2] != "Null0":
                naki.append(i)
                y = k["id"]
                who.append(y[6])
                what.append(k["class"][2])
        for k in b:
            if k["class"][2] != "Null1":
                naki.append(i)
                y = k["id"]
                who.append(y[6])
                what.append(k["class"][2])
        for k in c:
            if k["class"][2] != "Null2":
                naki.append(i)
                y = k["id"]
                who.append(y[6])
                what.append(k["class"][2])
        for k in d:
            if k["class"][2] != "Null3":
                naki.append(i)
                y = k["id"]
                who.append(y[6])
                what.append(k["class"][2])
        for k in tumo:
            if k != "":
                p = k["id"]
                p = p[6]
                tsumocount.append([i,p])
    #for a in tsumocount:
    #    for i in range(0,2):
    #        print(a[i])

    print("naki",naki)
    print("what",what)
    print(kazes)
    pee = kazes.index("北")
    for a in tsumocount:
        sutecount.append(int(a[0])+1)
    #for i in sutecount:
    #    print(i)
    oya = int(kaze)
    #print(naki)
    for i in naki:
        sutecount.append(int(i)+1)
    for i in range(0,len(naki)):
        i = int(i)
        if what[i] == "Reach":
            w= int(naki[i])
            sutecount.remove(w)
            c = int(naki[i]+1)
            rr[0].append(c)
            c = int(naki[i]+1)
            sutecount.append(c)
            reach[0].append(naki[i]-1)
        elif what[i] == "Ron" or what[i] == "Tsumo" and agari == False:
            agari = True
            TT = who[i]
            w = int(naki[i]+1)
            reach[1].append(w)
            T = True
            LAST = int(naki[i]+2)
            w= int(naki[i])
            stop = w
            print("LAST",int(LAST))
            if what[i] == "Tsumo":
                TSUMO = True
                w = int(naki[i])
                sutecount.remove(w)
            elif what[i] == "Ron":
                RON = True
                hurihuri = int(naki[i])
        elif what[i] == "Kan":
            #print("a")
            
            try:
                c = int(naki[i]+1)
                sutecount.remove(c)
            except:
                pass
            try:
                c = int(naki[i])
                sutecount.remove(c)
            except:
                pass
            c = int(naki[i]+2)
            kan[0].append(c)
            kan[1].append(int(who[i]))
            c = int(naki[i]+1)
            kansute[0].append(c)
            kansute[1].append(int(who[i]))
            zure[0].append(int(who[i]))
            w = int(naki[i])+3
            zure[1].append(w)

        else:
            zure[0].append(who[i])
            c = int(naki[i]+1)
            zure[1].append(c)
    for i in range(0,len(naki)):
        i = int(i)
        if what[i] == "Pon":
            w = int(naki[i]+1)
            nakinaki[0].append(w)
            nakinaki[1].append("Pon")
            j = who[i]
            nakinaki[2].append(j)
        elif what[i] == "Kan":
            w = int(naki[i]+1)
            nakinaki[0].append(w)
            nakinaki[1].append("Kan")
            j = who[i]
            nakinaki[2].append(j)
        elif what[i] == "Chi":
            w = int(naki[i]+1)
            nakinaki[0].append(w)
            nakinaki[1].append("Chi")
            j = who[i]
            nakinaki[2].append(j)
    #print(nakinaki)
    tsumonaki = [[],nakinaki[2]]
    for o in nakinaki[0]:
        tsumonaki[0].append(o-2)
    print("--------------tsumonaki--------------------s")
    print(tsumonaki)
    print("------------kan---------------")
    print(kan)
    print("----------------kansute--------")
    print(kansute)
    print("sutecount",sutecount)
    if agari == True:
        for z in sutecount:
            if stop <= int(z):
                sutecount.remove(z)
    sutecount = list(set(sutecount))
    sutecount.sort()

    if agari == False:
        del sutecount[-1]
    else:
        jj = []
        for i in sutecount:
            if int(i) < int(LAST):
                jj.append(i)
        del sutecount[:]
        sutecount = jj
    sutecountf = [sutecount,[]]
    for a in zure[1]:
        nakinasi.append(int(a)-2)
    #print(zure)
    k = 0
    print("----------------zure----------")
    print(zure)
    #print("sutecountf",sutecountf)
    #print(zure[1])

    for i in range(0,len(sutecount)):
        #print(sutecountf[0][i])
        if len(zure[0]) > 0 and sutecountf[0][i] == int(zure[1][k]):
            sutecountf[1].append(zure[0][k])
            k = (k+1)%len(zure[0])
        else:
            if len(sutecountf[1]) == 0:
                sutecountf[1].append(kaze)
            else:
                if san == True:
                    if str((int(sutecountf[1][-1])+1)%4) == str(pee):
                        w = (int(pee)+1)%4
                        sutecountf[1].append(w)
                    else:
                        to = sutecountf[1][-1]
                        too = (int(to)+1)%4
                        sutecountf[1].append(too)
                else:
                    to = sutecountf[1][-1]
                    too = (int(to)+1)%4
                    sutecountf[1].append(too)
    print("sutecountf",sutecountf)
    print("-----------------naiknaki--------------------")
    print(nakinaki)

                




    print("[+]鳴きのチェック完了")
    print("[+]初期化中")
    bar = browser.find_element_by_xpath('//*[@id="jSlider_Pinch"]')
    actions.click_and_hold(bar)
    actions.move_by_offset(-400, 0)
    actions.perform()
    print("[+]初期化完了")
    kazu = len(naki)-1
    sutec = int(kaze)
    sutec = (sutec + 1)%4
    k = 0
    y = 0
    nakiyou = ""
    l = 0
    KANSUTE = 0
    for i in range(0,int(maxn)):
        #print("\r{0:d}".format(i), end="")
        #print("/",maxn, end="")
        print(i)
        soup = CLICK()
        STOPER == False
            
        
        if i == 0:
            a = soup.find_all(id=re.compile("jTen"),limit=4)
            for a in a:
                num = int(a["id"][-1])
                motiten[num].append(a.string)
            for m in range(0,4):
            #a = soup.select('#v2-contents > div.viewerImage > div.cWrap > div > div.cTehai.PL2')
                m = str(m)
                s = "jTehai"+m+"_"
                a = soup.find_all(id=re.compile(s))
                for b in a:
                    if b["class"][1] != "Null":
                        hai = hai+b["class"][1]+","
                hai = hai[:-1]
                haipai.append(hai)
                hai = ""
            a = soup.find_all("div",attrs={"class":"Tsumo"},limit=1)
        
            for c in a:
                mum = c["id"]
                aid = mum[6]
                hai = c["class"][1]
                tsumos[i][0] = aid
                tsumos[i][1] = hai
                #print(aid)
                #print(hai)
                if len(kan[0]) > 0:
                    if len(kan[0]) == 1:
                        if i == kan[0][0]:
                            hai = hai+"K"
                    else:
                        if i == kan[0][kc]:
                            hai = hai + "K"
                            kc = (kc+1)%len(kan[0])
                tsumo[int(aid)].append(hai)
            #haipai.append(hai)

        else:
            tumotumo = int(tumotumo)
            tcount = tsumocount[tumotumo]
            k = int(k)
            #サンマ用
            #if flag == False and naki[count] == int(i):
            if len(kan[0]) > 0:
                if kan[0][l] == i:
                    print(i)
                    if len(kan[0]) != 1:
                        l = (l+1)%len(kan[0])
                    a = soup.find_all("div",attrs={"class":"Tsumo"})
                    STOPER = True
                    for c in a:
                        mum = c["id"]
                        aid = mum[6]
                        hai = c["class"][1]
                        tsumos[i][0] = aid
                        tsumos[i][1] = hai
                        #print(aid)
                        #print(hai)
                        #print(hai,aid)
                        if i not in reach[0]:
                            tsumo[int(aid)].append(hai)
            if len(kansute[0]) > 0:
                if kansute[0][KANSUTE] == i:
                    sutehai[kansute[1][KANSUTE]].append("Kan")
                    if len(kansute[0]) != 1:
                        KANSUTE = (KANSUTE+1)%len(kansute[0])
                    STOPER = True

            if sutecountf[0][k] == i:
                ai = "jSutehai"+str(sutecountf[1][k])+"_"
                a = soup.find_all(id=re.compile(ai))
                sutec = sutecountf[1][k]
                sutec = int(sutec)
                #print(i)
                #print(nakinasi[nam])
                
                if ff == False:

                    for h in a:
                    

                        if h["class"][1] != "Null":
                            if i not in nakinaki[0]:
                                
                                if "Tsumogiri" in h["class"]:
                                    sute = h["class"][1]
                                    nakiyou = h["class"][1]
                                    A = i
                                else:
                                    A = 1
                                    sute = h["class"][1]
                                    nakiyou = h["class"][1]
                            else:
                                n = nakinaki[0].index(i)
                                a = nakinaki[1][n]
                                apn = a[0]
                                if apn == "P":
                                    apn = "N"
                                sute = h["class"][1] + apn
                                nakiyou = h["class"][1]
                            
                        else:
                            ff = True
                if agari == True and RON == True:
                    if sute != "":
                        SUMO = sute
                if i in rr[0]:
                    sute = sute + "R"
                
                #print(sute,sutec)
                ff = False
                if len(tsumonaki[0]) > 0 and tsumonaki[0][y] == i:
                    mm = ""
                    mm = nakinaki[1][y]
                    emu = mm[0]
                    if emu == "P":
                        emu = "N"
                    print(emu)
                    tsumo[int(tsumonaki[1][y])].append(nakiyou+emu)
                    y = (y+1)%len(tsumonaki[0])
                    
                #sutehai[int(c)].append(sute)
                #k = a[-1]
                #k = k["class"][1]
                if i not in reach[1]:
                    sutehai[sutec].append(sute)
                    print(" ",sute)
                    
                tsumogiri.append(A-1)
                k = (k + 1)%len(sutecountf[1])
                A = 1
                sute = ""
                tg = [x for x in tsumogiri if x != 0]
                

                
            elif i == int(maxn)-1:
                #ふぁいなる
                a = soup.find_all(class_="cAgariPlyName")
                furikomi = sutecountf[1][-2]
                for k in a:
                    o = k.string
                    o = o.split(None)
                    agariway = o[0]
                    agariname = o[1]
                    agarinum = k["id"][-1]
                a = soup.find_all(class_="cTensuu")
                for k in a:
                    if len(rr[0]) > 0:
                        tenbou = k.span.string
                        print("tenbou",tenbou)
                    tensuu = k.string
                    
                    print("tensuu",tensuu)

                for k in range(0,4):
                    #m = str(jun[k])
                    m = str(k)
                    a = "jTehai"+m+"_"
                    b = soup.find_all(id=re.compile(a))
                    for n in b:
                        if n["class"][1] == "Null":
                            continue
                        else:
                            v = v+n["class"][1]+","
                    
                    if nakinaki[2].count(m) > 0:
                        #あったとき
                        a = nakinaki[2].count(m)
                        for q in range(0,a):
                            b = "jNakihai"+m+"_"+str(q)+"_"
                            b = soup.find_all(id=re.compile(b))
                            for z in b:
                                print(z["class"])
                                print(v)
                                if z["id"][-1] == "3" and len(z["class"]) > 1:
                                    print("append","4")
                                    sainaki[int(m)].append(4)
                                if len(z["class"]) < 2:
                                    if z["id"][-1] == "3" and len(z["class"]) == 1:
                                        print("append","3")
                                        sainaki[int(m)].append(3)
                                        #cNull = 0
                                
                                        #continue
                                elif len(z["class"]) > 2 and z["class"][2] == "Yoko":
                                    #cNull = cNull + 1
                                    v = v+z["class"][1]+"N"+"Y"+","

                                elif "URA" in z["class"]:
                                    v = v+z["class"][1]+"N"+"U"+","
                                    print("URAAAAAAAAAAAAAA")
                                    
                                
                                
                                    #cNull = cNull + 1
                                else:
                                    
                                    #cNull = cNull + 1
                                    v = v+z["class"][1]+"N"+","
                        v = v[:-1]
                        saisyuu.append(v)
                        v = ""
                    else:
                        v = v[:-1]
                        saisyuu.append(v)
                        v = ""
                """
            elif len(kan[0]) > 0:
                print("kan")
                if kan[0][l] == i:
                    if len(kan[0]) != 1:
                        l = (l+1)%len(kan[0])
                    browser.find_element_by_xpath('//*[@id="v2-contents"]/div[1]/div[2]/div[2]').click()
                    sleep(0.001)
                    browser.find_element_by_xpath('//*[@id="v2-contents"]/div[1]/div[2]/div[1]').click()
                    soup = BeautifulSoup(browser.page_source,'html.parser')
                    
                    a = soup.find_all("div",attrs={"class":"Tsumo"})
                    
                    for c in a:
                        mum = c["id"]
                        aid = mum[6]
                        hai = c["class"][1]
                        tsumos[i][0] = aid
                        tsumos[i][1] = hai
                        #print(aid)
                        #print(hai)
                        if i not in reach[0]:
                            tsumo[int(aid)].append(hai)
                """
            
            else:
                if san == True:
                
                    a = soup.find_all("div",attrs={"class":"Tsumo"},limit=1)
                
                    for c in a:
                        mum = c["id"]
                        aid = mum[6]
                        hai = c["class"][1]
                        tsumos[i][0] = aid
                        tsumos[i][1] = hai
                        #print(aid)
                        #print(hai)
                        if len(kan[0]) > 0:
                            if len(kan[0]) == 1:
                                if i == kan[0][0]:
                                    y = (y+1)%len(tsumonaki[0])
                                    hai = hai+"K"
                            else:
                                if i == kan[0][kc]:
                                    hai = hai + "K"
                                    kc = (kc+1)%len(kan[0])
                                    y = (y+1)%len(tsumonaki[0])
                                    
                        #print(hai,int(aid))
                        if i not in reach[0]:
                            if agari == True and TSUMO == True:
                                if i < stop:
                                    #print(" ",hai)
                                    tsumo[int(aid)].append(hai)
                                    SUMO = hai
                            else:
                                tsumo[int(aid)].append(hai)
                                

                            """
                    if i == tsumonaki[0][y]:
                        tsumo[int(tsumonaki[1][y])].append("N")
                        y = (y+1)%len(tsumonaki[0])

    """
                else:
                    a = soup.find_all("div",attrs={"class":"Tsumo"},limit=1)
                
                    for c in a:
                        mum = c["id"]
                        aid = mum[6]
                        hai = c["class"][1]
                        tsumos[i][0] = aid
                        tsumos[i][1] = hai
                        #print(aid)
                        #print(hai)
                        if len(kan[0]) > 0:
                            if len(kan[0]) == 1:
                                if i == kan[0][0]:
                                    hai = hai+"K"
                                    y = (y+1)%len(tsumonaki[0])
                            else:
                                if i == kan[0][kc]:
                                    hai = hai + "K"
                                    kc = (kc+1)%len(kan[0])
                                    y = (y+1)%len(tsumonaki[0])
                                    
                        #print(hai,int(aid))
                        if i not in reach[0]:
                            if agari == True and TSUMO == True:
                                if i < stop:
                                    #print(" ",hai)
                                    tsumo[int(aid)].append(hai)
                                    SUMO = hai
                            else:
                                tsumo[int(aid)].append(hai)
    if agari == True:
        print("あ！スーモ！",SUMO)
    if agari == True:
        if agariway == "ツモ":
            for i in range(4):
                if len(tsumo[i]) > 0:
                    if tsumo[i][-1] == SUMO:
                        tsumo[i][-1] = SUMO + "T"
        elif agariway == "ロン":
            AH = []
            for i in range(4):
                print(i)
                if len(sutehai[i]) > 0:
                    A = sutehai[i][-1]
                    AH.append(A[0:2])
                else:
                    AH.append("")
            furikomi = AH.index(SUMO)
            print("furikomi",furikomi)
            if sutehai[furikomi][-1] == SUMO:
                sutehai[furikomi][-1] = SUMO + "H"
            print("AH",AH)
        """   
    if agari == True:
        tsumo[agarimun] = tsumo[agarimun][:-1]
        """
    browser.quit()
    #tsumo = [[],[],[],[]]
    print("reach",reach)
    """
    for i in range(0,int(maxn)):
        browser.find_element_by_xpath('//*[@id="v2-contents"]/div[1]/div[2]/div[2]').click()
        sleep(0.001)
        browser.find_element_by_xpath('//*[@id="v2-contents"]/div[1]/div[2]/div[1]').click()
        if sutecountf[0][k] == i :
            k = (k + 1)%len(sutecountf[1])
        else:
            soup = BeautifulSoup(browser.page_source,'html.parser')
                    
            a = soup.find_all("div",attrs={"class":"Tsumo"})
                    
            for c in a:
                mum = c["id"]
                aid = mum[6]
                hai = c["class"][1]
                if i == tg[r]:
                    hai = hai + "T"
                    r = (r+1)%len(tg)
                tsumos[i][0] = aid
                tsumos[i][1] = hai
            #tsumo[int(aid)].append(hai)
    """
    """
    if agari == True:
        agarihai = sutehai[int(furikomi)][-1]
    """
    print("-------------N--------------")
    print(tsumonaki)
    print("-------------names------------")
    print(names)
    print("-----------haipai-------------")
    print(haipai)
    print("------tsumo------")                
    print(tsumo)
    print("tsumos",tsumos[1])
    print("-------------sutehai0------------")
    print(sutehai)

    print("------------motiten-----------------")
    print(motiten)
    print("--------------furikomi-------------------------")
    print(furikomi)
    print("----------saisyuu---------------------------")
    print(saisyuu)
    print("-------------agariway--------")
    print(agariway)
    print("---------------agariname-------------")
    print(agariname)
    print("-------------agarihai-----------------")
    print(agarihai)
    print("---------------------tsumogiri----------")
    print(tsumogiri)
    print(tg)
    print("-------------------------rr-------------")
    print(rr)
    print("-----------sainaki-------")
    print(sainaki)
    print("Ba",Ba)
    print("Honba",Honba)
    print("kyoutaku",kyoutaku)
    if agari == True:
        print("agarihai",agarihai)
        print("agarimun",agarimun)

    im1 = Image.open('bin/j1.png')
    im2 = Image.open('bin/p1.png')
    Sute = Image.open('pcts/S.png')
    Hai = Image.open('pcts/H.png')
    Motto = Image.open('pcts/M.png')
    Tsu = Image.open('pcts/T.png')
    Ton = Image.open('pcts/kaze/Ton.png')
    Nan = Image.open('pcts/kaze/Nan.png')
    Sya = Image.open('pcts/kaze/Sya.png')
    Pee = Image.open('pcts/kaze/Pe.png')
    Pon = Image.open('pcts/Pon.png')
    Chi = Image.open('pcts/Chi.png')
    Kan = Image.open('pcts/Kan.png')
    Waku= Image.open('pcts/Waku.png')
    Waku_Y = Image.open('pcts/Waku_yoko.png')
    Reach= Image.open('pcts/Reach.png')
    Huri = Image.open('pcts/huri.png')
    TS = Image.open('pcts/tsumo.png')
    YAZIRUSHI = Image.open('pcts/Yazirushi.png')
    lists = {'M1':'./bin/m1.png','M2':'./bin/m2.png','M3':'./bin/m3.png','M4':'./bin/m4.png','M5':'./bin/m5.png','M6':'./bin/m6.png','M7':'./bin/m7.png','M8':'./bin/m8.png','M9':'./bin/m9.png',
            'P1':'./bin/p1.png','P2':'./bin/p2.png','P3':'./bin/p3.png','P4':'./bin/p4.png','P5':'./bin/p5.png','P6':'./bin/p6.png','P7':'./bin/p7.png','P8':'./bin/p8.png','P9':'./bin/p9.png',
            'S1':'./bin/s1.png','S2':'./bin/s2.png','S3':'./bin/s3.png','S4':'./bin/s4.png','S5':'./bin/s5.png','S6':'./bin/s6.png','S7':'./bin/s7.png','S8':'./bin/s8.png','S9':'./bin/s9.png',
            'J1':'./bin/j1.png','J2':'./bin/j2.png','J3':'./bin/j3.png','J4':'./bin/j4.png','J5':'./bin/j5.png','J6':'./bin/j6.png','J7':'./bin/j7.png','Null':'./bin/j9.png',
            'M1Y':'./bin/2m1.png','M2Y':'./bin/2m2.png','M3Y':'./bin/2m3.png','M4Y':'./bin/2m4.png','M5Y':'./bin/2m5.png','M6Y':'./bin/2m6.png','M7Y':'./bin/2m7.png','M8Y':'./bin/2m8.png','M9Y':'./bin/2m9.png',
            'P1Y':'./bin/2p1.png','P2Y':'./bin/2p2.png','P3Y':'./bin/2p3.png','P4Y':'./bin/2p4.png','P5Y':'./bin/2p5.png','P6Y':'./bin/2p6.png','P7Y':'./bin/2p7.png','P8Y':'./bin/2p8.png','P9Y':'./bin/2p9.png',
            'S1Y':'./bin/2s1.png','S2Y':'./bin/2s2.png','S3Y':'./bin/2s3.png','S4Y':'./bin/2s4.png','S5Y':'./bin/2s5.png','S6Y':'./bin/2s6.png','S7Y':'./bin/2s7.png','S8Y':'./bin/2s8.png','S9Y':'./bin/2s9.png',
            'T':'./pcts/Yazirushi.png','N':'./bin/je.png','Kan':'./bin/je.png',
            'J1Y':'./bin/2j1.png','J2Y':'./bin/2j2.png','J3Y':'./bin/2j3.png','J4Y':'./bin/2j4.png','J5Y':'./bin/2j5.png','J6Y':'./bin/2j6.png','J7Y':'./bin/2j7.png',
            'M5a':'./bin/me.png','P5a':'./bin/pe.png','S5a':'./bin/se.png'}
    kana =["０","１","２","３","４","５","６","７","８","９"]
    #haipai = ['M1,P3,P3,P7,P8,S1,S4,S5,S9,J1,J2,J3,J4', 'M9,P2,P3,P3,P6,P8,P8,S4,S7,S7,S8,S9,J6', 'M1,M9,P1,P5,P9,P9,S1,S3,S6,S6,J3,J4,J5', '']
    #tsumo = [['M1', 'P9', 'S7', 'M9', 'P5a', 'P9P', 'M9P', 'P1', 'P1P', 'S1', 'J2', 'S5a'], [], ['J7', 'J5', 'J3', 'P1', 'S3', 'J6', 'S5', 'S8', 'J4', 'J7', 'J2', 'J3', 'S1'], ['J5', 'J1', 'P2', 'S3', 'P9', 'P6', 'M9', 'S3', 'P1', 'J1', 'J4', 'S9']]
    #sute = [['J3', 'J4', 'J5', 'P5', 'P5a', 'S7P', 'P9P', 'S6', 'S6P', 'S3', 'J2', 'S5a'], [], ['M1', 'J4', 'J5', 'J2', 'J1', 'J6', 'J7', 'S1', 'J4', 'P1', 'J7', 'J2', 'S1'], ['M9', 'J5', 'J6', 'J1', 'S9', 'P9', 'M9', 'S8R', 'P1', 'J1', 'J4', 'S9']]
    sute = sutehai
    ssute = []
    Tsumo = []
    #names = ['かずりゅう', '', 'えくすたしー', 'アテナ']
    #sainaki = [[], [], [3, 3, 3], []]
    #motiten = [['35000'], ['35000'], ['35000'], [None]]
    #Ba = "東一局"
    #Honba = "0本場"
    #URL = "https://pl.sega-mj.com/mj_viewer?B=0002&K=11203&V=6&DI=FrMuMj3HV01NPb&T=350_350_350&SA=10&D=m&S=15&H=vfxa9jr1nwcfr_d1vtaulqewilp_lqqigkolhy9gd&A=z1x91vxwtxrwvxkygxjuct9nctris_y_orP0gez9_P0rhacRhjfw_j_P0fzjt_acuzw_u_vui_-_a_~04&Y=11_208d320_115000d1E1mh411aaa32123rrr21239992123jjj&Z=ikdnxfmghq1mpzbdboppuboykmtbnmhefyz&N=%E3%81%8B%E3%81%9A%E3%82%8A%E3%82%85%E3%81%86_%E3%81%88%E3%81%8F%E3%81%99%E3%81%9F%E3%81%97%E3%83%BC_%E3%82%A2%E3%83%86%E3%83%8A"
    def get_shortenURL(longUrl):
        url = 'https://api-ssl.bitly.com/v3/shorten'
        access_token = 'c0c00a89588fb8917ce8883f025bca0f187fa0d6'
        query = {
                'access_token': access_token,
                'longurl':longUrl
                }
        r = requests.get(url,params=query).json()['data']['url']
        
        return r
    def create_QR():
        qr = qrcode.QRCode(
            version=6,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=5,
            border=0
            )
        qr.add_data(get_shortenURL(url))
        qr.make()
        img = qr.make_image()
        return img


    for a in range(10):

        if str(a) in Honba:
            Honba = Honba.replace(str(a),kana[a])
    #kyoutaku = "供託0点"
    for a in range(10):

        if str(a) in kyoutaku:
            kyoutaku = kyoutaku.replace(str(a),kana[a])
    Kyo = kyoutaku[0:2]
    Kpoint= kyoutaku[2:]

    for i in range(4):
        print(len(sute[i]))
        print(len(tsumo[i]))
        for k in range(len(sute[i])):
            if tsumo[i][k] == sute[i][k]:
                tsumo[i][k] = "T"
    
    for i in range(4):
        a = ""
        for k in tsumo[i]:
            a = a+k+","
        a = a[:-1]
        Tsumo.append(a)

    for i in range(4):
        a = ""
        for k in sute[i]:
            a = a+k+","
        a = a[:-1]
        ssute.append(a)
    print(Tsumo)
    print(ssute)
    j = 0
    #saisyuu = ['P3,P3,P7,P8,S3,S4,S5,S5,S8,S9,J3,J3,J3', 'P2,P2,P3,P3,P6,P6,P8,P8,S3,S3,S4,S7,S7', 'M1,M1,S1,S1,P9NY,P9N,P9N,M9NY,M9N,M9N,P1NY,P1N,P1N', '']

    #jun = [2,3,0,1]

    #牌→path
    W = 18
    H = 16
    width = W + 10 + 4 + 3
    height = H + 7 + 1
    SPACE = 8*24
    bl =  0
    hai= 0
    n = 0
    blank = 0
    l = 0

    #config
    config = configparser.ConfigParser()
    config.read('config.ini')
    path = config['Font']['path']


    dst = Image.new('RGBA', (im1.width*width, im1.height*height),(0,100,0))
    mask = dst.split()[3]
    dst.paste(Ton,(0,0),Ton)

    font = ImageFont.truetype(path, 32)
    Hfont = ImageFont.truetype(path, 40)
    draw = ImageDraw.Draw(dst)
    N = names[kazes.index("東")]
    size = math.floor(143/len(N))
    if size > 32:
        size = 32
        blank = math.floor(143 - 32*len(N))/2
    font = ImageFont.truetype(path, size)
    for k in names[kazes.index("東")]:
        draw.text((0,hai+5+32+n*size+blank),k,fill=(255,255,255),font = font)
        n = n +1
    i = 0
    nc = 0
    AA = 0
    nn = 0
    m = 0
    j = 0
    k = 0
    co = 0
    rasunaki = 0
    hhname = ""
    mfont = ImageFont.truetype(path, 20)
    draw.line((624,0,624,im1.height*height),fill=(255,0,0),width=1)
    FF = False
    KAZE = ""
    aaa = 0
    for a in range(0,4):
        co = 0
        aa = a
        if a == 0:
            KAZE = "東"
        if a == 1:
            KAZE = "南"
        if a == 2:
            KAZE = "西"
        if a == 3:
            KAZE = "北"
        aaa = kazes.index(KAZE)
        a = a*4*im1.height
        FF = False
        nc = 0
        nn = 0
        for b in range(0,4):
            
            if b == 0 and a == 0:
                hai = 0
            else:
                hai = hai + im1.height
            
            for i in range(0,18):
                
                if b == 0:
                    #配牌
                    if i == 0:
                        if aa != 0:
                            dst.paste(Hai,(im1.width*i+SPACE-27,hai+12),Hai)
                            ten = str(motiten[aaa])
                            ten = ten.replace("[","").replace("'","").replace("'","").replace("]","")
                            if aa != 3 or ten != "None":
                                draw.text((32+30,hai),"持ち点",fill=(255,255,255),font = mfont)
                                draw.text((32+25,hai+20),ten,fill=(255,255,255),font = mfont)
                            if aa == 1:
                                n = 0
                                blank = 0
                                N = names[kazes.index("南")]
                                size = math.floor(143/len(N))
                                if size > 32:
                                    size = 32
                                    blank = math.floor(143 - 32*len(N))/2
                                font = ImageFont.truetype(path, size)
                                for k in names[aaa]:
                                    draw.text((0,hai+5+32+n*size+blank),k,fill=(255,255,255),font = font)
                                    n = n +1
                                dst.paste(Nan,(0,hai+5),Nan)
                                #南
                            elif aa == 2:
                                #西
                                n = 0
                                blank = 0
                                N = names[kazes.index("西")]
                                size = math.floor(143/len(N))
                                if size > 32:
                                    size = 32
                                    blank = math.floor(143 - 32*len(N))/2
                                font = ImageFont.truetype(path, size)
                                for k in names[aaa]:
                                    draw.text((0,hai+5+32+n*size+blank),k,fill=(255,255,255),font = font)
                                    n = n +1
                                dst.paste(Sya,(0,hai+5),Sya)
                            elif aa == 3:
                                #北
                                n = 0
                                blank = 0
                                N = names[kazes.index("北")]
                                if len(N) != 0:
                                    size = math.floor(143/len(N))
                                    if size > 32:
                                        size = 32
                                        blank = math.floor(143 - 32*len(N))/2
                                    font = ImageFont.truetype(path, size)
                                    for k in names[aaa]:
                                        draw.text((0,hai+5+32+n*size+blank),k,fill=(255,255,255),font = font)
                                        n = n +1
                                dst.paste(Pee,(0,hai+5),Pee)
                            #fontを指定
                            hai = hai + 9
                        else:
                            dst.paste(Hai,(im1.width*i+SPACE-27,4),Hai) #fontを指定
                            ten = str(motiten[aaa])
                            ten = ten.replace("[","").replace("'","").replace("'","").replace("]","")
                            draw.text((32+25,-5+20),ten,fill=(255,255,255),font = mfont)
                            draw.text((32+30,-5),"持ち点",fill=(255,255,255),font = mfont)
                            draw.text((624+((im1.width*width-624)-len(Ba)*40)/2,-5),Ba,fill=(255,255,255),font = Hfont)
                            x = 624+((im1.width*width-624)-len(Ba)*40)/2
                            draw.line((624,45,im1.width*width,45),fill=(255,0,0),width=2)
                            draw.text((x,45),Honba,fill=(255,255,255),font = Hfont)
                            draw.line((624,95,im1.width*width,95),fill=(255,0,0),width=2)
                            Kfont = ImageFont.truetype(path, 35)
                            draw.text((624+((im1.width*width-624)-len(Kyo)*40)/2,95),Kyo,fill=(255,255,255),font = Kfont)
                            draw.text((624+((im1.width*width-624)-len(Kpoint)*40)/2,135),Kpoint,fill=(255,255,255),font = Kfont)
                            draw.line((624,180,im1.width*width,180),fill=(255,0,0),width=2)
                            draw.line((624,0,624,180),fill=(255,0,0),width=2)
                            gazou = create_QR()
                            pos = (dst.size[0]-gazou.size[0],735-gazou.size[1])
                            dst.paste(gazou,pos)
                            Dfont = ImageFont.truetype(path, 24)
                            draw.text((0,735),date,font = Dfont)
                    if i < 13:
                        k = haipai[aaa]
                        if len(k) != 0:
                            k = k.split(",")
                            hname = k[i]
                            A = Image.open(lists[hname])
                            dst.paste(A, (im1.width*i+SPACE, hai))
                            dst.paste(Waku,(im1.width*i+SPACE, hai),Waku)
                        else:
                            A = Image.open(lists["Null"])
                            dst.paste(A, (im1.width*i+SPACE, hai))
                elif b == 1:
                    #ツモ
                    
                    if i == 0:
                        dst.paste(Tsu,(im1.width*i+SPACE-27,hai+18),Tsu) #fontを指定
                        hai = hai + 16
                        bb = aaa
                        if len(Tsumo[bb]) != 0:
                            j = Tsumo[bb].split(",")
                            hname = j[i]
                            if len(hname) > 2:
                                if "N" not in hname and "C" not in hname and "K" not in hname and "T" not in hname:
                                    A = Image.open(lists[hname])
                                    
                                else:
                                    #ポン・チー・カンの時
                                    if "N" in hname:
                                        dst.paste(Pon,(im1.width*i+SPACE, hai-16), Pon)                                
                                        hname = hname.rstrip("N")
                                    if "C" in hname:
                                        dst.paste(Chi,(im1.width*i+SPACE, hai-16),Chi) 
                                        hname = hname.rstrip("C")
                                    if "K" in hname:
                                        dst.paste(Kan,(im1.width*i+SPACE, hai-16),Kan) 
                                        hname = hname.rstrip("K")
                                    if "T" in hname:
                                        dst.paste(TS,(im1.width*i+SPACE, hai+32+5),TS) 
                                        hname = hname.rstrip("T")
                                    A = Image.open(lists[hname])
                            else:
                                A = Image.open(lists[hname])
                        dst.paste(A, (im1.width*i+SPACE, hai))
                        if len(Tsumo[bb]) != 0: dst.paste(Waku,(im1.width*i+SPACE, hai),Waku)
                    else:
                        #hai = hai + 16
                        bb = aaa
                        if len(Tsumo[bb]) != 0:
                            
                            j = Tsumo[bb].split(",")
                            if i < len(j):
                                hname = j[i]
                                if len(hname) > 2:
                                    if "N" not in hname and "C" not in hname and "K" not in hname and "T" not in hname:
                                        A = Image.open(lists[hname])
                                    
                                    else:
                                        #ポン・チー・カンの時
                                        if "N" in hname:
                                            dst.paste(Pon,(im1.width*i+SPACE, hai-16),Pon)
                                            
                                            hname = hname.rstrip("N")
                                        if "C" in hname:
                                            dst.paste(Chi,(im1.width*i+SPACE, hai-16),Chi) 
                                            hname = hname.rstrip("C")
                                        if "K" in hname:
                                            dst.paste(Kan,(im1.width*i+SPACE, hai-16),Kan) 
                                            hname = hname.rstrip("K")
                                        if "T" in hname:
                                            dst.paste(TS,(im1.width*i+SPACE, hai+32+5),TS)
                                            hname = hname.rstrip("T")
                                        print(hname)
                                        A = Image.open(lists[hname])
                                else:
                                    A = Image.open(lists[hname])

                                    
                                dst.paste(A, (im1.width*i+SPACE, hai))
                                dst.paste(Waku,(im1.width*i+SPACE, hai),Waku)
                        else:
                            
                            A = Image.open(lists["Null"])
                            dst.paste(A, (im1.width*i+SPACE, hai))
                elif b == 2:
                    #捨牌
                    if i == 0:
                        dst.paste(Sute,(im1.width*i+SPACE-27,hai+6),Sute)
                        bb = aaa
                        print("hname",hname)
                        if len(ssute[bb]) != 0:
                            j = ssute[bb].split(",")
                            hname = j[i]
                            if "N" not in hname and "C" not in hname and "K" not in hname and "H" not in hname:
                                if "R" in hname:
                                    hname = hname.rstrip("R")
                                    dst.paste(Reach, (im1.width*i+SPACE, hai+5+32))
                                
                                A = Image.open(lists[hname])
                            
                            else:
                                #ポン・チー・カンの時
                                if "N" in hname:
                                    hname = hname.rstrip("N")
                                if "C" in hname:
                                    hname = hname.rstrip("C")
                                if "K" in hname:
                                    hname = hname.rstrip("K")
                                if "R" in hname:
                                    hname = hname.rstrip("R")
                                    dst.paste(Reach, (im1.width*i+SPACE-10, hai))
                                if "H" in hname:
                                    hname =hname.rstrip("H")
                                    print("hname",hname)
                                    dst.paste(Huri,(im1.width*i+SPACE,hai+10))
                                A = Image.open(lists[hname])
                            dst.paste(A, (im1.width*i+SPACE, hai))
                            dst.paste(Waku,(im1.width*i+SPACE, hai),Waku)
                        else:
                            A = Image.open(lists["Null"])
                            dst.paste(A, (im1.width*i+SPACE, hai))
                        #fontを指定
                    else:
                        #hai = hai + 16
                        bb = aaa
                        if len(ssute[bb]) != 0:
                            
                            j = ssute[bb].split(",")
                            if i < len(j):
                                hname = j[i]
                                if len(hname) > 2:
                                    if "N" not in hname and "C" not in hname and "K" not in hname and "H" not in hname:
                                        if "R" in hname:
                                            hname = hname.rstrip("R")
                                            dst.paste(Reach, (im1.width*i+SPACE, hai+5+32))
                                        
                                        A = Image.open(lists[hname])
                                    
                                    else:
                                        #ポン・チー・カンの時
                                        if "N" in hname:
                                            hname = hname.rstrip("N")
                                        if "C" in hname:
                                            hname = hname.rstrip("C")
                                        if "K" in hname:
                                            hname = hname.rstrip("K")
                                        if "R" in hname:
                                            hname = hname.rstrip("R")
                                            dst.paste(Reach, (im1.width*i+SPACE-10, hai))
                                        if "H" in hname:
                                            hname =hname.rstrip("H")
                                            print("hname",hname)
                                            dst.paste(Huri,(im1.width*i+SPACE,hai+10))
                                        A = Image.open(lists[hname])
                                    dst.paste(A, (im1.width*i+SPACE, hai))
                                    dst.paste(Waku,(im1.width*i+SPACE, hai),Waku)
                            else:
                                A = Image.open(lists[hname])
                        else:
                            A = Image.open(lists["Null"])
                            dst.paste(A, (im1.width*i+SPACE, hai))
                                #A = Image.open(lists[hname])
                        #dst.paste(im1, (im1.width*i+SPACE, hai))
                elif b == 3:
                    #最終
                    if i == 0:
                        dst.paste(Motto,(im1.width*i+SPACE-27,hai+36),Motto) #fontを指定
                        hai = hai + 32
                        #Draw系
                        draw.line((0,hai+32+4,624,hai+32+4),fill=(255,0,0),width=1)
                        #print("(0,"+str(hai+32+4)+",624,"+str(hai+32+4)+")")
                    if i < 21:
                        k = saisyuu[aaa]
                        if len(k) > 0:
                            k = k.split(",")
                            try:
                                hname = k[i]
                                if "N" not in hname and "Y" not in hname:
                                    A = Image.open(lists[hname])
                                    dst.paste(A, (im1.width*i+SPACE, hai))
                                    dst.paste(Waku,(im1.width*i+SPACE, hai),Waku)
                                
                                else:
                                    if len(sainaki[aaa]) == 1:
                                        l = 0
                                    if sainaki[aaa][l] ==  co:
                                        rasunaki = rasunaki + 12
                                        if len(sainaki[aaa]) != 1:
                                            l = (l+1)%len(sainaki[aaa])
                                        co = 0
                                        
                                    if "N" in hname and "Y" not in hname:
                                        #鳴きのみ
                                        if hname == "URANU":
                                            A = Image.open(lists["Null"])
                                        else:
                                            hname = hname.replace("N", "")
                                            A = Image.open(lists[hname])
                                        
                                    
                                            #dst.paste(A,(im1.width*i+SPACE+8+24, hai))

                                        dst.paste(A,(im1.width*i+SPACE+24+rasunaki, hai))
                                        #dst.paste(A,(im1.width*i+SPACE+16+24, hai))
                                        dst.paste(Waku,(im1.width*i+SPACE+24+rasunaki, hai),Waku)

                                    else:
                                        #鳴き+横
                                        hname = hname.replace("N", "")
                                        A = Image.open(lists[hname])
                                        
                                        
                                        #dst.paste(A,(im1.width*i+SPACE+24, hai+8))
                                        
                                        
                                        dst.paste(A,(im1.width*i+SPACE+24+rasunaki, hai+8))
                                        dst.paste(Waku_Y,(im1.width*i+SPACE+24+rasunaki, hai+8),Waku_Y)
                                        rasunaki = rasunaki + 8
                                        #dst.paste(A,(im1.width*i+SPACE+8+24, hai+8))
                                        #dst.paste(Waku,(im1.width*i+SPACE, hai),Waku)
                                    co = co + 1
                            except:
                                pass

                        else:
                            A = Image.open(lists["Null"])
                            dst.paste(A, (im1.width*i+SPACE, hai))
                            

                        #dst.paste(im1,(im1.width*i+SPACE, hai))
                        

                    #dst.paste(im1, (im1.width*i+SPACE, hai))
                    
    date = date.replace(" ","_").replace(":","")
    KANSUUZI = [["一","二","三","四"],["1","2","3","4"]]
    KANZI = [["東","南","西","北"],["Ton","Nan","Sha","Pei"]]
    kanzi = ""
    kanzi = KANZI[1][KANZI[0].index(Ba[0])]
    suuzi = ""
    suuzi = KANSUUZI[1][KANSUUZI[0].index(Ba[1])]
    print(date)
    print(kanzi)
    print(suuzi)
    print(Nhonba)
    fn = "./Paihu/"+date+"_"+kanzi+"_"+suuzi+"_"+Nhonba+".png"
    print(fn)
    #dst.save('./pillow_concat_h.png')
    dst.save(fn)
    #im = Image.open("./pillow_concat_h.png")
    #im.show()


                    
    """hai = a["class"][1]
    mem = a["id"]
    mem = mem[6]
    print(hai)
    print(mem)"""
    """a = soup.find(id=t)
    b = soup.find(id=n)
    c = soup.find(id=sss)
    if a["class"][1] != "Null":
        kazez[int(kaze)].append(a["class"][1])
        print("a:",a["class"][1])
        continue

    elif b["class"][1] != "Null":
        kazez[nn].append(b["class"][1])
        print("b:",b["class"][1])
        continue
    elif c["class"][1] != "Null":
        kazez[sn].append(c["class"][1])
        print("c:",c["class"][1])
        continue
                

            else:
                print("ヨンマ")"""
    """
    print("[+++++++]----------0--------")
    for i in kazez[0]:
        print(i)
    print("[+++++++]----------1--------")
    for i in kazez[1]:
        print(i)
    print("[+++++++]----------2--------")
    for i in kazez[2]:
        print(i)
    print("[+++++++]----------3--------")
    for i in kazez[3]:
        print(i)
                
            """       
            
            
            

        
    """print("[+]0")      
    for a in kazez[0]:
        print(a)
    print("[+]1")      
    for a in kazez[1]:
        print(a)
    print("[+]2")      
    for a in kazez[2]:
        print(a)
    print("[+]3")      
    for a in kazez[3]:
        print(a)
    print("[+]配牌")
    for a in haipai:
        print(a)
        #print(i)"""






        
def U_DATE(U,DATE):
    for i in reversed(range(len(U))):
        browser.quit()
        print(U[i])
        print(DATE[i])
        MJ(U[i],DATE[i])

        
while True:
    browser.get("https://pl.sega-mj.com/mydata_view?ref=login")
    print("MjM-IDでログインするなら0を、SEGA IDでログインするなら1を入力してください")
    print("また、保存したログイン情報を使うなら2を入力してください")
    a = input(">")
    if str.isdigit(a):
        if int(a) == 0:
            browser.find_element_by_xpath('//*[@id="v2-contents"]/div/div/div[2]/button[2]').click()
            print("MJM-IDを入力してください")
            #ID = input(">")
            ID= "mjm29594480"
            PASS = "hdlRs6GD77"
            print("パスワードを入力してください")
            #PASS = getpass.getpass(prompt=">")
            print("プレイデータを選択してください")
            print("iOSなら0を、PC/Androidなら1を入力してください")
            pl = input(">")
            win1 = browser.window_handles[-1]
            soup = MJM(ID,PASS,pl)
            if soup != "NOLOGIN":
                #ログイン成功
                ga = soup.find(class_ = "head").string
                ga = ga.strip()
                if ga == "MYデータMENU":
                    print("[+]ログインに成功しました！")
                    print("[+]ログイン情報を登録しますか？ いいえ:0 はい:1")
                    aa = input(">")
                    if aa == "1":
                        print("[+]登録中.....")
                        print(ANGOUKA(ID,PASS,int(a),int(pl)))
                        print("登録が完了しました！")
                        print("次回から入力を省略できます")

                    shI = hashlib.sha256(ID.encode("utf-8")).hexdigest()
                    A = History()
                    print("[+]URLを取得中.....")
                    #print(URLS(A,shI))
                    ALL = URLS(A,shI)
                    U = ALL[0]
                    DATE = ALL[1]
                    
                    print(len(U))
                    print(len(DATE))
                    if len(U) > 0:
                        U_DATE(U,DATE)
                    """
                    while True:
                        browser.get("https://pl.sega-mj.com/playdata_view/showHistory")
                        A = LOOP(shI)
                        print(A)
                        if len(A) > 0:
                            for u in range(len(A[0])):
                                MJ(A[0][u],A[1][u])
                        if A == "ERROR":
                            break
                    """
                    break
            else:
                #ログイン失敗
                print("[+]ログインに失敗しました！")
                browser.switch_to_window(win1)
                Alert(browser).accept()
                win2 = browser.window_handles[-1]
                browser.switch_to_window(win2)
                #browser.get("https://pl.sega-mj.com/mydata_view?ref=login")
            #browser.quit()
        elif int(a) == 1:
            browser.find_element_by_xpath('//*[@id="chage_segaid_button"]').click()
            print("SEGA IDを入力してください")
            ID = input(">")
            print("パスワードを入力してください")
            PASS =input(">")
            WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.ID, "auth_image")))
            soup = BeautifulSoup(browser.page_source,'html.parser')
            print("画像認証を行います")
            img = soup.find(class_ = "unit",id = "auth_image").find("img").get("src")
            download_img(img,"A.png")
            img = Image.open("A.png")
            img.show()
            print("表示されている文字を平仮名で入力してください")
            Gazou = input(">")
            print("プレイデータを選択してください")
            print("iOSなら0を、PC/Androidなら1を入力してください")
            pl = input(">")
            win1 = browser.window_handles[-1]
            soup = SEGA(ID,PASS,Gazou,pl)
            if soup != "NOLOGIN":
                ga = soup.find(class_ = "head").string
                ga = ga.strip()
                if ga == "MYデータMENU":
                    #成功
                    print("[+]ログインに成功しました！")
                                        
                    print("[+]ログイン情報を登録しますか？ いいえ:0 はい:1")
                    aa = input(">")
                    if aa == "1":
                        print("[+]登録中.....")
                        ANGOUKA(ID,PASS,int(a),int(pl))
                        print("登録が完了しました！")
                        print("次回から入力を省略できます")
   
                    A = History()
                    shI = hashlib.sha256(ID.encode("utf-8")).hexdigest()
                    print("[+]URLを取得中.....")
                    URLS(A,shI)
                    while True:
                        browser.get("https://pl.sega-mj.com/playdata_view/showHistory")
                        A = LOOP(shI)
                        print(A)
                        if A == "ERROR":
                            break
                    break
                    
            else:
                print("[+]ログインに失敗しました！")
                browser.switch_to_window(win1)
                Alert(browser).accept()
                win2 = browser.window_handles[-1]
                browser.switch_to_window(win2)
                #browser.refresh()
                #browser.get("https://pl.sega-mj.com/mydata_view?ref=login")
                #browser.quit()
        elif int(a) == 2:
            browser.get("https://pl.sega-mj.com/mydata_view?ref=login")
            config = configparser.ConfigParser()
            config.read('temporary.ini')
            if config['IDS']['lists'] !=  "None":
                print("読み込み中.....")
                HUKUGOU()
                ID = HUKUGOU()[0]
                PASS = HUKUGOU()[1]
                W = config['CONFIG']['w']
                pl = config['CONFIG']['p']
                if str(W) == "0":
                    browser.find_element_by_xpath('//*[@id="v2-contents"]/div/div/div[2]/button[2]').click()
                    win1 = browser.window_handles[-1]
                    soup = MJM(ID,PASS,pl)
                    if soup != "NOLOGIN":
                        print("[+]ログインに成功しました！")
                        shI = hashlib.sha256(ID.encode("utf-8")).hexdigest()
                    else:
                        print("[+]ログインに失敗しました！")
                        browser.switch_to_window(win1)
                        Alert(browser).accept()
                        win2 = browser.window_handles[-1]
                        browser.switch_to_window(win2)
                        #browser.get("https://pl.sega-mj.com/mydata_view?ref=login")
                elif str(W) == "1":
                    browser.find_element_by_xpath('//*[@id="chage_segaid_button"]').click()
                    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.ID, "auth_image")))
                    soup = BeautifulSoup(browser.page_source,'html.parser')
                    print("画像認証を行います")
                    img = soup.find(class_ = "unit",id = "auth_image").find("img").get("src")
                    download_img(img,"A.png")
                    img = Image.open("A.png")
                    img.show()
                    print("表示されている文字を平仮名で入力してください")
                    Gazou = input(">")
                    win1 = browser.window_handles[-1]
                    soup = SEGA(ID,PASS,Gazou,pl)
                    if soup != "NOLOGIN":
                        print("[+]ログインに成功しました！")
                        shI = hashlib.sha256(ID.encode("utf-8")).hexdigest()
                    else:
                        print("[+]ログインに失敗しました！")
                        browser.switch_to_window(win1)
                        Alert(browser).accept()
                        win2 = browser.window_handles[-1]
                        browser.switch_to_window(win2)
                        #browser.get("https://pl.sega-mj.com/mydata_view?ref=login")
            else:
                print("登録されているデータがありません！")
        else:
            print("0か1を入力してください！")
    else:
        print("数字を入力してください！")
browser.quit()
ID= "mjm29594480"
PASS = "hdlRs6GD77"

# クッキー取得
#print(browser.get_cookies())
