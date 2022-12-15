from selenium.webdriver.common.by import By

from EVNCrawlFacebook.selenium.utils import facebook_login
from EVNCrawlFacebook.utils import pre_process_selenium

import time


def crawler_general_info(post_link: str, post_id: str):
    general_info = {}
    driver = facebook_login.login()
    driver.get(post_link)
    time.sleep(2)
    xpath_address = f'//*[@id="sentence_{post_id}"]/a/div/div'
    general_interaction = driver.find_element(by=By.XPATH, value=xpath_address)
    general_info['Total'] = general_interaction.text
    xpath_address = f'//*[@id="sentence_{post_id}"]/a'
    interaction_link = driver.find_element(by=By.XPATH, value=xpath_address).get_attribute('href')
    driver.get(interaction_link)
    xpath_address = '//*[@id="root"]/table/tbody/tr/td/div/div/a'
    interaction_list = driver.find_elements(by=By.XPATH, value=xpath_address)
    for interaction in interaction_list:
        try:
            reaction_type = interaction.find_element(by=By.TAG_NAME, value='img').get_attribute('alt')
            total_reaction = interaction.find_element(by=By.TAG_NAME, value='span').text
            general_info[reaction_type] = total_reaction.strip()
        except Exception:
            continue
    return general_info


def process_general_info(post_link: str):
    post_id = pre_process_selenium.get_post_id_from_post_link(post_link)
    post_link = pre_process_selenium.change_facebook_link_to_mbasic(post_link)
    if "groups" not in post_link or not post_id:
        return None
    else:
        general_info = crawler_general_info(post_link, post_id)
        return general_info
