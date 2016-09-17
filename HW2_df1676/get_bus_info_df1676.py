from __future__ import print_function
import json
import urllib2
import os
import sys

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Please input your API Key, Bus Line and CSV File in order.")
    sys.exit()

apikey = sys.argv[1]
bus_line = sys.argv[2]
#file_name = sys.argv[3]
fout = open(sys.argv[3], "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

url_mta = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, bus_line)

response = urllib2.urlopen(url_mta)
data = response.read().decode("utf-8")
data = json.loads(data)

bus = data[u'Siri'][u'ServiceDelivery'][u'VehicleMonitoringDelivery'][0][u'VehicleActivity']
bus_num = len(bus)

for i in xrange(bus_num):
	'''
	bus_info = "Bus " + str(i) + " is at latitude {} and longitude {}".format(
		bus[i][u'MonitoredVehicleJourney'][u'VehicleLocation'][u'Latitude'], 
		bus[i][u'MonitoredVehicleJourney'][u'VehicleLocation'][u'Longitude'])
	'''
	bus_lat = bus[i][u'MonitoredVehicleJourney'][u'VehicleLocation'][u'Latitude']
	bus_long = bus[i][u'MonitoredVehicleJourney'][u'VehicleLocation'][u'Longitude']
	if bus[i][u'MonitoredVehicleJourney'][u'OnwardCalls']:
		bus_stop_name = bus[i][u'MonitoredVehicleJourney'][u'OnwardCalls'][u'OnwardCall'][0][u'StopPointName']
		bus_stop_status = bus[i][u'MonitoredVehicleJourney'][u'OnwardCalls'][u'OnwardCall'][0][u'Extensions'][u'Distances'][u'PresentableDistance']
	else:
		bus_stop_name = 'N/A'
		bus_stop_status = 'N/A'
	
	stop_info_print = "{}, {}, {}, {}".format(bus_lat, bus_long, bus_stop_name, bus_stop_status) 
	print (stop_info_print)

	stop_info = "{},{},{},{}".format(bus_lat, bus_long, bus_stop_name, bus_stop_status)
	fout.write(stop_info)
	fout.write("\n")




