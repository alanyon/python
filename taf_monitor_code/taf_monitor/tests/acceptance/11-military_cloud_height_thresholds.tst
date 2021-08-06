{
    "EGWC 150800Z 1509/1518 18005KT 9999 BKN040 TEMPO 1510/1511 BKN020 TEMPO 1511/1512 BKN010 TEMPO 1512/1513 BKN006 TEMPO 1513/1514 BKN004 TEMPO 1514/1515 BKN002 TEMPO 1515/1516 BKN001": {
        "TAF base conditions cover METAR - cloud BKN040": {
            "metar": "EGWC 150850Z 18005KT 9999 BKN040",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN020": {
            "metar": "EGWC 150850Z 18005KT 9999 BKN020",
            "test time": "20200615T0900Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN020": {
            "metar": "EGWC 150950Z 18005KT 9999 BKN020",
            "test time": "20200615T1000Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN010": {
            "metar": "EGWC 150950Z 18005KT 9999 BKN010",
            "test time": "20200615T1000Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN010": {
            "metar": "EGWC 151050Z 18005KT 9999 BKN010",
            "test time": "20200615T1100Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN006": {
            "metar": "EGWC 151050Z 18005KT 9999 BKN006",
            "test time": "20200615T1100Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN006": {
            "metar": "EGWC 151150Z 18005KT 9999 BKN006",
            "test time": "20200615T1200Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN004": {
            "metar": "EGWC 151150Z 18005KT 9999 BKN004",
            "test time": "20200615T1200Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN004": {
            "metar": "EGWC 151250Z 18005KT 9999 BKN004",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN002": {
            "metar": "EGWC 151250Z 18005KT 9999 BKN002",
            "test time": "20200615T1300Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN002": {
            "metar": "EGWC 151350Z 18005KT 9999 BKN002",
            "test time": "20200615T1400Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN001": {
            "metar": "EGWC 151350Z 18005KT 9999 BKN001",
            "test time": "20200615T1400Z",
            "expected": "EGWC TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN001": {
            "metar": "EGWC 151450Z 18005KT 9999 BKN001",
            "test time": "20200615T1500Z",
            "expected": ""
        }
    },
    "description": "A contrived test with 1 hour tempo groups descending the military cloud height thresholds. Each cloud height is tested twice, once in the hour preceding the tempo group it requires, making the TAF invalid, and once during the hour of the tempo group making the TAF valid."
}
