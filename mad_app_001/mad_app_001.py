# Version 000 of MAD's advertising app. Associated .kv file is mad_app_000.kv

# Import statements
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
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

class MainWidgetsCreateCustomerAccount(Widget):
    pass

class ScreenManagement(ScreenManager):
    pass

Builder.load_file('mad_app_001.kv')

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


# Run it
if __name__ == '__main__':
    MADApp().run()
