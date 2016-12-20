from django.shortcuts import render,render_to_response
from .models import *
import urllib
import requests
import json
import urllib2
from django.views.decorators.csrf import csrf_exempt
from login.models import UserData,UserGroup
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.shortcuts import render,get_object_or_404

@csrf_exempt
def Requestes(request):  
  send_json=[]
  print "get method"
  if request.method=='POST':
    try:
      print request.POST["textmsg"]
      group_name=request.POST["Groupid"]
      textmsg=request.POST["textmsg"]
      group_name=group_name[1:len(group_name)-1]
      group_list=group_name.split(',')
      for group_names in group_list :
        print group_names.replace(" ","")
        group_names=group_names.replace(" ","")
        group_id=UserGroup.objects.get(group_name=str(group_names)).group_id
        print group_id
        #selectUserGroup= get_object_or_404(selectUserGroup, groupid=group_id)
        user_datas=UserData.objects.filter(group_id=group_id)
        for mobile_number in user_datas :
          print mobile_number.mobile_number
          #mon=UserData.objects.get(userid=mobile_number).mobilenumber
          authkey = "125195AvX4LUlVf57dcd941"
          sender = "mNavmo"
          route = "4"
          try:
            url = "http://api.msg91.com/api/sendhttp.php?authkey="+str(authkey)+"&mobiles="+str(mobile_number.mobile_number)+"&message="+str(textmsg)+"&sender=Meghal&route=4"
            print requests.request('GET',url)
          except Exception,e:
            print send_json.append(str("Failed To Send Msg"))
        
        send_json.append(str(group_names))
        print send_json
        send_json1={"Groups":send_json}
        print send_json1
      print str(send_json1)
      return HttpResponse(str({"Groups":send_json}))
    except Exception,e:
      print e
      return HttpResponse(str({"Groups":send_json}))
  else:
    send_json=[]
    send_json.append('Meghal')
    return HttpResponse(str({"Groups":send_json}))  

def user_group(request):
   if request.method=='GET':
    selectUserGroup=UserGroup.objects.all()
    User_ids=[]
    
    
    #usergroup=UserGroup.objects.values_list('userid','userid').order_by('userid').distinct()
    for user in selectUserGroup :
      User_ids.append(str(user.group_name))
      #JsonArray={"Groups":User_ids.append(user.groupid)}
      #json.dumps(User_ids)
      #print JsonArray
      #print   json.dumps(User_ids)


    JsonArray={"Groups":User_ids}
    print JsonArray
    json.dumps(JsonArray)


      
      


   return HttpResponse(str(JsonArray))
  

