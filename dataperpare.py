import newspaper as nw
text =[]
papers=[]
popular_urls = nw.popular_urls()
for url in popular_urls:
    print 'building: ' , url
    paper = nw.build(language='en',url=url, memoize_articles=False, )
    papers.append(paper)
    print 'done..'
#nw.news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
#nw.news_pool.join()
with open('dataset.txt', 'w+') as f:
    for paper in papers:
        print len(paper.articles)
        for article in paper.articles:
            article.download()
            article.parse()
            text.append(article.title)
            try:
                if article.title!='Something\'s Gone Terribly Wrong':
                    f.write((article.title.decode('utf-8').encode('cp1250'))+'\n')
            except:
                pass


