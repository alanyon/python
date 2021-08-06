{
    "EGTE 150800Z 1509/1518 18005KT 9999 BKN040 TEMPO 1511/1512 BKN010 TEMPO 1512/1513 BKN006 TEMPO 1513/1514 BKN003 TEMPO 1514/1515 BKN001": {
        "TAF base conditions cover METAR - cloud BKN050": {
            "metar": "EGTE 150850Z 18005KT 9999 BKN050",
            "test time": "20200615T0900Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN010": {
            "metar": "EGTE 150950Z 18005KT 9999 BKN010",
            "test time": "20200615T1000Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN010": {
            "metar": "EGTE 151050Z 18005KT 9999 BKN010",
            "test time": "20200615T1100Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN006": {
            "metar": "EGTE 151050Z 18005KT 9999 BKN006",
            "test time": "20200615T1100Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN006": {
            "metar": "EGTE 151150Z 18005KT 9999 BKN006",
            "test time": "20200615T1200Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN003": {
            "metar": "EGTE 151150Z 18005KT 9999 BKN003",
            "test time": "20200615T1200Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN003": {
            "metar": "EGTE 151250Z 18005KT 9999 BKN003",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF base conditions do not cover METAR - cloud BKN001": {
            "metar": "EGTE 151250Z 18005KT 9999 BKN001",
            "test time": "20200615T1300Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF base conditions cover METAR - cloud BKN001": {
            "metar": "EGTE 151350Z 18005KT 9999 BKN001",
            "test time": "20200615T1400Z",
            "expected": ""
        }
    },
    "description": "A contrived test with 1 hour tempo groups descending the civil cloud thresholds. Each cloud height is tested twice, once in the hour preceding the tempo group it requires, making the TAF invalid, and once during the hour of the tempo group making the TAF valid."
}
