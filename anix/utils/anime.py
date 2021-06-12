import requests

query = '''
query ($search_term: String) {
  Media (search: $search_term type: ANIME) {
    id
    title {
      english
      romaji
    }
    coverImage {
      extraLarge
      large
      medium
      color
    }
    season
    duration
    seasonYear
    bannerImage
    episodes
    description
    genres
    format
    averageScore
    status
     startDate {
      year
      month
      day
    }
    endDate {
      year
      month
      day
    }
    trailer {
      id
    }
  }
}
'''

def parse_anime(response):
    episode_links = response.css('ul.episodes li a::attr("href")').getall()

    search_term = response.css('.single-anime-desktop::text').get()
    variables = {
        'search_term': search_term
    }
    url = 'https://graphql.anilist.co'

    res = requests.post(url, json={'variables': variables, 'query': query})

    if(res.status_code == 200):
        data = res.json()
        anime = data["data"]["Media"]
        anime["episode_links"] = episode_links
        anime["slug"] = response.url.split("/")[-1]
        return anime


# deprecated, not using this
def anime(self, response):
    details = response.css("div.detail")

    poster = response.css("div.cover img::attr('src')").get()
    slug = response.url.split("/")[-1]
    title = response.css("p.single-anime-desktop::text").get()
    genres = response.css('div.list.tag a::text').getall()
    episodes = len(response.css('ul.episodes li').getall())

    # from details
    category = details[0].css('a::text').get()
    studio = details[1].css('a::text').get()
    status = details[2].css('a::text').get()

    # season, seasonYear
    release = details[2].css('a')
    season = release[0].css('a::text').get()
    seasonYear = release[1].css('a::text').get()

    return {
        'coverImage': {
            'extraLarge': response.urljoin(poster)
        },
        'title': {
            'english': title
        },
        'seasonYear': seasonYear,
        'season': season,
        'studio': studio,
        'format': category,
        'genres': genres,
        'slug': slug,
        'episodes': episodes
    }
