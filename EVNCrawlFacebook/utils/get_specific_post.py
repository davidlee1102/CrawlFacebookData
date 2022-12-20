import pprint

from selenium.webdriver.common.by import By

from EVNCrawlFacebook.selenium.utils import facebook_login
from EVNCrawlFacebook.utils import pre_process_selenium

import time
import re
import json


def crawler_specific_info(post_link: str, post_id: str):
    driver = facebook_login.login()
    post_link = post_link.replace("mbasic", "m")
    driver.get(post_link)
    time.sleep(2)
    xpath_address = f'//*[@id="sentence_{post_id}"]/a'
    interaction_link = driver.find_element(by=By.XPATH, value=xpath_address).get_attribute('href')
    driver.get(interaction_link)

    specific_info_list = []

    xpath_address = f'/html/body/div[1]/div/div[4]/div/div[1]/div/div/div[1]/div/div/div/span'
    reaction_type_list = driver.find_elements(by=By.XPATH, value=xpath_address)
    for reaction_type in reaction_type_list:
        reaction_type.click()
        time.sleep(2)
        try:
            try:
                reaction_type_text = reaction_type.find_element(by=By.TAG_NAME, value='span') \
                    .get_attribute('aria-label')
                match = re.compile(r'([A-Z].*)')
                reaction_type_text = match.search(reaction_type_text).group(1) or ''
            except:
                pass
            reaction_type = json.loads(reaction_type.get_attribute('data-store'))
            if reaction_type.get("reactionID", "") is 'all':
                continue

            else:

                reaction_id = reaction_type.get("reactionID", "")
                try:
                    xpath_address = f'//*[@id="reaction_profile_pager{reaction_id}"]/a/div/div/div/strong'
                    check_still = driver.find_element(by=By.XPATH, value=xpath_address)
                    while "xem" in check_still.text.lower():
                        check_still.click()
                        time.sleep(2)
                        check_still = driver.find_element(by=By.XPATH, value=xpath_address)
                except:
                    pass

                xpath_address = f'//*[@id="reaction_profile_browser{reaction_id}"]/div'
                reaction_info_list = driver.find_elements(by=By.XPATH, value=xpath_address)
                for reaction_info in reaction_info_list:
                    specific_info_json = {}

                    specific_info_json['reaction_type'] = reaction_type_text
                    try:
                        specific_info_json['user_info_name'] = reaction_info.find_element(by=By.TAG_NAME,
                                                                                          value='strong').text.strip()
                        specific_info_json['user_info_link'] = \
                            reaction_info.find_element(by=By.TAG_NAME,
                                                       value='a').get_attribute('href').replace("m.", "").split(
                                'groupid=')[
                                0].strip()[:-1]
                    except:
                        continue
                    specific_info_list.append(specific_info_json)
        except:
            continue
    return specific_info_list


def process_specific_info(post_link: str):
    post_id = pre_process_selenium.get_post_id_from_post_link(post_link)
    post_link = pre_process_selenium.change_facebook_link_to_mbasic(post_link)
    if "groups" not in post_link or not post_id:
        return None
    else:
        general_info = crawler_specific_info(post_link, post_id)
        return general_info
