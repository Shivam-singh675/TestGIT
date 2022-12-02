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
extern FlowReturn Fulfilment_offerings();
extern FlowReturn Checkout_preview_CMD();
extern FlowReturn Checkout_Preview_QRY();
// End - List of used flows in the runlogic


void SimpleRL()
{
    NSDL2_RUNLOGIC(NULL, NULL, "Executing init_script()");

    init_script();

    NSDL2_RUNLOGIC(NULL, NULL, "Executing sequence block - Start");
    {
        UPDATE_USER_FLOW_COUNT(0)
        NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - Fulfilment_offerings");
        UPDATE_USER_FLOW_COUNT(1)
        Fulfilment_offerings();
        NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - Checkout_preview_CMD");
        UPDATE_USER_FLOW_COUNT(3)
        Checkout_preview_CMD();
        NSDL2_RUNLOGIC(NULL, NULL, "Executing flow - Checkout_Preview_QRY");
        UPDATE_USER_FLOW_COUNT(5)
        Checkout_Preview_QRY();
    }

    NSDL2_RUNLOGIC(NULL, NULL, "Executing ns_exit_session()");
    ns_exit_session();
}
