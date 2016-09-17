from __future__ import print_function
import json
import urllib2
import os
import sys

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Please input your API Key and Bus Line in order.")
    sys.exit()

#apikey = "4ddc7632-195f-4df2-b8c7-5b4f8b0447a5"
apikey = sys.argv[1]
bus_line = sys.argv[2]
"""
url_mta = 
"http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" 
+ apikey 
+ "&VehicleMonitoringDetailLevel=calls&LineRef="
+ bus
"""
url_mta = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, bus_line)

response = urllib2.urlopen(url_mta)
data = response.read().decode("utf-8")
data = json.loads(data)

bus = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity']
bus_num = len(bus)

#the 1st print line
print ("Bus Line : ", bus_line)
#the 2nd print line
print ("Number of Active Buses : ", bus_num)
#the other print lines
for i in xrange(bus_num):
	bus_info = "Bus " + str(i) + " is at latitude {} and longitude {}".format(
		bus[i][u'MonitoredVehicleJourney'][u'VehicleLocation'][u'Latitude'], 
		bus[i][u'MonitoredVehicleJourney'][u'VehicleLocation'][u'Longitude'])
	print (bus_info)


