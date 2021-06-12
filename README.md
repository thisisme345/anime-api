# AniX - Stream Animes

<img style="border-radius: 4px; margin-bottom: 16px" src="https://res.cloudinary.com/tylerdurden/image/upload/v1611635911/random/cb_amdqeu.png" alt="banner" height="280">

This is the backend repository of AniX built with scrapy framework. If you want to visit the frontend repo, [click here](https://github.com/manikandanraji/AniX).

## Spiders

| name                                           | description                  |
| ---------------------------------------------- | ---------------------------- |
| [animes](anix/spiders/animes.py)               | fetch animes                 |
| [anime](anix/spiders/anime.py)                 | fetch a single anime         |
| [search_animes](anix/spiders/search_animes.py) | search animes                |
| [stream](anix/spiders/stream.py)               | fetch mp4 link for a episode |

## Running Locally

- Clone this repo to your local machine and navigate to the root directory

- Run the following commands to start the http server

	```bash
	pipenv shell # creating a virtual env

	pipenv install # installing dependencies

	scrapyrt # start the http server
	```
- By default, the http server will listening for requests at port 9080
