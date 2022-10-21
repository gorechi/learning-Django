from models import District, Location, Place, PlaceRate

d = District()
d.name = 'Дзержинский район'
d.description = 'Северный жилой район, также известный как Брагино.'

d.save()