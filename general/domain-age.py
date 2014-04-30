#!/usr/bin/env python

try:
  import whois
  from dateutil import relativedelta
except ImportError:
  print("Error importing necessary modules, check if they are installed.")
  exit(1)

import datetime
import sys

if len(sys.argv) < 2:
  print("Please supply a domain name")
  exit(1)

domain = sys.argv[1]
whois_info = whois.whois(domain.lower())

if whois_info.creation_date:
  current_date = datetime.datetime.now()
  try:
    created_on = whois_info.creation_date[0]
    diff = relativedelta.relativedelta(current_date, created_on)
  except TypeError:
    print("Error calculating age difference - whois data may be missing or invalid")
    exit(1)

  print("%s was created %s years and %s months ago on %s" % (domain, diff.years, diff.months, created_on.strftime("%Y-%m-%d")))

else:
  print("No creation date returned :(")
  exit(1)
