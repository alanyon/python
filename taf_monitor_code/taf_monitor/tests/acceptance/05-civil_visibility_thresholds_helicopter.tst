{
    "EGNJ 150800Z 1509/1518 18005KT 9999 FEW040 TEMPO 1511/1512 8000 TEMPO 1512/1513 5000 TEMPO 1513/1514 4000 TEMPO 1514/1515 2000 TEMPO 1515/1516 1000 TEMPO 1516/1517 0500 TEMPO 1517/1518 0200": {
        "TAF base conditions cover METAR - visibility 9999": {
            "metar": "EGNJ 150850Z 18005KT 9999 FEW040",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base confitions do not cover METAR - visibility 8000": {
            "metar": "EGNJ 150850Z 18005KT 8000 FEW040",
            "test time": "20200615T0900Z",
            "expected": "EGNJ TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 8000": {
            "metar": "EGNJ 151050Z 18005KT 8000 FEW040",
            "test time": "20200615T1100Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - visibility 5500": {
            "metar": "EGNJ 151050Z 18005KT 5500 FEW040",
            "test time": "20200615T1100Z",
            "expected": "EGNJ TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 5500": {
            "metar": "EGNJ 151150Z 18005KT 5500 FEW040",
            "test time": "20200615T1200Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - visibility 4000": {
            "metar": "EGNJ 151150Z 18005KT 4000 FEW040",
            "test time": "20200615T1200Z",
            "expected": "EGNJ TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 4000": {
            "metar": "EGNJ 151250Z 18005KT 4000 FEW040",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - visibility 2000": {
            "metar": "EGNJ 151250Z 18005KT 2000 FEW040",
            "test time": "20200615T1300Z",
            "expected": "EGNJ TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 2000": {
            "metar": "EGNJ 151350Z 18005KT 2000 FEW040",
            "test time": "20200615T1400Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - visibility 1000": {
            "metar": "EGNJ 151350Z 18005KT 1000 FEW040",
            "test time": "20200615T1400Z",
            "expected": "EGNJ TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 1000": {
            "metar": "EGNJ 151450Z 18005KT 1000 FEW040",
            "test time": "20200615T1500Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - visibility 500": {
            "metar": "EGNJ 151450Z 18005KT 0500 FEW040",
            "test time": "20200615T1500Z",
            "expected": "EGNJ TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 500": {
            "metar": "EGNJ 151550Z 18005KT 0500 FEW040",
            "test time": "20200615T1600Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - visibility 200": {
            "metar": "EGNJ 151550Z 18005KT 0200 FEW040",
            "test time": "20200615T1600Z",
            "expected": "EGNJ TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 200": {
            "metar": "EGNJ 151650Z 18005KT 0200 FEW040",
            "test time": "20200615T1700Z",
            "expected": ""
        }
    },
    "description": "A contrived test with 1 hour tempo groups descending the civil visibility thresholds for airfields using helicopter thresholds. Each visibility is tested twice, once in the hour preceding the tempo group it requires, making the TAF invalid, and once during the hour of the tempo group making the TAF valid."
}
