#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ns_string.h"
#ifdef ENABLE_RUNLOGIC_PROGRESS
  #define UPDATE_USER_FLOW_COUNT(count) update_user_flow_count(count);
#else
  #define UPDATE_USER_FLOW_COUNT(count)
#endif


extern int init_script();
extern int exit_script();

typedef void FlowReturn;

// Note: Following extern declaration is used to find the list of used flows. Do not delete/edit it
// Start - List of used flows in the runlogic
extern FlowReturn Token();
extern FlowReturn Fulfilment_offerings();
extern FlowReturn Checkout_preview_CMD();
// End - List of used flows in the runlogic


void DoubleCMD()
{
    NSDL2_RUNLOGIC(NULL, NULL, "Executing init_script()");

    init_script();

    NSDL2_RUNLOGIC(NULL, NULL, "Executing sequence block - Start");
    {
        UPDATE_USER_FLOW_COUNT(0)
        NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - Token");
        UPDATE_USER_FLOW_COUNT(1)
        Token();
        NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - Fulfilment_offerings");
        UPDATE_USER_FLOW_COUNT(4)
        Fulfilment_offerings();

        NSDL2_RUNLOGIC(NULL, NULL, "Executing count block - CP_CMD. Min = 5, Max = 6");
        {
            UPDATE_USER_FLOW_COUNT(6)
            int CP_CMDCount = ns_get_random_number_int(5, 6);
            int CP_CMDLoop;
             for(CP_CMDLoop = 1; CP_CMDLoop <= CP_CMDCount; CP_CMDLoop++)
            {
                NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - Checkout_preview_CMD");
                UPDATE_USER_FLOW_COUNT(7)
                Checkout_preview_CMD();
            }
        }
    }

    NSDL2_RUNLOGIC(NULL, NULL, "Executing ns_exit_session()");
    ns_exit_session();
}
