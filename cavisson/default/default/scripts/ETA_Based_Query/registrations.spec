//nsl_decl_var(id, DefaultValue={{$guid}});
//nsl_decl_var(get-by, DefaultValue=-1);
//nsl_decl_var(checkoutpreviews-items, DefaultValue=-1);
//nsl_decl_var(checkout-id, DefaultValue=-1);


//----------------------------Generate Job-Id--------------------------------------------
nsl_decl_var(job-id,RETAINPREVALUE="NO");
nsl_random_string_var(dbid1, Min=8, Max=8, CharSet="a-f0-9", Refresh=USE);
nsl_random_string_var(dbid2, Min=4, Max=4, CharSet="a-f0-9", Refresh=USE);
nsl_random_string_var(dbid3, Min=4, Max=4, CharSet="a-f0-9", Refresh=SESSION);
nsl_random_string_var(dbid4, Min=4, Max=4, CharSet="a-f0-9", Refresh=SESSION);
nsl_random_string_var(dbid5, Min=12, Max=12, CharSet="a-f0-9", Refresh=SESSION);


//-----------------------------------------------------------------------------------------------
nsl_static_var(endpoint:1, File=endpoint, Refresh=SESSION, Mode=SEQUENTIAL, EncodeMode=All);
nsl_static_var(skuId:1, File=skuId, Refresh=SESSION, Mode=SEQUENTIAL, EncodeMode=All);
nsl_static_var(userEmail:1, File=userEmail, Refresh=SESSION, Mode=SEQUENTIAL, EncodeMode=All);
nsl_static_var(productId:1, File=productId, Refresh=SESSION, Mode=SEQUENTIAL, EncodeMode=All);
nsl_static_var(userPhone:1, File=userPhone, Refresh=SESSION, Mode=SEQUENTIAL, EncodeMode=All);
nsl_static_var(price:1, File=price, Refresh=SESSION, Mode=SEQUENTIAL, EncodeMode=All);
nsl_search_var(ItemgetBySP, PAGE=Fulfillment_offerings_v1_MEMBER, LB="\"getBy\":", RB=",\"price\":", LBMATCH=FIRST, SaveOffset=0, RETAINPREVALUE="NO", EncodeMode=None);

//-----------------------------------GENERATE_TOKEN----------------------------------------------------------------
nsl_decl_var(codeVerifier,RETAINPREVALUE="YES");
nsl_decl_var(codeChallenger,RETAINPREVALUE="YES");
nsl_random_string_var(state, Min=33, Max=33, CharSet="a-zA-Z0-9", Refresh=SESSION);
nsl_search_var(code, PAGE=v1_7, LB="?code=", RB="&state=", LBMATCH=FIRST, SaveOffset=0, RETAINPREVALUE="NO", EncodeMode=None);
//nsl_json_var(v1_6, PAGE=v1_6, OBJECT_PATH="root.access_token", ORD=1, SaveOffset=0, RETAINPREVALUE="YES", EncodeMode=None);
//nsl_json_var(token, PAGE=token, OBJECT_PATH="root.access_token", ORD=1, SaveOffset=0, RETAINPREVALUE="YES", EncodeMode=None);
//nsl_web_find(TEXT="orderId", PAGE=BuyCheckoutsQRYMember, FAIL=NOTFOUND, ID="order id is not generated", ActionOnFail=STOP);
		//nsl_static_var(token:1, File=token, Refresh=SESSION, Mode=SEQUENTIAL, ColumnDelimiter=#, EncodeMode=All);

//-------------------------------------------------------------------------------------------------------------------------------------
//nsl_json_var(dyn_token_jp, PAGE=token, OBJECT_PATH="root.access_token", ORD=1, SaveOffset=0, RETAINPREVALUE="YES", EncodeMode=None);
nsl_decl_var(token,RETAINPREVALUE="NO");
nsl_json_var(dyn_token_jp, PAGE=token, OBJECT_PATH="root.access_token", ORD=1, SaveOffset=0, RETAINPREVALUE="YES", EncodeMode=None);



nsl_json_var(cmd_eta_jp, PAGE=Put_Checkout_Previews_V3_CMD_MEMBER, OBJECT_PATH="root.eta", ORD=1, SaveOffset=0, RETAINPREVALUE="YES", EncodeMode=None);

nsl_json_var(cmd_status_jp, PAGE=Get_Checkout_Previews_V3_QRY_MEMBER, OBJECT_PATH="root.status", ORD=1, SaveOffset=0, RETAINPREVALUE="YES", EncodeMode=None);


//----------------------------------------------cHECKPOINTS-----------------------------------------------------------------------------------------

nsl_web_find(TEXT="Internal Server Error", PAGE=*, FAIL=FOUND, ID="Internal server error found", ActionOnFail=STOP, Search_IN=BODY);
nsl_web_find(TEXT="Unauthorized user access", PAGE=*, FAIL=FOUND, ID="Invalid Token", ActionOnFail=STOP);
nsl_web_find(TEXT="getBy", PAGE=Fulfillment_offerings_v1_MEMBER, FAIL=NOTFOUND, ID="GetBy not found", ActionOnFail=STOP);
nsl_web_find(TEXT="\"error\":{\"message\":\"Internal Server Error\",\"httpStatus\":500", PAGE=Get_Checkout_Previews_V3_QRY_MEMBER, SaveCount=CP_Qry_5xx_count, Search_IN=BODY);

//----------------------------------LOGGING IN A FILE--------------------
nsl_decl_var(CP_Qry_5xx_count,DefaultValue="0",RETAINPREVALUE="NO");
nsl_search_var(traceid, PAGE=*, LB="X-B3-TraceId: ", RB="\n", LBMATCH=FIRST, SaveOffset=0, Search=ALL, RETAINPREVALUE="NO", EncodeMode=None);
nsl_search_var(server_date_sp, PAGE=*, LB="date: ", RB="\n", LBMATCH=FIRST, SaveOffset=0, Search=Header, RETAINPREVALUE="NO", EncodeMode=None);
nsl_search_var(x_swift_savetime_sp, PAGE=*, LB="x-swift-savetime: ", RB="\n", LBMATCH=FIRST, SaveOffset=0, Search=Header, RETAINPREVALUE="NO", EncodeMode=None);
nsl_search_var(x_nike_zhenghe_timing_ms_sp, PAGE=*, LB="x-nike-zhenghe-timing-ms: ", RB="\n", LBMATCH=FIRST, SaveOffset=0, Search=Header, RETAINPREVALUE="NO", EncodeMode=None);
nsl_search_var(ali_swift_global_savetime_sp, PAGE=*, LB="ali-swift-global-savetime: ", RB="\n", LBMATCH=FIRST, SaveOffset=0, Search=Header, RETAINPREVALUE="NO", EncodeMode=None);
//nsl_web_find(TEXT="IN_PROGRESS", PAGE=*, SaveCount=CP_Qry_5xx_count, Search_IN=BODY);
//nsl_search_var(ETA_SEC_SP, PAGE=Put_Checkout_Previews_V3_CMD_MEMBER, PAGE=Get_Checkout_Previews_V3_QRY_MEMBER, LB="\"eta\":", RB=",\"links\"", LBMATCH=FIRST, ORD=1, SaveLen=0, ActionOnNotFound=Error, Search=Body, RETAINPREVALUE="NO", EncodeMode=All);
