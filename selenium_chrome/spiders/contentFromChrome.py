# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep




class ContentfromchromeSpider(scrapy.Spider):
    name = 'contentFromChrome'
    #start_urls = ['https://www.google.com/search?q=jobs+near+me&ibp=htl;jobs']
    def start_requests(self):
        yield scrapy.Request(url='https://www.google.com/search?q=jobs+near+me&ibp=htl;jobs', callback=self.parse)
    
    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get('https://www.google.com/search?q=jobs+near+me&ibp=htl;jobs')
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//html"))
        )
        self.driver.maximize_window()
        elems=self.driver.find_elements_by_xpath("//div[contains(@class,'nsol9b hxSlV') or contains(@class, 'k8RiQ nsol9b hxSlV')]")
        i=0
        links=''
        list=[]
        listOfApplys=[]
        list_of_list=[]
        for ele in elems:
            list.append(ele.text)
            if(i==2):
                i=0
                list_of_list.append(list)
                list=[]
            else:
                i=i+1

        apply_links=self.driver.find_elements_by_xpath("//a[@class='D7VqAe LwS2ce']")
        for link in apply_links:
            tag_=link.text
            if(tag_!=''):
                listOfApplys.append(tag_)

       	yield{
                    "Left_side_values" : list_of_list,
                    "Right side_values" : listOfApplys,
                }
