#Author: Jospin Amisi
#Location: Malawi
#Phone Number: 0992129078
#Version: 1.0.0

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#the link to grabe the page
my_url = 'https://www.wecater.com.au/corporate-catering'

#opening up connection
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#page html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("li", {"class":"RestaurantMenuTableViewOrderImglessOption__item___3wwvx"})

#Create a file CSV
filename = "nourritures.csv" 

#Open the file CSV
f = open(filename, "w")

#header of the file CSV
headers = "Nom, Description, Prix\n";

#Write headers to the file CSV
f.write(headers)

for container in containers:
    #Brand name
    brand = container.div.div.div["RestaurantMenuTableViewOrderImglessOption__itemtitle___WgZWl"]
    
    #Product name 
    #title_container = container.div.div.div["RestaurantMenuTableViewOrderImglessOption__itemdescription___oYbzR"]
    title_container = container.findAll("div", {"class":"RestaurantMenuTableViewOrderImglessOption__itemdescription___oYbzR"})
    product_name = title_container[0].text
    
    #shiping address and price
    #shipping_container = container.div.div["RestaurantMenuTableViewOrderImglessOption__price___UZkek"]
    shipping_container = container.findAll("li", {"div": "RestaurantMenuTableViewOrderImglessOption__price___UZkek"})
    shipping = shipping_container[0].text.strip()
    
    #Printing information
    print("Brand: " + brand)
    print("Product Name " + product_name)
    print("Shipping Price " + shipping)
    
    #Write information to the file CSV
    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
 
#Close the file CSV
f.close()

