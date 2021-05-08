## complete_path_1
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart
     

## complete_path_2
* greet
    - utter_greet
* deny
    - utter_goodbye
    - action_restart

## complete_path_3
* goodbye
    - utter_goodbye
    - action_restart

## complete_path_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## complete_path_5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart

## complete_path_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## complete_path_7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart


## complete_path_8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_9
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_10
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_12
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_13
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}  
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_14
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}   
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_15
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}    
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_16
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}  
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_17
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}   
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_18
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}   
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_19
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}    
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_20
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}  
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_21
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}   
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_22
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"} 
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_23
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}    
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_24
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}  
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_25
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}   
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_26
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}   
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_27
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}  
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_28
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}  
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_29
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"} 
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_30
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}   
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_31
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}   
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_32
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}    
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_33
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}  
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_34
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"} 
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_35
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}   
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_36
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"} 
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_37
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}  
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_38
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_39
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}  
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_40
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}  
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_41
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"} 
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_42
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"} 
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_43
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}  
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_44
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_45
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"} 
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_46
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}   
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_47
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}   
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_48
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}   
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_49
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}    
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_50
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}   
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     
## complete_path_51
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}   
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_52
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}   
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_53
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}   
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_54
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}    
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_55
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}   
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_56
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}   
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

     

## complete_path_57
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}   
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_58
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}   
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_59
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}   
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_60
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}    
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_61
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}   
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_62
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}   
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_63
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}    
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_64
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}    
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_65
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}   
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_66
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"} 
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_67
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}  
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_68
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}   
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_69
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"} 
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_70
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}   
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_71
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}   
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_72
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}  
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_73
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}    
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart

## complete_path_74
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}   
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_75
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}   
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_76
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}  
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_77
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}   
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_78
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"} 
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_79
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_80
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_81
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_82
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_83
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_84
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_85
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_86
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_87
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_88
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_89
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_90
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}    
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_91
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}   
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## complete_path_92
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}   
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart
     

## complete_path_93
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"} 
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart

## location specified 1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"} 
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## location specified 2
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"} 
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## cuisine specified 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## cuisine specified 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"} 
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## budget specified 1
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}   
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
*  restaurant_search{"cuisine": "North India"}
    - slot{"cuisine": "North India"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## budget specified 2
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}   
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
*  restaurant_search{"cuisine": "North India"}
    - slot{"cuisine": "North India"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart
     

## happy_path_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "bangalore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart

## happy_path_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "delhi"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true} 
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "delhi"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true} 
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai", "budget": "high"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"budget": "high"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai", "budget": "high"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - slot{"budget": "high"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "mumbai", "budget": "mid"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - slot{"budget": "mid"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart

## happy_path_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "bangalore", "budget": "high"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "bangalore"}
    - slot{"budget": "high"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "bangalore", "budget": "high"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "bangalore"}
    - slot{"budget": "high"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path_6
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "bangalore", "budget": "low"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "bangalore"}
    - slot{"budget": "low"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart


## happy_path_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi", "budget": "low"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "delhi"}
    - slot{"budget": "low"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi", "budget": "low"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "delhi"}
    - slot{"budget": "low"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "kolkatta", "budget": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkatta"}
    - slot{"budget": "high"}
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## happy_path_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "kolkatta", "budget": "high"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkatta"}
    - slot{"budget": "high"}
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path_1
* greet
    - utter_greet
* restaurant_search{"location": "nasik"}
    - slot{"location": "nasik"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path_1
* greet
    - utter_greet
* restaurant_search{"location": "nasik"}
    - slot{"location": "nasik"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path_2
* greet
    - utter_greet
* restaurant_search{"location": "nasik"}
    - slot{"location": "nasik"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart

## loc_path_3
* greet
    - utter_greet
* restaurant_search{"location": "mohali"}
    - slot{"location": "mohali"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - verify_location
    - slot{"location": "chennai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart

## loc_path_4
* greet
    - utter_greet
* restaurant_search{"location": "mohali"}
    - slot{"location": "mohali"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path_4
* greet
    - utter_greet
* restaurant_search{"location": "mohali"}
    - slot{"location": "mohali"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path_3
* greet
    - utter_greet
* restaurant_search{"location": "secunderabad"}
    - slot{"location": "secunderabad"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
*  restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart

## loc_path_5
* greet
    - utter_greet
* restaurant_search{"location": "secunderabad"}
    - slot{"location": "secunderabad"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path_5
* greet
    - utter_greet
* restaurant_search{"location": "secunderabad"}
    - slot{"location": "secunderabad"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path_6
* greet
    - utter_greet
* restaurant_search{"location": "panchkula"}
    - slot{"location": "panchkula"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - verify_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
*  restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart

## loc_path_5
* greet
    - utter_greet
* restaurant_search{"location": "panchkula"}
    - slot{"location": "panchkula"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path_5
* greet
    - utter_greet
* restaurant_search{"location": "panchkula"}
    - slot{"location": "panchkula"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path
* greet
    - utter_greet
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "kolkatta"}
    - slot{"location": "kolkatta"}
    - verify_location
    - slot{"location": "kolkatta"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path
* greet
    - utter_greet
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path
* greet
    - utter_greet
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - verify_location
    - slot{"location": "mumbai"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart


## loc_path
* greet
    - utter_greet
* restaurant_search{"location": "xyza"}
    - slot{"location": "xyza"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path
* greet
    - utter_greet
* restaurant_search{"location": "xyza"}
    - slot{"location": "xyza"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path
* greet
    - utter_greet
* restaurant_search{"location": "xyza"}
    - slot{"location": "xyza"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart

## loc_path
* greet
    - utter_greet
* restaurant_search{"location": "bluru"}
    - slot{"location": "bluru"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* affirm
    - utter_ask_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path
* greet
    - utter_greet
* restaurant_search{"location": "bluru"}
    - slot{"location": "bluru"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
*  restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* email_confirm
    - action_send_email
    - utter_goodbye
    - action_restart

## loc_path
* greet
    - utter_greet
* restaurant_search{"location": "bluru"}
    - slot{"location": "bluru"}
    - verify_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - verify_location
    - slot{"location": "bangalore"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - utter_require_email
* deny
    - utter_goodbye
    - action_restart