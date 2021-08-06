{
    "EGTE 150800Z 1509/1518 18005KT CAVOK TEMPO 1512/1518 BKN040": {
        "TAF matches METAR exactly": {
            "metar": "EGTE 150950Z 18005KT CAVOK",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - FEW040 cloud": {
            "metar": "EGTE 150950Z 18005KT 9999 FEW040",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - visibility drop": {
            "metar": "EGTE 150950Z 18005KT 9000 NSC",
            "test time": "20200615T1000Z",
            "expected": "EGTE TAF bust by visibility"
        },
        "TAF base conditions cover METAR - SCT040 cloud": {
            "metar": "EGTE 150950Z 18005KT 9999 SCT040",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - BKN040 cloud": {
            "metar": "EGTE 150950Z 18005KT 9999 BKN040",
            "test time": "20200615T1000Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF base conditions do not cover METAR - OVC040 cloud": {
            "metar": "EGTE 150950Z 18005KT 9999 OVC040",
            "test time": "20200615T1000Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF base conditions do not cover METAR - VV/// cloud": {
            "metar": "EGTE 150950Z 18005KT 9999 VV///",
            "test time": "20200615T1000Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF tempo group covers METAR - BKN040 cloud": {
            "metar": "EGTE 151250Z 18005KT 9999 BKN040",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF tempo group covers METAR - OVC040 cloud": {
            "metar": "EGTE 151250Z 18005KT 9999 OVC040",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - VV/// cloud": {
            "metar": "EGTE 151250Z 18005KT 9999 VV///",
            "test time": "20200615T1300Z",
            "expected": "EGTE TAF bust by cloud"
        }
    },
    "description": "A CAVOK day, testing how TAF Monitor handles CAVOK in forecasts."
}
