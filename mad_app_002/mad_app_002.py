# Version 000 of MAD's advertising app. Associated .kv file is mad_app_000.kv

# Import statements
import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class LoginScreen(Screen):
    # makes a basic login screen
    pass

class CreateAcctScreen(Screen):
    pass

class PasswordsDontMatchScreen(Screen):
    pass

class UsernameTakenScreen(Screen):
    pass

class EmailTakenScreen(Screen):
    pass

class RegistrationSuccessfulScreen(Screen):
    pass

class MainAcctScreen(Screen):
    pass

class InvalidCredentialsScreen(Screen):
    pass

class BusinessAccountScreen(Screen):
    pass

class AdvertiserAccountScreen(Screen):
    pass

class CustomerAccountScreen(Screen):
    pass

class CreateBusinessAccountScreen(Screen):
    pass

class CreateAdvertiserAccountScreen(Screen):
    pass

class CreateCustomerAccountScreen(Screen):
    pass

class BusinessRegistrationSuccessfulScreen(Screen):
    pass

class AdvertiserRegistrationSuccessfulScreen(Screen):
    pass

class CustomerRegistrationSuccessfulScreen(Screen):
    pass

class NotEnoughFundsToCashOutCustomerScreen(Screen):
    pass

class NotEnoughFundsToCashOutAdvertiserScreen(Screen):
    pass

class CashOutAdvertiserScreen(Screen):
    pass

class CashOutRequestSubmittedAdvertiserScreen(Screen):
    pass

class CashOutCustomerScreen(Screen):
    pass

class CashOutRequestSubmittedCustomerScreen(Screen):
    pass

class CustomerHistoryScreen(Screen):
    pass

class AdvertiserHistoryScreen(Screen):
    pass

class BusinessHistoryScreen(Screen):
    pass

class CreateAdScreen(Screen):
    pass

class PreviewAdScreen(Screen):
    pass

class AdPaymentScreen(Screen):
    pass

class AdRecordedScreen(Screen):
    pass

class ActiveAdsScreen(Screen):
    pass

class AdScreen(Screen):
    pass

class MainWidgetsAd(Widget):
    pass

class MainWidgetsActiveAds(Widget):
    pass

class MainWidgetsAdPayment(Widget):
    pass

class MainWidgetsPreviewAd(Widget):
    pass

class MainWidgetsLog(Widget):
    pass

class MainWidgetsCreate(Widget):
    pass

class MainWidgetsMainAcct(Widget):
    pass

class MainWidgetsBusinessAccount(Widget):
    pass

class MainWidgetsCreateBusinessAccount(Widget):
    pass

class MainWidgetsAdvertiserAccount(Widget):
    pass

class MainWidgetsCustomerAccount(Widget):
    pass

class MainWidgetsCreateAdvertiserAccount(Widget):
    pass

class MainWidgetsCashOutAdvertiser(Widget):
    pass

class MainWidgetsCashOutCustomer(Widget):
    pass

class MainWidgetsCreateCustomerAccount(Widget):
    pass

class MainWidgetsCustomerHistory(Widget):
    pass

class MainWidgetsAdvertiserHistory(Widget):
    pass

class MainWidgetsBusinessHistory(Widget):
    pass

class MainWidgetsCreateAd(Widget):
    pass

class MultilineTextInput(TextInput):
    pass

class LongButton(Button):
    pass

class AutoWrapLabel(Label):
    pass

class ScreenManagement(ScreenManager):
    pass

Builder.load_file('mad_app_002.kv')

sm = ScreenManager()
# add new screens as below
# except ones that call on input that has to be loaded in or input
# In that case, follow businessaccountscreen example
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(CreateAcctScreen(name='createacctscreen'))
sm.add_widget(PasswordsDontMatchScreen(name='passwordsdontmatchscreen'))
sm.add_widget(UsernameTakenScreen(name='usernametakenscreen'))
sm.add_widget(EmailTakenScreen(name='emailtakenscreen'))
sm.add_widget(RegistrationSuccessfulScreen(name='registrationsuccessfulscreen'))
sm.add_widget(MainAcctScreen(name='mainacctscreen'))
sm.add_widget(InvalidCredentialsScreen(name='invalidcredentialsscreen'))
#sm.add_widget(BusinessAccountScreen(name='businessaccountscreen'))
sm.add_widget(CreateBusinessAccountScreen(name='createbusinessaccountscreen'))
sm.add_widget(BusinessRegistrationSuccessfulScreen(name='businessregistrationsuccessfulscreen'))
#sm.add_widget(AdvertiserAccountScreen(name='advertiseraccountscreen'))
sm.add_widget(CreateAdvertiserAccountScreen(name='createadvertiseraccountscreen'))
sm.add_widget(AdvertiserRegistrationSuccessfulScreen(name='advertiserregistrationsuccessfulscreen'))
#sm.add_widget(CustomerAccountScreen(name='customeraccountscreen'))
sm.add_widget(CreateCustomerAccountScreen(name='createcustomeraccountscreen'))
sm.add_widget(CustomerRegistrationSuccessfulScreen(name='customerregistrationsuccessfulscreen'))
#sm.add_widget(CashOutAdvertiserScreen(name='cashoutadvertiserscreen'))
sm.add_widget(CashOutRequestSubmittedAdvertiserScreen(name='cashoutrequestsubmittedadvertiserscreen'))
#sm.add_widget(CashOutCustomerScreen(name='cashoutcustomerscreen'))
sm.add_widget(CashOutRequestSubmittedCustomerScreen(name='cashoutrequestsubmittedcustomerscreen'))
sm.add_widget(NotEnoughFundsToCashOutCustomerScreen(name='notenoughfundstocashoutcustomerscreen'))
sm.add_widget(NotEnoughFundsToCashOutAdvertiserScreen(name='notenoughfundstocashoutadvertiserscreen'))
#sm.add_widget(CustomerHistoryScreen(name='customerhistoryscreen'))
#sm.add_widget(AdvertiserHistoryScreen(name='advertiserhistoryscreen'))
#sm.add_widget(BusinessHistoryScreen(name='businesshistoryscreen'))
sm.add_widget(CreateAdScreen(name='createadscreen'))
#sm.add_widget(PreviewAdScreen(name='previewadscreen'))
sm.add_widget(AdPaymentScreen(name='adpaymentscreen'))
sm.add_widget(AdRecordedScreen(name='adrecordedscreen'))
#sm.add_widget(AdScreen(name='adscreen'))


class MADApp(App):
    # creates the app
    def build(self):
        return sm

    def create_account(self,new_username,new_email,new_password,new_verify_password):
        # method for creating an account. to be replaced in production Version
        # with something that communicates with a database
        new_username = new_username.strip()
        new_email = new_email.strip()
        new_password = new_password.strip()
        new_verify_password = new_verify_password.strip()
        if new_password != new_verify_password:
            self.root.current = 'passwordsdontmatchscreen'
            return
        else:
            f = open('login_info.csv','r')
            members = []
            for line in f:
                members.append(line.strip().split(','))
            f.close()
            # check to see if username or email already exists
            for member in members:
                if member[0] == new_username:
                    self.root.current = 'usernametakenscreen'
                    return
                if member[1] == new_email:
                    self.root.current = 'emailtakenscreen'
                    return
            members.append([new_username,new_email,new_password])
            members = '\n'.join([','.join(mem) for mem in members]) + '\n'
            g = open('login_info.csv','w')
            g.write(members)
            g.close()
            self.root.current = 'registrationsuccessfulscreen'
            return

    def verify_credentials(self,username,password):
        # logs the user in. to be replaced in the production Version
        # for a database function
        username = username.strip()
        password = password.strip()
        members = []
        f = open('login_info.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        for member in members:
            if member[0] == username and member[2] == password:
                self.username = username
                self.root.current = 'mainacctscreen'
                return
        self.root.current = 'invalidcredentialsscreen'
        return

    def get_business_account(self,username):
        # redirects user to their business account's screen or helps
        # them create one
        members = []
        f = open('mad_account_info_business.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        for member in members:
            if member[0] == username:
                # now assign the stuff to self.<> that we will display
                if not hasattr(self,'BAbusiness_name'):
                    self.BAbusiness_name = member[1]
                    self.BAowner = member[2]
                    self.BAaddress = member[3]
                    self.BAcity = member[4]
                    self.BAstate = member[5]
                    self.BAzip_code = member[6]
                    self.BAowed = member[7]
                    self.BAactive_ads = member[8]
                    sm.add_widget(BusinessAccountScreen(name='businessaccountscreen'))
                self.root.current = 'businessaccountscreen'
                return
        self.root.current = 'createbusinessaccountscreen'
        return

    def get_advertiser_account(self,username):
        # redirects user to their business account's screen or helps
        # them create one
        members = []
        f = open('mad_account_info_advertiser.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        for member in members:
            if member[0] == username:
                # now assign the stuff to self.<> that we will display
                if not hasattr(self,'AAname'):
                    self.AAname = member[1]
                    self.AAaddress = member[2]
                    self.AAcity = member[3]
                    self.AAstate = member[4]
                    self.AAzip_code = member[5]
                    self.AAbalance = member[6]
                    self.AAactive_ads = member[7]
                    sm.add_widget(AdvertiserAccountScreen(name='advertiseraccountscreen'))
                self.root.current = 'advertiseraccountscreen'
                return
        self.root.current = 'createadvertiseraccountscreen'
        return

    def get_customer_account(self,username):
        # redirects user to their business account's screen or helps
        # them create one
        members = []
        f = open('mad_account_info_customer.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        for member in members:
            if member[0] == username:
                # now assign the stuff to self.<> that we will display
                if not hasattr(self,'CAname'):
                    self.CAname = member[1]
                    self.CAaddress = member[2]
                    self.CAcity = member[3]
                    self.CAstate = member[4]
                    self.CAzip_code = member[5]
                    self.CAbalance = member[6]
                    self.CAcart_size = member[7]
                    sm.add_widget(CustomerAccountScreen(name='customeraccountscreen'))
                self.root.current = 'customeraccountscreen'
                return
        self.root.current = 'createcustomeraccountscreen'
        return

    def create_business_account(self,storage):
        # creates the user's business account
        business_name = str(storage.createbusinessaccount_business_name_text_input.text.strip())
        owner = str(storage.createbusinessaccount_owner_text_input.text.strip())
        address = str(storage.createbusinessaccount_address_text_input.text.strip())
        city = str(storage.createbusinessaccount_city_text_input.text.strip())
        state = str(storage.createbusinessaccount_state_text_input.text.strip())
        zip_code = str(storage.createbusinessaccount_zip_code_text_input.text.strip())
        self.BAbusiness_name = business_name
        self.BAowner = owner
        self.BAaddress = address
        self.BAcity = city
        self.BAstate = state
        self.BAzip_code = zip_code
        self.BAowed = '0.00'
        self.BAactive_ads = '0'
        members = []
        f = open('mad_account_info_business.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        members.append([self.username,business_name,owner,address,city,state,zip_code,self.BAowed,self.BAactive_ads])
        members = '\n'.join([','.join(mem) for mem in members]) + '\n'
        g = open('mad_account_info_business.csv','w')
        g.write(members)
        g.close()
        sm.add_widget(BusinessAccountScreen(name='businessaccountscreen'))
        self.root.current = 'businessregistrationsuccessfulscreen'
        return

    def create_advertiser_account(self,storage):
        # creates the user's business account
        name = str(storage.createadvertiseraccount_name_text_input.text.strip())
        address = str(storage.createadvertiseraccount_address_text_input.text.strip())
        city = str(storage.createadvertiseraccount_city_text_input.text.strip())
        state = str(storage.createadvertiseraccount_state_text_input.text.strip())
        zip_code = str(storage.createadvertiseraccount_zip_code_text_input.text.strip())
        self.AAname = name
        self.AAaddress = address
        self.AAcity = city
        self.AAstate = state
        self.AAzip_code = zip_code
        self.AAbalance = '0.00'
        self.AAactive_ads = '0'
        members = []
        f = open('mad_account_info_advertiser.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        members.append([self.username,name,address,city,state,zip_code,self.AAbalance,self.AAactive_ads])
        members = '\n'.join([','.join(mem) for mem in members]) + '\n'
        g = open('mad_account_info_advertiser.csv','w')
        g.write(members)
        g.close()
        sm.add_widget(AdvertiserAccountScreen(name='advertiseraccountscreen'))
        self.root.current = 'advertiserregistrationsuccessfulscreen'
        return

    def create_customer_account(self,storage):
        # creates the user's business account
        name = str(storage.createcustomeraccount_name_text_input.text.strip())
        address = str(storage.createcustomeraccount_address_text_input.text.strip())
        city = str(storage.createcustomeraccount_city_text_input.text.strip())
        state = str(storage.createcustomeraccount_state_text_input.text.strip())
        zip_code = str(storage.createcustomeraccount_zip_code_text_input.text.strip())
        self.CAname = name
        self.CAaddress = address
        self.CAcity = city
        self.CAstate = state
        self.CAzip_code = zip_code
        self.CAbalance = '0.00'
        self.CAcart_size = '0'
        members = []
        f = open('mad_account_info_customer.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        members.append([self.username,name,address,city,state,zip_code,self.CAbalance,self.CAcart_size])
        members = '\n'.join([','.join(mem) for mem in members]) + '\n'
        g = open('mad_account_info_customer.csv','w')
        g.write(members)
        g.close()
        sm.add_widget(CustomerAccountScreen(name='customeraccountscreen'))
        self.root.current = 'customerregistrationsuccessfulscreen'
        return

    def verify_20_customer(self):
        # checks to see that the user has 20 to cash out
        if float(self.CAbalance) < 20:
            self.root.current = 'notenoughfundstocashoutcustomerscreen'
            return
        if not hasattr(self,'check_once_customer'):
            sm.add_widget(CashOutCustomerScreen(name='cashoutcustomerscreen'))
            self.check_once_customer = 1
        self.root.current = 'cashoutcustomerscreen'
        return

    def verify_20_advertiser(self):
        # checks to see that the user has 20 to cash out
        if float(self.AAbalance) < 20:
            self.root.current = 'notenoughfundstocashoutadvertiserscreen'
            return
        if not hasattr(self,'check_once_advertiser'):
            sm.add_widget(CashOutAdvertiserScreen(name='cashoutadvertiserscreen'))
            self.check_once_advertiser = 1
        self.root.current = 'cashoutadvertiserscreen'
        return

    def record_paypal_email_customer(self,storage):
        # records the paypal email of the customer
        g = open('to_be_paid.csv','a')
        g.write(self.username + ',' + str(storage.customer_paypal_email_text_input.text.strip()) + ',' + self.CAbalance + '\n')
        g.close()
        write_history(self.username,'customer','Requested $' + self.CAbalance + '.')
        self.CAbalance = '0.00'
        members = []
        f = open('mad_account_info_customer.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        for member in members:
            if member[0] == self.username:
                member[6] = '0.00'
        members = '\n'.join([','.join(mem) for mem in members]) + '\n'
        h = open('mad_account_info_customer.csv','w')
        h.write(members)
        h.close()
        sm.remove_widget(sm.children[0].manager.get_screen('customeraccountscreen'))
        sm.add_widget(CustomerAccountScreen(name='customeraccountscreen'))
        self.root.current = 'cashoutrequestsubmittedcustomerscreen'
        return

    def record_paypal_email_advertiser(self,storage):
        # records the paypal email of the customer
        g = open('to_be_paid.csv','a')
        g.write(self.username + ',' + str(storage.advertiser_paypal_email_text_input.text.strip()) + ',' + self.AAbalance + '\n')
        g.close()
        write_history(self.username,'advertiser','Requested $' + self.AAbalance + '.')
        self.AAbalance = '0.00'
        members = []
        f = open('mad_account_info_advertiser.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        for member in members:
            if member[0] == self.username:
                member[6] = '0.00'
        members = '\n'.join([','.join(mem) for mem in members]) + '\n'
        h = open('mad_account_info_advertiser.csv','w')
        h.write(members)
        h.close()
        sm.remove_widget(sm.children[0].manager.get_screen('advertiseraccountscreen'))
        sm.add_widget(AdvertiserAccountScreen(name='advertiseraccountscreen'))
        self.root.current = 'cashoutrequestsubmittedadvertiserscreen'
        return

    def make_history_customer(self):
        # adds the customer history to be printed to the app
        makescr = 0
        history = make_history_list(self.username,'customer')
        if len(history) < 10:
            for k in range(10-len(history)):
                history.append('')
        if not hasattr(self,'CAhistory'):
            makescr = 1
        self.CAhistory = history
        if makescr == 1:
            sm.add_widget(CustomerHistoryScreen(name='customerhistoryscreen'))
        self.root.current = 'customerhistoryscreen'
        return

    def make_history_advertiser(self):
        # adds the customer history to be printed to the app
        makescr = 0
        history = make_history_list(self.username,'advertiser')
        if len(history) < 10:
            for k in range(10-len(history)):
                history.append('')
        if not hasattr(self,'AAhistory'):
            makescr = 1
        self.AAhistory = history
        if makescr == 1:
            sm.add_widget(AdvertiserHistoryScreen(name='advertiserhistoryscreen'))
        self.root.current = 'advertiserhistoryscreen'
        return

    def make_history_business(self):
        # adds the customer history to be printed to the app
        makescr = 0
        history = make_history_list(self.username,'business')
        if len(history) < 10:
            for k in range(10-len(history)):
                history.append('')
        if not hasattr(self,'BAhistory'):
            makescr = 1
        self.BAhistory = history
        if makescr == 1:
            sm.add_widget(BusinessHistoryScreen(name='businesshistoryscreen'))
        self.root.current = 'businesshistoryscreen'
        return

    def store_ad(self,storage):
        # temporarily stores the ad information
        self.createad_deal_name = str(storage.createad_deal_name_text_input.text.strip())
        self.createad_description = str(storage.createad_description_text_input.text.strip())
        self.createad_start_date = str(storage.createad_start_date_text_input.text.strip())
        self.createad_end_date = str(storage.createad_end_date_text_input.text.strip())
        self.createad_other_offers = str(storage.createad_other_offers_text_input.text.strip())
        if hasattr(self,'admadeonce'):
            sm.remove_widget(sm.children[0].manager.get_screen('previewadscreen'))
        self.admadeonce = 1
        sm.add_widget(PreviewAdScreen(name='previewadscreen'))
        self.root.current = 'previewadscreen'
        return

    def write_ad(self,storage,option):
        # stores the ad
        paypal_email = str(storage.adpayment_paypal_email_text_input.text.strip())
        start_year = int(self.createad_start_date.split('/')[2])
        end_year = int(self.createad_end_date.split('/')[2])
        start_mo = int(self.createad_start_date.split('/')[0])
        end_mo = int(self.createad_end_date.split('/')[0])
        months = str(int((end_mo-start_mo) + 1 + 12*(end_year-start_year)))
        if option == 1:
            total_cost = int(months)*100
            tbw = ','.join([self.username,paypal_email,months,str(100),str(0.65)]) + '\n'
            g = open('to_be_invoiced.csv','a')
            g.write(tbw)
            g.close()
            adstr = ',;,;'.join([self.username,self.BAbusiness_name,self.createad_deal_name,self.createad_description,self.createad_start_date,self.createad_end_date,self.createad_other_offers,self.BAaddress,self.BAcity,self.BAstate,self.BAzip_code,'0.10','0.05','0','0']) + '\n'
            f = open('ad_storage.csv','a')
            f.write(adstr)
            f.close()
        elif option == 2:
            total_cost = int(months)*200
            tbw = ','.join([self.username,paypal_email,months,str(200),str(0.50)]) + '\n'
            g = open('to_be_invoiced.csv','a')
            g.write(tbw)
            g.close()
            adstr = ',;,;'.join([self.username,self.BAbusiness_name,self.createad_deal_name,self.createad_description,self.createad_start_date,self.createad_end_date,self.createad_other_offers,self.BAaddress,self.BAcity,self.BAstate,self.BAzip_code,'0.15','0.05','0','0']) + '\n'
            f = open('ad_storage.csv','a')
            f.write(adstr)
            f.close()
        else:
            total_cost = int(months)*300
            tbw = ','.join([self.username,paypal_email,months,str(300),str(0.50)]) + '\n'
            g = open('to_be_invoiced.csv','a')
            g.write(tbw)
            g.close()
            adstr = ',;,;'.join([self.username,self.BAbusiness_name,self.createad_deal_name,self.createad_description,self.createad_start_date,self.createad_end_date,self.createad_other_offers,self.BAaddress,self.BAcity,self.BAstate,self.BAzip_code,'0.25','0.10','0','0']) + '\n'
            f = open('ad_storage.csv','a')
            f.write(adstr)
            f.close()
        members = []
        qq = open('mad_account_info_business.csv','r')
        for line in qq:
            members.append(line.strip().split(','))
        qq.close()
        for mem in members:
            if mem[0] == self.username:
                mem[7] = str(round(float(mem[7]) + total_cost,2))
                mem[8] = str(int(mem[8]) + 1)
                self.BAowed = mem[7]
                self.BAactive_ads = mem[8]
        members = '\n'.join([','.join(mem) for mem in members]) + '\n'
        gg = open('mad_account_info_business.csv','w')
        gg.write(members)
        gg.close()
        write_history(self.username,'business','Created ad named ' + self.createad_deal_name)
        del self.createad_deal_name
        del self.createad_description
        del self.createad_start_date
        del self.createad_end_date
        del self.createad_other_offers
        del self.admadeonce
        sm.remove_widget(sm.children[0].manager.get_screen('businessaccountscreen'))
        sm.remove_widget(sm.children[0].manager.get_screen('createadscreen'))
        sm.add_widget(BusinessAccountScreen(name='businessaccountscreen'))
        sm.add_widget(CreateAdScreen(name='createadscreen'))
        self.root.current = 'adrecordedscreen'
        return

    def make_active_ads_screen(self):
        # make the active ads screens
        members = []
        f = open('ad_storage.csv','r')
        for line in f:
            members.append(line.strip().split(',;,;'))
        f.close()
        ad_list = []
        for mem in members:
            if mem[0] == self.username and check_date(mem[4],mem[5]):
                ad_list.append(mem)
        if len(ad_list) < 10:
            for k in range(10-len(ad_list)):
                ad_list.append(['' for kk in range(20)])
        self.ad_list = ad_list
        if hasattr(self,'adsscreenmade'):
            sm.remove_widget(sm.children[0].manager.get_screen('activeadsscreen'))
        sm.add_widget(ActiveAdsScreen(name='activeadsscreen'))
        self.adsscreenmade = 1
        self.root.current = 'activeadsscreen'
        return

    def make_ad_screen(self,ad_list):
        # makes the screen for an ad
        self.viewad_business_name = ad_list[1]
        self.viewad_description = ad_list[3]
        self.viewad_start_date = ad_list[4]
        self.viewad_end_date = ad_list[5]
        self.viewad_other_offers = ad_list[6]
        self.viewad_business_address = ad_list[7]
        self.viewad_business_city = ad_list[8]
        self.viewad_business_state = ad_list[9]
        self.viewad_business_zip_code = ad_list[10]
        self.viewad_advertisers = ad_list[13]
        self.viewad_uses = ad_list[14]
        if hasattr(self,'viewad_made_screen'):
            sm.remove_widget(sm.children[0].manager.get_screen('adscreen'))
        sm.add_widget(AdScreen(name='adscreen'))
        self.viewad_made_screen = 1
        self.root.current = 'adscreen'
        return

### End of class def

def check_date(start_date,end_date):
    # makes sure current date is in start and end date
    month = int(datetime.date.today().strftime('%m'))
    day = int(datetime.date.today().strftime('%d'))
    year = int(datetime.date.today().strftime('%Y'))
    start = start_date.split('/')
    start = [int(k) for k in start]
    end = end_date.split('/')
    end = [int(k) for k in end]
    inrange = 0
    if month <= end[0] and month >= start[0] and day >= start[1] and day <= end[1] and year <= end[2] and year >= start[2]:
        inrange = 1
    return inrange

def make_history_list(username,tag):
    # make the history screens
    members = []
    f = open('mad_app_history.csv','r')
    for line in f:
        members.append(line.strip().split(','))
    f.close()
    messages = [mem[2] for mem in members if mem[0] == username and mem[1] == tag]
    return messages

def write_history(username,tag,action):
    # writes action to history file
    timestr = datetime.date.today().strftime('%Y%m%dT%H%M')
    action = username + ',' + tag + ',' + timestr + ': ' + action + '\n'
    f = open('mad_app_history.csv','a')
    f.write(action)
    f.close()
    return

# Run it
if __name__ == '__main__':
    MADApp().run()
