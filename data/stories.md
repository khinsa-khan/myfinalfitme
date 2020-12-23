## happy path

* greet
  - utter_greet
* mood_great
  - utter_newdress

## new dress path11

* greet
  - utter_greet
* new_dress
  - utter_newdress
* affirm
  - utter_know
  - size_form
  - form{"name": "size_form"}
  - form{"name": null}  
  - utter_ask_clothtype
* clothtype{"clothtype_value":"formal"}
  - utter_ask_patterns
* patterns{"patterns_value":"floral"}
  - utter_ask_fittings
* fittings{"fittings_value":"loose"}
  - action_tag_types1
  - utter_did_that_help
* affirm
  - utter_happy

## new dress path22

* greet
  - utter_greet
* new_dress
  - utter_newdress
* affirm
  - utter_know
  - size_form
  - form{"name": "size_form"}
  - form{"name": null}  
  - utter_ask_clothtype
* clothtype{"clothtype_value":"formal"}
  - utter_ask_patterns
* patterns{"patterns_value":"plain"}
  - utter_ask_fittings
* fittings{"fittings_value":"loose"}
  - action_tag_types1
  - utter_did_that_help
* affirm
  - utter_happy

## new dress path33

* greet
  - utter_greet
* new_dress
  - utter_newdress
* affirm
  - utter_know
  - size_form
  - form{"name": "size_form"}
  - form{"name": null}  
  - utter_ask_clothtype
* clothtype{"clothtype_value":"formal"}
  - utter_ask_patterns
* patterns{"patterns_value":"floral"}
  - utter_ask_fittings
* fittings{"fittings_value":"slim"}
  - action_tag_types1
  - utter_did_that_help
* affirm
  - utter_happy

## new dress path44

* greet
  - utter_greet
* new_dress
  - utter_newdress
* affirm
  - utter_know
  - size_form
  - form{"name": "size_form"}
  - form{"name": null}  
  - utter_ask_clothtype
* clothtype{"clothtype_value":"formal"}
  - utter_ask_patterns
* patterns{"patterns_value":"plain"}
  - utter_ask_fittings
* fittings{"fittings_value":"slim"}
  - action_tag_types1
  - utter_did_that_help
* affirm
  - utter_happy

## new dress path55

* greet
  - utter_greet
* new_dress
  - utter_newdress
* affirm
  - utter_know
  - size_form
  - form{"name": "size_form"}
  - form{"name": null}  
  - utter_ask_clothtype
* clothtype{"clothtype_value":"casual"}
  - utter_ask_patterns
* patterns{"patterns_value":"floral"}
  - utter_ask_fittings
* fittings{"fittings_value":"loose"}
  - action_tag_types1
  - utter_did_that_help
* affirm
  - utter_happy

## new dress path66

* greet
  - utter_greet
* new_dress
  - utter_newdress
* affirm
  - utter_know
  - size_form
  - form{"name": "size_form"}
  - form{"name": null}  
  - utter_ask_clothtype
* clothtype{"clothtype_value":"casual"}
  - utter_ask_patterns
* patterns{"patterns_value":"plain"}
  - utter_ask_fittings
* fittings{"fittings_value":"loose"}
  - action_tag_types1
  - utter_did_that_help
* affirm
  - utter_happy

## new dress path77

* greet
  - utter_greet
* new_dress
  - utter_newdress
* affirm
  - utter_know
  - size_form
  - form{"name": "size_form"}
  - form{"name": null}  
  - utter_ask_clothtype
* clothtype{"clothtype_value":"casual"}
  - utter_ask_patterns
* patterns{"patterns_value":"floral"}
  - utter_ask_fittings
* fittings{"fittings_value":"slim"}
  - action_tag_types1
  - utter_did_that_help
* affirm
  - utter_happy

## new dress path88

* greet
  - utter_greet
* new_dress
  - utter_newdress
* affirm
  - utter_know
  - size_form
  - form{"name": "size_form"}
  - form{"name": null}  
  - utter_ask_clothtype
* clothtype{"clothtype_value":"casual"}
  - utter_ask_patterns
* patterns{"patterns_value":"plain"}
  - utter_ask_fittings
* fittings{"fittings_value":"slim"}
  - action_tag_types1
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 1

* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2

* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye

* goodbye
  - utter_goodbye

## bot challenge

* bot_challenge
  - utter_iamabot
