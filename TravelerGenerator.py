import os
from openpyxl import load_workbook as ld
from openpyxl.drawing.image import Image
from traveler_gen import *

class candidateAlloy:
    compData = []
    uniqueId = ""
    solid_range = ""
    prop_density = ""
    prop_THDC = ""
    predict_SFE = ""
    
    def __init__(self, data, uuid, sr, pd, pt, ps):
        self.compData = data
        self.uniqueId = uuid
        self.solid_range = sr
        self.prop_density = pd
        self.prop_THDC = pt
        self.predict_SFE = ps
        
        if abs(sum(self.compData) - 1) > 1e-5:
            raise ValueError(f"{self.uniqueId}'s constituents sum to {sum(self.compData)}. This number must be 100%!")

def getInput(inputPath):
    candidateList = []
    
    wb = ld(filename=inputPath)
    active = wb.active

    # Data Extraction from Input File

    for sheet in wb:
        active = sheet
        for row in active.iter_rows(min_row = 2):
            id = row[0].value
            Co = row[1].value
            Cr = row[2].value
            Fe = row[3].value
            Ni = row[4].value
            Va = row[5].value
            Al = row[6].value
            solid_range = row[7].value
            prop_density = row[8].value
            prop_THCD = row[9].value
            predict_SFE = row[10].value
            alloy_data = [Fe, Ni, Co, Cr, Va, Al]
            alloy = candidateAlloy(alloy_data, id, solid_range, prop_density, prop_THCD, predict_SFE)
            candidateList.append(alloy)
                
    wb.close()
    
    return candidateList

def create_folders(data, current_path, batch, prefix, candidateAlloys, date, current_alloy=0, ded_first_time = True):
    for key, value in data.items():
        alloy = current_alloy
        if key.startswith('@prefix'):
            try:
                alloy = int(key[len('@prefix'):]) - 1
            except ValueError:
                pass
                
        if key == "@prefix01-@prefix08":
            ded_first_time = True
        if key == "@prefix09-@prefix16":
            ded_first_time = False
        
        candidateAlloy = candidateAlloys[alloy]
        
        new_key = key.replace("@batch", batch).replace("@prefix", prefix)
        new_path = os.path.join(current_path, new_key)
        
        if value is None:
            
            if new_key == "ded-traveler-v1.json":
                if ded_first_time:
                    ded_traveler_generator(new_path, new_key, candidateAlloys[0:8], batch, date)
                else:
                    ded_traveler_generator(new_path, new_key, candidateAlloys[8:16], batch, date)
            elif new_key == "lipit-details-v1.json":
                lipit_details_generator(new_path, new_key, candidateAlloy, date)
                
            elif new_key == "ni-hsr-details-v1.json":
                ni_hsr_details_generator(new_path, new_key, candidateAlloy, date)
                
            elif new_key == "ni-imicro-details-v1.json":
                ni_imicro_details_generator(new_path, new_key, candidateAlloy, date)
                
            elif new_key == "tensile-details-v1.json":
                tensile_details_generator(new_path, new_key, candidateAlloy, date)
                
            elif new_key == "vam-processing-details-v1.json":
                vam_processing_details_generator(new_path, new_key, candidateAlloy, batch, date)
                
            elif new_key == "vam-synthesis-details-v1.json":
                vam_synthesis_details_generator(new_path, new_key, candidateAlloy, batch, date)
                
            elif new_key == "vam-traveler-v1.json":
                vam_traveler_generator(new_path, new_key, candidateAlloy, batch, date)
                
            elif new_key == "xrd-details-v1.json":
                xrd_details_generator(new_path, new_key, candidateAlloy, date)
                
        
        else:
            os.makedirs(new_path, exist_ok=True)
            create_folders(value, current_path=new_path, batch=batch, prefix=prefix, candidateAlloys=candidateAlloys, date=date, current_alloy=alloy, ded_first_time=ded_first_time)

def read_existing_folders(output_path, prefix, batch):
    if os.path.exists(os.path.join(output_path, prefix, "DED", batch)) or os.path.exists(os.path.join(output_path,prefix,"VAM",batch)):
        return False
    return True

