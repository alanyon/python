{
    "EGWC 150800Z 1509/1518 18005KT 9999 SCT010 BKN040CB BECMG 1512/1515 SCT010 TEMPO 1517/1518 BKN010CB": {
        "TAF matches METAR exactly - CB included in observations": {
            "metar": "EGWC 150850Z 18005KT 9999 SCT010 BKN040CB",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions cover METAR - CB at differeng height, same bracket": {
            "metar": "EGWC 150850Z 18005KT 9999 SCT010 BKN030CB",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF does not cover METAR - CB group with lower base than expected": {
            "metar": "EGWC 150850Z 18005KT 9999 FEW004 BKN006CB",
            "test time": "20200615T0900Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF does not cover METAR - CB persist beyond expected period": {
            "metar": "EGWC 151550Z 18005KT 9999 SCT010 BKN040CB",
            "test time": "20200615T1600Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF tempo group covers METAR - lower altitude CB late in the day": {
            "metar": "EGWC 151650Z 18005KT 9999 BKN010CB",
            "test time": "20200615T1700Z",
            "expected": ""
        }
    },
    "description": "Tests for military TAFs that do or do not include CBs when they are required."
}
