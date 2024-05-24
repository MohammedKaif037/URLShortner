import requests

def shorten_url(long_url, api_url="http://tinyurl.com/api-create.php"):
    """
    Shortens a long URL using the specified API endpoint URL.

    Args:
        long_url (str): The long URL to be shortened.
        api_url (str, optional): The URL of the API endpoint for URL shortening. Defaults to TinyURL API.

    Returns:
        str: The shortened URL.
    """
    try:
        # Make the GET request
        response = requests.get(api_url, params={'url': long_url})

        # Check if the request was successful
        if response.status_code == 200:
            # Return the shortened URL
            return response.text
        else:
            # Return an error message if the request failed
            return f"Error: Unable to shorten the URL. Status code: {response.status_code}"
    except Exception as e:
        # Return an error message if an exception occurs
        return f"Error: {str(e)}"

# Example usage
long_url = input("Enter the long URL to be shortened: ")
short_url = shorten_url(long_url)
print(f"Short URL: {short_url}")
