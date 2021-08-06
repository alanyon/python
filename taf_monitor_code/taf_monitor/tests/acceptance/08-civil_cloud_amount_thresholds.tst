{
    "EGTE 150800Z 1509/1518 18005KT 9999 FEW010 TEMPO 1510/1511 BKN010 TEMPO 1511/1512 OVC010 BECMG 1512/1515 CAVOK": {
        "TAF base conditions cover METAR - CAVOK": {
            "metar": "EGTE 150850Z 18005KT CAVOK",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud NSC": {
            "metar": "EGTE 150850Z 18005KT 9999 NSC",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud FEW010": {
            "metar": "EGTE 150850Z 18005KT 9999 FEW010",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud SCT010": {
            "metar": "EGTE 150850Z 18005KT 9999 SCT010",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud BKN020": {
            "metar": "EGTE 150850Z 18005KT 9999 BKN020",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud OVC020": {
            "metar": "EGTE 150850Z 18005KT 9999 OVC020",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN010": {
            "metar": "EGTE 150850Z 18005KT 9999 BKN010",
            "test time": "20200615T0900Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF base conditions do not cover METAR - cloud OVC010": {
            "metar": "EGTE 150850Z 18005KT 9999 OVC010",
            "test time": "20200615T0900Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF tempo conditions cover METAR - cloud BKN010 (TAF BKN)": {
            "metar": "EGTE 150950Z 18005KT 9999 SCT020",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF tempo conditions cover METAR - cloud OVC010 (TAF BKN)": {
            "metar": "EGTE 150950Z 18005KT 9999 OVC010",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF tempo conditions cover METAR - cloud BKN010 (TAF OVC)": {
            "metar": "EGTE 151050Z 18005KT 9999 BKN010",
            "test time": "20200615T1100Z",
            "expected": ""
        },
        "TAF tempo conditions cover METAR - cloud OVC010 (TAF OVC)": {
            "metar": "EGTE 151050Z 18005KT 9999 OVC010",
            "test time": "20200615T1100Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud CAVOK": {
            "metar": "EGTE 151550Z 18005KT CAVOK",
            "test time": "20200615T1600Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud NSC": {
            "metar": "EGTE 151550Z 18005KT 9999 NSC",
            "test time": "20200615T1600Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud FEW040": {
            "metar": "EGTE 151550Z 18005KT 9999 FEW040",
            "test time": "20200615T1600Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud SCT040": {
            "metar": "EGTE 151550Z 18005KT 9999 SCT040",
            "test time": "20200615T1600Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN040": {
            "metar": "EGTE 151550Z 18005KT 9999 BKN040",
            "test time": "20200615T1600Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF base conditions do not cover METAR - cloud OVC040": {
            "metar": "EGTE 151550Z 18005KT 9999 OVC040",
            "test time": "20200615T1600Z",
            "expected": "EGTE TAF bust by cloud"
        }
    },
    "description": "A contrived test with 1 hour tempo groups to check the grouping of BKN/OVC cloud amounts as significant for civil TAFs below 1500FT, or for changes to NSC below 5000FT."
}
