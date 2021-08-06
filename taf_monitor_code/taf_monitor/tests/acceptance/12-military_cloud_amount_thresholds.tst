{
    "EGWC 150800Z 1509/1518 18005KT 9999 FEW030 TEMPO 1510/1511 SCT020 TEMPO 1511/1512 BKN020 TEMPO 1512/1513 OVC020 BECMG 1513/1515 OVC020": {
        "TAF base conditions cover METAR - CAVOK": {
            "metar": "EGWC 150850Z 18005KT CAVOK",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud NSC": {
            "metar": "EGWC 150850Z 18005KT 9999 NSC",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud FEW030": {
            "metar": "EGWC 150850Z 18005KT 9999 FEW030",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud SCT030": {
            "metar": "EGWC 150850Z 18005KT 9999 SCT030",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud BKN030": {
            "metar": "EGWC 150850Z 18005KT 9999 BKN030",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud OVC030": {
            "metar": "EGWC 150850Z 18005KT 9999 OVC030",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud SCT020": {
            "metar": "EGWC 150850Z 18005KT 9999 SCT020",
            "test time": "20200615T0900Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF base conditions do not cover METAR - cloud BKN020": {
            "metar": "EGWC 150850Z 18005KT 9999 BKN020",
            "test time": "20200615T0900Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF base conditions do not cover METAR - cloud OVC020": {
            "metar": "EGWC 150850Z 18005KT 9999 OVC020",
            "test time": "20200615T0900Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF tempo conditions cover METAR - cloud SCT020 (TAF SCT)": {
            "metar": "EGWC 150950Z 18005KT 9999 SCT020",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF tempo conditions cover METAR - cloud BKN020 (TAF SCT)": {
            "metar": "EGWC 150950Z 18005KT 9999 BKN020",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF tempo conditions cover METAR - cloud OVC020 (TAF SCT)": {
            "metar": "EGWC 150950Z 18005KT 9999 OVC020",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF tempo conditions cover METAR - cloud SCT020 (TAF BKN)": {
            "metar": "EGWC 151050Z 18005KT 9999 SCT020",
            "test time": "20200615T1100Z",
            "expected": ""
        },
        "TAF tempo conditions cover METAR - cloud BKN020 (TAF BKN)": {
            "metar": "EGWC 151050Z 18005KT 9999 BKN020",
            "test time": "20200615T1100Z",
            "expected": ""
        },
        "TAF tempo conditions cover METAR - cloud OVC020 (TAF BKN)": {
            "metar": "EGWC 151050Z 18005KT 9999 OVC020",
            "test time": "20200615T1100Z",
            "expected": ""
        },
        "TAF tempo conditions cover METAR - cloud SCT020 (TAF OVC)": {
            "metar": "EGWC 151150Z 18005KT 9999 SCT020",
            "test time": "20200615T1200Z",
            "expected": ""
        },
        "TAF tempo conditions cover METAR - cloud BKN020 (TAF OVC)": {
            "metar": "EGWC 151150Z 18005KT 9999 BKN020",
            "test time": "20200615T1200Z",
            "expected": ""
        },
        "TAF tempo conditions cover METAR - cloud OVC020 (TAF OVC)": {
            "metar": "EGWC 151150Z 18005KT 9999 OVC020",
            "test time": "20200615T1200Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud OVC020": {
            "metar": "EGWC 151550Z 18005KT 9999 OVC020",
            "test time": "20200615T1600Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud BKN020": {
            "metar": "EGWC 151550Z 18005KT 9999 BKN020",
            "test time": "20200615T1600Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - cloud SCT020": {
            "metar": "EGWC 151550Z 18005KT 9999 SCT020",
            "test time": "20200615T1600Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud FEW020": {
            "metar": "EGWC 151550Z 18005KT 9999 FEW020",
            "test time": "20200615T1600Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF base conditions do not cover METAR - cloud NSC": {
            "metar": "EGWC 151550Z 18005KT 9999 NSC",
            "test time": "20200615T1600Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF base conditions do not cover METAR - CAVOK": {
            "metar": "EGWC 151550Z 18005KT CAVOK",
            "test time": "20200615T1600Z",
            "expected": "EGWC TAF bust by cloud"
        }

    },
    "description": "A contrived test with 1 hour tempo groups to check the grouping of SCT/BKN/OVC cloud amounts as significant for military TAFs below 2500FT."
}
