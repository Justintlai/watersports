import lxml.etree
import newspaper


def main():
    cnn_paper = newspaper.build('https://news.google.com')
    for article in cnn_paper.articles:
        print(article.url)


if __name__ == "__main__":
    main()
