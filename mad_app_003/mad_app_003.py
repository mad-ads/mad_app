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
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import random


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

class PossibleAdsScreen(Screen):
    pass

class PAdScreen(Screen):
    pass

class AdAddedSuccessfullyScreen(Screen):
    pass

class ServerErrorScreen(Screen):
    pass

class AddressErrorScreen(Screen):
    pass

class CurrentAdsScreen(Screen):
    pass

class CAdScreen(Screen):
    pass

class SeeDealsScreen(Screen):
    pass

class SAdScreen(Screen):
    pass

class AdAddedSuccessfullyCartScreen(Screen):
    pass

class CartScreen(Screen):
    pass

class SAAdScreen(Screen):
    pass

class VAdScreen(Screen):
    pass

class RedeemSentScreen(Screen):
    pass

class RedeemConfirmationScreen(Screen):
    pass

class ConfirmConfirmationScreen(Screen):
    pass

class DisputeConfirmationScreen(Screen):
    pass

class VerifyCouponsScreen(Screen):
    pass

class ThanksBackScreen(Screen):
    pass

class MainWidgetsVerifyCoupons(Widget):
    pass

class MainWidgetsSAAd(Widget):
    pass

class MainWidgetsVAd(Widget):
    pass

class MainWidgetsCart(Widget):
    pass

class MainWidgetsSAd(Widget):
    pass

class MainWidgetsSeeDeals(Widget):
    pass

class MainWidgetsCAd(Widget):
    pass

class MainWidgetsCurrentAds(Widget):
    pass

class MainWidgetsPAd(Widget):
    pass

class MainWidgetsPossibleAds(Widget):
    pass

class AuxWidgetsPossibleAds(Widget):
    pass

class AuxWidgetsSeeDeals(Widget):
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

Builder.load_file('mad_app_003.kv')
geolocator = Nominatim()

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
#sm.add_widget(PossibleAdsScreen(name='possibleadsscreen'))
#sm.add_widget(PAdScreen(name='padscreen'))
#sm.add_widget(PAdScreen(name='adaddedsuccessfullyscreen'))
sm.add_widget(ServerErrorScreen(name='servererrorscreen'))
sm.add_widget(AddressErrorScreen(name='addresserrorscreen'))
#sm.add_widget(CurrentAdsScreen(name='currentadsscreen'))
#sm.add_widget(CAdScreen(name='cadscreen'))
#sm.add_widget(SeeDealsScreen(name='seedealsscreen'))
#sm.add_widget(SAdScreen(name='sadscreen'))
#sm.add_widget(AdAddedSuccessfullyCartScreen(name='adaddedsuccessfullycartscreen'))
#sm.add_widget(CartScreen(name='cartscreen'))
sm.add_widget(RedeemSentScreen(name='redeemsentscreen'))
sm.add_widget(RedeemConfirmationScreen(name='redeemconfirmationscreen'))
#sm.add_widget(VerifyCouponsScreen(name='verifycouponsscreen'))
sm.add_widget(ConfirmConfirmationScreen(name='confirmconfirmationscreen'))
sm.add_widget(DisputeConfirmationScreen(name='disputeconfirmationscreen'))
sm.add_widget(ThanksBackScreen(name='thanksbackscreen'))

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
                    self.BAcoords = (float(member[8]),float(member[9]))
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
                    self.AAcoords = (float(member[7]),float(member[8]))
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
                    self.CAcoords = (float(member[7]),float(member[8]))
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
        try:
            business_address = geolocator.geocode(self.BAaddress + ' ' + self.BAzip_code)
        except:
            self.root.current = 'servererrorscreen'
            return
        if business_address is None:
            try:
                business_address = geolocator.geocode(self.BAcity + ' ' + self.BAzip_code)
            except:
                self.root.current = 'servererrorscreen'
                return
        if business_address is None:
            self.root.current = 'addresserrorscreen'
            return
        coords = (business_address.latitude,business_address.longitude)
        self.BAcoords = coords
        members = []
        f = open('mad_account_info_business.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        members.append([self.username,business_name,owner,address,city,state,zip_code,self.BAowed,str(coords[0]),str(coords[1])])
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
        geolocator = Nominatim()
        try:
            advertiser_address = geolocator.geocode(self.AAaddress + ' ' + self.AAzip_code)
        except:
            self.root.current = 'servererrorscreen'
            return
        if advertiser_address is None:
            try:
                advertiser_address = geolocator.geocode(self.AAcity + ' ' + self.AAzip_code)
            except:
                self.root.current = 'servererrorscreen'
                return
        if advertiser_address is None:
            self.root.current = 'addresserrorscreen'
            return
        coords = (advertiser_address.latitude,advertiser_address.longitude)
        self.AAcoords = coords
        members = []
        f = open('mad_account_info_advertiser.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        members.append([self.username,name,address,city,state,zip_code,self.AAbalance,str(coords[0]),str(coords[1])])
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
        try:
            customer_address = geolocator.geocode(self.CAaddress + ' ' + self.CAzip_code)
        except:
            self.root.current = 'servererrorscreen'
            return
        if customer_address is None:
            try:
                customer_address = geolocator.geocode(self.CAcity + ' ' + self.CAzip_code)
            except:
                self.root.current = 'servererrorscreen'
                return
        if customer_address is None:
            self.root.current = 'addresserrorscreen'
            return
        coords = (customer_address.latitude,customer_address.longitude)
        self.CAcoords = coords
        members = []
        f = open('mad_account_info_customer.csv','r')
        for line in f:
            members.append(line.strip().split(','))
        f.close()
        members.append([self.username,name,address,city,state,zip_code,self.CAbalance,str(coords[0]),str(coords[1])])
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
            adstr = ',;,;'.join([self.username,self.BAbusiness_name,self.createad_deal_name,self.createad_description,self.createad_start_date,self.createad_end_date,self.createad_other_offers,self.BAaddress,self.BAcity,self.BAstate,self.BAzip_code,'0.10','0.05','0','0',str(self.BAcoords[0]),str(self.BAcoords[1])]) + '\n'
            f = open('ad_storage.csv','a')
            f.write(adstr)
            f.close()
        elif option == 2:
            total_cost = int(months)*200
            tbw = ','.join([self.username,paypal_email,months,str(200),str(0.50)]) + '\n'
            g = open('to_be_invoiced.csv','a')
            g.write(tbw)
            g.close()
            adstr = ',;,;'.join([self.username,self.BAbusiness_name,self.createad_deal_name,self.createad_description,self.createad_start_date,self.createad_end_date,self.createad_other_offers,self.BAaddress,self.BAcity,self.BAstate,self.BAzip_code,'0.15','0.05','0','0',str(self.BAcoords[0]),str(self.BAcoords[1])]) + '\n'
            f = open('ad_storage.csv','a')
            f.write(adstr)
            f.close()
        else:
            total_cost = int(months)*300
            tbw = ','.join([self.username,paypal_email,months,str(300),str(0.50)]) + '\n'
            g = open('to_be_invoiced.csv','a')
            g.write(tbw)
            g.close()
            adstr = ',;,;'.join([self.username,self.BAbusiness_name,self.createad_deal_name,self.createad_description,self.createad_start_date,self.createad_end_date,self.createad_other_offers,self.BAaddress,self.BAcity,self.BAstate,self.BAzip_code,'0.25','0.10','0','0',str(self.BAcoords[0]),str(self.BAcoords[1])]) + '\n'
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
                self.BAowed = mem[7]
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

    def make_current_ads_screen(self):
        # make the active ads screens
        members = []
        f = open('accepted_ads.csv','r')
        for line in f:
            members.append(line.strip().split(',;,;'))
        f.close()
        ad_list = []
        for mem in members:
            if mem[-1] == self.username and check_date(mem[4],mem[5]):
                ad_list.append(mem)
        if len(ad_list) < 10:
            for k in range(10-len(ad_list)):
                ad_list.append(['' for kk in range(20)])
        self.ad_list = ad_list
        if hasattr(self,'currentadsscreenmade'):
            sm.remove_widget(sm.children[0].manager.get_screen('currentadsscreen'))
        sm.add_widget(CurrentAdsScreen(name='currentadsscreen'))
        self.currentadsscreenmade = 1
        self.root.current = 'currentadsscreen'
        return

    def make_cart_screen(self):
        # make the active ads screens
        members = []
        f = open('carts.csv','r')
        for line in f:
            members.append(line.strip().split(',;,;'))
        f.close()
        ad_list = []
        for mem in members:
            if mem[-1] == self.username and check_date(mem[4],mem[5]):
                ad_list.append(mem)
        if len(ad_list) < 10:
            for k in range(10-len(ad_list)):
                ad_list.append(['' for kk in range(20)])
        self.ad_list = ad_list
        if hasattr(self,'cartscreenmade'):
            sm.remove_widget(sm.children[0].manager.get_screen('cartscreen'))
        sm.add_widget(CartScreen(name='cartscreen'))
        self.cartscreenmade = 1
        self.kappa = 0
        self.root.current = 'cartscreen'
        return

    def make_verify_coupons(self):
        # make the active ads screens
        members = []
        f = open('awaiting_approval.csv','r')
        for line in f:
            members.append(line.strip().split(',;,;'))
        f.close()
        ad_list = []
        for mem in members:
            if mem[0] == self.username:
                ad_list.append(mem)
        if len(ad_list) < 10:
            for k in range(10-len(ad_list)):
                ad_list.append(['' for kk in range(20)])
        self.ad_list = ad_list
        if hasattr(self,'verifyscreenmade'):
            sm.remove_widget(sm.children[0].manager.get_screen('verifycouponsscreen'))
        sm.add_widget(VerifyCouponsScreen(name='verifycouponsscreen'))
        self.verifyscreenmade = 1
        self.kappa = 0
        self.root.current = 'verifycouponsscreen'
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

    def get_possible_ads_advertiser(self):
        # finds ads within 50 miles for advertiser to use
        advertiser_coords = (self.AAcoords[0],self.AAcoords[1])
        members = []
        f = open('ad_storage.csv','r')
        for line in f:
            members.append(line.strip().split(',;,;'))
        f.close()
        active_members = [['' for k in range(20)]]
        qq = open('accepted_ads.csv','r')
        for line in qq:
            active_members.append(line.strip().split(',;,;'))
        qq.close()
        possible_ads = []
        active_members = [amem for amem in active_members if len(amem) > 10]
        for mem in members:
            business_coords = (float(mem[15]),float(mem[16]))
            distance = geodesic(advertiser_coords,business_coords).miles
            if distance < 50:
                for amem in active_members:
                    if sum([amem[lk] == mem[lk] for lk in range(len(mem))]) >= 15:
                        break
                if sum([amem[lk] == mem[lk] for lk in range(len(mem))]) >= 15:
                    continue
                possible_ads.append(mem)
        random.shuffle(possible_ads)
        if len(possible_ads) < 10:
            for k in range(10-len(possible_ads)):
                possible_ads.append(['' for kk in range(20)])
        self.ad_list_p = possible_ads
        if hasattr(self,'possibleadsscreenmade'):
            sm.remove_widget(sm.children[0].manager.get_screen('possibleadsscreen'))
        self.possibleadsscreenmade = 1
        sm.add_widget(PossibleAdsScreen(name='possibleadsscreen'))
        self.root.current = 'possibleadsscreen'
        return

    def search_business(self,query):
        # searches for ads with query in business name
        advertiser_coords = (self.AAcoords[0],self.AAcoords[1])
        members = []
        f = open('ad_storage.csv','r')
        for line in f:
            members.append(line.strip().split(',;,;'))
        f.close()
        active_members = [['' for k in range(20)]]
        qq = open('accepted_ads.csv','r')
        for line in qq:
            active_members.append(line.strip().split(',;,;'))
        qq.close()
        possible_ads = []
        active_members = [amem for amem in active_members if len(amem) > 10]
        for mem in members:
            business_coords = (float(mem[15]),float(mem[16]))
            distance = geodesic(advertiser_coords,business_coords).miles
            if distance < 50 and query.lower() in mem[1].lower():
                for amem in active_members:
                    if sum([amem[lk] == mem[lk] for lk in range(len(mem))]) >= 15:
                        break
                if sum([amem[lk] == mem[lk] for lk in range(len(mem))]) >= 15:
                    continue
                possible_ads.append(mem)
        random.shuffle(possible_ads)
        if len(possible_ads) < 10:
            for k in range(10-len(possible_ads)):
                possible_ads.append(['' for kk in range(20)])
        self.ad_list_p = possible_ads
        if hasattr(self,'possibleadsscreenmade'):
            sm.remove_widget(sm.children[0].manager.get_screen('possibleadsscreen'))
        self.possibleadsscreenmade = 1
        sm.add_widget(PossibleAdsScreen(name='possibleadsscreen'))
        self.root.current = 'possibleadsscreen'
        return

    def make_ad_screen_p(self,ad_list):
        # makes the screen for an ad
        self.pad = ad_list
        self.pad_business_name = ad_list[1]
        self.pad_description = ad_list[3]
        self.pad_start_date = ad_list[4]
        self.pad_end_date = ad_list[5]
        self.pad_other_offers = ad_list[6]
        self.pad_business_address = ad_list[7]
        self.pad_business_city = ad_list[8]
        self.pad_business_state = ad_list[9]
        self.pad_business_zip_code = ad_list[10]
        self.pad_payout = ad_list[11]
        self.pad_advertisers = ad_list[13]
        self.pad_uses = ad_list[14]
        if hasattr(self,'viewad_made_screen_p'):
            sm.remove_widget(sm.children[0].manager.get_screen('padscreen'))
        sm.add_widget(PAdScreen(name='padscreen'))
        self.viewad_made_screen_p = 1
        self.root.current = 'padscreen'
        return

    def make_ad_screen_c(self,ad_list):
        # makes the screen for an ad
        self.cad = ad_list
        self.cad_business_name = ad_list[1]
        self.cad_description = ad_list[3]
        self.cad_start_date = ad_list[4]
        self.cad_end_date = ad_list[5]
        self.cad_other_offers = ad_list[6]
        self.cad_business_address = ad_list[7]
        self.cad_business_city = ad_list[8]
        self.cad_business_state = ad_list[9]
        self.cad_business_zip_code = ad_list[10]
        self.cad_payout = ad_list[11]
        self.cad_advertiser = ad_list[-1]
        self.cad_uses = ad_list[14]
        if hasattr(self,'viewad_made_screen_c'):
            sm.remove_widget(sm.children[0].manager.get_screen('cadscreen'))
        sm.add_widget(CAdScreen(name='cadscreen'))
        self.viewad_made_screen_c = 1
        self.root.current = 'cadscreen'
        return

    def make_ad_screen_s(self,ad_list):
        # makes the screen for an ad
        self.sad = ad_list
        self.sad_business_name = ad_list[1]
        self.sad_description = ad_list[3]
        self.sad_start_date = ad_list[4]
        self.sad_end_date = ad_list[5]
        self.sad_other_offers = ad_list[6]
        self.sad_business_address = ad_list[7]
        self.sad_business_city = ad_list[8]
        self.sad_business_state = ad_list[9]
        self.sad_business_zip_code = ad_list[10]
        self.sad_payout = ad_list[12]
        self.sad_advertiser = ad_list[-1]
        self.sad_uses = ad_list[14]
        if hasattr(self,'viewad_made_screen_s'):
            sm.remove_widget(sm.children[0].manager.get_screen('sadscreen'))
        sm.add_widget(SAdScreen(name='sadscreen'))
        self.viewad_made_screen_s = 1
        self.root.current = 'sadscreen'
        return

    def make_ad_screen_sa(self,ad_list):
        # makes the screen for an ad
        self.saad = ad_list
        self.saad_business_name = ad_list[1]
        self.saad_description = ad_list[3]
        self.saad_start_date = ad_list[4]
        self.saad_end_date = ad_list[5]
        self.saad_other_offers = ad_list[6]
        self.saad_business_address = ad_list[7]
        self.saad_business_city = ad_list[8]
        self.saad_business_state = ad_list[9]
        self.saad_business_zip_code = ad_list[10]
        self.saad_payout = ad_list[12]
        self.saad_advertiser = ad_list[-1]
        self.saad_uses = ad_list[14]
        if hasattr(self,'viewad_made_screen_sa'):
            sm.remove_widget(sm.children[0].manager.get_screen('saadscreen'))
        sm.add_widget(SAAdScreen(name='saadscreen'))
        self.viewad_made_screen_sa = 1
        self.root.current = 'saadscreen'
        return

    def make_ad_screen_v(self,ad_list):
        # makes the screen for an ad
        self.vad = ad_list
        self.vad_business_name = ad_list[1]
        self.vad_description = ad_list[3]
        self.vad_start_date = ad_list[4]
        self.vad_end_date = ad_list[5]
        self.vad_other_offers = ad_list[6]
        self.vad_business_address = ad_list[7]
        self.vad_business_city = ad_list[8]
        self.vad_business_state = ad_list[9]
        self.vad_business_zip_code = ad_list[10]
        self.vad_payout_advertiser = ad_list[11]
        self.vad_payout_customer = ad_list[12]
        self.vad_advertiser = ad_list[-3]
        self.vad_customer = ad_list[-2]
        self.vad_date_used = ad_list[-1]
        self.vad_uses = ad_list[14]
        if self.vad_payout_advertiser == '0.10':
            self.vad_business_payout = '0.65'
        else:
            self.vad_business_payout = '0.65'
        if hasattr(self,'viewad_made_screen_v'):
            sm.remove_widget(sm.children[0].manager.get_screen('vadscreen'))
        sm.add_widget(VAdScreen(name='vadscreen'))
        self.viewad_made_screen_v = 1
        self.root.current = 'vadscreen'
        return

    def accept_ad(self):
        # records that the ad has been accepted.
        if sum(['' == k for k in self.pad]) > 10:
            return
        members = []
        f = open('ad_storage.csv','r')
        for line in f:
            members.append(line.strip().split(',;,;'))
        f.close()
        for mem in members:
            if 15 <= sum([1 for k in range(len(mem)) if mem[k] == self.pad[k]]):
                # we have the right ad
                mem[13] = str(int(mem[13]) + 1)
                self.pad[13] = mem[13]
                self.pad[14] = '0'
        members = '\n'.join([',;,;'.join(mem) for mem in members]) + '\n'
        g = open('ad_storage.csv','w')
        g.write(members)
        g.close()
        self.pad.append(self.username)
        gg = open('accepted_ads.csv','a')
        gg.write(',;,;'.join(self.pad) + '\n')
        gg.close()
        if hasattr(self,'addedsuccessfullyscrmade'):
            sm.remove_widget(sm.children[0].manager.get_screen('adaddedsuccessfullyscreen'))
        sm.add_widget(AdAddedSuccessfullyScreen(name='adaddedsuccessfullyscreen'))
        self.root.current = 'adaddedsuccessfullyscreen'
        write_history(self.username,'advertiser','Accepted Ad ' + self.pad[2])
        self.addedsuccessfullyscrmade = 1
        return

    def add_to_cart(self):
        # records that the ad has been accepted.
        if sum(['' == k for k in self.sad]) > 10:
            return
        self.sad.append(self.username)
        gg = open('carts.csv','a')
        gg.write(',;,;'.join(self.sad) + '\n')
        gg.close()
        if hasattr(self,'addedsuccessfullycartmade'):
            sm.remove_widget(sm.children[0].manager.get_screen('adaddedsuccessfullycartscreen'))
        sm.add_widget(AdAddedSuccessfullyCartScreen(name='adaddedsuccessfullycartscreen'))
        self.root.current = 'adaddedsuccessfullycartscreen'
        write_history(self.username,'customer','Placed Ad ' + self.sad[2] + ' in cart.')
        self.addedsuccessfullycartmade = 1
        return

    def get_possible_ads_customer(self):
        # finds ads within 50 miles for advertiser to use
        customer_coords = (self.CAcoords[0],self.CAcoords[1])
        members = []
        f = open('accepted_ads.csv','r')
        for line in f:
            members.append(line.strip().split(',;,;'))
        f.close()
        active_members = [['' for k in range(20)]]
        qq = open('carts.csv','r')
        for line in qq:
            active_members.append(line.strip().split(',;,;'))
        qq.close()
        active_members = [amem for amem in active_members if len(amem) > 10]
        possible_ads = []
        for mem in members:
            business_coords = (float(mem[15]),float(mem[16]))
            distance = geodesic(customer_coords,business_coords).miles
            if distance < 50:
                for amem in active_members:
                    if sum([amem[lk] == mem[lk] for lk in range(len(mem))]) >= 15:
                        break
                if sum([amem[lk] == mem[lk] for lk in range(len(mem))]) >= 15:
                    continue
                possible_ads.append(mem)
        random.shuffle(possible_ads)
        if len(possible_ads) < 10:
            for k in range(10-len(possible_ads)):
                possible_ads.append(['' for kk in range(20)])
        self.ad_list = possible_ads
        if hasattr(self,'seedealsscreenmade'):
            sm.remove_widget(sm.children[0].manager.get_screen('seedealsscreen'))
        self.seedealsscreenmade = 1
        sm.add_widget(SeeDealsScreen(name='seedealsscreen'))
        self.root.current = 'seedealsscreen'
        return

    def search_deals(self,query):
        # searches for ads with query in business name
        customer_coords = (self.CAcoords[0],self.CAcoords[1])
        members = []
        f = open('accepted_ads.csv','r')
        for line in f:
            members.append(line.strip().split(',;,;'))
        f.close()
        active_members = [['' for k in range(20)]]
        qq = open('carts.csv','r')
        for line in qq:
            active_members.append(line.strip().split(',;,;'))
        qq.close()
        possible_ads = []
        active_members = [amem for amem in active_members if len(amem) > 10]
        for mem in members:
            business_coords = (float(mem[15]),float(mem[16]))
            distance = geodesic(customer_coords,business_coords).miles
            if distance < 50 and (query.lower() in mem[1].lower() or query.lower() in mem[-1].lower()):
                for amem in active_members:
                    if sum([amem[lk] == mem[lk] for lk in range(len(mem))]) >= 15:
                        break
                if sum([amem[lk] == mem[lk] for lk in range(len(mem))]) >= 15:
                    continue
                possible_ads.append(mem)
        random.shuffle(possible_ads)
        if len(possible_ads) < 10:
            for k in range(10-len(possible_ads)):
                possible_ads.append(['' for kk in range(20)])
        self.ad_list = possible_ads
        if hasattr(self,'seedealsscreenmade'):
            sm.remove_widget(sm.children[0].manager.get_screen('seedealsscreen'))
        self.seedealsscreenmade = 1
        sm.add_widget(SeeDealsScreen(name='seedealsscreen'))
        self.root.current = 'seedealsscreen'
        return

    def next_10(self):
        # displays next 10 in cart
        self.ad_list.append(['' for j in range(20)])
        self.ad_list = sum([self.ad_list[10:],self.ad_list[:10]],[])
        for zz in range(len(self.ad_list)):
            if sum([words == '' for words in self.ad_list[zz]]) >= 15:
                continue
            break
        self.ad_list = sum([self.ad_list[zz:],self.ad_list[:zz]],[])
        self.kappa += 1
        sm.remove_widget(sm.children[0].manager.get_screen('cartscreen'))
        sm.add_widget(CartScreen(name='cartscreen'))
        self.root.current = 'cartscreen'
        return

    def prev_10(self):
        # displays prev 10
        if self.kappa == 0:
            return
        self.ad_list = sum([self.ad_list[-10:],self.ad_list[:-10]],[])
        self.kappa -= 1
        for zz in range(len(self.ad_list)):
            if sum([words == '' for words in self.ad_list[zz]]) >= 15:
                continue
            break
        self.ad_list = sum([self.ad_list[zz:],self.ad_list[:zz]],[])
        sm.remove_widget(sm.children[0].manager.get_screen('cartscreen'))
        sm.add_widget(CartScreen(name='cartscreen'))
        self.root.current = 'cartscreen'
        return

    def next_10_active(self):
        # displays next 10 in cart
        if not hasattr(self,'kappa_active'):
            self.kappa_active = 0
        self.ad_list.append(['' for j in range(20)])
        self.ad_list = sum([self.ad_list[10:],self.ad_list[:10]],[])
        for zz in range(len(self.ad_list)):
            if sum([words == '' for words in self.ad_list[zz]]) >= 15:
                continue
            break
        self.ad_list = sum([self.ad_list[zz:],self.ad_list[:zz]],[])
        self.kappa_active += 1
        sm.remove_widget(sm.children[0].manager.get_screen('activeadsscreen'))
        sm.add_widget(ActiveAdsScreen(name='activeadsscreen'))
        self.root.current = 'activeadsscreen'
        return

    def prev_10_active(self):
        # displays prev 10
        if self.kappa_active == 0:
            return
        self.ad_list = sum([self.ad_list[-10:],self.ad_list[:-10]],[])
        self.kappa_active -= 1
        for zz in range(len(self.ad_list)):
            if sum([words == '' for words in self.ad_list[zz]]) >= 15:
                continue
            break
        self.ad_list = sum([self.ad_list[zz:],self.ad_list[:zz]],[])
        sm.remove_widget(sm.children[0].manager.get_screen('activeadsscreen'))
        sm.add_widget(ActiveAdsScreen(name='activeadsscreen'))
        self.root.current = 'activeadsscreen'
        return

    def next_10_current(self):
        # displays next 10 in cart
        if not hasattr(self,'kappa_current'):
            self.kappa_current = 0
        self.ad_list.append(['' for j in range(20)])
        self.ad_list = sum([self.ad_list[10:],self.ad_list[:10]],[])
        for zz in range(len(self.ad_list)):
            if sum([words == '' for words in self.ad_list[zz]]) >= 15:
                continue
            break
        self.ad_list = sum([self.ad_list[zz:],self.ad_list[:zz]],[])
        self.kappa_current += 1
        sm.remove_widget(sm.children[0].manager.get_screen('currentadsscreen'))
        sm.add_widget(CurrentAdsScreen(name='currentadsscreen'))
        self.root.current = 'currentadsscreen'
        return

    def prev_10_current(self):
        # displays prev 10
        if self.kappa_current == 0:
            return
        self.ad_list = sum([self.ad_list[-10:],self.ad_list[:-10]],[])
        self.kappa_current -= 1
        for zz in range(len(self.ad_list)):
            if sum([words == '' for words in self.ad_list[zz]]) >= 15:
                continue
            break
        self.ad_list = sum([self.ad_list[zz:],self.ad_list[:zz]],[])
        sm.remove_widget(sm.children[0].manager.get_screen('currentadsscreen'))
        sm.add_widget(CurrentAdsScreen(name='currentadsscreen'))
        self.root.current = 'currentadsscreen'
        return

    def next_10_verify(self):
        # displays next 10 in cart
        if not hasattr(self,'kappa_verify'):
            self.kappa_verify = 0
        self.ad_list.append(['' for j in range(20)])
        self.ad_list = sum([self.ad_list[10:],self.ad_list[:10]],[])
        for zz in range(len(self.ad_list)):
            if sum([words == '' for words in self.ad_list[zz]]) >= 15:
                continue
            break
        self.ad_list = sum([self.ad_list[zz:],self.ad_list[:zz]],[])
        self.kappa_verify += 1
        sm.remove_widget(sm.children[0].manager.get_screen('verifycouponsscreen'))
        sm.add_widget(VerifyCouponsScreen(name='verifycouponsscreen'))
        self.root.current = 'verifycouponsscreen'
        return

    def prev_10_verify(self):
        # displays prev 10
        if self.kappa_verify == 0:
            return
        self.ad_list = sum([self.ad_list[-10:],self.ad_list[:-10]],[])
        self.kappa_verify -= 1
        for zz in range(len(self.ad_list)):
            if sum([words == '' for words in self.ad_list[zz]]) >= 15:
                continue
            break
        self.ad_list = sum([self.ad_list[zz:],self.ad_list[:zz]],[])
        sm.remove_widget(sm.children[0].manager.get_screen('verifycouponsscreen'))
        sm.add_widget(VerifyCouponsScreen(name='verifycouponsscreen'))
        self.root.current = 'verifycouponsscreen'
        return

    def redeem_deal(self):
        # redeems a deal and sends it to the business
        extended = sum([self.saad,[datetime.date.today().strftime('%Y%m%d')]],[])
        adstr = ',;,;'.join(extended) + '\n'
        f = open('awaiting_approval.csv','a')
        f.write(adstr)
        f.close()
        members = []
        g = open('carts.csv','r')
        for line in g:
            members.append(line.strip().split(',;,;'))
        g.close()
        new_members = []
        for mem in members:
            if len(mem) == sum([mem[k] == self.saad[k] for k in range(len(mem))]):
                continue
            new_members.append(mem)
        tbw = '\n'.join([',;,;'.join(nmem) for nmem in new_members]) + '\n'
        gg = open('carts.csv','w')
        gg.write(tbw)
        gg.close()
        self.root.current = 'redeemsentscreen'
        write_history(self.username,'customer','Used ' + self.saad[2] + ' coupon.')
        self.ad_list = [ad for ad in self.ad_list if sum([self.saad[k] == ad[k] for k in range(len(self.saad))]) < 15]
        self.ad_list.append(['' for j in range(20)])
        sm.remove_widget(sm.children[0].manager.get_screen('cartscreen'))
        sm.add_widget(CartScreen(name='cartscreen'))
        return

    def dispute_deal(self):
        # disputes the deal
        adstr = ',;,;'.join(self.vad) + '\n'
        f = open('disputed.csv','a')
        f.write(adstr)
        f.close()
        members = []
        g = open('awaiting_approval.csv','r')
        for line in g:
            members.append(line.strip().split(',;,;'))
        g.close()
        new_members = []
        for mem in members:
            if len(mem) == sum([mem[k] == self.vad[k] for k in range(len(mem))]):
                continue
            new_members.append(mem)
        tbw = '\n'.join([',;,;'.join(nmem) for nmem in new_members]) + '\n'
        gg = open('awaiting_approval.csv','w')
        gg.write(tbw)
        gg.close()
        self.root.current = 'thanksbackscreen'
        write_history(self.username,'business','Disputed ' + self.vad[2] + ' coupon used by ' + self.vad[-2] + '.')
        new_ad_list = []
        counter = 0
        for ad in self.ad_list:
            if sum([self.vad[k] == ad[k] for k in range(len(self.vad))]) < 15 or counter > 0:
                new_ad_list.append(ad)
            else:
                counter += 1
        self.ad_list = new_ad_list
        self.ad_list.append(['' for j in range(20)])
        sm.remove_widget(sm.children[0].manager.get_screen('verifycouponsscreen'))
        sm.add_widget(VerifyCouponsScreen(name='verifycouponsscreen'))
        return

    def confirm_deal(self):
        # confirms the deal!
        tbw = ','.join([self.vad[0],'','','',self.vad_business_payout]) + '\n'
        f = open('to_be_invoiced.csv','a')
        f.write(tbw)
        f.close()
        members = []
        g = open('awaiting_approval.csv','r')
        for line in g:
            members.append(line.strip().split(',;,;'))
        g.close()
        new_members = []
        for mem in members:
            if len(mem) == sum([mem[k] == self.vad[k] for k in range(len(mem))]):
                continue
            new_members.append(mem)
        new_members.append(['' for j in range(20)])
        tbw = '\n'.join([',;,;'.join(nmem) for nmem in new_members]) + '\n'
        gg = open('awaiting_approval.csv','w')
        gg.close()
        members = []
        g = open('mad_account_info_business.csv','r')
        for line in g:
            members.append(line.strip().split(','))
        g.close()
        for mem in members:
            if mem[0] == self.username:
                mem[7] = str(float(mem[7]) + float(self.vad_business_payout))
                self.BAowed = mem[7]
        tbw = '\n'.join([','.join(nmem) for nmem in members]) + '\n'
        gg = open('mad_account_info_business.csv','w')
        gg.write(tbw)
        gg.close()
        members = []
        g = open('mad_account_info_customer.csv','r')
        for line in g:
            members.append(line.strip().split(','))
        g.close()
        for mem in members:
            if mem[0] == self.vad_customer:
                mem[6] = str(float(mem[6]) + float(self.vad_payout_customer))
        tbw = '\n'.join([','.join(nmem) for nmem in members]) + '\n'
        gg = open('mad_account_info_customer.csv','w')
        gg.write(tbw)
        gg.close()
        members = []
        g = open('mad_account_info_advertiser.csv','r')
        for line in g:
            members.append(line.strip().split(','))
        g.close()
        for mem in members:
            if mem[0] == self.vad_advertiser:
                mem[6] = str(float(mem[6]) + float(self.vad_payout_advertiser))
        tbw = '\n'.join([','.join(nmem) for nmem in members]) + '\n'
        gg = open('mad_account_info_advertiser.csv','w')
        gg.write(tbw)
        gg.close()
        members = []
        g = open('accepted_ads.csv','r')
        for line in g:
            members.append(line.strip().split(',;,;'))
        g.close()
        for mem in members:
            if sum([self.vad[lk] == mem[lk] for lk in range(len(mem))]) >= 15:
                mem[14] = str(int(mem[14]) + 1)
        tbw = '\n'.join([',;,;'.join(nmem) for nmem in members]) + '\n'
        gg = open('accepted_ads.csv','w')
        gg.write(tbw)
        gg.close()
        members = []
        g = open('ad_storage.csv','r')
        for line in g:
            members.append(line.strip().split(',;,;'))
        g.close()
        for mem in members:
            if sum([self.vad[lk] == mem[lk] for lk in range(len(mem))]) >= 15:
                mem[14] = str(int(mem[14]) + 1)
        tbw = '\n'.join([',;,;'.join(nmem) for nmem in members]) + '\n'
        gg = open('ad_storage.csv','w')
        gg.write(tbw)
        gg.close()
        self.root.current = 'thanksbackscreen'
        write_history(self.username,'business','Confirmed ' + self.vad[2] + ' coupon used by ' + self.vad[-2] + '.')
        new_ad_list = []
        counter = 0
        for ad in self.ad_list:
            if sum([self.vad[k] == ad[k] for k in range(len(self.vad))]) < 15 or counter > 0:
                new_ad_list.append(ad)
            else:
                counter += 1
        self.ad_list = new_ad_list
        self.ad_list.append(['' for j in range(20)])
        sm.remove_widget(sm.children[0].manager.get_screen('verifycouponsscreen'))
        sm.add_widget(VerifyCouponsScreen(name='verifycouponsscreen'))
        sm.remove_widget(sm.children[0].manager.get_screen('businessaccountscreen'))
        sm.add_widget(BusinessAccountScreen(name='businessaccountscreen'))
        return

### End of class def

def check_date(start_date,end_date):
    # makes sure current date is in start and end date
    ymd = int(datetime.date.today().strftime('%Y%m%d'))
    start = start_date.split('/')
    end = end_date.split('/')
    start = int(start[2]+start[0]+start[1])
    end = int(end[2]+end[0]+end[1])
    inrange = 0
    if ymd <= end and ymd >= start:
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
