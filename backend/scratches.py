basic = {"name": "John Doe","label": [{"tags":["tag"],"label":"Programmer"}],"image": "https://somesite.tld/img.png","email": "john@gmail.com","phone": "(912) 555-4321","url": "https://johndoe.com","summary": [{"tags":["tag"],"summary":"A summary of John Doe…"}],"location": {"address": "2712 Broadway St","postal_code": "CA 94115","city": "San Francisco","countryCode": "US","region": "California"},"profiles": [{"tags": ["tag"],"network": "Twitter","username": "john","url": "https://twitter.com/john"}]}

def resume():
    return {"basics":{"name":"John Doe","label":[{"tags":["tag"],"label":"Programmer"}],"image":"","email":"john@gmail.com","phone":"(912) 555-4321","url":"https://johndoe.com","summary":[{"tags":["tag"],"summary":"A summary of John Doe…"}],"location":{"address":"2712 Broadway St","postalCode":"CA 94115","city":"San Francisco","countryCode":"US","region":"California"},"profiles":[{"tags":["tag"],"network":"Twitter","username":"john","url":"https://twitter.com/john"}]},"work":[{"tags":["tag"],"name":"Company","position":"President","url":"https://company.com","startDate":"2013-01-01","endDate":"2014-01-01","summary":"Description…","highlights":["Started the company"]}],"volunteer":[{"tags":["tag"],"organization":"Organization","position":"Volunteer","url":"https://organization.com/","startDate":"2012-01-01","endDate":"2013-01-01","summary":"Description…","highlights":["Awarded 'Volunteer of the Month'"]}],"education":[{"tags":["tag"],"institution":"University","url":"https://institution.com/","area":"Software Development","studyType":"Bachelor","startDate":"2011-01-01","endDate":"2013-01-01","score":"4.0","courses":["DB1101 - Basic SQL"]}],"awards":[{"tags":["tag"],"title":"Award","date":"2014-11-01","awarder":"Company","summary":"There is no spoon."}],"certificates":[{"tags":["tag"],"name":"Certificate","date":"2021-11-07","issuer":"Company","url":"https://certificate.com"}],"publications":[{"tags":["tag"],"name":"Publication","publisher":"Company","releaseDate":"2014-10-01","url":"https://publication.com","summary":"Description…"}],"skills":[{"tags":["tag"],"name":"Web Development","level":"Master","keywords":["HTML","CSS","JavaScript"]}],"languages":[{"tags":["tag"],"language":"English","fluency":"Native speaker"}],"interests":[{"tags":["tag"],"name":"Wildlife","keywords":["Ferrets","Unicorns"]}],"references":[{"tags":["tag"],"name": "Jane Doe", "reference": "Reference…"}],"projects": [{"tags": ["tag"], "name": "Project", "startDate": "2019-01-01", "endDate": "2021-01-01", "description": "Description...", "highlights": ["Won award at AIHacks 2016"], "url": "https://project.com/"}],"tags":["tag"]}

def testy_resume():
    return {
        "basics": {
            "name": "Test McTest",
            "label": [
                {
                    "tags": [
                        "tech"
                    ],
                    "label": "Programmer"
                },
                {
                    "tags": [
                        "craft"
                    ],
                    "label": "Wood Worker"
                }
            ],
            "image": "",
            "email": "test@notmail.not",
            "phone": "(912) 555-4321",
            "url": "https://johndoe.not",
            "summary": [
                {
                    "tags": [
                        "tech"
                    ],
                    "summary": "Once uppon a computer..."
                },
                {
                    "tags": [
                        "craft"
                    ],
                    "summary": "From a we lad to an ax man..."
                }
            ],
            "location": {
                "address": "2712 Broadway St",
                "postalCode": "CA 94115",
                "city": "San Francisco",
                "countryCode": "US",
                "region": "California"
            },
            "profiles": [
                {
                    "tags": [
                        "tech"
                    ],
                    "network": "github",
                    "username": "Test",
                    "url": "https://github.not/john"
                },
                {
                    "tags": [
                        "craft"
                    ],
                    "network": "Wood workers united",
                    "username": "Test",
                    "url": "https://wwu.not/john"
                }
            ]
        },
        "work": [
            {
                "tags": [
                    "tech"
                ],
                "name": "techie name",
                "position": "President",
                "url": "https://company.not",
                "startDate": "2013-01-01",
                "endDate": "2014-01-01",
                "summary": "Description…",
                "highlights": [
                    "Started techie name"
                ]
            },
            {
                "tags": [
                    "craft"
                ],
                "name": "woodie place",
                "position": "craftsman",
                "url": "https://woodplace.not",
                "startDate": "2013-01-01",
                "endDate": "2014-01-01",
                "summary": "Description…",
                "highlights": [
                    "did cool things"
                ]
            },
            {
                "tags": [
                    "tech"
                ],
                "name": "Company",
                "position": "President",
                "url": "https://company.com",
                "startDate": "2013-01-01",
                "endDate": "2014-01-01",
                "summary": "Description…",
                "highlights": [
                    "Started the company"
                ]
            }
        ],
        "volunteer": [
            {
                "tags": [
                    "tech"
                ],
                "organization": "Organization",
                "position": "Volunteer",
                "url": "https://organization.com/",
                "startDate": "2012-01-01",
                "endDate": "2013-01-01",
                "summary": "Description…",
                "highlights": [
                    "Awarded 'Volunteer of the Month'"
                ]
            }
        ],
        "education": [
            {
                "tags": [
                    "tech"
                ],
                "institution": "Totally Tech the institution",
                "url": "https://tech.not/",
                "area": "Software Development",
                "studyType": "Bachelor",
                "startDate": "2011-01-01",
                "endDate": "2013-01-01",
                "score": "4.0",
                "courses": [
                    "DB1101 - Basic SQL"
                ]
            }
        ],
        "awards": [
            {
                "tags": [
                    "craft"
                ],
                "title": "wudward",
                "date": "2014-11-01",
                "awarder": "theBigWood",
                "summary": "There is only wood."
            }
        ],
        "certificates": [
            {
                "tags": [
                    "tech"
                ],
                "name": "Certified Nerd",
                "date": "2021-11-07",
                "issuer": "Nerdify",
                "url": "https://certificate.not"
            }
        ],
        "publications": [
            {
                "tags": [
                    "craft"
                ],
                "name": "Publication",
                "publisher": "Company",
                "releaseDate": "2014-10-01",
                "url": "https://publication.com",
                "summary": "I think this menas books or papers?"
            }
        ],
        "skills": [
            {
                "tags": [
                    "tech"
                ],
                "name": "Web Development",
                "level": "Master",
                "keywords": [
                    "HTML",
                    "CSS",
                    "JavaScript",
                    "puppets"
                ]
            }
        ],
        "languages": [
            {
                "tags": [
                    "wood"
                ],
                "language": "elvish",
                "fluency": "Native speaker"
            }
        ],
        "interests": [
            {
                "tags": [
                    "wood"
                ],
                "name": "Wildlife",
                "keywords": [
                    "Ferrets",
                    "Unicorns"
                ]
            },
            {
                "tags": [
                    "tech"
                ],
                "name": "Cybersecurity",
                "keywords": [
                    "Cyber Ferrets",
                    "Cyber Unicorns"
                ]
            }

        ],
        "references": [
            {
                "tags": [
                    "tech"
                ],
                "name": "Smarty nerd",
                "reference": "is good"
            },
            {
                "tags": [
                    "tech"
                ],
                "name": "impressive refference person",
                "reference": "really awesome"
            },
            {
                "tags": [
                    "craft"
                ],
                "name": "donny McWood",
                "reference": "can craft"
            }
        ],
        "projects": [
            {
                "tags": [
                    "tech"
                ],
                "name": "ultimate hacker ai",
                "startDate": "2019-01-01",
                "endDate": "2021-01-01",
                "description": "is kinda scary and might eat you.",
                "highlights": [
                    "Won award at AIHacks 2016"
                ],
                "url": "https://project.not/"
            },
            {
                "tags": [
                    "tech"
                ],
                "name": "project writing project",
                "startDate": "2019-01-01",
                "endDate": "2021-01-01",
                "description": "Makes projects for you",
                "highlights": [
                    "is very creative"
                ],
                "url": "https://projectproject.not/"
            },
            {
                "tags": [
                    "craft"
                ],
                "name": "Chair",
                "startDate": "2019-01-01",
                "endDate": "2021-01-01",
                "description": "the nices chair you have ever seen...",
                "highlights": [
                    "Won award at chair con 2016"
                ],
                "url": "https://awesomechairs.not/"
            }
        ],
        "tags":["tech","wood","craft"]
    }
