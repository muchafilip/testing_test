import argparse
import requests
import sys
import json
import webbrowser
import urllib
import random


class CLIApp():
    """
    Get random media assets from nasa image/video API
    Example use: python3 nasa.py -c 5 -m image -l Mars -y 2018
    """

    def __init__(self):
        print("hello")

    def get_options(self, args=sys.argv[1:]):
        parser = argparse.ArgumentParser(description="Parses command.")
        parser.add_argument("-c", "--count", type=int,
                            help="Number of results displayed")
        parser.add_argument(
            "-m", "--media", type=str, choices=["image", "video"], help="Specify media type (image/video)")
        parser.add_argument("-l", "--location", type=str,
                            help="Where image/video was taken")
        parser.add_argument("-y", "--year", type=int,
                            help="year specified in format YYYY")
        options = parser.parse_args(args)
        return options

    def get_response(self, options):
        base_url = "https://images-api.nasa.gov"
        search_endpoint = "/search"
        # build querystring
        payload = {
            "q": options.location,
            "media_type": options.media,
            "year_start": options.year,
            "year_end": options.year,
            "keywords": options.location
        }
        url = base_url+search_endpoint
        try:
            response = requests.get(url=url, params=payload)
            # print(response.json())
            return response.json()
        except Exception as e:
            print(e, " error")

    def parse_results(self, results, options):
        output = []
        assets = results['collection']['items']
        random.shuffle(assets)
        if options.media == 'image':
            for result in assets[:options.count]:
                links = result['links']
                for link in links:
                    output.append(link['href'])
        else:
            for result in assets[:options.count]:
                videos_assets = result['href']
                links_collection = requests.get(videos_assets).json()
                for link in links_collection:
                    if link.endswith('orig.mp4'):
                        output.append(link)
        return output

    def open_assets(self, asset_array):
        for asset in asset_array:
            input(f"Press enter to open {asset}")
            webbrowser.open_new_tab(asset)


def main():
    app = CLIApp()
    options = app.get_options(sys.argv[1:])
    results = app.get_response(options)
    asset_array = app.parse_results(results, options)
    app.open_assets(asset_array)


if __name__ == '__main__':
    main()
