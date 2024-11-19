from flet import *
import time
import  supabase
from datetime import date
import smtplib
import random 
import os
import threading,sys  
import deep_translator
import wikipediaapi as wikipedia
import sys 
user_agent = "Mostafa Ai/1.0 (mustaphakessassi76@gmail.com)"
if sys.platform == "emscripten": # check if run in Pyodide environment
    import micropip
    micropip.install("regex")
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

url = "https://faxpxfwubctpvckzbpit.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZheHB4Znd1YmN0cHZja3picGl0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMTY4NzE1MiwiZXhwIjoyMDQ3MjYzMTUyfQ.c8GPmYAvFdcHEVW6EWJUYN5aO9l_ES3vr3bBpVUUQY4"


supabase = create_client(url, key)
users_response = ""
server=""
account_cookie_1=""
def resource_path2(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)
def stm(*args):
        try:
            while True:
                time.sleep(1.5)
                global server
                server = smtplib.SMTP("smtp.gmail.com",587)
                server.ehlo()
                server.starttls()
                server.login(user="mostafaaipro33@gmail.com",password="wskx juda lbfm rxfa")
                global users_response
                users_response = supabase.auth.admin.list_users()
                break
        except Exception as er:
            print(er)
            threading.Thread(daemon=True,target=stm).start()
threading.Thread(daemon=True,target=stm).start()



num = ['1','2','3','4','5','6','7','8','9','10','é','&','à','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


langa = {"English" : "en",
         "French" : "fr",
         "Arabic" : "ar",
         }
User=""
class Data:
    def __init__(self) -> None:
        self.counter = 0
def main(page:Page,**args):
    # page.window_height=682
    page.spacing = 0
    # page.window_width=330
    page.window.height=600
    page.window.width=353
    page.title="Mostafa Ai"
    page.padding=0
    page.bgcolor=colors.RED
    page.update()
    d = Data()
    def main_1(name_link:str):
        try:
            
            reponse = supabase.table("Mostafa Ai Links").select(name_link).execute()
            page.launch_url(reponse.data[0][name_link],web_window_name=name_link,web_popup_window=False)
            
            
        except:
            pass
    page.window.full_screen=False
    def Toast(*args,tetx,colors_):
            snack_bar = SnackBar(bgcolor=colors_,content=Text(f"{tetx}"))
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()
    def login(*args):
            try:
                if not "@" in email.value:
                    Toast(tetx="Please Enter Email",colors_=colors.RED)
                elif not ".com" in email.value:
                    Toast(tetx="Please Enter Email",colors_=colors.RED)
                    bt1.disabled=True
                    page.update()
                elif password.value=="":
                    bt1.disabled=True
                    page.update()
                    Toast(tetx="Please Enter Password",colors_=colors.RED)
                elif password.value!="" and email.value!="":
                    prog.value=None
                    forget_button.disabled=True
                    Sign_up_button.disabled=True
                    password.read_only=True
                    email.read_only=True
                    bt1.disabled=True
                    page.update()
                    print("#############################################################")
                    
                    print("#############################################################################")
                    pasw=""
                    global users_response
                    users_response = supabase.auth.admin.list_users()
                    users_response1 =users_response
                    for userss in users_response:
                        if userss.email==email.value.replace(' ','').replace("\n",""):
                            user_metadata = getattr(userss, "user_metadata", {})
                            if "password" in user_metadata :
                                if user_metadata['password']==str(password.value).replace(" ",""):
                                    pasw = user_metadata['password']
                                    global User
                                    User = user_metadata['name']
                                    Toast(tetx="Login secssec",colors_=colors.GREEN)
                                    page.update()
                                    #time.sleep(1.5)
                                    page.go('/page_1')
                                    open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="w").write(f"email : {email.value} password : {password.value} Name : {user_metadata['name']}")
                                    page.update()
                                    time.sleep(1)
                                    file_=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read()
                                    email_=file_.split()[2]
                                    paass=file_.split()[5]
                                    full_name_=file_.replace(f"email : {email_} password : {paass} Name : ","")
                                    old_pass=file_.split()[5]
                                
                                    page_5.content=Column(expand=True,controls=[Container(alignment=alignment.top_left,expand=False,padding=0,content=Column(controls=[Text(""),Text(""),IconButton(icon=icons.ARROW_BACK,on_click=lambda _: page.go('/page_1'))])),Container(alignment=alignment.top_center,padding=-10,content=Icon(name=icons.PERSON,color=colors.WHITE,size=150)),Container(expand=True,padding=10,content=Column(expand=True,controls=[TextField(border_color=colors.WHITE,label="Email",value=email_,read_only=True,text_size=15),Row(controls=[TextField(border_color=colors.WHITE,expand=True,label="Full Name",value=full_name_,read_only=True,width=220)]),Row(controls=[password_new,IconButton(icon=icons.MODE,on_click=change)]),Container(alignment=alignment.top_center,padding=10,content=Column(alignment=alignment.top_center,controls=[Container(alignment=alignment.top_center,content=ElevatedButton(text="save",on_click=lambda _: threading.Thread(daemon=True,target=save(old_password=old_pass,name_user=file_.replace(f"email : "+file_.split()[2]+" password : "+file_.split()[5]+ " Name : ",""))).start())),Container(alignment=alignment.top_center,content=ElevatedButton(text="Log out",on_click=Log_out))]))]))])
                                    password_new.value=pasw
                                    page.update()
                                else:
                                
                                    Toast(tetx="Error Password is wrong",colors_=colors.RED)
                        elif not email.value in str(users_response1):
                            Toast(tetx="Error It email not found",colors_=colors.RED)




            except Exception as erp:
                print(erp)
                Toast(tetx="Error You Dont Have Internet ",colors_=colors.RED)
                page.update()
                password.read_only=False
                email.read_only=False
                bt1.disabled=False
                Sign_up_button.disabled=False
                forget_button.disabled=False
                prog.value=0.0
                page.update()
            password.read_only=False
            email.read_only=False
            bt1.disabled=False
            Sign_up_button.disabled=False
            forget_button.disabled=False
            prog.value=0.0
            page.update()


    
    page.theme_mode=ThemeMode.DARK
    page.update()
    def wek(*agrs):
        if txt1.value.replace(" ","")!="" and str(txt1.value)!=None and com1.value!=None:
                    txt2.read_only=False
                    nas = txt1.value
                    txt2.value=txt2.value+f"\n~{User}~  :  "+nas
                    txt2.read_only=True     
                    #print(txt1.value)
                    
                    txt1.value=""
                    bt.disabled = True
                    page.update()
                    print(com1.value)
                    print(langa[com1.value])
                    wiki = wikipedia.Wikipedia(user_agent=user_agent,language=langa[com1.value])
                    #print(wikipedia.languages())
                    try:
                        paht1 = wiki.page(title=nas)
                        if  paht1.exists():
                            paht = paht1.summary
                        elif not paht1.exists():
                            # جلب البيانات من الجدول
                            data_exists = supabase.table("Mostafa Ai Data").select("Mostafa Ai Data Exists").execute()
                            data_not_exists = supabase.table("Mostafa Ai Data").select("Mostafa Ai Data Not Exists").execute()
                            
                            found = False  # متغير لتتبع إذا تم العثور على النص
                            for record in data_exists.data:
                                for key, value in record.items():
                                    if nas.lower() in str(value).lower():
                                        paht = deep_translator.GoogleTranslator(source="en", target=langa[com1.value]).translate(str(value))
                                        found = True
                                        break  # الخروج من الحلقة إذا تم العثور على النص
                            
                            # إذا لم يتم العثور في الحقول الأولى
                            if not found:
                                for record in data_not_exists.data:
                                    for key, value in record.items():
                                        if nas.lower() in str(value).lower():
                                            paht = f"{deep_translator.GoogleTranslator(source="en", target=langa[com1.value]).translate("Not Found Right Now Sorry For That")}\n"
                                            found = True
                                            break

                            # إذا لم يتم العثور عليه على الإطلاق
                            if not found:
                                # التحقق من عدم إدخال النص مسبقًا
                                if not any(nas in str(record) for record in data_not_exists.data):
                                    supabase.table("Mostafa Ai Data").insert({"Mostafa Ai Data Not Exists": str(nas)}).execute()
                                paht = f"{deep_translator.GoogleTranslator(source="en", target=langa[com1.value]).translate("Not Found Right Now Sorry For That")}\n"
                                    

                    except Exception as error:
                            print(error)
                            if com1.value.lower()=="arabic":
                                paht="الشبكة ضعيفة حاول مرة اخرى "+"\n"
                            elif com1.value.lower()=="french":
                                paht="Le réseau est faible, réessayez.\n"
                            else:
                                paht="You Dont Have Good Internet\n"                   
                    txt2.read_only=False
                    txt2.value=txt2.value+"\n𓆩Mostafa Ai𓆪  :  "+str(paht)+"\n"
                    txt2.read_only=True                
                    bt.disabled = False
                    page.update()

        
    
    # page.add(HTML("<link rel='icon' href='path_to_your_favicon.ico' type='image/x-icon'>"))
    #page.vertical_alignment=MainAxisAlignment.CENTER
    #page.window_resizable=False
    

    
    #page.add(com1)
    #page.add()
    tr = Text("",size=5)
    
    def crée_user(*args):
        if not len(full_name.value.split())>=2:
             code_button.disabled=True
             full_email.read_only=True
             full_password.read_only=True
             full_password_cunform.read_only=True
             full_name.read_only=True
             have_account_button.disabled=True
             page.update()
             Toast(tetx="Please Enter full name",colors_=colors.RED)
        elif not "@" in full_email.value:
             code_button.disabled=True
             full_email.read_only=True
             full_password.read_only=True
             full_password_cunform.read_only=True
             full_name.read_only=True
             have_account_button.disabled=True
             page.update()
             Toast(tetx="Please Enter Email",colors_=colors.RED)
        elif not ".com" in full_email.value:
             code_button.disabled=True
             full_email.read_only=True
             full_password.read_only=True
             full_password_cunform.read_only=True
             full_name.read_only=True
             have_account_button.disabled=True
             page.update()
             Toast(tetx="Please Enter Email",colors_=colors.RED)
        elif full_password.value.replace(" ","")=="":
             code_button.disabled=True
             full_email.read_only=True
             full_password.read_only=True
             full_password_cunform.read_only=True
             full_name.read_only=True
             have_account_button.disabled=True
             page.update()
             Toast(tetx="Please Enter Password",colors_=colors.RED)

        elif len(full_password.value)<=7:
             code_button.disabled=True
             full_email.read_only=True
             full_password.read_only=True
             full_password_cunform.read_only=True
             full_name.read_only=True
             have_account_button.disabled=True
             page.update()
             Toast(tetx="Please Enter a strong Password",colors_=colors.RED)
        elif " " in full_password.value:
             code_button.disabled=True
             full_email.read_only=True
             full_password.read_only=True
             full_password_cunform.read_only=True
             full_name.read_only=True
             have_account_button.disabled=True
             page.update()
             Toast(tetx="Please Do Tot Use a Space in Your Password",colors_=colors.RED)
        elif str(full_password.value)!=str(full_password_cunform.value):
             code_button.disabled=True
             full_email.read_only=True
             full_password.read_only=True
             full_password_cunform.read_only=True
             full_name.read_only=True
             have_account_button.disabled=True
             page.update()
             Toast(tetx="Please Confirm Your Password",colors_=colors.RED)
        elif full_password.value==full_password_cunform.value and len(full_name.value.split())>=2 and "@" in full_email.value and ".com" in full_email.value and full_password.value.replace(" ","")!="" and len(full_password.value)>=7 and not " " in full_password.value:
            try:
                par.value=None
                code_button.disabled=True
                full_email.read_only=True
                full_password.read_only=True
                full_password_cunform.read_only=True
                full_name.read_only=True
                have_account_button.disabled=True
                page.update()
                ch1d = random.choices(population=num,k=7)
                ch2d = str(ch1d).replace("']","").replace("',","").replace("'","").replace("['","").replace("[","").replace(" ","")
                subject = "Mostafa Ai"
                body = f"For Confirm You Email Use The Code \"{ch2d}\", you can ignore this message with all \nThanks Team Mostafa Ai"
                massage = "subject : {}\n\n{}".format(subject,body)
                mm = full_email.value.replace(" ","").strip()
                print(ch2d)
                server.sendmail("mostafaaipro33@gmail.com",f"{mm}",massage)
                code = TextField(border_color=colors.WHITE,expand=True,expand_loose=True)
                dlg.content=Text(size=9,value="Enter the code that was sent to you email : " + full_email.value.replace(" ",""))
                ok_button=TextButton("Ok",on_click=lambda _: des("True"))
                cancel_button=TextButton("cancel",on_click=lambda _: des("False"))
                dlg.actions=[code,Row([ok_button,cancel_button])]

                def des(what,*args):
                    if what=="False":
                        
                        page.close(dlg)
                        page.update()
                    elif what=="True":
                        ok_button.disabled=True
                        cancel_button.disabled=True
                        code.disabled=True
                        page.update()
                        if str(code.value).strip()==ch2d.strip():
                            try:
                                page.open(dlg)
                                par.value=None
                                code_button.disabled=True
                                full_email.read_only=True
                                full_password.read_only=True
                                full_password_cunform.read_only=True
                                full_name.read_only=True
                                have_account_button.disabled=True
                                page.update()
                                supabase.auth.admin.create_user({
                                    'email': str(full_email.value),
                                    'password': str(full_password.value),
                                    'user_metadata': {
                                        'name': str(full_name.value),
                                        'password': str(full_password_cunform.value),
                                        'email': str(full_email.value)
                                    }
                                })


                                open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="w").write(f"email : {full_email.value} password : {full_password.value} Name : {full_name.value}")
                                page.update()
                                time.sleep(1)
                                file_=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read()
                                email_=file_.split()[2]
                                paass=file_.split()[5]
                                full_name_=file_.replace(f"email : {email_} password : {paass} Name : ","")
                                old_pass=file_.split()[5]
                                password_new.value=old_pass
                                page.update()
                                page_5.content=Column(expand=True,controls=[Container(alignment=alignment.top_left,expand=False,padding=0,content=Column(controls=[Text(""),Text(""),IconButton(icon=icons.ARROW_BACK,on_click=lambda _: page.go('/page_1'))])),Container(alignment=alignment.top_center,padding=-10,content=Icon(name=icons.PERSON,color=colors.WHITE,size=150)),Container(expand=True,padding=10,content=Column(expand=True,controls=[TextField(border_color=colors.WHITE,label="Email",value=email_,read_only=True,text_size=15),Row(controls=[TextField(border_color=colors.WHITE,expand=True,label="Full Name",value=full_name_,read_only=True,width=220)]),Row(controls=[password_new,IconButton(icon=icons.MODE,on_click=change)]),Container(alignment=alignment.top_center,padding=10,content=Column(alignment=alignment.top_center,controls=[Container(alignment=alignment.top_center,content=ElevatedButton(text="save",on_click=lambda _: threading.Thread(daemon=True,target=save(old_password=old_pass,name_user=file_.replace(f"email : "+file_.split()[2]+" password : "+file_.split()[5]+ " Name : ",""))).start())),Container(alignment=alignment.top_center,content=ElevatedButton(text="Log out",on_click=Log_out))]))]))])
                                page.update()
                                page.close(dlg)
                                page.update()
                                Toast(colors_=colors.GREEN_100,tetx="Done!")
                                page.go('/page_1')
                                global User
                                User=full_name.value
                                
                            except Exception as er:
                                    pop_=supabase.auth.admin.list_users()
                                    for user in pop_:
                                        if user.email==full_email.value:
                                            Toast(tetx="Email Is Already Exists Try Autre Email",colors_=colors.RED)
                                            page.close(dlg)
                                            page.update()
                                            full_email.value=""
                                            code_button.disabled=False
                                            full_email.read_only=False
                                            full_password.read_only=False
                                            full_password_cunform.read_only=False
                                            full_name.read_only=False
                                            have_account_button.disabled=False
                                            par.value=0.0
                                            page.update()    
                        elif str(code.value).strip()!=ch2d.strip():
                                page.open(dlg)
                                page.update()
                                Toast(tetx="Code is Wrong",colors_=colors.RED)
                    ok_button.disabled=False
                    cancel_button.disabled=False
                    code.disabled=False
                    page.update()
                
                page.open(dlg)
                page.update()
            except smtplib.SMTPConnectError:
                 Toast(tetx="Try Agrain Layter",colors_=colors.RED)
            except smtplib.SMTPNotSupportedError:
                 Toast(tetx="Try Agrain Layter",colors_=colors.RED)

            except Exception as error_1:
                 if "codec can't encode character" in str(error_1):
                      Toast(tetx="Try Agrain !",colors_=colors.RED)
                 else:
                    print(error_1)
                    Toast(tetx=f"{error_1}",colors_=colors.RED)
                    page.open(dlg)
                    page.update()
                    code_button.disabled=False
                    full_email.read_only=False
                    full_password.read_only=False
                    full_password_cunform.read_only=False
                    full_name.read_only=False
                    have_account_button.disabled=False
                    par.value=0.0
                    page.update()
            par.value=0.0
            page.update()
        code_button.disabled=False
        full_email.read_only=False
        full_password.read_only=False
        full_password_cunform.read_only=False
        full_name.read_only=False
        have_account_button.disabled=False
        par.value=0.0
        page.update()
    def have_account(*args):
        full_name.value="";full_email.value="";full_password.value="";full_password_cunform.value=""
        page.go('/home')
        page.update()
         #page_2.offset=transform.Offset(-2, 0)
         
    def sign_up(*args):
        page.go('/page_2')
        page.update()
    #page.add(inpu)

    #page.add(et)




    def update_user(*args):
        if forget_email.value!="" and forget_email.value.replace(" ","")!="" and "@" in forget_email.value and ".com" in forget_email.value:
            z = False
            for usern in users_response:
                if forget_email.value==usern.email:
                    def buttons_dlg(name,*args):
                        if name=="Ok":
                            
                            page.close(update_user_dlg)
                            page.update()
                            if number_1==email_get_code.value:
                                page.go('/page_4')
                            elif number_1!=email_get_code.value:
                                Toast(tetx="Error The Code is incorrect",colors_=colors.RED)

                        elif name=="Cancel":
                            page.close(update_user_dlg)
                            forget_email.disabled=False
                            Ok_button_.disabled=False
                            page.update()
                    try:
                        forget_email.disabled=True
                        Ok_button_.disabled=True
                        page.update()
                        #googletrans.Translator().translate(text="hello",dest='en',src="en")
                        
                        
                        update_user_dlg.actions=[Container(padding=10,alignment=alignment.top_left,content=Column(expand=True,controls=[Text(f"Enter the code that was sent to you email {forget_email.value}",max_lines=99,size=9),email_get_code,Row([TextButton("Ok",on_click=lambda _: buttons_dlg("Ok")),TextButton("Cancel",on_click=lambda _: buttons_dlg("Cancel"))])]))]
                        page.update()
                        number = random.choices(population=num,k=7)
                        number_1 = str(number).replace("']","").replace("',","").replace("'","").replace("['","").replace("[","").replace(" ","")
                        subject_1 = "Mostafa Ai"
                        body_1 = f"To change the password, copy the following code \"{number_1}\" and paste it into the input field. If you do not request this procedure, you can ignore this message with all \nThanks Team Mostafa Ai"
                        massage_1 = "subject : {}\n\n{}".format(subject_1,body_1)
                        mm_1 = forget_email.value.replace(" ","").strip()
                        print(number_1)
                        server.sendmail("mostafaaipro33@gmail.com",f"{mm_1}",massage_1)
                        page.open(update_user_dlg)
                        page.update()
                    except Exception as error_2:
                        if "codec can't encode character" in str(error_2):
                                Toast(tetx="Try Agrain !",colors_=colors.RED)
                        else:
                            Toast(tetx=error_2,colors_=colors.RED)
                        forget_email.disabled=False
                        Ok_button_.disabled=False
                        page.update()
                elif not forget_email.value in str(users_response):
                    Toast(tetx="Error It email not found",colors_=colors.RED) 
        else:
            Toast(tetx="Please Enter Email",colors_=colors.RED)
            forget_email.disabled=False
            Ok_button_.disabled=False
            page.update()


    page.window.bgcolor=colors.BLACK
    page.bgcolor=colors.RED
    def account(*args):
        page.go('/page_5')
    email_get_code=TextField(border_color=colors.WHITE,hint_text="Enter Code")
    prog=ProgressBar(expand=True,expand_loose=True,value=0.0,bgcolor="white_20",color="black",bar_height=3,scale=1.99)
    cc1 = Container(expand_loose=True,content=Column(expand=True,controls=[Container(content=prog,padding=1),Text(""),Text(''),Text(""),Row(alignment=MainAxisAlignment.CENTER,controls=[Text(italic=True,color=colors.WHITE,value="Login",weight=FontWeight.W_900,size=30)]),Text("")]),padding=0,alignment=alignment.top_center)
    email = TextField(border_color=colors.WHITE,color=colors.WHITE,border_radius=20,height=70,hint_text="Type Here...",label="Email",prefix_icon=icons.EMAIL)
    password = TextField(border_color=colors.WHITE,border_radius=20,show_cursor=True,can_reveal_password=True,height=70,hint_text="Type Here...",label="Password",password=True,prefix_icon=icons.PASSWORD)
    #txt_1=Container(padding=0,expand=True,alignment=alignment.top_center,content=Column([Text(weight=FontWeight.BOLD,size=23,value=" ˗ˏˋ꒰Mostafa Ai꒱ˎˊ˗          ")]))#,italic=True,text_align=TextAlign.CENTER,size=23,theme_style=TextThemeStyle.LABEL_LARGE,weight=FontWeight.W_900
    txt_1=Container(padding=0,expand=True,alignment=alignment.top_center,content=Column([Text(weight=FontWeight.BOLD,size=23,value="˗ˏˋ꒰ Mostafa Ai ꒱ˎˊ˗",text_align=TextAlign.CENTER)]))
    ic=IconButton(icon=icons.DENSITY_MEDIUM_OUTLINED)
    et1_1=SafeArea(content=Container(content=Row(controls=[txt_1],alignment=MainAxisAlignment.CENTER),height=50))
    #et1_1=SafeArea(content=Container(content=Row(controls=[ic,txt_1],alignment=MainAxisAlignment.CENTER),height=50))
    com1 = Dropdown(height=60,border_radius=23,content_padding=20,alignment=alignment.top_center,focused_border_color=colors.AMBER,border_color=colors.WHITE,hint_text="Chosse Longuage",options=[dropdown.Option(text="Arabic"),dropdown.Option(text="French"),dropdown.Option(text="English")],suffix_icon=icons.LANGUAGE)
    dlg = AlertDialog(modal=True,title=Text(size=14,value="Please confirm"))
    txt2 = CupertinoTextField(read_only=True,multiline=True,text_size=13,expand=True,border_radius=23,bgcolor=colors.BLACK,color=colors.WHITE)
    txt1 = CupertinoTextField(border_radius=23,placeholder_text="Type What You Need...!",width=page.window.width*0.7,expand=True,height=60)
    bt = IconButton(icon=icons.SEND,on_click=wek)
    et = SafeArea(Column(alignment=MainAxisAlignment.CENTER,controls=[Row(controls=[txt1,bt],expand=True),Text("")]))
    bt1 = ElevatedButton(color=colors.BLACK,bgcolor=colors.BLUE_100,text="Login",on_click=login)
    full_name=TextField(border_color=colors.WHITE,label="Full Name",hint_text="Enter Full Name here",border_radius=20,prefix_icon=icons.PERSON)
    full_email=TextField(border_color=colors.WHITE,hint_text="Enter email here",border_radius=20,label="Email",prefix_icon=icons.EMAIL)
    full_password=TextField(border_color=colors.WHITE,label="Password",password=True,can_reveal_password=True,prefix_icon=icons.PASSWORD,hint_text="Enter your password here",border_radius=20)
    full_password_cunform=TextField(border_color=colors.WHITE,label="Confirm Password",password=True,can_reveal_password=True,prefix_icon=icons.PASSWORD,hint_text="Confirm the password",border_radius=20)
    code_button=ElevatedButton(text="Crée account",icon=icons.PERSON,on_click=crée_user)
    have_account_button=TextButton(on_click=have_account,expand=True,text="You Already have Account ?")
    par=ProgressBar(width=400, bgcolor="white_20",color="black",value=0.0)
    forget_button=TextButton(text="Forget Password?",on_click=lambda _: page.go('/page_3'))
    Sign_up_button=ElevatedButton(text="Sign up",icon=icons.PERSON,on_click=sign_up)
    forget_email=TextField(border_color=colors.WHITE,border_radius=23,hint_text="Enter You Email Here",hint_style=TextStyle(size=14,italic=True,weight=FontWeight.W_900),label="Email",label_style=TextStyle(weight=FontWeight.BOLD),prefix_icon=icons.EMAIL)
    update_user_dlg=AlertDialog(modal=True,title=Text(size=14,value="Please confirm"))
    def run__(*args):
        full_password_new.value=""
        full_password.value=""
        page.go("/home")
        page.update()
    have_account_button_new=TextButton(expand=True,text="Login With Password ?",on_click=run__)
    
    full_password_new=TextField(border_color=colors.WHITE,label="New Password",password=True,can_reveal_password=True,prefix_icon=icons.PASSWORD,hint_text="Enter your password here",border_radius=20)
    full_password_cunform_new=TextField(border_color=colors.WHITE,label="Confirm Password",password=True,can_reveal_password=True,prefix_icon=icons.PASSWORD,hint_text="Confirm the password",border_radius=20)
    Ok_button_=ElevatedButton(text="Next",on_click=update_user)
    try:
        password_new=TextField(border_color=colors.WHITE,expand=True,label="Password",value=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().split()[5],read_only=True,width=220,password=True,can_reveal_password=True)
    except:
        full_new_name=TextField(border_color=colors.WHITE,expand=True,label="Full Name",read_only=True,width=220)
        password_new =TextField(border_color=colors.WHITE,expand=True,label="Password",read_only=True,width=220,password=True,can_reveal_password=True)

    page.update()
    def save(old_password,name_user,*args):
        try:            
            password_new.read_only=True
            page.update()
            email_new = open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r",encoding="utf-8").read().split()[2]
            
            for user in users_response:
                if user.email==email_new:
                    passwo = getattr(user,"user_metadata",{})
                    if "password" in passwo:
                        print(user.id)
                        supabase.auth.admin.update_user_by_id(uid=user.id,attributes={'password': password_new.value,'user_metadata':{
                                                'name': name_user,
                                                'password':password_new.value,
                                                'email':email_new}})                   #uid=name_user,password=password_new.value,display_name=password_new.value)
                        Toast(tetx="Done !",colors_=colors.GREEN)
                        page.update()
                        
                        open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="w").write(f"email : {email_new} password : {password_new.value} Name : {name_user}")
        except Exception as error_2_1:
            if "Connection" in str(error_2_1):
                Toast(tetx="You Dont Have Internet",colors_=colors.RED)
                page.update()
                password_new.read_only=False
                page.update()
                password_new.value=old_password
                password_new.read_only=True
                page.update()
            else:
                Toast(tetx=f"{error_2_1}",colors_=colors.RED)
                page.update()
                password_new.read_only=False
                page.update()
                password_new.value=old_password
                password_new.read_only=True
                page.update()
            print(error_2_1)
            
    def change(*args):
        try:
            password_new.read_only=False
            page.update()
        except Exception as error_3:
            Toast(tetx=error_3,colors_=colors.RED)
    def Log_out(*args):
        if os.path.exists(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll")):
            os.remove(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"))
            supabase.auth.sign_out()

            email.disabled=False
            password.disabled=False
            forget_button.disabled=False
            bt1.disabled=False
            prog.value=0.0
            Sign_up_button.disabled=False
            forget_button.disabled=False
            page.update()
            page.go("/home")
        else:
            page.go("/home")            
            email.value=""
            password.value=""
            password.read_only=False
            email.read_only=False
            bt1.disabled=False
            Sign_up_button.disabled=False
            forget_button.disabled=False
            prog.value=0.0
            page.update()
    def done_new_password(*args):
        try:                
            code_button_new.disabled=True
            full_password_cunform_new.disabled=True
            full_password_new.disabled=True
            have_account_button_new.disabled=True
            page.update()
            if full_password_new.value.replace(" ","")!="" and full_password_cunform_new.value.replace(" ","")!="" and full_password_new.value==full_password_cunform_new.value and not " " in full_password_new.value:
                
                for us in users_response:
                    if us.email==forget_email.value:
                        name_=getattr(us,"user_metadata",{})
                        supabase.auth.admin.update_user_by_id(uid=us.id,attributes={'password':full_password_new.value,'user_metadata':{
                            'password':full_password_new.value
                        }})
                    
                        Toast(tetx="Login secssec",colors_=colors.GREEN)
                        page.go('/page_1')
                        open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="w").write(f"email : {forget_email.value} password : {full_password_cunform_new.value} Name : {name_["name"]}")
                        global User
                        
                        file_=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read()
                        email_=file_.split()[2]
                        paass=file_.split()[5]
                        full_name_=file_.replace(f"email : {email_} password : {paass} Name : ","")
                        old_pass=file_.split()[5]
                            
                        page_5.content=Column(expand=True,controls=[Container(alignment=alignment.top_left,expand=False,padding=0,content=Column(controls=[Text(""),Text(""),IconButton(icon=icons.ARROW_BACK,on_click=lambda _: page.go('/page_1'))])),Container(alignment=alignment.top_center,padding=-10,content=Icon(name=icons.PERSON,color=colors.WHITE,size=150)),Container(expand=True,padding=10,content=Column(expand=True,controls=[TextField(border_color=colors.WHITE,label="Email",value=email_,read_only=True,text_size=15),Row(controls=[TextField(border_color=colors.WHITE,expand=True,label="Full Name",value=full_name_,read_only=True,width=220)]),Row(controls=[password_new,IconButton(icon=icons.MODE,on_click=change)]),Container(alignment=alignment.top_center,padding=10,content=Column(alignment=alignment.top_center,controls=[Container(alignment=alignment.top_center,content=ElevatedButton(text="save",on_click=lambda _: threading.Thread(daemon=True,target=save(old_password=old_pass,name_user=file_.replace(f"email : "+file_.split()[2]+" password : "+file_.split()[5]+ " Name : ",""))).start())),Container(alignment=alignment.top_center,content=ElevatedButton(text="Log out",on_click=Log_out))]))]))])
                        #page_5.content=Column(expand=True,controls=[Container(alignment=alignment.top_left,expand=False,padding=0,content=IconButton(icon=icons.ARROW_BACK,on_click=lambda _: page.go('/page_1'))),Container(alignment=alignment.top_center,padding=-10,content=Icon(name=icons.PERSON,color=colors.WHITE,size=150)),Container(expand=True,padding=10,content=Column(expand=True,controls=[TextField(border_color=colors.WHITE,label="Email",value=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().split()[2],read_only=True,width=page.width,text_size=15),Row(controls=[TextField(border_color=colors.WHITE,expand=True,label="Full Name",value=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().replace(f"email : {open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().split()[2]} password : {open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().split()[5]} Name : ",""),read_only=True,width=220)]),Row(controls=[password_new,IconButton(icon=icons.MODE,on_click=change)]),Container(alignment=alignment.top_center,padding=10,content=ElevatedButton(text="save",on_click=lambda _: threading.Thread(daemon=True,target=save(old_password=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().split()[5],name_user=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().replace(f"email : "+open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().split()[2]+" password : "+open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().split()[5]+ " Name : ",""))).start()))]))])
                        time.sleep(1)
                        password_new.value=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().split()[5]
            elif full_password_new.value.replace(" ","")=="":
                Toast(tetx="Please Enter Password",colors_=colors.RED)
            elif len(full_password_new.value)<=7:
                Toast(tetx="Please Enter a strong Password",colors_=colors.RED)
            elif " " in full_password_new.value:
                Toast(tetx="Please Do Tot Use a Space in Your Password",colors_=colors.RED)
            elif full_password_new.value!=full_password_cunform_new.value:
                Toast(tetx="Please Confirm Your Password",colors_=colors.RED)
        except :
            Toast(tetx="You Dont Have Internet",colors_=colors.RED)
        full_password_cunform_new.disabled=False
        code_button_new.disabled=False
        full_password_new.disabled=False
        have_account_button_new.disabled=False
        page.update()
    code_button_new=ElevatedButton(text="Ok",on_click=done_new_password)
    #dlg_new1=AlertDialog(bgcolor=colors.GREY_900,title=Text('Info'),content=Column(height=190,alignment=MainAxisAlignment.END,expand=True,controls=[Container(alignment=alignment.top_center,content=Row([Icon(name=icons.SMART_DISPLAY,color=colors.RED,expand=True),Text(value='Link Channel Youtube')],alignment=MainAxisAlignment.CENTER)),Container(Row(alignment=MainAxisAlignment.END,controls=[Icon(name=icons.WALLET,color=colors.WHITE,expand=True),Text('Support Me               ')])),Container(Row([Icon(name=icons.PERSON,color=colors.WHITE,expand=True),Text('Information About\nYour Account             ')])),Container(Row([Icon(name=icons.DOWNLOADING_ROUNDED,color=colors.WHITE,expand=True),Text('Download Autre App\nAnd Update Mostafa\nAi')])),Container(Row([Icon(name=icons.FACEBOOK,color=colors.BLUE_ACCENT_700,expand=True),Text('Link Page Facebook  ')]))]))
    page_1 = Container(image_src='assets/image.png',image_fit=ImageFit.FILL,bgcolor=colors.BACKGROUND,border_radius=23,expand=True,expand_loose=True,padding=7,alignment=alignment.top_center,content=Column(controls=[Text(""),Container(border_radius=30,height=38,content=Row(expand=True,alignment=MainAxisAlignment.CENTER,controls=[IconButton(icon=icons.SMART_DISPLAY,on_click=lambda _: main_1(name_link="link youtube"),icon_color=colors.RED,expand=True),IconButton(expand=True,icon=icons.WALLET,icon_color=colors.WHITE,on_click=lambda _: threading.Thread(daemon=True,target=main_1(name_link="link paypal")).start()),IconButton(expand=True,icon=icons.PERSON,icon_color="white",on_click=account),IconButton(expand=True,icon=icons.DOWNLOADING_ROUNDED,icon_color="white",on_click=lambda _: threading.Thread(daemon=True,target=main_1(name_link="link app")).start()),IconButton(expand=True,icon=icons.FACEBOOK,icon_color=colors.BLUE_ACCENT_700,on_click=lambda _: threading.Thread(daemon=True,target=main_1(name_link="link facebook")).start())]),bgcolor=colors.GREY_500),et1_1,com1,Container(border_radius=23,content=Column(controls=[txt2,et],expand=True),expand=True)],expand=True))
    page_2 = Container(image_src="assets/image.png",image_fit=ImageFit.FILL,expand=True,expand_loose=True,bgcolor=colors.CYAN_800,content=Column(expand=True,controls=[par,Container(content=Column(controls=[Text(""),Text(""),Row(alignment=MainAxisAlignment.CENTER,controls=[Icon(icons.PERSON),Text(size=23,value="Crée Account",weight=FontWeight.BOLD)])]),alignment=alignment.center),Container(alignment=alignment.top_center,padding=10,content=Column(expand=True,controls=[full_name,full_email,full_password,full_password_cunform])),Container(padding=0,content=have_account_button),Container(alignment=alignment.center,content=code_button)]))
    page_3=Container(image_src="assets/image.png",image_fit=ImageFit.FILL,alignment=alignment.top_center,bgcolor=colors.BLUE,expand=True,expand_loose=True,content=Column(expand=True,controls=[Text(''),Text(''),Container(alignment=alignment.top_left,content=IconButton(icon=icons.ARROW_CIRCLE_LEFT_OUTLINED,on_click=lambda _: page.go('/home'))),Text("\n\n"),Container(alignment=alignment.top_center,padding=10,content=Row(alignment=MainAxisAlignment.CENTER,controls=[Text(value="Forgot Password",italic=True,visible=True,rtl=True,size=15,weight=FontWeight.W_900)])),Container(padding=20,content=Column(expand=True,controls=[forget_email])),Container(alignment=alignment.top_center,content=Ok_button_)]))
    page_4=Container(image_src="assets/image.png",image_fit=ImageFit.FILL,expand=True,expand_loose=True,bgcolor=colors.CYAN_800,content=Column(expand=True,controls=[par,Container(content=Column(controls=[Text(""),Text(""),Text(""),Text(""),Row(alignment=MainAxisAlignment.CENTER,controls=[Icon(icons.PERSON),Text(size=23,value="Change Password",weight=FontWeight.BOLD)])]),alignment=alignment.center),Column(expand=True,controls=[Container(padding=10,content=Column(expand=True,controls=[full_password_new,full_password_cunform_new,Container(padding=0,content=have_account_button_new),Container(alignment=alignment.center,content=code_button_new)]))])]))
    page_5=Container(image_src="assets/image.png",image_fit=ImageFit.FILL,expand_loose=True,bgcolor=colors.BLUE,content=Column(expand=True,controls=[Container(alignment=alignment.top_left,expand=False,padding=0,content=Column(controls=[Text(""),Text(""),IconButton(icon=icons.ARROW_BACK,on_click=lambda _: page.go('/page_1'))])),Container(alignment=alignment.top_center,padding=-10,content=Icon(name=icons.PERSON,color=colors.WHITE,size=150)),Container(expand=True,padding=10,content=Column(expand=True,controls=[TextField(border_color=colors.WHITE,label="Email",read_only=True,text_size=15),Row(controls=[TextField(border_color=colors.WHITE,expand=True,label="Full Name",read_only=True,width=220)]),Row(controls=[password_new,IconButton(icon=icons.MODE,on_click=change)]),Container(alignment=alignment.top_center,padding=10,content=Column(alignment=alignment.top_center,controls=[Container(alignment=alignment.top_center,content=ElevatedButton(text="save")),Container(alignment=alignment.top_center,content=ElevatedButton(text="Log out",on_click=Log_out))]))]))]),alignment=alignment.top_center,expand=True)
    tc = Container(image_src="assets/image.png",image_fit=ImageFit.FILL,expand=True,content=Column(expand=True,controls=[cc1,Container(content=Column(expand=True,controls=[email,password,forget_button]),padding=8),Container(Column([bt1]),alignment=alignment.center,padding=0),Container(content=Column([Sign_up_button],expand=True),alignment=alignment.center,padding=0)]),bgcolor=colors.CYAN)
    def route_change(route):
        page.views.clear()
        page.views.append(
            View(padding=0,route="/home",controls=[tc]))
        if page.route=='/page_2':
             page.views.append(
                  View(padding=0,route='/page_2',controls=[page_2])
             )
        elif page.route=='/page_1':
            page.views.append(
                  View(padding=0,route='/page_1',controls=[page_1])
             )  
        elif page.route=='/page_3':
            page.views.append(
                  View(padding=0,route='/page_3',controls=[page_3])
             )      
        elif page.route=='/page_4':
            page.views.append(
                  View(padding=0,route='/page_4',controls=[page_4])
             )
        elif page.route=='/page_5':
            page.views.append(
                  View(padding=0,route='/page_5',controls=[page_5])
             )
        page.update()
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    page.on_route_change = route_change
    #page.on_view_pop = view_pop
    #page.add(page_1)f
    page.go("/home")
    
    if not os.path.exists(os.path.abspath("Mostafa Ai")):
        os.mkdir(os.path.abspath("Mostafa Ai"))
    #print(page.window_width)
    if os.path.exists(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll")):
            def firt_login(*args):
                try:
                    while True:
                        
                        
                        email.disabled=True
                        password.disabled=True
                        forget_button.disabled=True
                        bt1.disabled=True
                        prog.value=None
                        
                        Sign_up_button.disabled=True
                        forget_button.disabled=True
                        page.update()
                        deep_translator.GoogleTranslator(source="en",target="ar").translate("hello")
                        global account_cookie
                        account_cookie = open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read()
                        global email_cookie
                        email_cookie = str(account_cookie).split()[2]
                        
                       
                        for user in users_response:
                            if user.email==email_cookie:
                                global account_cookie_2,account_cookie_3
                                account_cookie_2 = getattr(user,"user_metadata",{})
                                if "password" in account_cookie_2:
                                    account_cookie_3 = account_cookie_2['password']

                        password_cookie = str(account_cookie).split()[5].replace(' ',"").replace("\n","")
                        
                        print(str(email_cookie),str(password_cookie))
                        if not "@" in str(account_cookie):
                            if os.path.exists(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll")):
                                    os.remove(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"))
                                    email.disabled=False
                                    password.disabled=False
                                    forget_button.disabled=False
                                    bt1.disabled=False
                                    prog.value=0.0
                                    Sign_up_button.disabled=False
                                    forget_button.disabled=False
                                    page.update()
                                    page.go("/home")
                                    break
                        elif not "password" in str(account_cookie).lower():
                            if os.path.exists(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll")):
                                    os.remove(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"))
                                    email.disabled=False
                                    password.disabled=False
                                    forget_button.disabled=False
                                    bt1.disabled=False
                                    prog.value=0.0
                                    Sign_up_button.disabled=False
                                    forget_button.disabled=False
                                    page.update()
                                    page.go("/home")
                                    break
                        elif not "email" in str(account_cookie).lower():
                            if os.path.exists(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll")):
                                    os.remove(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"))
                                    email.disabled=False
                                    password.disabled=False
                                    forget_button.disabled=False
                                    bt1.disabled=False
                                    prog.value=0.0
                                    Sign_up_button.disabled=False
                                    forget_button.disabled=False
                                    page.update()
                                    page.go("/home")
                                    break
                        elif not "name" in str(account_cookie).lower():
                            if os.path.exists(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll")):
                                    os.remove(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"))
                                    email.disabled=False
                                    password.disabled=False
                                    forget_button.disabled=False
                                    bt1.disabled=False
                                    prog.value=0.0
                                    Sign_up_button.disabled=False
                                    forget_button.disabled=False
                                    page.update()
                                    page.go("/home")
                                    break
                        elif not ":" in account_cookie:
                            if os.path.exists(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll")):
                                    os.remove(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"))
                                    email.disabled=False
                                    password.disabled=False
                                    forget_button.disabled=False
                                    bt1.disabled=False
                                    prog.value=0.0
                                    Sign_up_button.disabled=False
                                    forget_button.disabled=False
                                    page.update()
                                    page.go("/home")
                                    break
                        elif ":" in str(account_cookie) and "name" in str(account_cookie).lower() and "@" in str(account_cookie) and ".com" in str(account_cookie) and "password" in str(account_cookie).lower() and "email" in str(account_cookie).lower():
                            if str(account_cookie_3)!=str(password_cookie):
                                if os.path.exists(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll")):
                                        os.remove(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"))
                                        email.disabled=False
                                        password.disabled=False
                                        forget_button.disabled=False
                                        bt1.disabled=False
                                        prog.value=0.0
                                        Sign_up_button.disabled=False
                                        forget_button.disabled=False
                                        page.update()
                                        page.go("/home")
                                        break
                            elif account_cookie_3==password_cookie:
                                    global User
                                    file_=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read()
                                    email_=file_.split()[2]
                                    paass=file_.split()[5]
                                    full_name_=file_.replace(f"email : {email_} password : {paass} Name : ","")
                                    old_pass=file_.split()[5]
                                
                                    page_5.content=Column(expand=True,controls=[Container(alignment=alignment.top_left,expand=False,padding=0,content=Column(controls=[Text(""),Text(""),IconButton(icon=icons.ARROW_BACK,on_click=lambda _: page.go('/page_1'))])),Container(alignment=alignment.top_center,padding=-10,content=Icon(name=icons.PERSON,color=colors.WHITE,size=150)),Container(expand=True,padding=10,content=Column(expand=True,controls=[TextField(border_color=colors.WHITE,label="Email",value=email_,read_only=True,text_size=15),Row(controls=[TextField(border_color=colors.WHITE,expand=True,label="Full Name",value=full_name_,read_only=True,width=220)]),Row(controls=[password_new,IconButton(icon=icons.MODE,on_click=change)]),Container(alignment=alignment.top_center,padding=10,content=Column(alignment=alignment.top_center,controls=[Container(alignment=alignment.top_center,content=ElevatedButton(text="save",on_click=lambda _: threading.Thread(daemon=True,target=save(old_password=old_pass,name_user=file_.replace(f"email : "+file_.split()[2]+" password : "+file_.split()[5]+ " Name : ",""))).start())),Container(alignment=alignment.top_center,content=Container(alignment=alignment.top_center,content=ElevatedButton(text="Log out",on_click=Log_out)))]))]))])
                                    password_new.value=account_cookie_3
                                    page.update()
                                    password.read_only=False
                                    email.read_only=False
                                    bt1.disabled=False
                                    Sign_up_button.disabled=False
                                    forget_button.disabled=False
                                    prog.value=0.0
                                    page.update()
                                    
                                    open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="w").write(f"email : {email_cookie} password : {password_cookie} Name : {account_cookie_2['name']}")
                                    User=account_cookie_2["name"]
                                    #full_new_name.value=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().replace(f"email : {open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().split()[2]} password : {open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read().split()[5]} Name : ","")
                                    page.go('/page_1')
                                    print("good")
                                    break
                            password.read_only=False
                            email.read_only=False
                            bt1.disabled=False
                            Sign_up_button.disabled=False 
                            forget_button.disabled=False
                            prog.value=0.0
                            page.update()
                except IndexError as er:
                    print(er)
                    if os.path.exists(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll")):
                        os.remove(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"))
                        email.disabled=False
                        password.disabled=False
                        forget_button.disabled=False
                        bt1.disabled=False
                        prog.value=0.0
                        Sign_up_button.disabled=False
                        forget_button.disabled=False
                        page.update()
                        page.go("/home")
                                    
                except Exception as error:
                            
                            email.disabled=False
                            password.disabled=False
                            bt1.disabled=False
                            forget_button.disabled=False
                            prog.value=0.0
                            Sign_up_button.disabled=False
                            forget_button.disabled=False
                            page.update()
                            page.go("/page_1")
                            #global User
                            user_name=open(os.path.abspath("Mostafa Ai/𓆩Mostafa_Ai𓆪.dll"),mode="r").read()
                            email_cookie_new = str(user_name).split()[2]
                            password_cookie_new = str(user_name).split()[5]
                            print(email_cookie_new,password_cookie_new)
                            User = user_name.replace(f"email : {email_cookie_new} password : {password_cookie_new} Name : ","")
                            
                            threading.Thread(daemon=True,target=firt_login).start()   

                   

            threading.Thread(daemon=True,target=firt_login).start()
    if os.path.exists(os.path.abspath("Mostafa Ai/link_Mostafa_Ai.dll")):
        try:
            file_1 = open(os.path.abspath("Mostafa Ai/link_Mostafa_Ai.dll"),mode="r")
            file = file_1.read()
            data = supabase.table("Mostafa Ai Links").select("Link Mostafa Ai").execute()
            link = data.data[0]["Link Mostafa Ai"]
            if str(file).replace(" ","")!="" and 'https://' in str(file).replace(" ","") and str(file)!=str(link):
                    
                    
                    dl = AlertDialog(title=Text("New Update !",text_align=TextAlign.CENTER),actions=[Container(alignment=alignment.top_center,content=Column(alignment=MainAxisAlignment.CENTER,controls=[Container(alignment=alignment.top_center,content=Text("Download Now !",text_align=TextAlign.CENTER,color=colors.GREEN_100)),Container(alignment=alignment.top_center,content=TextButton(icon=icons.DOWNLOAD,text="Download",on_click=lambda _: threading.Thread(daemon=True,target=main_1(name_link="link Mostafa Ai")).start()))]))])
                    page.open(dl)
                    open(os.path.abspath("Mostafa Ai/link_Mostafa_Ai.dll"),mode="w").write(f"{link}")
            elif str(file).replace(" ","")=="":
                    open(os.path.abspath("Mostafa Ai/link_Mostafa_Ai.dll"),mode="w").write(f"{link}")
        except Exception as ederr:
            print(ederr)
            print('feirufnie')
    elif not os.path.exists(os.path.abspath("Mostafa Ai/link_Mostafa_Ai.dll")):
                    try:
                        data = supabase.table("Mostafa Ai Links").select("Link Mostafa Ai").execute()
                        link = data.data[0]["Link Mostafa Ai"]
                        open(os.path.abspath("Mostafa Ai/link_Mostafa_Ai.dll"),mode="w").write(f"{link}")
                    except:
                         pass   
User=""
account_cookie_1=""
email_cookie=""

app(target=main,assets_dir="assets",view=AppView.FLET_APP)#python -m pip install -r C:\Users\ninja\Downloads\requirements.txt
