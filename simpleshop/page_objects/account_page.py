

account_page_header = '#post-9 > header > h1'

def is_account_visible(driver_instance):
    account_header = driver_instance.find_element_by_css_selector(account_page_header)
    return account_header.is_displayed()