import itunes

# Lookup Achtung Baby album by U2
# U2_ACHTUNGBABY_ID = 462638897
# album = itunes.lookup(U2_ACHTUNGBABY_ID)

# print album.get_url()


# print itunes.lookup(462638897);
items = itunes.rss_search(6013);

for item in items:
	print 'name: ' + item.get_name()
	print 'current version: ' + str(item.version)
	print 'price: ' + str(item.price)
	print 'avg rating: ' + str(item.avg_rating)
	print 'num ratings: ' + str(item.num_ratings)
	print 'release date: ' + str(item.release_date)
	print ''