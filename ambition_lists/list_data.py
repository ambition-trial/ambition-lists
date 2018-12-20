from ambition_form_validators import HEADACHE, VISUAL_LOSS
from edc_constants.constants import OTHER, NORMAL, NONE, NOT_APPLICABLE
from edc_list_data import PreloadData

list_data = {
    'ambition_lists.antibiotic': [
        ('amoxicillin_ampicillin', 'Amoxicillin/Ampicillin'),
        ('ceftriaxone', 'Ceftriaxone'),
        ('ciprofloxacin', 'Ciprofloxacin'),
        ('doxycycline', 'Doxycycline'),
        ('erythromycin', 'Erythromycin'),
        ('flucloxacillin', 'Flucloxacillin'),
        ('gentamicin', 'Gentamicin'),
        (OTHER, 'Other, specify')
    ],
    'ambition_lists.neurological': [
        ('focal_neurologic_deficit', 'Focal neurologic deficit'),
        ('meningism', 'Meningism'),
        ('papilloedema', ' Papilloedema'),
        ('CN_III_palsy', 'Cranial Nerve III palsy'),
        ('CN_IV_palsy', 'Cranial Nerve IV palsy'),
        ('CN_VIII_palsy', 'Cranial Nerve VIII palsy'),
        ('CN_VII_palsy', 'Cranial Nerve VII palsy'),
        ('CN_VI_palsy', 'Cranial Nerve VI palsy'),
        (OTHER, 'Other CN palsy'),
    ],
    'ambition_lists.day14medication': [
        ('co_trimoxazole', 'Co-trimoxazole'),
        ('fluconazole', 'Fluconazole'),
        ('rifampicin', ' Rifampicin'),
        (OTHER, 'Other'),
        (NONE, 'None, no other medications given'),
        (NOT_APPLICABLE, 'Not applicable'),
    ],
    'ambition_lists.medication': [
        ('TMP-SMX', 'TMP-SMX'),
        (OTHER, 'Other, specify;')
    ],
    'ambition_lists.otherdrug': [
        ('anti_convulsants', 'Anticonvulsants'),
        ('antibiotics', 'Antibiotics'),
        ('magnesium', 'Magnesium'),
        ('potassium', ' Potassium'),
        ('tmp_smx_Cotrimoxazole', ' TMP-SMX/Cotrimoxazole'),
        ('vitamins', ' Vitamins'),
        (OTHER, 'Other, specify'),
        (NONE, 'None, no other drugs/interventions given'),
        (NOT_APPLICABLE, 'Not applicable'),
    ],
    'ambition_lists.significantnewdiagnosis': [
        ('bacteraemia', 'Bacteraemia'),
        ('bacterial_pneumonia', 'Bacterial pneumonia'),
        ('diarrhoeal_wasting', 'Diarrhoeal wasting'),
        ('kaposi_sarcoma', 'Kaposi’s sarcoma'),
        ('malaria', 'Malaria'),
        ('tb_extra_pulmonary', 'TB extra-pulmonary'),
        ('tb_pulmonary', 'TB pulmonary'),
        (OTHER, 'Other, please specify:'),
    ],
    'ambition_lists.symptom': [
        ('double_vision', 'Double vision'),
        ('behaviour_change', 'Behaviour change'),
        ('confusion', 'Confusion'),
        ('cough', 'Cough'),
        ('drowsiness', 'Drowsiness'),
        ('fever', 'Fever'),
        ('focal_weakness', 'Focal weakness'),
        (HEADACHE, 'Headache'),
        ('hearing_loss', 'Hearing loss'),
        ('nausea', 'Nausea'),
        ('seizures_gt_72', 'Seizures (72 hrs - 1 mo)'),
        ('seizures_lt_72 hrs', 'Seizures (<72 hrs)'),
        ('shortness_of_breath', 'Shortness of breath'),
        ('skin_lesions', 'Skin lesions'),
        (VISUAL_LOSS, 'Visual loss'),
        ('vomiting', 'Vomiting'),
        ('weight_loss', 'Weight loss'),
    ],
    'ambition_lists.abnormalresultsreason': [
        ('cerebral_oedema', 'Cerebral oedema'),
        ('cryptococcomas', 'Cryptococcomas'),
        ('dilated_virchow_robin_spaces', 'Dilated Virchow-Robin spaces'),
        ('enhancing_mass_lesions',
         'Enhancing mass lesions DD toxoplasmosis, TB, lymphoma'),
        ('hydrocephalus', 'Hydrocephalus'),
        ('infarcts', 'Infarcts'),
        (OTHER, 'Other'),
    ],
    'ambition_lists.cxrtype': [
        ('hilar_adenopathy', 'Hilar adenopathy'),
        ('infiltrates', 'Infiltrates'),
        ('miliary_appearance', 'Miliary appearance'),
        (NORMAL, 'Normal'),
        ('pleural_effusion', 'Pleural effusion'),
    ],
    'ambition_lists.infiltratelocation': [
        ('diffuse', 'Diffuse'),
        ('lll', 'LLL'),
        ('lul', 'LUL'),
        ('rll', 'RLL'),
        ('rml', 'RML'),
        ('rul', 'RUL'),
    ],
    'ambition_lists.misseddoses': [
        ('dose_1', 'Dose 1'),
        ('dose_2', 'Dose 2'),
        ('dose_3', 'Dose 3'),
        ('dose_4', 'Dose 4')
    ],
}


preload_data = PreloadData(list_data=list_data)
