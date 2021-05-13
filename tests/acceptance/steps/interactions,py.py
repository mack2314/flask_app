from behave import *

use_step_matcher('re') # this will allow to receive argument from scenarios in navigation.feature file

@when('I click on the the link with id"(.*)"')
def step_impl(context,link_id):
    link = context.browser.find_element_by_id(link_id)
    link.click()