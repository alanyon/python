{
    "EGNJ 150800Z 1509/1518 18005KT 9999 BKN040 TEMPO 1511/1512 BKN010 TEMPO 1512/1513 BKN008 TEMPO 1513/1514 BKN005 TEMPO 1514/1515 BKN003 TEMPO 1515/1516 BKN001": {
        "TAF base conditions cover METAR - cloud BKN050": {
            "metar": "EGNJ 150850Z 18005KT 9999 BKN050",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN010": {
            "metar": "EGNJ 150950Z 18005KT 9999 BKN010",
            "test time": "20200615T1000Z",
            "expected": "EGNJ TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN010": {
            "metar": "EGNJ 151050Z 18005KT 9999 BKN010",
            "test time": "20200615T1100Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN008": {
            "metar": "EGNJ 151050Z 18005KT 9999 BKN008",
            "test time": "20200615T1100Z",
            "expected": "EGNJ TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN008": {
            "metar": "EGNJ 151150Z 18005KT 9999 BKN008",
            "test time": "20200615T1200Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN006": {
            "metar": "EGNJ 151150Z 18005KT 9999 BKN006",
            "test time": "20200615T1200Z",
            "expected": "EGNJ TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN006": {
            "metar": "EGNJ 151250Z 18005KT 9999 BKN006",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN003": {
            "metar": "EGNJ 151250Z 18005KT 9999 BKN003",
            "test time": "20200615T1300Z",
            "expected": "EGNJ TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN003": {
            "metar": "EGNJ 151350Z 18005KT 9999 BKN003",
            "test time": "20200615T1400Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN001": {
            "metar": "EGNJ 151350Z 18005KT 9999 BKN001",
            "test time": "20200615T1400Z",
            "expected": "EGNJ TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN001": {
            "metar": "EGNJ 151450Z 18005KT 9999 BKN001",
            "test time": "20200615T1500Z",
            "expected": ""
        }
    },
    "description": "A contrived test with 1 hour tempo groups descending the civil cloud height thresholds for airfields using helicopter thresholds. Each cloud height is tested twice, once in the hour preceding the tempo group it requires, making the TAF invalid, and once during the hour of the tempo group making the TAF valid."
}
