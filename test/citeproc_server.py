# curl --header "Content-type: application/json"
# --data @1.json -X POST   'http://127.0.0.1:8085?responseformat=json&style=4or&citations=1'
import json

import requests
import time
import urllib


def request_citeprocServer(json_input, style="4or", locale="en-US", bibliography=1, citations=1, outputformat="html",
                           responseformat="json"):
    begin = time.time()

    params = {
        "style": style,
        "locale": locale,
        "bibliography": bibliography,
        "citations": citations,
        "outputformat": outputformat,
        "responseformat": responseformat,
    }

    json_input = {
        "items": json_input
    }
    # api_url = "%s?%s" % ("http://192.168.1.62:8085", urllib.parse.urlencode(params))
    api_url = "%s?%s" % ("http://192.168.1.223:8085", urllib.parse.urlencode(params))
    result = requests.post(
        api_url,
        data=json.dumps(json_input),
        headers={"Content-type": "application/json"}

    )
    print(result.json()["bibliography"][1])
    # handle_file_server_response(result, sys._getframe().f_code.co_name)

    end = time.time()
    # logger.info("image2text cost: " + str(end - begin))
    # logger.info("image2text result: " + str(status))
    return result


if __name__ == '__main__':
    json_input = [{
            "id":107251,
            "indexed": {
                "date-parts": [
                    [
                        2021,
                        5,
                        24
                    ]
                ],
                "date-time": "2021-05-24T10:10:40Z",
                "timestamp": 1621851040754
            },
            "reference-count": 0,
            "publisher": "SAGE Publications",
            "issue": "3",
            "license": [
                {
                    "URL": "http://journals.sagepub.com/page/policies/text-and-data-mining-license",
                    "start": {
                        "date-parts": [
                            [
                                2021,
                                5,
                                5
                            ]
                        ],
                        "date-time": "2021-05-05T00:00:00Z",
                        "timestamp": 1620172800000
                    },
                    "delay-in-days": 0,
                    "content-version": "tdm"
                }
            ],
            "content-domain": {
                "domain": [
                    "journals.sagepub.com"
                ],
                "crossmark-restriction": True
            },
            "short-container-title": [
                "Journal of Family History"
            ],
            "published-print": {
                "date-parts": [
                    [
                        2021,
                        7
                    ]
                ]
            },
            "DOI": "10.1177/03631990211014871",
            # "DOI": "",
            # "type": "article-journal",
            "type": "webpage",
            "created": {
                "date-parts": [
                    [
                        2021,
                        5,
                        9
                    ]
                ],
                "date-time": "2021-05-09T06:40:19Z",
                "timestamp": 1620542419000
            },
            "page": "384-387",
            "update-policy": "http://dx.doi.org/10.1177/sage-journals-update-policy",
            "source": "Crossref",
            "is-referenced-by-count": 0,
            "title": [
                "Book Review: A Troubled Marriage: Indigenous Elites of the Colonial Americas, by McEnroe, Sean F"
            ],
            "prefix": "10.1177",
            "volume": "46",
            "author": [
                {
                    "given": "Ryan",
                    "family": "Hall",
                    "sequence": "first",
                    "affiliation": [
                        {
                            "name": "Colgate University, New York, NY, USA"
                        }
                    ]
                }
            ],
            "member": "179",
            "published-online": {
                "date-parts": [
                    [
                        2021,
                        5,
                        5
                    ]
                ]
            },
            # "container-title": [
            #     "Journal of Family History"
            # ],
            "original-title": [

            ],
            "language": "en",
            "link": [
                {
                    "URL": "http://journals.sagepub.com/doi/pdf/10.1177/03631990211014871",
                    "content-type": "application/pdf",
                    "content-version": "vor",
                    "intended-application": "text-mining"
                },
                {
                    "URL": "http://journals.sagepub.com/doi/full-xml/10.1177/03631990211014871",
                    "content-type": "application/xml",
                    "content-version": "vor",
                    "intended-application": "text-mining"
                },
                {
                    "URL": "http://journals.sagepub.com/doi/pdf/10.1177/03631990211014871",
                    "content-type": "unspecified",
                    "content-version": "vor",
                    "intended-application": "similarity-checking"
                }
            ],
            "deposited": {
                "date-parts": [
                    [
                        2021,
                        5,
                        24
                    ]
                ],
                "date-time": "2021-05-24T09:38:56Z",
                "timestamp": 1621849136000
            },
            "score": "1.0",
            "subtitle": [

            ],
            "short-title": [

            ],
            "issued": {
                "date-parts": [
                    [
                        2021,
                        5,
                        5
                    ]
                ]
            },
            "references-count": 0,
            "journal-issue": {
                "published-print": {
                    "date-parts": [
                        [
                            2021,
                            7
                        ]
                    ]
                },
                "issue": "3"
            },
            "alternative-id": [
                "10.1177/03631990211014871"
            ],
            "URL": "http://dx.doi.org/10.1177/03631990211014871",
            "relation": {

            },
            "ISSN": [
                "0363-1990",
                "1552-5473"
            ],
            "issn-type": [
                {
                    "value": "0363-1990",
                    "type": "print"
                },
                {
                    "value": "1552-5473",
                    "type": "electronic"
                }
            ],
            "subject": [
                "Social Sciences (miscellaneous)",
                "Arts and Humanities (miscellaneous)",
                "Anthropology"
            ]
        }]


    # request_citeprocServer(json_input, style="china-national-standard-gb-t-7714-2015-numeric")
    # request_citeprocServer(json_input, style="china-national-standard-gb-t-7714-2015-author-date")
    # request_citeprocServer(json_input, style="china-national-standard-gb-t-7714-2015-note")
    # request_citeprocServer(json_input, style="optics-letters")
    # request_citeprocServer(json_input, style="chinese-gb7714-1987-numeric")
    request_citeprocServer(json_input, style="chinese-gb7714-2005-numeric")
