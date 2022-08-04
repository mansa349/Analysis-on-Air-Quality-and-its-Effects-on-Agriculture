from django.shortcuts import render
from django.http import HttpResponse
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def croplist(request):
    '''
    state_list = ['Chhattisgarh', 'Gujarat', 'Haryana', 'Madhya Pradesh', 'Punjab', 
       'Uttarakhand', 'Uttar Pradesh', 'West Bengal', 'Andhra Pradesh', 'Assam', 
       'Bihar', 'Chandigarh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala',
       'Maharashtra', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry',
       'Rajasthan', 'Sikkim', 'Tamil Nadu']

    croplist = ["Arecanut", "Arhar/Tur", "Bajra", "Banana", "Barley", "Black pepper",
      "Cardamom", "Cashewnut", "Castor seed", "Coconut", "Coriander", "Cotton(lint)",
      "Cowpea(Lobia)", "Dry chillies", "Dry Ginger", "Garlic", "Ginger", "Gram",
      "Groundnut", "Guar seed", "Horse-gram", "Jowar", "Jute", "Khesari", "Linseed",
      "Maize", "Masoor", "mesta", "Moong(Green Gram)", "Moth", "Niger seed",
      "Oilseeds total", "Onion", "Other  Rabi pulses", "Other Cereals", "Other Kharif pulses",
      "other oilseeds", "Other Summer Pulses", "Peas & beans (Pulses)", "Potato", "Ragi",
      "Rapeseed & Mustard", "Rice", "Safflower", "Sannhamp", "Sesamum", "Small millets",
      "Soyabean", "Sugarcane", "Sunflower", "Sweet potato", "Tapioca", "Tobacco",
      "Turmeric", "Urad", "Wheat"
      ]'''


    #croplist =  enumerate(croplist)
    graphs_path = os.path.join(BASE_DIR, "media") + "/"
    
    image_names = []
    crops = []
    states = []

    '''
    for crop in croplist:
        for state in state_list:
            name = "dashboard_graph_"+ crop + "_" + state + ".png"
            #print(graphs_path + name)
            if os.path.exists(graphs_path + name):
                image_names.append("/media/" + name)
                crops.append(crop)
                states.append(state)'''
    
    #print(image_names,crops, states)
    image_name =  "/media/gases1.jpeg"

    #everything = zip(image_names, crops, states)
    return render(request, 'dashboard.html', {  "image_name":image_name})