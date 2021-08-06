{
    "EGTE 150800Z 1509/1518 18005KT 9999 FEW040": {
        "TAF matches METAR exactly": {
            "metar": "EGTE 150950Z 18005KT 9999 FEW040",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - wind speed differs within bounds": {
            "metar": "EGTE 150950Z 18010KT 9999 FEW040",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - wind light and variable, TAF at 5kt": {
            "metar": "EGTE 150950Z VRB03KT 9999 FEW040",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - wind speed exceeds allowed bounds": {
            "metar": "EGTE 150950Z 18015KT 9999 FEW040",
            "test time": "20200615T1000Z",
            "expected": "EGTE TAF bust by wind"
        },
        "TAF base conditions do not cover METAR - visibility too low": {
            "metar": "EGTE 150950Z 18005KT 9000 FEW040",
            "test time": "20200615T1000Z",
            "expected": "EGTE TAF bust by visibility"
        },
        "TAF base conditions cover METAR - CAVOK instead of 9999 FEW040": {
            "metar": "EGTE 150950Z 18005KT CAVOK",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - unforecast weather type": {
            "metar": "EGTE 150950Z 18005KT 9999 RA FEW040",
            "test time": "20200615T1000Z",
            "expected": "EGTE TAF bust by weather"
        },
        "TAF base conditions cover METAR - cloud differs within bounds": {
            "metar": "EGTE 150950Z 18005KT 9999 SCT040",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud too abundant at 1400FT": {
            "metar": "EGTE 150950Z 18005KT 9999 BKN014",
            "test time": "20200615T1000Z",
            "expected": "EGTE TAF bust by cloud"
        }
    },
    "description": "A summer day with light winds, good visibility, and a little fair weather cumulus."
}
