schemes = [

    # ================= TELANGANA STATE SCHEMES =================

    {
        "scheme_id": "TS-AASARA-PENSION",
        "scheme_name": "ఆసరా పింఛన్ పథకం",
        "scope": "state",
        "state": "Telangana",
        "eligibility": {
            "min_age": 57,
            "max_income": 150000
        },
        "benefits": "నెలకు రూ. 3000 పింఛన్",
        "required_documents": ["ఆధార్", "రేషన్ కార్డు", "బ్యాంక్ పాస్‌బుక్"],
        "apply_steps": ["గ్రామ సచివాలయం సందర్శించండి", "ఫారమ్ సమర్పించండి"]
    },

    {
        "scheme_id": "TS-RYTHU-BANDHU",
        "scheme_name": "రైతు బంధు పథకం",
        "scope": "state",
        "state": "Telangana",
        "eligibility": {
            "farmer": True,
            "land_owner": True
        },
        "benefits": "ప్రతి ఎకరాకు సంవత్సరానికి రూ. 10,000",
        "required_documents": ["పట్టాదారు పాస్బుక్", "ఆధార్"],
        "apply_steps": ["ఆటోమేటిక్‌గా బ్యాంక్ ఖాతాలో జమ"]
    },

    {
        "scheme_id": "TS-KALYANA-LAKSHMI",
        "scheme_name": "కళ్యాణ లక్ష్మి పథకం",
        "scope": "state",
        "state": "Telangana",
        "eligibility": {
            "gender": "female",
            "marital_status": "unmarried",
            "min_age": 18,
            "max_age": 35,
            "max_income": 200000
        },
        "benefits": "పెళ్లి ఖర్చులకు రూ. 1,00,116",
        "required_documents": ["ఆధార్", "ఆదాయ ధృవీకరణ"],
        "apply_steps": ["తెలంగాణ పోర్టల్ ద్వారా ఆన్‌లైన్ దరఖాస్తు"]
    },

    {
        "scheme_id": "TS-SHADI-MUBARAK",
        "scheme_name": "షాదీ ముబారక్ పథకం",
        "scope": "state",
        "state": "Telangana",
        "eligibility": {
            "gender": "female",
            "marital_status": "unmarried",
            "minority": True,
            "max_income": 200000
        },
        "benefits": "పెళ్లికి రూ. 1,00,116",
        "required_documents": ["ఆధార్", "మత ధృవీకరణ"],
        "apply_steps": ["ఆన్‌లైన్ దరఖాస్తు చేయాలి"]
    },

    {
        "scheme_id": "TS-EBC-SCHOLARSHIP",
        "scheme_name": "EBC స్కాలర్‌షిప్",
        "scope": "state",
        "state": "Telangana",
        "eligibility": {
            "student": True,
            "max_income": 100000
        },
        "benefits": "విద్యా ఖర్చులకు ఆర్థిక సహాయం",
        "required_documents": ["కాలేజ్ ఐడీ", "ఆధార్"],
        "apply_steps": ["ePASS పోర్టల్ ద్వారా"]
    },

    {
        "scheme_id": "TS-KCR-KIT",
        "scheme_name": "KCR కిట్ పథకం",
        "scope": "state",
        "state": "Telangana",
        "eligibility": {
            "pregnant_woman": True
        },
        "benefits": "మాతృ శిశు సంరక్షణ కిట్",
        "required_documents": ["ఆధార్", "గర్భిణీ నమోదు"],
        "apply_steps": ["ప్రభుత్వ ఆసుపత్రిలో నమోదు చేయాలి"]
    },

    {
    "scheme_id": "TS-DALIT-BANDHU",
    "scheme_name": "దళిత బంధు పథకం",
    "scope": "state",
    "state": "Telangana",
    "eligibility": {
        "caste": "SC",
        "min_age": 25,
        "student": False,
        "self_employed": True
    },
    "benefits": "ఉద్యోగ స్థాపనకు రూ. 10 లక్షలు",
    "required_documents": [
        "కుల ధృవీకరణ",
        "ఆధార్",
        "వ్యాపార ప్రణాళిక"
    ],
    "apply_steps": [
        "గ్రామ సచివాలయం ద్వారా ఎంపిక ప్రక్రియ",
        "లైవ్లీహుడ్ ప్రణాళిక సమర్పణ",
        "అర్హులైన వారికి ఆర్థిక సహాయం"
    ]
},

    # ================= CENTRAL GOVERNMENT SCHEMES =================

    {
        "scheme_id": "PM-KISAN",
        "scheme_name": "ప్రధాన్ మంత్రి కిసాన్ సమ్మాన్ నిధి",
        "scope": "central",
        "eligibility": {
            "farmer": True
        },
        "benefits": "సంవత్సరానికి రూ. 6000",
        "required_documents": ["ఆధార్", "భూమి పత్రాలు"],
        "apply_steps": ["pmkisan.gov.in ద్వారా"]
    },

    {
        "scheme_id": "PM-UJJWALA",
        "scheme_name": "ఉజ్జ్వల యోజన",
        "scope": "central",
        "eligibility": {
            "gender": "female",
            "bpl": True
        },
        "benefits": "ఉచిత LPG గ్యాస్ కనెక్షన్",
        "required_documents": ["BPL రేషన్ కార్డు"],
        "apply_steps": ["గ్యాస్ ఏజెన్సీ ద్వారా"]
    },

    {
        "scheme_id": "PM-SCHOLARSHIP",
        "scheme_name": "ప్రధాన్ మంత్రి స్కాలర్‌షిప్",
        "scope": "central",
        "eligibility": {
            "student": True
        },
        "benefits": "విద్యా సహాయం",
        "required_documents": ["కాలేజ్ ఐడీ"],
        "apply_steps": ["నేషనల్ స్కాలర్‌షిప్ పోర్టల్"]
    },

    {
        "scheme_id": "PM-JAN-DHAN",
        "scheme_name": "జన్ ధన్ యోజన",
        "scope": "central",
        "eligibility": {
            "bank_account": False
        },
        "benefits": "జీరో బ్యాలెన్స్ బ్యాంక్ ఖాతా",
        "required_documents": ["ఆధార్"],
        "apply_steps": ["సమీప బ్యాంక్‌లో ఖాతా తెరవాలి"]
    },

    {
        "scheme_id": "PM-AYUSHMAN",
        "scheme_name": "ఆయుష్మాన్ భారత్",
        "scope": "central",
        "eligibility": {
            "bpl": True
        },
        "benefits": "రూ. 5 లక్షల ఆరోగ్య బీమా",
        "required_documents": ["ఆధార్", "రేషన్ కార్డు"],
        "apply_steps": ["ఆసుపత్రి వద్ద నమోదు"]
    },

    {
        "scheme_id": "PM-MUDRA",
        "scheme_name": "ముద్రా లోన్ పథకం",
        "scope": "central",
        "eligibility": {
            "self_employed": True
        },
        "benefits": "వ్యాపారానికి లోన్",
        "required_documents": ["ఆధార్", "వ్యాపార వివరాలు"],
        "apply_steps": ["బ్యాంక్ ద్వారా దరఖాస్తు"]
    },

    {
        "scheme_id": "PM-ATAL-PENSION",
        "scheme_name": "అటల్ పెన్షన్ యోజన",
        "scope": "central",
        "eligibility": {
            "min_age": 18,
            "max_age": 40
        },
        "benefits": "వృద్ధాప్య పెన్షన్",
        "required_documents": ["ఆధార్", "బ్యాంక్ ఖాతా"],
        "apply_steps": ["బ్యాంక్‌లో నమోదు"]
    }
]
print("Total schemes loaded:", len(schemes))