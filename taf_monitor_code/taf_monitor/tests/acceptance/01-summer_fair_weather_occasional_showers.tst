{
    "EGTE 150800Z 1509/1518 18005KT 9999 FEW040 TEMPO 1512/1518 20015KT 7000 SHRA BKN014": {
        "TAF matches METAR tempo group exactly": {
            "metar": "EGTE 151250Z 18005KT 7000 SHRA BKN014",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF tempo group covers METAR - wind speed differs within bounds": {
            "metar": "EGTE 151250Z 20020KT 7000 SHRA BKN014",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF tempo group covers METAR - wind direction differs within bounds": {
            "metar": "EGTE 151250Z 25015KT 7000 SHRA BKN014",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - wind speed and direction combined breach bounds": {
            "metar": "EGTE 151250Z 25020KT 7000 SHRA BKN014",
            "test time": "20200615T1300Z",
            "expected": "EGTE TAF bust by wind"
        },
        "TAF tempo group does not cover METAR - wind exceeds allowed speed": {
            "metar": "EGTE 151250Z 20025KT 7000 SHRA BKN014",
            "test time": "20200615T1300Z",
            "expected": "EGTE TAF bust by wind"
        },
        "TAF tempo group does not cover METAR - unforecast wind gust speed": {
            "metar": "EGTE 151250Z 20015G25KT 7000 SHRA BKN014",
            "test time": "20200615T1300Z",
            "expected": "EGTE TAF bust by wind"
        },
        "TAF tempo group does not cover METAR - unexpected weather type": {
            "metar": "EGTE 151250Z 20015KT 7000 TSRA BKN014",
            "test time": "20200615T1300Z",
            "expected": "EGTE TAF bust by weather"
        },
        "TAF tempo group covers METAR - visibility differs within bounds": {
            "metar": "EGTE 151250Z 20015KT 8000 SHRA BKN014",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - visibility too low": {
            "metar": "EGTE 151250Z 20015KT 4000 SHRA BKN014",
            "test time": "20200615T1300Z",
            "expected": "EGTE TAF bust by visibility"
        },
        "TAF tempo group covers METAR - cloud base differs within bounds": {
            "metar": "EGTE 151250Z 20015KT 7000 SHRA BKN010",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF tempo group covers METAR - cloud amount differs within bounds": {
            "metar": "EGTE 151250Z 20015KT 7000 SHRA OVC010",
            "test time": "20200615T1300Z",
            "expected": ""
        },
        "TAF tempo group does not cover METAR - cloud base too low": {
            "metar": "EGTE 151250Z 20015KT 7000 SHRA BKN009",
            "test time": "20200615T1300Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF tempo group covers METAR - shower at 1150Z ob for tempo group starting 1200Z": {
            "metar": "EGTE 151150Z 20015KT 7000 SHRA BKN014",
            "test time": "20200615T1200Z",
            "expected": ""
        },
        "TAF does not cover METAR - shower before tempo group start time": {
            "metar": "EGTE 151120Z 20015KT 7000 SHRA BKN014",
            "test time": "20200615T1130Z",
            "expected": "EGTE TAF bust by wind\nEGTE TAF bust by visibility\nEGTE TAF bust by weather\nEGTE TAF bust by cloud"
        },
        "TAF base conditions cover METAR - CAVOK conditions": {
            "metar": "EGTE 151120Z 18005KT CAVOK",
            "test time": "20200615T1130Z",
            "expected": ""
        }
    },
    "description": "A summer day with light winds, good visibility, and a little fair weather cumulus. A tempo group describes intermittent showers in the afternoon."
}
