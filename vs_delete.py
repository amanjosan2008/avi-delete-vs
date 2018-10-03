import argparse
from avi.sdk.avi_api import ApiSession
from requests import urllib3

urllib3.disable_warnings()

#Get Api Session
api = ApiSession.get_session('10.10.30.63','admin','Admin@123',tenant='admin', api_version="17.2.10")

c = 0
try:
    for i in range(1,254):
         for j in range(1,254):
            c += 1
            print str(c) + ': ',

            # VS Delete
            vs_name = 'my_vs-%d.%d' %(i,j)
            addr2 = '10.91.%d.%d' %(i,j)

            resp2 = api.get_object_by_name('virtualservice', vs_name)
            if resp2 == None:
                print vs_name + ' Already Deleted '
            else:
                resp3 = api.delete_by_name('virtualservice', vs_name)
                print vs_name + ' VS Deleted: ' + str(resp3.status_code)

            # Pool Delete
            pool = 'pool-%d.%d' %(i,j)
            addr = '10.92.%d.%d' %(i,j)

            resp = api.get_object_by_name('pool', pool)
            if resp == None:
                print pool + ' Already Deleted '
            else:
                resp4 = api.delete_by_name('pool', pool)
                print pool + ' Pool Deleted: ' + str(resp4.status_code)

except KeyboardInterrupt:
    print '\nScript killed by user'
