{
    "EGTE 150800Z 1509/1518 18005KT 9999 FEW040 TEMPO 1511/1512 8000 TEMPO 1512/1513 4000 TEMPO 1513/1514 1000 TEMPO 1514/1515 0500 TEMPO 1515/1516 0200": {
        "TAF base conditions cover METAR - visibility 9999": {
            "metar": "EGTE 150850Z 18005KT 9999 FEW040",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - visibility 7000": {
            "metar": "EGTE 150850Z 18005KT 7000 FEW040",
            "test time": "20200615T0900Z",
            "expected": "EGTE TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 7000": {
            "metar": "EGTE 151050Z 18005KT 7000 FEW040",
            "test time": "20200615T1100Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - visibility 4000": {
            "metar": "EGTE 151050Z 18005KT 4000 FEW040",
            "test time": "20200615T1100Z",
            "expected": "EGTE TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 4000": {
            "metar": "EGTE 151150Z 18005KT 4000 FEW040",
            "test time": "20200615T1200Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - visibility 1000": {
            "metar": "EGTE 151150Z 18005KT 1000 FEW040",
            "test time": "20200615T1200Z",
            "expected": "EGTE TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 1000": {
            "metar": "EGTE 151250Z 18005KT 1000 FEW040",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - visibility 0500": {
            "metar": "EGTE 151250Z 18005KT 0500 FEW040",
            "test time": "20200615T1300Z",
            "expected": "EGTE TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 0500": {
            "metar": "EGTE 151350Z 18005KT 0500 FEW040",
            "test time": "20200615T1400Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - visibility 0200": {
            "metar": "EGTE 151350Z 18005KT 0200 FEW040",
            "test time": "20200615T1400Z",
            "expected": "EGTE TAF bust by visibility"
        },
        "TAF tempo group covers METAR - visibility 0200": {
            "metar": "EGTE 151450Z 18005KT 0200 FEW040",
            "test time": "20200615T1500Z",
            "expected": ""
        }
    },
    "description": "A contrived test with 1 hour tempo groups descending the civil visibility thresholds. Each visibility is tested twice, once in the hour preceding the tempo group it requires, making the TAF invalid, and once during the hour of the tempo group making the TAF valid."
}
