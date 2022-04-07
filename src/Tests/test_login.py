import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Base.base import Base
import pytest


@pytest.mark.usefixtures('set_up')
class TestLogin(Base):


    def test_login_success(self):
        driver = self.driver
        # login = LoginPage(driver)
        # login.enter_email(self.df.loc[0,"username"])
        # login.enter_password(self.df.loc[0,"pass"])
        # login.click_login()

        try:
            assert "uSync App" == driver.title
        except Exception as e:
            raise
            print("Title is wrong", format(e))