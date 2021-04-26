# JIRA REPORTS

Playing around with Jira REST endpoint to check if we can build our custom reports not provided by EazyBI plugin. Based on `atlassian-python-api` client.

Tested on Python 3.7.9

## AUTHOR

PMO

## AUTH

To get oauth credentials follow (these instructions)[https://github.com/worldofchris/jlf/blob/master/README.md#configuring-oauth-access-to-jira], but in the current Jira cloud version the "Add Link" menu is in Gear menu --> Products --> Application Links"

The final cmd line to interactively get them looks like this:
```shell
jirashell -s  https://smartlis.atlassian.net -od -ck "pmo"  -k jira.pem -pt
```

## RUN

FIrst install dependencies with `pip install -r requirements.txt` then edit your own `.env` file and then run

### getReleases

``` python getReleases.py```

to get list and count of all releases in a particular project category