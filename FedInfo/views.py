from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from . models import Federation,District
from datetime import date, datetime
from django.contrib import messages
def home(request):
    user = request.user
    federation = ''
    numDone = 0
    if user.is_authenticated:
        try:
            federation = get_object_or_404(Federation, user = user)
            numDone = getNumDone(federation)+1
        except:
            pass
    return render(request,'FedInfo/home.html',{"federation":federation,"numDone":numDone})


@login_required
def addFederation(request):
    
    user = request.user
    
    if request.method =='GET':
        
        return render(request, 'FedInfo/addFederation.html')
    
    
    if request.method == 'POST':
        
        fed = Federation.objects.create(
            user = user,
            FederationName = request.POST["FederationName"],
            PresidentName = request.POST["PresidentName"],
            PresidentLastName = request.POST["PresidentLastName"],
            PresidentEmail = request.POST["PresidentEmail"],
            PresidentPhone = request.POST["PresidentPhone"],
            ContactPersonName = request.POST["ContactPersonName"],
            ContactPersonLastName = request.POST["ContactPersonLastName"],
            ContactPersonPosition = request.POST["ContactPersonPosition"],
            yearUpdate = request.POST["yearUpdate"],
            Email = request.POST["ContactPersonEmail"],
            Phone = request.POST["ContactPersonPhone"],
            AddedDate = datetime.now(), 
        )
        messages.success(request,f"The {fed.FederationName} federation information saved successfull\n please correct mistakes and continue to the survey")
         #request.session['process'] = None
        request.session['createProcess'] = True
        
        return redirect("updateFederation")
    
        
        
@login_required
def updateFederation(request):
    #if request.session["process"] =="Parent":
    user = request.user
    federation = get_object_or_404(Federation, user = user)
    
    if request.method == 'GET':
        createProcess = False
        try:
            if request.session["createProcess"] ==True:
                createProcess = True
        except:
            pass
                
        return render(request, 'FedInfo/updateFedertion.html', {"federation":federation,"createProcess": createProcess})

    
    if request.method == 'POST':
        numUpdates = 0
        
        if federation.FederationName != request.POST["FederationName"]:
            federation.FederationName = request.POST["FederationName"]
            numUpdates += 1
            
        if federation.PresidentName != request.POST["PresidentName"]:
            federation.PresidentName = request.POST["PresidentName"]
            numUpdates += 1
            
        if federation.PresidentLastName != request.POST["PresidentLastName"]:
            federation.PresidentLastName = request.POST["PresidentLastName"]
            numUpdates += 1
        if federation.PresidentEmail != request.POST["PresidentEmail"]:
            federation.PresidentEmail = request.POST["PresidentEmail"]
            numUpdates += 1
            
        if federation.PresidentPhone != request.POST["PresidentPhone"]:
            federation.PresidentPhone = request.POST["PresidentPhone"]
            numUpdates += 1 
        if federation.ContactPersonName != request.POST["ContactPersonName"]:
            federation.ContactPersonName = request.POST["ContactPersonName"]
            numUpdates += 1
            
        if federation.ContactPersonLastName != request.POST["ContactPersonLastName"]:
            federation.ContactPersonLastName = request.POST["ContactPersonLastName"]
            numUpdates += 1
            
        if federation.Email != request.POST["ContactPersonEmail"]:
            federation.Email = request.POST["ContactPersonEmail"]
            numUpdates += 1
            
        if federation.Phone != request.POST["ContactPersonPhone"]:
            federation.Phone = request.POST["ContactPersonPhone"]
            numUpdates += 1
            
        if federation.ContactPersonPosition != request.POST["ContactPersonPosition"]:
            federation.ContactPersonPosition = request.POST["ContactPersonPosition"]
            numUpdates += 1
            
        
        if federation.yearUpdate != request.POST["yearUpdate"]:
            federation.yearUpdate = request.POST["yearUpdate"]
            numUpdates += 1
         
        if numUpdates > 0:
            federation.save()
            msg = str(numUpdates)+" fields updated successfully"
            messages.success(request, msg)
        else:
            msg = "No changes made"
            messages.success(request, msg)
            
        return redirect("updateFederation")
    
    
@login_required
def AnsDistricts(request, numDone):
    user = request.user
    federation = get_object_or_404(Federation, user = user)
    AllDistricts = District.objects.all()
    DistrictAns = getAnsDistrict(numDone)
    
    districts = []
    for district in AllDistricts:
        if district.Federation == federation:
            districts.append(district)
    if request.method == 'GET':
       
        return render(request, 'FedInfo/AnsDistricts.html', {"federation":federation,"districts":districts,"DistrictAns":DistrictAns})
    
    if request.method == 'POST':
       
        district = District.objects.create(
            Federation = federation,
            DistrictName = request.POST["DistrictName"],
            NumberOfClubs = request.POST["NumberOfClubs"],
            Participation = request.POST["Participation"],#
            ContactPersonName = request.POST["ContactPersonName"],
            ContactPersonLastName = request.POST["ContactPersonLastName"],
            Phone = request.POST["Phone"],
            Email = request.POST["Email"],
            FormalStructure = request.POST["FormalStructure"],
            NoStructureReason = request.POST["NoStructureReason"],
            DistrictOrProvince = request.POST["DistrictOrProvince"],
            
            AddDate = datetime.now(),
        )
        
        if numDone == 0:
            numDone = 2
        else:
            numDone +=1
        if (getNumDone(federation) +1) > 11:
            try:
                if request.session['createProcess'] == True:
                    
                    messages.success(request, "Well done! the survey is completed successfully.\nBelow are the responses you made.")
                    request.session['createProcess'] = None
            except:
                messages.success(request, "Well done! the survey is completed successfully.\nBelow are the responses you made.")

            return redirect("FederationDetails", federationId =0 )
                    
            
        messages.success(request,f"Response saved successfully, please continue answering for the {getAnsDistrict(numDone)} district.")
        return redirect("AnsDistricts", numDone= numDone)
            
        
        
        
def getAnsDistrict(numDone):
    
    DistrictList = [
        {
            "id": 1,
            "name":"Harry Gwala"
        },
        {
            "id": 2,
            "name":"Ethekwini"
        },
        {
            "id": 3,
            "name":"Amajuba"
        },
        {
            "id": 4,
            "name":"Ilembe"
        },
        {
            "id": 5,
            "name":"Uthukela"
        },
        {
            "id": 6,
            "name":"Umgungundlovu"
        },
        {
            "id": 7,
            "name":"Ugu"
        },
        {
            "id": 8,
            "name":"Umzinyathi"
        },
        {
            "id": 9,
            "name":"Zululand"
        },
        {
            "id": 10,
            "name":"Uthungulu"
        },
        {
            "id": 11,
            "name":"Umkhanyakude"
        },
        
    ]
    district = ""
    if numDone == 0:
    
        numDone += 1

    for item in DistrictList:
        if item["id"] == numDone:
            district = item["name"]
    print(f"Num done: {numDone}")   
    return district
    
    
@login_required
def updateDistrict(request, districtId):
    oncreate = False
    
    try:
        if request.session['createProcess'] == True:
            oncreate = True
    except:
        pass
    district = get_object_or_404(District, pk = districtId)
    federation = district.Federation
    numDone = getNumDone(federation)+1
    if request.method == 'GET':
        
        
        return render(request, 'FedInfo/updateDistrict.html', {"district":district,"federation":federation, "oncreate":oncreate,"numDone":numDone})
    if request.method =='POST':
        numUpdates = 0
        if district.Participation != request.POST["Participation"]:
            district.Participation = request.POST["Participation"]
            numUpdates += 1
        if district.FormalStructure != request.POST["FormalStructure"]:
            district.FormalStructure = request.POST["FormalStructure"]
            numUpdates += 1
            
        if district.ContactPersonName != request.POST["ContactPersonName"]:
            district.ContactPersonName = request.POST["ContactPersonName"]
            numUpdates += 1
            
        if district.ContactPersonLastName != request.POST["ContactPersonLastName"]:
            district.ContactPersonLastName = request.POST["ContactPersonLastName"]
            numUpdates += 1
            
        if district.Phone != request.POST["Phone"]:
            district.Phone = request.POST["Phone"]
            numUpdates += 1
            
        if district.Email != request.POST["Email"]:
            district.Email = request.POST["Email"]
            numUpdates += 1
            
        if district.DistrictOrProvince != request.POST["DistrictOrProvince"]:
            district.DistrictOrProvince = request.POST["DistrictOrProvince"]
            numUpdates += 1
            
        if district.NoStructureReason != request.POST["NoStructureReason"]:
            district.NoStructureReason = request.POST["NoStructureReason"]
            numUpdates += 1
            
        if district.NumberOfClubs != int(request.POST["NumberOfClubs"]):
           
            district.NumberOfClubs = request.POST["NumberOfClubs"]
            numUpdates += 1
            
        if numUpdates > 0:
            district.save()
            messages.success(request, f"{numUpdates} fields updated")
        else:
            messages.success(request, "No changes made.")
            
        return redirect('updateDistrict', districtId = district.DistrictId)
def count(list):
    total = 0
    for item in list:
        total += 1
    return total

def getNumDone(federation):
    numDone = 0
    
    Districts = District.objects.filter(Federation = federation)
    
    for item in Districts:
        numDone += 1
    return numDone

@login_required
def FederationDetails(request, federationId):
    user = request.user
    try:
        federation = get_object_or_404(Federation, user = user)
    except:
        federation = get_object_or_404(Federation, pk = federationId)
        
    districts = District.objects.filter(Federation = federation)
    
    if request.method == 'GET':
        
        return render(request, 'FedInfo/FederationDetails.html',{"federation":federation,"districts":districts})

@login_required
def ViewFederations(request):
    user = request.user
    if user.is_superuser == False:
        return HttpResponse("This page is only accessable to super users only,awubuyel emuva please.yin ukuhlupha?")
     
    federations = Federation.objects.all()
    
    if request.method == 'GET':
        
        return render(request, 'FedInfo/ViewFederations.html', {"federations":federations})