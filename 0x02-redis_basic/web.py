#!/usr/bin/env python3
"""implements a web cache"""
import requests
import redis


r = redis.Redis()


def get_page(url: str) -> str:
    '''implements the cache'''
    key = "count:{}".format(url)
    '''
    increment the count of how many times url has been visited
    '''
    r.incr(key)
    cached_data = r.get(url)
    '''
    check if we have data associated with url in cache
    '''
    if cached_data is not None:
        return cached_data.decode('utf-8')
    '''
    incase we have no data, query the url and add in cache for 10 seconds
    '''
    resp = requests.get(url)
    info = resp.text
    r.setex(url, 10, info)
    return info