from functools import wraps
import redis
import requests


redis_client = redis.Redis()
def cache_page(func):
    @wraps(func)
    def wrapper(url):
        # Check if the result is cached in Redis
        cached_result = redis_client.get(f"page_cache:{url}")
        if cached_result:
            return cached_result.decode('utf-8')

        # If not cached, call the original function
        html_content = func(url)

        # Cache the result with expiration time of 10 seconds
        redis_client.set(f"page_cache:{url}", html_content, ex=10)

        return html_content
    
    return wrapper

@cache_page
def get_page(url: str) -> str:
    """
    Fetches the HTML content of the specified URL.

    Args:
        url (str): The URL to fetch HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    # Fetch HTML content from the URL
    response = requests.get(url)

    return response.text