from pprint import pprint
from boto import ec2
import sys
from collections import Counter
import json
import urllib2
import pprint
import logging

ondemand_count = Counter()
total_instances = Counter()
ondemand_count = Counter()

aws_pricing = "https://a0.awsstatic.com/pricing/1/deprecated/ec2/pricing-on-demand-instances.json"


class inventory_cost:
    def __init__(self,region,aws_access,aws_secret):
        self.region=region
        self.aws_access=aws_access
        self.aws_secret=aws_secret
        
    def list_all(self):      
        con = ec2.connect_to_region(self.region, aws_access_key_id=self.aws_access, aws_secret_access_key=self.aws_secret)
        reservations = con.get_all_instances()
        instances = [i for r in reservations for i in r.instances]
        for i in instances:
            
            total_instances[i.__dict__['instance_type']] +=1            

        ondemand_inst=total_instances

        if self.region == 'us-east-1':
            region = "us-east"
        if self.region == 'us-west-2':
            region = "us-west-2"            
        if self.region == 'us-west-1':
            region = "us-west"           
        if self.region == 'ap-southeast-1':            
            region = "apac-sin"
        if self.region == 'ap-southeast-2' :
            region = "apac-sin"
        if self.region == 'eu-west-1':
            region = "eu-ireland"
        if self.region == 'ap-northeast-1':
            region = "apac-tokyo"
        if self.region == 'ap-southeast-2':
            region = "apac-syd"
        if self.region == 'sa-east-1':
            region == "sa-east-1"
 
        data = json.loads(urllib2.urlopen(aws_pricing).read())       


        for i in data["config"]["regions"]:
            
            if i["region"] == region:
            
                for j in i["instanceTypes"]:
                    
                    for k in j["sizes"]:
   
                        
                        l = [ o for o in [n['USD']  for n in  [ m['prices']  for m in k['valueColumns']]]]
                       
                        ondemand_count[k['size']] += float("".join(l))

        print "***********************************************************"
        print "           $ Monthly Calculator in USD $   "
        print "***********************************************************"
                        
        print "Instance_type Count total_per_hour_cost total_cost_per_month"
        print "______________ _____ ___________________ _______________________"
        for i in ondemand_inst:
            print i,"    ",ondemand_inst[i],"    ","$"+str(float(ondemand_inst[i])*ondemand_count[i]),"        ","$"+str(float(ondemand_inst[i])*ondemand_count[i]*24*30)


if __name__ == '__main__':    
    if len(sys.argv) > 1:
        fileName= (sys.argv[1]) 
        inventory_cost(sys.argv[1],sys.argv[2],sys.argv[3]).list_all()
        
       
    else :
        print "please pass three values in command line <region> <aws access keys> <aws secret keys>"
