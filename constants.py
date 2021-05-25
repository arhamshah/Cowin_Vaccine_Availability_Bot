# Change these variables to your custom settings for telegram configuration
chat_id = "Your Config"
base_url = "Your Config"

# Change these variables to your custom settings for district configuration
# Default district_id = Ahmedabad
district_id = "770"

# Change these variables to your custom settings for API configuration
cowin_api = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date="
header_api = {'accept': 'application/json',
              'user-agent': 'TrackCovidVaccine Bot/V1.0; +https://arhamshah.tech/contact'}
