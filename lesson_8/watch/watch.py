"""
iframe is an HTML 'element' and arc is one of several HTML 'attributes' therein, the value of which, between quotes
is https://www.youtube.com/embed/xvFZjo5PgG0
    <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"
    title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
    clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
    </iframe>

Suppose that you'd like to extract URLs of YT videos that are embedded in pages, converting them back to shorter,
shareable youtu.be URLs (e.g. https://youtu.be/xvFZjo5PgG0) where they can watched on YT itself.

Implement a fnction called 'parse' that expects a str of HTML as input, extracts any YouTube URL that's the value
of a src attribute of an iframe element therin, and returns its shorter, shareable youtu.be equivalent as a str.
    * Expect that any such URL will be in one for the formats below.
                http://youtube.com/embed/xvFZjo5PgG0
                https://youtube.com/embed/xvFZjo5PgG0
                https://www.youtube.com/embed/xvFZjo5PgG0
        * Assume that the value of src will be surrounded by double quotes.
        * Assume that the input will contain no more than one such URL.
            * If the input does not contain any such URL at all, return 'None'
"""
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"<iframe * src=\"https?://(?:www\.)?youtube\.com/embed/(?P<link>\w+)\""
    iframe = re.search(pattern, s)
    if iframe:
        link = iframe.group("link")
        short_link = reformat(link)
        return short_link
    else:
        return None


def reformat(link):
    return f"https://youtu.be/{link}"

if __name__ == "__main__":
    main()
