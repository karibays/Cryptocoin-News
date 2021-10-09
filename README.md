# python_assignment_2

SOME DESCRIPTION ABOUT PROGRAMM IS ALREADY INSIDE THE CODE
AND HERE I WILL EXPLAIM ALL MY ACTIONS STEP BY STEP.

1) INSTALLED 'requests','beautifulsoup4' LIBRARIES
2) WROTE 3 FUNCTIONS: get_html, get_content, parse (LATER get_html WILL BE REMOVED)
3) GOT CONNECTION WITH THE WEBSITE, AND BY USING THIS 2 LIBRARIES, PARSED : coin_name, coin_price, coin_rank, coin_profit
4) THEN STARTED PARSING NEWS ABOUT THE COINS, BUT I FAILED DUE TO JAVASCRIPT. IT'S IMPOSSIBLE TO PARSE THE WEBSITE, IF JAVASCRIPT IS USED FOR OUTPUTTING THE DATA.
5) THEN FOUND SOLUTION BY INSTALLING SOME NEW LIBRARIES: WEBDRIVER, GOOGLEDRIVER, SELENIUM. 
6) WROTE A FUNCTION TO GET HTML CODE, AND THEN BY USING "BEAUTIFULSOUP4" FOUND NECESSARY BLOCKS OF THE CODE AND ADDED THEM TO THE LIST.
7) PROGRAM WAS WORKING SUCCESSFULLY, BUT BY REQUIRENMENT TO ASSIGNMENT I HAD TO USE OOP.
8) CREATED A NEW FILE "coin.py", CREATED CLASS 'coin_info' AND PASTED ALL THE CODE RIGHT THERE
9) THEN PROGRAMM STOPPED WORKING DUE TO SOME TROUBLES WITH THE FUNCTIONS (RIGTH AT THIS MOMENT THERE WAS DECIDED TO REMOVE "get_html" FUNCTION, AND JUST CREATE A VARIABLE INSTEAD)
10) FIXED ALL THE BUGS, TESTED 165446465465 TIMES, AND UPLOADED TO THE GITHUB

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

TITLE: ASSIGNMENT 2 PYTHON OR PARSING THE https://coinmarketcap.com 

INSTALLATION: pip install requests, pip install beautifulsoup4, pip install selenium, pip install webdriver, and google driver from https://chromedriver.storage.googleapis.com/index.html?path=2.26/

USAGE: 
requests - to send a request to a website. if it runs successfully, we get 'respond 200', or we can use '.status_code' method and get just 200, and by using '.text' methon we get HTML code
beautifulsoup4 - to get HTML code, and parse it by using '.find_all' , '.find' , '.BeautifulSoup' methods
selenium - to get access to a driver (most cases need to install '.exe' driver file)
webdriver - to get HTML code from JavaScripts and then parse it by using 'beautifulsoup4'

EXAMPLES(1 EXAMPLE TO 1 LIBRARY): 
requests: r = requests.get(coin_info.URL,headers = coin_info.HEADERS)
beautifulsoup4: soup = BeautifulSoup(html, 'html.parser')
selenium: driver = webdriver.Chrome(r"C:\Users\Карибай\Desktop\Homework\chromedriver.exe") --------- THERE IS A LINK TO THE DRIVER IN MY PC (EXE FILE)
webdriver: driver.get(coin_info.URL_NEWS)
