from selenium import webdriver
from time import sleep

from config import email, password, user

SLEEP_TIME = 1

class ChromeAuto:
  def __init__(self):
    self.driver_path = 'useful-modules/selenium/chromedriver'
    self.options = webdriver.ChromeOptions()
    self.options.add_argument('user-data-dir=Profile')
    self.chrome = webdriver.Chrome(
      self.driver_path,
      options=self.options
    )

  def access(self, site):
    self.chrome.get(site)

  def quit(self):
    self.chrome.quit()

  def click_sign_in(self):
    try:
      sign_in_button = self.chrome.find_element_by_link_text('Sign in')
      sign_in_button.click()
    except Exception as e:
      print('Error clicking sign in:', e)

  def sign_in(self):
    try:
      login_input = self.chrome.find_element_by_id('login_field')
      password_input = self.chrome.find_element_by_id('password')
      login_button = self.chrome.find_element_by_name('commit')
      login_input.send_keys(email)
      password_input.send_keys(password)
      sleep(SLEEP_TIME)
      login_button.click()
    except Exception as e:
      print('Error signing in:', e)
  
  def click_profile(self):
    try:
      css_selector = 'body > div.position-relative.js-header-wrapper > header '
      css_selector += '> div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details'
      profile = self.chrome.find_element_by_css_selector(css_selector)
      profile.click()
    except Exception as e:
      print('Error clicking profile:', e)

  def log_out(self):
    try:
      css_selector = 'body > div.position-relative.js-header-wrapper > '
      css_selector += 'header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex'
      css_selector += ' > details > details-menu > form > button'
      sign_out = self.chrome.find_element_by_css_selector(css_selector)
      sign_out.click()
    except Exception as e:
      print('Error logging out:', e)

  def check_user(self, user):
    profile_link = self.chrome.find_element_by_class_name('user-profile-link')
    profile_link_html = profile_link.get_attribute('innerHTML')
    print(profile_link_html)
    assert user in profile_link_html

if __name__ == '__main__':
  chrome = ChromeAuto()
  chrome.access('https://github.com/')
  sleep(SLEEP_TIME)
  chrome.click_sign_in()
  sleep(SLEEP_TIME)
  chrome.click_sign_in()
  sleep(SLEEP_TIME)
  chrome.sign_in()
  sleep(SLEEP_TIME)
  chrome.click_profile()
  sleep(SLEEP_TIME)
  chrome.check_user(user)
  sleep(SLEEP_TIME)
  chrome.log_out()
  sleep(SLEEP_TIME)
  chrome.quit()
