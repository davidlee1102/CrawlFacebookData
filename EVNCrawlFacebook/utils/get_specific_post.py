from selenium.webdriver.common.by import By

from EVNCrawlFacebook.selenium.utils import facebook_login
from EVNCrawlFacebook.utils import pre_process_selenium

import time


def crawler_specific_info(post_link: str, post_id: str):
    general_info = {}
    driver = facebook_login.login()
    post_link = post_link.replace("mbasic", "m")
    driver.get(post_link)
    time.sleep(2)
    xpath_address = f'//*[@id="sentence_{post_id}"]/a'
    interaction_link = driver.find_element(by=By.XPATH, value=xpath_address).get_attribute('href')
    driver.get(interaction_link)

    try:
        xpath_address = f'//*[@id="reaction_profile_pager"]/a/div/div/div/strong'
        check_still = driver.find_element(by=By.XPATH, value=xpath_address)
        while "xem" in check_still.text.lower():
            check_still.click()
            time.sleep(2)
            check_still = driver.find_element(by=By.XPATH, value=xpath_address)
    except:
        pass

    xpath_address = f'//*[@id="reaction_profile_browser"]/div'
    reaction_info_list = driver.find_elements(by=By.XPATH, value=xpath_address)
    print(len(reaction_info_list))

    #
    # for reaction_info in reaction_info_list:
    #     try:
    #         if "Xem" in reaction_info.find_element(by=By.TAG_NAME, value='span').text:
    #             print(reaction_info.find_element(by=By.TAG_NAME, value='a').get_attribute('href'))
    #         else:
    #             continue
    #     except:
    #
    #         continue
    time.sleep(5000)
    return None


def process_specific_info(post_link: str):
    post_id = pre_process_selenium.get_post_id_from_post_link(post_link)
    post_link = pre_process_selenium.change_facebook_link_to_mbasic(post_link)
    if "groups" not in post_link or not post_id:
        return None
    else:
        general_info = crawler_specific_info(post_link, post_id)
        return general_info
