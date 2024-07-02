from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Scraper.constants as const
from selenium.webdriver.common.keys import Keys
import os
from dataclasses import dataclass
from time import sleep
import time

@dataclass
class Product:
    title: str
    price: str
    product_dimension: str
    item_weight: str
    model_number: int
    battery_power_rating: str
    seller_rank: str
    customer_review: str
    os: str
    ram: str
    color: str
    country_of_origin: str





class Amazon(webdriver.Chrome):
    def __init__(self, driver_path= const.PATH, ex= False ):
        self.ex=ex
        self.driver= driver_path
        os.environ['PATH']+= self.driver
        super(Amazon,self).__init__()
        self.implicitly_wait(5)
        self.maximize_window()


    def get_website(self):
        self.get(const.URL)

    def __exit__ (self, exc_type,exc_val,exc_tb):
        if self.ex:
            self.quit()


    def search(self):
        search_box= self.find_element(
            By.ID,"twotabsearchtextbox"
            )
        search_box.clear()
        search_box.send_keys("iphone")
        search_box.send_keys(Keys.RETURN)
        """search_icon =  self.find_element(
            By.XPATH,' //*[@id="nav-search-submit-button"]'
        )
        search_icon.click()"""

    def shop_now(self):
        shop= self.find_element(By.CSS_SELECTOR,'a[class="a-link-normal see-more truncate-1line"]')

        shop.click()


    def find_all_box(self):
        names=self.find_elements(By.CSS_SELECTOR,'span[class="a-size-base-plus a-color-base a-text-normal"]')
        print(names)
        """for i in names:
            print(i.text)"""


    def filter(self):
        brand= self.find_element(By.XPATH,
        '/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[5]/ul/li[1]/span/a/span'
        )

        brand.click()

    def phone_price(self):
        prices = self.find_elements(By.CSS_SELECTOR,'span[class="a-price-whole"]')
        for price in prices:
            print(price.text)

   

    def phone(self,link):  # sourcery skip: use-contextlib-suppress

        
        self.get(link)

        try:
            title= self.find_element(By.XPATH,'//span[@id="productTitle"]').text
        except Exception:
            pass
        try:
            price= self.find_element(By.XPATH,'//span[@class="a-offscreen"]').text
        except:
            pass
        try:
            product_dimension= self.find_element(By.XPATH,'//td[@class="a-size-base prodDetAttrValue"]').text
        except:
            pass
        try:
            item_weight= self.find_element(By.XPATH,'//*[contains(text(),"Item Weight")]/following-sibling::td').text
        except:
            pass
        try:

            model_number= self.find_element(By.XPATH,'//*[contains(text(),"Item model number")]/following-sibling::td').text
        except:
            pass
        try:
            battery_power_rating= self.find_element(By.XPATH,'//*[contains(text(),"Battery Power Rating")]/following-sibling::td').text
        except:
            pass
        try:
            seller_rank= self.find_element(By.XPATH,'//*[contains(text(),"Best Sellers Rank")]/following-sibling::td/span/span').text
        except:
            pass
        try:
            customer_review=self.find_element(By.XPATH,'//*[contains(text(),"Customer Reviews")]/following-sibling::td').text
        except:
            pass
        try:
            os=self.find_element(By.XPATH,'//*[contains(text(),"OS")]/following-sibling::td').text.strip('\n')
        except:
            pass
        try:
            ram=self.find_element(By.XPATH,'//*[contains(text(),"RAM")]/following-sibling::td').text
        except:
            pass
        try:
            color=self.find_element(By.XPATH,'//*[contains(text(),"Colour")]/following-sibling::td').text
        except:
            pass
        try:
            country_of_origin=self.find_element(By.XPATH,'//*[contains(text(),"Country of Origin")]/following-sibling::td').text  
        except:
            pass  

        print(title)






        

   

    def phone_details(self):
        
            all_phone= WebDriverWait(self,10).until(EC.presence_of_element_located(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]'))
            products=[]
            try:
                for phone in all_phone:
                    phone= WebDriverWait(self,10).until(EC.presence_of_element_located(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]'))
                    phone.click()
                    new_item= Product(
                            title= self.find_element(By.ID,"productTitle").text,
                            price= self.find_element(By.CSS_SELECTOR,'span[aria-hidden="true"]').text,
                            product_dimension= self.find_element(By.XPATH,'//td[@class="a-size-base prodDetAttrValue"]').text,
                            item_weight= self.find_element(By.XPATH,'//*[contains(text(),"Item Weight")]/following-sibling::td').text,
                            model_number= self.find_element(By.XPATH,'//*[contains(text(),"Item model number")]/following-sibling::td').text,
                            battery_power_rating= self.find_element(By.XPATH,'//*[contains(text(),"Battery Power Rating")]/following-sibling::td').text,
                            seller_rank= self.find_element(By.XPATH,'//*[contains(text(),"Best Sellers Rank")]/following-sibling::td/span/span').text,
                            customer_review=self.find_element(By.XPATH,'//*[contains(text(),"Customer Reviews")]/following-sibling::td').text,
                            os=self.find_element(By.XPATH,'//*[contains(text(),"OS")]/following-sibling::td').text.strip('\n'),
                            ram=self.find_element(By.XPATH,'//*[contains(text(),"RAM")]/following-sibling::td').text,
                            color=self.find_element(By.XPATH,'//*[contains(text(),"Colour")]/following-sibling::td').text,
                            country_of_origin=self.find_element(By.XPATH,'//*[contains(text(),"Country of Origin")]/following-sibling::td').text    

                                        )
                    products.append(new_item)
                    self.back()
                    time.sleep(5)
            except Exception as e:
                print(e)
        



            print((products))


    def details(self):
        all_phone= WebDriverWait(self,10).until(EC.presence_of_all_elements_located(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]'))
        products=[]
        try:
            for phone in all_phone:
                phone= WebDriverWait(self,10).until(EC.presence_of_element_located(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]'))
                phone.click()
                new_item= Product(
                            title= self.find_element(By.ID,"productTitle").text,
                            price= self.find_element(By.CSS_SELECTOR,'span[aria-hidden="true"]').text,
                            product_dimension= self.find_element(By.XPATH,'//td[@class="a-size-base prodDetAttrValue"]').text,
                            item_weight= self.find_element(By.XPATH,'//*[contains(text(),"Item Weight")]/following-sibling::td').text,
                            model_number= self.find_element(By.XPATH,'//*[contains(text(),"Item model number")]/following-sibling::td').text,
                            battery_power_rating= self.find_element(By.XPATH,'//*[contains(text(),"Battery Power Rating")]/following-sibling::td').text,
                            seller_rank= self.find_element(By.XPATH,'//*[contains(text(),"Best Sellers Rank")]/following-sibling::td/span/span').text,
                            customer_review=self.find_element(By.XPATH,'//*[contains(text(),"Customer Reviews")]/following-sibling::td').text,
                            os=self.find_element(By.XPATH,'//*[contains(text(),"OS")]/following-sibling::td').text.strip('\n'),
                            ram=self.find_element(By.XPATH,'//*[contains(text(),"RAM")]/following-sibling::td').text,
                            color=self.find_element(By.XPATH,'//*[contains(text(),"Colour")]/following-sibling::td').text,
                            country_of_origin=self.find_element(By.XPATH,'//*[contains(text(),"Country of Origin")]/following-sibling::td').text    

                                        )
                products.append(new_item)
                self.back()
                time.sleep(5)
        except Exception as e:
            print(e)
        else:


            print((products))

    def details_1(self):
        wait = WebDriverWait(self, 10)
        length = len(self.find_elements_by_xpath('//span[@class="a-size-base-plus a-color-base a-text-normal"]'))
        print(f"List length is: {length}")
        for j in range(1, length+1):
            try:
                print(f"Clicking Page {str(j)}")
                wait.until(
                    EC.visibility_of_element_located((By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]')))
                wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='paginate_button next'][@id='proxylisttable_next']/a")))
            finally:
                next_phone = self.find_element_by_xpath(
                    "//li[@class='paginate_button next'][@id='proxylisttable_next']/a")
                next_phone.click()
                new_item= Product(
                            title= self.find_element(By.ID,"productTitle").text,
                            price= self.find_element(By.CSS_SELECTOR,'span[aria-hidden="true"]').text,
                            product_dimension= self.find_element(By.XPATH,'//td[@class="a-size-base prodDetAttrValue"]').text,
                            item_weight= self.find_element(By.XPATH,'//*[contains(text(),"Item Weight")]/following-sibling::td').text,
                            model_number= self.find_element(By.XPATH,'//*[contains(text(),"Item model number")]/following-sibling::td').text,
                            battery_power_rating= self.find_element(By.XPATH,'//*[contains(text(),"Battery Power Rating")]/following-sibling::td').text,
                            seller_rank= self.find_element(By.XPATH,'//*[contains(text(),"Best Sellers Rank")]/following-sibling::td/span/span').text,
                            customer_review=self.find_element(By.XPATH,'//*[contains(text(),"Customer Reviews")]/following-sibling::td').text,
                            os=self.find_element(By.XPATH,'//*[contains(text(),"OS")]/following-sibling::td').text.strip('\n'),
                            ram=self.find_element(By.XPATH,'//*[contains(text(),"RAM")]/following-sibling::td').text,
                            color=self.find_element(By.XPATH,'//*[contains(text(),"Colour")]/following-sibling::td').text,
                            country_of_origin=self.find_element(By.XPATH,'//*[contains(text(),"Country of Origin")]/following-sibling::td').text    

                                        )
                products.append(new_item)
                self.back()
                time.sleep(5)


    def all_links(self):
        link= self.find_elements(By.CSS_SELECTOR,'a[class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"')

        all_url=[l.get_attribute('href') for l in link]
        all_url_2= list(set(all_url))

        print(len(all_url))
        print(len(all_url_2))

        
        """for l in all_url:
            Amazon.phone(self,l)
            sleep(2)"""


    