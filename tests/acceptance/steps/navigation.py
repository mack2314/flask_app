from behave import *
from selenium import webdriver

use_step_matcher('re') # this will allow to receive argument from scenarios in navigation.feature file

@given('I am on the homepage') #('/')
def step_impl(context): #this function will navigate through homepage
    context.browser = webdriver.chrome('chromedrive') # it will launch new chrome windonws
    context.browser.get('http://127.0.0.1:5000') # this will navigate

@then('I am in the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert  context.browser.current_url == expected_url
