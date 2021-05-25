import sched
import time

import requests
from cachetools import TTLCache

from constants import cowin_api, header_api
from telegram_bot import initiate_send_message

# Initializing Scheduler Object
s = sched.scheduler(time.time, time.sleep)

# Caching the data to prevent sending multiple messages for same data
cache_memory = TTLCache(maxsize=50, ttl=3600)


def is_cached(session_id):
    '''
    This function checks whether given element is present in cached memory and returns a boolean
    :param session_id: Checks whether session_id is stored in cached memory or not (String)
    :return: Boolean: Returns True if session_id is present in cache_memory
    '''
    return session_id in cache_memory.keys()


def set_value_to_cache(session_id, center_name):
    '''
    This functions stores values in cached memory for specific amount of time
    :param session_id: session_id acts as a key in cached memory (String)
    :param center_name: center_name acts as a value in cached memory (String)
    :return: None
    '''
    cache_memory[session_id] = center_name


# API variables declared in constants.py
cowin_api
header_api


def fetch(date=time.strftime("%d-%m-%y", time.localtime())):
    '''
    This functions fetches real-time vaccine availability data from Cowin API and notifies users via telegram messages
    :param date: Today's date (String)
    :return: None
    '''
    # Requesting a response from API
    try:
        response = requests.get(cowin_api + date, headers=header_api)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    data = response.json()
    list_vaccine_avail = []

    # Filter List of Dictionaries by Availability of Vaccines
    for center in data["centers"]:
        for session in center["sessions"]:
            if session["available_capacity_dose1"] >= 5 or session["available_capacity_dose2"] >= 5:
                temp = dict(session)
                temp["name"] = center["name"]
                temp["block_name"] = center["block_name"]
                temp["pincode"] = center["pincode"]
                temp["fee_type"] = center["fee_type"]
                list_vaccine_avail.append(temp)

    # Sorting of list with date of availability
    list_vaccine_avail = sorted(list_vaccine_avail, key=lambda x: x["date"])

    # Condition Check if len(list_vaccine_avail) > 0
    if len(list_vaccine_avail) != 0:
        # Initiating initiate_send_message() to write messages to a particular telegram chat
        send_message = initiate_send_message()

        # Iterating through all available vaccine centers
        for i in list_vaccine_avail:
            # Check whether center is already cached
            if not is_cached(i["session_id"]):
                # Set session id and center name of available vaccine center in cached memory
                set_value_to_cache(i["session_id"], i["name"])
                msg_string = f'{i["name"]}\n({i["block_name"]}) - PinCode:- {i["pincode"]}\nDose 1:- {i["available_capacity_dose1"]}' \
                             f'\nDose 2 :- {i["available_capacity_dose2"]}\nMin. Age:- {i["min_age_limit"]}\nDate:- {i["date"]}' \
                             f'\nFee:- {i["fee_type"]}\nVaccine:- {i["vaccine"]}\nwww.cowin.gov.in'
                # Send Message to a particular telegram chat
                send_message(msg_string)
    else:
        print(time.asctime(time.localtime(time.time())))
        print("No Vaccine Available")

    # Scheduling fetch() for iterating at 4 seconds interval
    s.enter(4, 1, fetch)
    s.run()


# Calling the function fetch()
fetch()
