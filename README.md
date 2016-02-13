# alfred-jira-browse-ticket

[![Build Status](https://travis-ci.org/cskeppstedt/alfred-jira-browse-ticket.svg?branch=master)](https://travis-ci.org/cskeppstedt/alfred-jira-browse-ticket)

Workflow for Alfred 2 that opens a JIRA ticket in the browser. Enter `jira 12345` or `jira PROJ-12345` in Alfred, and the full URL for the ticket will be suggested to you.

## Demo

![jira alfred](https://cloud.githubusercontent.com/assets/569742/13027725/a03e4db0-d25a-11e5-903c-0074bf37ef7e.gif)

## Setup

Download and install the workflow. Open alfred preferences, go to the Worflows tab.

1. Right click the workflow "Jira browse ticket" and select "Show in Finder"
2. Open projects.txt
3. Add the full URL for your JIRA setup, with the project prefix. Example: https://your.jira.com/PROJ

Now you can use Alfred and enter "jira 12345" which will suggest "https://your.jira.com/PROJ-12345". You can repeat step 3 if you want additional projects/instances.
