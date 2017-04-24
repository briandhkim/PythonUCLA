# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 16:19:34 2016

@author: Brian

the goal of this assignment was to create a .csv file to get the name, number, and description of different pokemon
by using Scrapy and pulling the data from a website. 
"""

import scrapy
from scrapy import Request

class Pokemonspider(scrapy.Spider):
    name = "pokemon"
    start_urls = ["https://fevgames.net/pokedex/"]
   
#   z = response.css('div.row') = 38 rows
#   z[0].css("a") = 4 objects
#   z[0].css("br") = 8 objects. number, name, number, name
   
    def parse(self, response):
        rows = response.css('div.row a')    #all the pokemons listed in rows
                                            #38 rows with 4 pokemon in each without a included
        
            
        for row in rows:
            d = {
                'Name: ':row.css("::text")[1].extract(),
                'Number: ':row.css("::text")[0].extract(),            
            }
            #yield d
            rel_url = row.css('a.pokedex-item::attr(href)').extract_first() #link to indiv poke
            full_url = response.urljoin(rel_url) #link to indiv. poke
            r = Request(full_url,self.parse2)
            r.meta["item"] = d
            yield r
            
            
    def parse2(self,response):
        d = response.meta["item"]
        description = response.css('article#omc-full-article td')[3]
        text = "".join(description.css("::text").extract())
        #text = "".join(description.extract())
        d["description"] = text
        yield d