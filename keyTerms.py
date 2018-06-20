def getKeyTerms():
    return [
        ['airline', 'Air Transport', 'positive'],
        ['airlines', 'Air Transport', 'positive'],
        ['delta', 'Air Transport', 'positive'],
        ['american airlines', 'Air Transport', 'positive'],
        ['united continental', 'Air Transport', 'positive'],
        ['southwest airlines', 'Air Transport', 'positive'],
        ['faa', 'Air Transport', 'positive'],
        ['aviation', 'Air Transport', 'positive'],

        # ['', 'Business Services'],

        ['casinos', 'Casinos/Gambling', 'positive'],
        ['gambling', 'Casinos/Gambling', 'positive'],

        ['jp morgan', 'Commercial Banks', 'positive'],
        ['jpmorgan', 'Commercial Banks', 'positive'],
        ['bank of america', 'Commercial Banks', 'positive'],
        ['wells fargo', 'Commercial Banks', 'positive'],
        ['citigroup', 'Commercial Banks', 'positive'],
        ['morgan stanley', 'Commercial Banks', 'positive'],
        ['banks', 'Commercial Banks', 'positive'],
        ['dodd frank', 'Commercial Banks', 'positive'],

        ['drone', 'Defense Aerospace', 'positive'],
        ['drones', 'Defense Aerospace', 'positive'],

        # ['', 'Democratic/Liberal'],

        # REMOVED: Never good calls
        # ['public education', 'Education'],
        # ['charter schools', 'Education'],
        # ['student loans', 'Education'],
        # ['students', 'Education'],
        # ['teachers', 'Education'],
        # ['educators', 'Education'],
        # ['college loans', 'Education'],
        # ['colleges', 'Education'],

        # ['', 'Electric Utilities'],

        # ['health insurance', 'Health Professionals', 'positive'],
        # ['health care', 'Health Professionals', 'positive'],
        # ['health-care', 'Health Professionals', 'positive'],
        # ['healthcare', 'Health Professionals', 'positive'],

        # ['', 'Human Rights'],

        ['insurance', 'Insurance', 'positive'],

        ['net neutrality', 'Internet', 'negative'],
        ['net-neutrality', 'Internet', 'negative'],
        ['netneutrality', 'Internet', 'negative'],
        ['comcast', 'Internet', 'positive'],
        ['verizon', 'Internet', 'positive'],

        # ['', 'Lawyers/Law Firms'],
        # ['', 'Leadership PACs'],
        # ['', 'Lobbyists'],

        ['mining', 'Mining', 'positive'],
        ['miners', 'Mining', 'positive'],
        ['coal', 'Mining', 'positive'],
        ['shale', 'Mining', 'positive'],
        [' epa ', 'Mining', 'negative'],
        ['scott pruit', 'Mining', 'positive'],

        # ['', 'Misc Finance'],
        # ['', 'Misc Manufacturing & Distributing'],

        [' oil ', 'Oil & Gas', 'positive'],
        [' gas ', 'Oil & Gas', 'positive'],
        ['gasoline', 'Oil & Gas', 'positive'],
        ['diesel', 'Oil & Gas', 'positive'],
        ['petroleum', 'Oil & Gas', 'positive'],
        ['keystone', 'Oil & Gas', 'positive'],
        [' shale ', 'Oil & Gas', 'positive'],

        # ['pharma', 'Pharmaceuticals/Health Products', 'positive'],
        # ['pharmaceutical', 'Pharmaceuticals/Health Products', 'positive'],
        # ['pharmaceuticals', 'Pharmaceuticals/Health Products', 'positive'],
        # ['opioid', 'Pharmaceuticals/Health Products', 'positive'],
        # ['drug', 'Pharmaceuticals/Health Products', 'na'],
        # ['drugs', 'Pharmaceuticals/Health Products', 'na'],
        # ['drug war', 'Pharmaceuticals/Health Products', 'na'],
        # ['drug-war', 'Pharmaceuticals/Health Products', 'na'],
        # ['war on drugs', 'Pharmaceuticals/Health Products', 'na'],
        # ['health insurance', 'Pharmaceuticals/Health Products', 'na'],
        # ['health care', 'Pharmaceuticals/Health Products', 'na'],
        # ['health-care', 'Pharmaceuticals/Health Products', 'na'],
        # ['healthcare', 'Pharmaceuticals/Health Products', 'na'],
        # ['medicine', 'Pharmaceuticals/Health Products', 'positive'],
        # [' rx ', 'Pharmaceuticals/Health Products', 'positive'],
        # ['marijuana', 'Pharmaceuticals/Health Products', 'negative'],

        ['israel', 'Pro-Israel', 'positive'],
        ['israeli', 'Pro-Israel', 'positive'],
        ['jerusalem', 'Pro-Israel', 'positive'],
        ['holy city', 'Pro-Israel', 'positive'],

        ['housing market', 'Real Estate', 'positive'],
        ['home owners', 'Real Estate', 'positive'],
        ['real estate', 'Real Estate', 'positive'],

        # ['', 'Republican/Conservative'],
        # ['', 'Retail Sales'],
        # ['', 'Retired'],

        ['nasdaq', 'Securities & Investment', 'positive'],
        [' dow ', 'Securities & Investment', 'positive'],
        [' stock ', 'Securities & Investment', 'positive'],
        [' stocks ', 'Securities & Investment', 'positive'],


        ['hollywood', 'TV/Movies/Music', 'positive'],
        # ['fake news', 'TV/Movies/Music', 'negative'],
        [' fox ', 'TV/Movies/Music', 'na'],

        ['net neutrality', 'Telecom Services', 'negative'],
        ['net-neutrality', 'Telecom Services', 'negative'],
        ['netneutrality', 'Telecom Services', 'negative'],
        ['at&t', 'Telecom Services', 'positive'],
        ['verizon', 'Telecom Services', 'positive'],
        ['sprint', 'Telecom Services', 'positive'],
        ['t-mobile', 'Telecom Services', 'positive'],
        ['comcast', 'Telecom Services', 'positive'],
        ['cable', 'Telecom Services', 'positive'],
        ['media', 'Telecom Services', 'positive'],
        # ['fake news', 'Telecom Services', 'na'],
        [' fcc ', 'Telecom Services', 'positive'],
    ]

def getExceptions():
    return [
        ' rip ',
        'rest in peace',
        '#restinpeace',
        'r.i.p.',
        'passed away'
    ]






























































# keyTerms = [
#     'airline' : 'Air Transport',
#     'airlines' : 'Air Transport',
#     'delta' : 'Air Transport',
#     'american airlines' : 'Air Transport',
#     'united continental' : 'Air Transport',
#     'southwest airlines' : 'Air Transport',
#
#     # '' : 'Business Services',
#
#     'casinos' : 'Casinos/Gambling',
#     'gambling' : 'Casinos/Gambling',
#
#     'jp morgan' : 'Commercial Banks',
#     'jpmorgan' : 'Commercial Banks',
#     'bank of america' : 'Commercial Banks',
#     'wells fargo' : 'Commercial Banks',
#     'citigroup' : 'Commercial Banks',
#     'morgan stanley' : 'Commercial Banks',
#     'banks' : 'Commercial Banks',
#
#     # '' : 'Defense Aerospace',
#     # '' : 'Democratic/Liberal',
#
#     'public education' : 'Education',
#     'charter schools' : 'Education',
#
#     # '' : 'Electric Utilities',
#
#     'health insurance' : 'Health Professionals',
#     'health care' : 'Health Professionals',
#     'health-care' : 'Health Professionals',
#     'healthcare' : 'Health Professionals',
#
#     # '' : 'Human Rights',
#
#     'insurance' : 'Insurance',
#
#     'net neutrality' : 'Internet',
#     'net-neutrality' : 'Internet',
#     'comcast' : 'Internet',
#     'verizon' : 'Internet',
#
#     # '' : 'Lawyers/Law Firms',
#     # '' : 'Leadership PACs',
#     # '' : 'Lobbyists',
#
#     'mining' : 'Mining',
#     'miners' : 'Mining',
#     'coal' : 'Mining',
#     'shale' : 'Mining',
#
#     # '' : 'Misc Finance',
#     # '' : 'Misc Manufacturing & Distributing',
#
#     'oil' : 'Oil & Gas',
#     'gas' : 'Oil & Gas',
#     'gasoline' : 'Oil & Gas',
#     'diesel' : 'Oil & Gas',
#     'petroleum' : 'Oil & Gas',
#     'keystone' : 'Oil & Gas',
#     'shale' : 'Oil & Gas',
#
#     'pharma' : 'Pharmaceuticals/Health Products',
#     'pharmaceutical' : 'Pharmaceuticals/Health Products',
#     'pharmaceuticals' : 'Pharmaceuticals/Health Products',
#     'opioid' : 'Pharmaceuticals/Health Products',
#     'drug' : 'Pharmaceuticals/Health Products',
#     'drugs' : 'Pharmaceuticals/Health Products',
#     'drug war' : 'Pharmaceuticals/Health Products',
#     'drug-war' : 'Pharmaceuticals/Health Products',
#     'war on drugs' : 'Pharmaceuticals/Health Products',
#     'health insurance' : 'Pharmaceuticals/Health Products',
#     'health care' : 'Pharmaceuticals/Health Products',
#     'health-care' : 'Pharmaceuticals/Health Products',
#     'healthcare' : 'Pharmaceuticals/Health Products',
#
#     'israel' : 'Pro-Israel',
#
#     'housing market' : 'Real Estate',
#
#     # '' : 'Republican/Conservative',
#     # '' : 'Retail Sales',
#     # '' : 'Retired',
#
#     'nasdaq' : 'Securities & Investment',
#     'dow' : 'Securities & Investment',
#
#     'hollywood' : 'TV/Movies/Music',
#     'fake news' : 'TV/Movies/Music',
#     'fox' : 'TV/Movies/Music',
#
#     'net neutrality' : 'Telecom Services',
#     'net-neutrality' : 'Telecom Services',
#     'at&t' : 'Telecom Services',
#     'verizon' : 'Telecom Services',
#     'sprint' : 'Telecom Services',
#     't-mobile' : 'Telecom Services',
#     'comcast' : 'Telecom Services',
#     'cable' : 'Telecom Services',
# ]
#
