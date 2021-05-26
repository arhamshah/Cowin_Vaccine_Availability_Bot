<h1 align="center">
  <a href="#"><img src="https://i.ibb.co/4tWKYXz/Orange-and-Blue-Illustrative-Coping-with-Stress-Landscape-COVID-Flyer.gif" alt="Logo of Program" width="400"></a>
  <br>
    Cowin Vaccine Availability Notifier Telegram Bot
  <br>
</h1>

<h3 align="center">A bot that notifies the available vaccines at given district in realtime.</h3>
  
<p align="center">
  <img src="https://forthebadge.com/images/badges/made-with-python.svg" alt="made with python">
  <img src="https://forthebadge.com/images/badges/built-with-love.svg" alt="built with love">
</p>

<p align="center">
  <a href="#introduction">Introduction</a> •
  <a href="#requirements">Requirements</a>  •
  <a href="#installation">Installation</a> •
  <a href="#working-of-bot">Working of Bot</a>               •
  <a href="#how-it-works">How it Works</a> •
  <a href="#thanks">Thanks ❤</a>
</p>

---

## Introduction
This Project uses an [API](https://apisetu.gov.in/public/marketplace/api/cowin#/) from Cowin Portal to find available doses of vaccines and automatically notifies the users via
Telegram Chat.

## Requirements

- Python 3.3+
- macOs or Linux or Windows

## Installation

### Building the source code

#### 1. Clone the repository
```sh
git clone https://github.com/arhamshah/Cowin_Vaccine_Availability_Bot.git
cd Cowin_Vaccine_Availability_Bot
```
#### 2. Create Virtual Environment 
```sh
python -m venv c:\path\to\myenv
```

#### 3. Download & Install all the Dependencies
```sh
pip install -r requirements.txt
``` 

## Working of Bot
<a href="#"><img src="https://i.ibb.co/hKfNmLT/Screenshot-20210525-235437.jpg" alt="Working of Project" width="300"></a>

## How it Works
- Data for upto 7 days is extracted from an API.
- Iterating over data to check for available vaccine doses.
- If any dose available then a message is sent via Telegram API to a specific channel.
- The particular data which have been sent to telegram is cached for 1 hour to prevent multiple notifications. 
- Data from API is updated every 4 seconds.  

## Thanks
- Government of India for providing open [API](https://apisetu.gov.in/public/marketplace/api/cowin#/) to extract the data in real time.
- Shout-out to developers & contributors of [Requests](https://docs.python-requests.org/en/master/), [cachetools](https://cachetools.readthedocs.io/en/stable/#).
