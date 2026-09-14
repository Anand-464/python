blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
views = 0
trending = 0

for x in blog_views:
    if x>1000:
        print("Trending")
        trending +=1
    elif x>500 and x<1000:
        print("Average")
    else:
        print("Low traffic")
    views +=x
print("total views = ",views)
print("trending = ", trending)