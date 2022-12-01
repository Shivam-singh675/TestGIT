nsl_web_find(TEXT="Mercury Tours", PAGE=welcome, FAIL=NOTFOUND, ID="welcome not found", ActionOnFail=STOP);
nsl_web_find(TEXT="Welcome to Mercury Tours", PAGE=login, FAIL=NOTFOUND, ID="login page failure", ActionOnFail=STOP);
nsl_web_find(TEXT="Find Flights", PAGE=reservation, FAIL=NOTFOUND, ID="reservation failure", ActionOnFail=STOP);
nsl_web_find(TEXT="Search Results", PAGE=findflight, FAIL=NOTFOUND, ID="findflighrs failure", ActionOnFail=STOP);
nsl_web_find(TEXT="Your reservation has been confirmed.  Thank you for booking through Mercury Tour", PAGE=findflight_3, FAIL=NOTFOUND, ID="findflights_3 failure", ActionOnFail=STOP);
nsl_static_var(uname:1,pswd:2, File=login, Refresh=SESSION, Mode=SEQUENTIAL, FirstDataLine=2, EncodeMode=All);
nsl_search_var(user_session, PAGE=welcome, LB="userSession value=", RB=">", LBMATCH=FIRST, SaveOffset=0, RETAINPREVALUE="NO", EncodeMode=None);
nsl_search_var(arrival, PAGE=reservation, LB="><OPTION  VALUE=\"", RB="\">", LBMATCH=FIRST, ORD=ANY, SaveOffset=0, RETAINPREVALUE="NO", EncodeMode=None);
nsl_search_var(depart, PAGE=reservation, LB="><OPTION  VALUE=\"", RB="\">", LBMATCH=FIRST, ORD=ANY, SaveOffset=0, RETAINPREVALUE="NO", EncodeMode=None);
