#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import webbrowser

"""class Movie encapsulate four parameters of one movie which contains title、
   storyline、box art imagine url、the trailer url of youtube and class method
   whose name is play_trailer allows any instance can call itself to play the
   trailer."""


class Movie():
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
