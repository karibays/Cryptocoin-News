# --------- LIBRARIES || PACKAGES -------------
import requests 
from bs4 import BeautifulSoup
from bs4.element import ProcessingInstruction
from bs4 import BeautifulSoup
from selenium import webdriver

# -------- PROGRAM'S BEGINNIG ---------
class coin_info:

    # -------- NECESSARY VALUES ------------- 
    coin = input("Enter a coin name: ").lower() # constructor didn`t work the right way I need, so there was decided to use 'input' method
   
     # --------------- URL ---------------------
    URL = f"https://coinmarketcap.com/currencies/{coin}/"
    URL_NEWS = f"https://coinmarketcap.com/currencies/{coin}/news/"
    
    # ----------- HEADER OF THE WEBSITE --------------------- 
    HEADERS = {"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36",
                "accept" : "*/*"}
    

    # ----------------- SENDING REQUEST TO A WEBSITE -------------------
    def parse(self):
        r = requests.get(coin_info.URL,headers = coin_info.HEADERS)

        # -------------- IF OUTPUT IS 200, THEN CONDITION WILL EXECUTE 'GET_CONTENT' FUNCTION ---------------------
        if r.status_code == 200:
            coin_info.get_content(r.text)
        else:
            print("There is no such a coin")
    

    #------- GET CONTENT --------
    def get_content(self):

        #-------- GETTING REQUESTS --------------
        html = requests.get(coin_info.URL,headers = coin_info.HEADERS).text
        soup = BeautifulSoup(html, 'html.parser')

        #-------- SEARCHING BLOCK OF HTML CODE BY CLASS -----------
        items = soup.find_all('div',class_='sc-16r8icm-0 eMxKgr container')

        #-------- COINS LIST ------------
        coins = []
        for item in items:
            coins.append({
                'title': item.find('h2', class_='jCInrl').get_text(strip=True),
                'rank': item.find('div', class_='namePill namePillPrimary').get_text(strip=True),
                'usd_price': item.find('div', class_='priceValue').get_text(strip=True),
                'profit': item.find('span', class_='sc-15yy2pl-0').get_text(strip=True)
            })

         # First I parsed information about the coin we input, like: title, rank in the world, price in USD, profit
         # Only then parsed news about the coin 
         #--------------------------------------------------------------------------------------------
        
        
        # -------------- GOOGLE GHROME DRIVER -------------------------------
        driver = webdriver.Chrome(r"C:\Users\Карибай\Desktop\Homework\chromedriver.exe")
        driver.get(coin_info.URL_NEWS)
        page = driver.page_source
        # The website uses JavaScript to output news about coins, and this is why it`s impossible to get a code 
        # Just by using 'request'. 



        # ------------ PARSING THE WEBSITE ------------------
        page_soup = BeautifulSoup(page,'html.parser')
        blocks = page_soup.findAll("div",{"class":"svowul-5 czQlor"})

        # ----------- COINS NEWS LIST -----------------
        coin_news = []
        for item in blocks:
            coin_news.append({
                        'news_title': item.find('h3', class_='sc-1q9q90x-0 gEZmSc').get_text(strip=True),
                        'news_content': item.find('p', class_='sc-1eb5slv-0 svowul-3 ddtKCV').get_text(strip=True),
                        'more-information': item.find('a', class_='svowul-0 jMBbOf cmc-link').get('href')
                    })
        
        # ------------ OUTPUTING THE COINS_LIST AND COINS_NEWS_LIST -----------------------
        print(coins)
        print() # SPACE
        for item in coin_news:
            print(item)
            print("---------------------"*3)

# ------------------------------- THE END OF THE PROGRAM ---------------------------------------