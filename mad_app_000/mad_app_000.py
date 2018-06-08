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

class MainWidgetsLog(Widget):
    pass

class MainWidgetsCreate(Widget):
    pass

class MainWidgetsMainAcct(Widget):
    pass

class ScreenManagement(ScreenManager):
    pass

Builder.load_file('mad_app_000.kv')

sm = ScreenManager()
# add new screens as below
sm.add_widget(LoginScreen(name='loginscreen'))
sm.add_widget(CreateAcctScreen(name='createacctscreen'))
sm.add_widget(PasswordsDontMatchScreen(name='passwordsdontmatchscreen'))
sm.add_widget(UsernameTakenScreen(name='usernametakenscreen'))
sm.add_widget(EmailTakenScreen(name='emailtakenscreen'))
sm.add_widget(RegistrationSuccessfulScreen(name='registrationsuccessfulscreen'))
sm.add_widget(MainAcctScreen(name='mainacctscreen'))
sm.add_widget(InvalidCredentialsScreen(name='invalidcredentialsscreen'))

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
                self.root.current = 'mainacctscreen'
                return
        self.root.current = 'invalidcredentialsscreen'
        return

# Run it
if __name__ == '__main__':
    MADApp().run()
