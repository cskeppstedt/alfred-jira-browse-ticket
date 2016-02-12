# coding=utf-8

from feedback import Feedback
import sys
import urllib


def generate_items(projects=[], query=""):
    keys = set([p.split("/")[-1] for p in projects])
    query_split = query.split("-")
    query_key = query_split[0].upper()
    matches = set(k for k in keys if k.startswith(query_key))
    hasMatches = len(matches) > 0

    items = []

    for project in projects:
        proj_key = project.split("/")[-1]
        ticket_url = "%s-%s" % (project, query)

        if hasMatches:
            if proj_key not in matches:
                continue
            else:
                query_num = ""
                if len(query_split) > 1:
                    query_num = query_split[1]

                ticket_url = "%s-%s" % (project, query_num)

        items.append({
            "title": ticket_url,
            "subtitle": ticket_url,
            "valid": "YES",
            "arg": ticket_url,
            "icon": "icon.png"
        })

    return items


def send_feedback(feeds, items):
    for item in items:
        feeds.add_item(**item)

    print feeds


def main(projects, query):
    feeds = Feedback()
    items = generate_items(projects, query)
    send_feedback(feeds, items)


if len(sys.argv) == 2:
    with open('projects.txt') as f:
        projects = f.read().splitlines()
        query = urllib.quote(sys.argv[1])
        main(projects, query)
