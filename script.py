from world.models import Waypoint
Waypoint(name='New York', geometry='POINT(-73.9869510 40.7560540)').save()
Waypoint(name='Buenos Aires', geometry='POINT(-58.4173090 -34.6117810)').save()
Waypoint(name='Moscow', geometry='POINT(37.6176330 55.7557860)').save()
Waypoint(name='Atlanta', geometry='POINT(-84.3896630 33.7544870)').save()
print(Waypoint.objects.all())
