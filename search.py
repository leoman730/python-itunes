import itunes

# Lookup Achtung Baby album by U2
# U2_ACHTUNGBABY_ID = 462638897
# album = itunes.lookup(U2_ACHTUNGBABY_ID)

# print album.get_url()


# print itunes.lookup(462638897);
items = itunes.rss_lookup(6013);

for item in items:
	print 'name: ' + item.get_name()
	print 'price: ' + str(item.get_price())
	print 'avg rating: ' + str(item.get_avg_rating())
	print 'num ratings: ' + str(item.get_num_ratings())
	print ''