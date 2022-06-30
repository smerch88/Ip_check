import re
import ipinfo
import csv
from collections import Counter


def reader(filename):

    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(filename) as f:
        log = f.read()

        ip_list = re.findall(regexp, log)

    return ip_list


def count(ip_list):
    count = Counter(ip_list)    
    return count


def get_info_ip(ip_address='112.93.204.145', access_token=''):
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    all_details = details.all
    return all_details


def write_csv(count):
    
    with open('output.csv', 'w', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP', 'Frequency', 'City', 'Region', 'Country', 'Location', 'Organisation', 'Timezone', 'Country Name', 'Latitude', 'Longitude', 'Extra Data']
        writer.writerow(header)

        for item in count:
            all_details = get_info_ip(item)
            writer.writerow( (item, count[item], all_details['city'], all_details['region'], all_details['country'], all_details['loc'], all_details['org'], all_details['timezone'], all_details['country_name'], all_details['latitude'], all_details['longitude'], all_details) )

if __name__ == '__main__':
    
    reader('access.log')

    get_info_ip()

    write_csv(count(reader('access.log')))
