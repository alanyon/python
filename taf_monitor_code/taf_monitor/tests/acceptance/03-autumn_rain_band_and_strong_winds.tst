{
    "EGTE 150800Z 1509/1518 27015KT 9999 BKN010 BECMG 1509/1512 34015KT 7000 -RA BKN007 TEMPO 1512/1518 35025G35KT 4000 RA BKN004": {
        "TAF matches METAR base conditions exactly": {
            "metar": "EGTE 150850Z 27015KT 9999 BKN010",
            "test time": "20201115T0900Z",
            "expected": ""
        },
        "TAF does not cover METAR - cloud base lifts": {
            "metar": "EGTE 151050Z 27015KT 9999 BKN015",
            "test time": "20201115T1100Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF does not cover METAR - early rain": {
            "metar": "EGTE 151050Z 27015KT 9999 RA BKN010",
            "test time": "20201115T1100Z",
            "expected": "EGTE TAF bust by weather"
        },
        "TAF becmg group covers METAR - wind direction very wrong, but covered by becmg": {
            "metar": "EGTE 151050Z 20015KT 9999 BKN010",
            "test time": "20201115T1100Z",
            "expected": ""
        },
        "TAF does not cover METAR - wind speed outside bounds during becmg period": {
            "metar": "EGTE 151050Z 27025KT 9999 BKN010",
            "test time": "20201115T1100Z",
            "expected": "EGTE TAF bust by wind"
        },
        "TAF tempo group covers METAR - wind speed differs within bounds": {
            "metar": "EGTE 151250Z 34030G40KT 7000 -RA BKN007",
            "test time": "20201115T1300Z",
            "expected": ""
        },
        "TAF tempo group covers METAR - rain": {
            "metar": "EGTE 151250Z 34015KT 7000 RA BKN007",
            "test time": "20201115T1300Z",
            "expected": ""
        },
        "TAF tempo group covers METAR - lower cloud": {
            "metar": "EGTE 151250Z 34015KT 7000 -RA BKN003",
            "test time": "20201115T1300Z",
            "expected": ""
        },
        "TAF tempo group covers METAR - lower visibility": {
            "metar": "EGTE 151250Z 34015KT 4000 -RA BKN007",
            "test time": "20201115T1300Z",
            "expected": ""
        },
        "TAF does not cover METAR - rain too heavy": {
            "metar": "EGTE 151250Z 34015KT 7000 +RA BKN007",
            "test time": "20201115T1300Z",
            "expected": "EGTE TAF bust by weather"
        },
        "TAF does not cover METAR - cloud too low": {
            "metar": "EGTE 151250Z 34015KT 7000 -RA BKN001",
            "test time": "20201115T1300Z",
            "expected": "EGTE TAF bust by cloud"
        },
        "TAF does not cover METAR - visibility too low": {
            "metar": "EGTE 151250Z 34015KT 0800 -RAFG BKN007",
            "test time": "20201115T1300Z",
            "expected": "EGTE TAF bust by visibility"
        },
        "TAF does not cover METAR - wind too strong": {
            "metar": "EGTE 151250Z 34035G45KT 7000 -RA BKN007",
            "test time": "20201115T1300Z",
            "expected": "EGTE TAF bust by wind"
        },
        "TAF does not cover METAR - multiple failures": {
            "metar": "EGTE 151250Z 34035KT 0800 +RAFG BKN001",
            "test time": "20201115T1300Z",
            "expected": "EGTE TAF bust by wind\nEGTE TAF bust by visibility\nEGTE TAF bust by weather\nEGTE TAF bust by cloud"
        }
    },
    "description": "An autumn day with a band of rain and strong winds arriving from the south-west. The cloud and visibility are expected to deteriorate significantly with any moderate rain."
}
