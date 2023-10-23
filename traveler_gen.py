import json
import os

def ded_traveler_generator(path, key, candidateAlloys, batch, date):
    with open(os.path.join("TravellerGen/templates", key), 'r') as template_file:
        template = json.load(template_file)
        
    template["cartaMetadata"]["updated"] = date
    
    for i, alloy in enumerate(candidateAlloys):
        template["data"]["Material Composition"][i]["Al"] = alloy.compData[5]
        template["data"]["Material Composition"][i]["Co"] = alloy.compData[2]
        template["data"]["Material Composition"][i]["Cr"] = alloy.compData[3]
        template["data"]["Material Composition"][i]["Fe"] = alloy.compData[0]
        template["data"]["Material Composition"][i]["Ni"] = alloy.compData[1]
        template["data"]["Material Composition"][i]["Sample ID"] = alloy.uniqueId
        template["data"]["Material Composition"][i]["Sum"] = str(round(sum(alloy.compData),5))
        template["data"]["Material Composition"][i]["V"] = alloy.compData[4]

        template["data"]["Sample ID"][i]["Unique Code"] = alloy.uniqueId
        template["data"]["Sample ID"][i]["Prod. Batch"] = batch
        template["data"]["Sample ID"][i]["Production Location & Physical Sample Number"] = 'C' + alloy.uniqueId[-2:]
        template["data"]["Sample ID"][i]["VAM or DED"] = "DED"
        template["data"]["Sample ID"][i]["Year and Month"] = date
            
    with open(path, 'w') as output_file:
        json.dump(template, output_file, indent=4)

    
def lipit_details_generator(path, key, candidateAlloy, date):
    with open(os.path.join("TravellerGen/templates", key), 'r') as template_file:
        template = json.load(template_file)
    template["cartaMetadata"]["updated"] = date
    
    template["data"]["Sample ID"] = candidateAlloy.uniqueId

            
    with open(path, 'w') as output_file:
        json.dump(template, output_file, indent=4)
        
def ni_hsr_details_generator(path, key, candidateAlloy, date):
    with open(os.path.join("TravellerGen/templates", key), 'r') as template_file:
        template = json.load(template_file)
    template["cartaMetadata"]["updated"] = date
    template["data"]["Sample ID"] = candidateAlloy.uniqueId
            
    with open(path, 'w') as output_file:
        json.dump(template, output_file, indent=4)

def ni_imicro_details_generator(path, key, candidateAlloy, date):
    with open(os.path.join("TravellerGen/templates", key), 'r') as template_file:
        template = json.load(template_file)
    template["cartaMetadata"]["updated"] = date
    template["data"]["Sample ID"] = candidateAlloy.uniqueId

            
    with open(path, 'w') as output_file:
        json.dump(template, output_file, indent=4)
    
def tensile_details_generator(path, key, candidateAlloy, date):
    with open(os.path.join("TravellerGen/templates", key), 'r') as template_file:
        template = json.load(template_file)
    template["cartaMetadata"]["updated"] = date
    template["data"]["Sample ID"] = candidateAlloy.uniqueId

            
    with open(path, 'w') as output_file:
        json.dump(template, output_file, indent=4)
    
def vam_processing_details_generator(path, key, candidateAlloy, batch, date):
    with open(os.path.join("TravellerGen/templates", key), 'r') as template_file:
        template = json.load(template_file)
    template["cartaMetadata"]["updated"] = date
    template["data"]["Sample ID"]["Prod. Batch"] = batch
    template["data"]["Sample ID"]["Production Location & Physical Sample Number"] = 'T' + candidateAlloy.uniqueId[-2:]
    template["data"]["Sample ID"]["Unique Code"] = candidateAlloy.uniqueId
    template["data"]["Sample ID"]["VAM or DED"] = "VAM"
    template["data"]["Sample ID"]["Year & Month"] = date
    
    with open(path, 'w') as output_file:
        json.dump(template, output_file, indent=4)

def vam_synthesis_details_generator(path, key, candidateAlloy, batch, date):
    with open(os.path.join("TravellerGen/templates", key), 'r') as template_file:
        template = json.load(template_file)
    template["cartaMetadata"]["updated"] = date
    template["data"]["Sample ID"]["Prod. Batch"] = batch
    template["data"]["Sample ID"]["Production Location & Physical Sample Number"] = 'T' + candidateAlloy.uniqueId[-2:]
    template["data"]["Sample ID"]["Unique Code"] = candidateAlloy.uniqueId
    template["data"]["Sample ID"]["VAM or DED"] = "VAM"
    template["data"]["Sample ID"]["Year & Month"] = date

            
    with open(path, 'w') as output_file:
        json.dump(template, output_file, indent=4)
    
def vam_traveler_generator(path, key, candidateAlloy, batch, date):
    with open(os.path.join("TravellerGen/templates", key), 'r') as template_file:
        template = json.load(template_file)
    template["cartaMetadata"]["updated"] = date
    template["data"]["Sample ID"]["Prod. Batch"] = batch
    template["data"]["Sample ID"]["Production Location & Physical Sample Number"] = 'T' + candidateAlloy.uniqueId[-2:]
    template["data"]["Sample ID"]["Unique Code"] = candidateAlloy.uniqueId
    template["data"]["Sample ID"]["VAM or DED"] = "VAM"
    template["data"]["Sample ID"]["Year & Month"] = date
    template["data"]["Material Composition"]["Al"] = candidateAlloy.compData[5]
    template["data"]["Material Composition"]["Co"] = candidateAlloy.compData[2]
    template["data"]["Material Composition"]["Cr"] = candidateAlloy.compData[3]
    template["data"]["Material Composition"]["Fe"] = candidateAlloy.compData[0]
    template["data"]["Material Composition"]["Ni"] = candidateAlloy.compData[1]
    template["data"]["Material Composition"]["Sample ID"] = candidateAlloy.uniqueId
    template["data"]["Material Composition"]["Sum"] = str(round(sum(candidateAlloy.compData),5))
    template["data"]["Material Composition"]["V"] = candidateAlloy.compData[4]

            
    with open(path, 'w') as output_file:
        json.dump(template, output_file, indent=4)
    
def xrd_details_generator(path, key, candidateAlloy, date):
    with open(os.path.join("TravellerGen/templates", key), 'r') as template_file:
        template = json.load(template_file)
    template["cartaMetadata"]["updated"] = date
    template["data"]["Sample ID"] = candidateAlloy.uniqueId

            
    with open(path, 'w') as output_file:
        json.dump(template, output_file, indent=4)
    
