
COLUMNS_RENAME = {
    'participant_ID_1': 'participant_id',
    'age_1': 'age',
    'gender_1': 'gender',
    'Room': 'room',
    'Study_programme_1': 'study_programme',
    'freq_1': 'use_frequency_q',
    'Expert_1': 'expertise_level_q',
    'subscr_1': 'premium_subscription_q',
    'Abonnement_1': 'which_suscriptions_q',
    'subj_knowl_1': 'entrepreneurship_self_knowledge_q',
    'subj_knowl_2': 'entrepreneurship_friends_q',
    'subj_knowl_3': 'entrepreneurship_feel_q',
    'subj_knowl_4': 'entrepreneurship_compared_q',
    'pre_humanness_1': 'perception_pleasant_q',
    'pre_humanness_2': 'perception_capable_q',
    'pre_humanness_3': 'perception_attentive_q',
    'pre_humanness_4': 'perception_polite_q',
    'pre_humanness_5': 'perception_responsive_q',
    'pre_humanness_6': 'perception_stimulating_q',
    'PANAVA_1': 'panava_satisfaction_q',
    'PANAVA_2': 'panava_energy_q',
    'PANAVA_3': 'panava_stress_q',
    'PANAVA_4': 'panava_tiredness_q',
    'PANAVA_5': 'panava_peacefulness_q',
    'PANAVA_6': 'panava_happiness_q',
    'PANAVA_7': 'panava_motivation_q',
    'PANAVA_8': 'panava_nervousness_q',
    'PANAVA_9': 'panava_boringness_q',
    'PANAVA_10': 'panava_worryness_q',
    'MC_humannessIndex_1': 'humanness_artificial_q',
    'MC_humannessIndex_2': 'humanness_made_by_humans_q',
    'MC_humannessIndex_3': 'humanness_no_moral_consciousness_q',
    'MC_humannessIndex_4': 'humanness_no_lifespan_q',
    'MC_humannessIndex_5': 'humanness_sexless_q',
    'MC_humannessIndex_6': 'humanness_automatically_q',
    'MC_humannessIndex_7': 'humanness_lifeless_q',
    'MC_humannessIndex_8': 'humanness_mechanical_q',
    'MC_humannessIndex_9': 'humanness_synthetic_q',
    'MC_eerinessIndex_1': 'feelings_calmness_q',
    'MC_eerinessIndex_2': 'feelings_creepiness_q',
    'MC_eerinessIndex_3': 'feelings_naturalness_q',
    'MC_eerinessIndex_4': 'feelings_scaryness_q',
    'MC_eerinessIndex_5': 'feelings_goosebumps_q',
    'MC_eerinessIndex_6': 'feelings_inspirational_q',
    'MC_eerinessIndex_7': 'feelings_excitement_q',
    'MC_eerinessIndex_8': 'feelings_shock_q',
    'MC_attractivenessIndex_1': 'feelings_obtrusive_q',
    'MC_attractivenessIndex_2': 'feelings_complexity_q',
    'MC_attractivenessIndex_3': 'feelings_spectacular_q',
    'MC_attractivenessIndex_4': 'feelings_breathtaking_q',
    'MC_attractivenessIndex_5': 'feelings_striking_q',
    'MC_attractivenessIndex_6': 'feelings_elegance_q',
    'MC_attractivenessIndex_7': 'feelings_attractiveness_q',
    'MC_attractivenessIndex_8': 'feelings_pleasing_q',
    'MC_attractivenessIndex_9': 'feelings_niceness_q',
    'MC_attractivenessIndex_10': 'feelings_organized_q',
    'MC_attractivenessIndex_11': 'feelings_stilish_q',
    'MC_Social_presence_1': 'behavior_human_contact_q',
    'MC_Social_presence_2': 'behavior_personal_touch_q',
    'MC_Social_presence_3': 'behavior_sociability_q',
    'MC_Social_presence_4': 'behavior_warmth_q',
    'MC_Social_presence_5': 'behavior_sensitivity_q',
    'attention_check_1': 'attention_check_q',
    'post_Engagement_1': 'engagement_time_flies_q',
    'post_Engagement_2': 'engagement_immersed_q',
    'post_Engagement_3': 'engagement_frustrated_q',
    'post_Engagement_4': 'engagement_confused_q',
    'post_Engagement_5': 'engagement_exhausted_q',
    'post_Engagement_6': 'engagement_attracted_q',
    'post_Engagement_7': 'engagement_aesthetic_q',
    'post_Engagement_8': 'engagement_appealing_q',
    'post_Engagement_9': 'engagement_worthwhile_q',
    'post_Engagement_10': 'engagement_rewarding_q',
    'post_Engagement_11': 'engagement_interesting_q',
    'Post_Trust_1': 'beliefs_negative_consequences_q',
    'Post_Trust_2': 'beliefs_careful_q',
    'Post_Trust_3': 'beliefs_risky_q',
    'Post_Trust_4': 'beliefs_act_in_my_best_interest_q',
    'Post_Trust_5': 'beliefs_help_me_q',
    'Post_Trust_6': 'beliefs_understands_me_q',
    'Post_Trust_7': 'beliefs_competent_q',
    'Post_Trust_8': 'beliefs_fulfills_its_role_q',
    'Post_Trust_9': 'beliefs_can_rely_on_q',
    'Post_Trust_10': 'beliefs_can_trust_information_q',
}

ATTENTION_CHECK_WEIGHTING = {
    1: 0.5,
    2: 0.65,
    3: 0.75,
    4: 0.85,
    5: 1.0
}

ENGAGEMENT_SURVEY_COLUMNS = [
    'engagement_time_flies_q', 'engagement_immersed_q', 'engagement_frustrated_q',
    'engagement_confused_q', 'engagement_exhausted_q', 'engagement_attracted_q',
    'engagement_aesthetic_q', 'engagement_appealing_q', 'engagement_worthwhile_q',
    'engagement_rewarding_q', 'engagement_interesting_q'
]

ENGAGEMENT_SURVEY_COLUMNS_REMAP = {
    'engagement_frustrated_q': {1:5, 2:4, 3:3, 4:2, 5:1},
    'engagement_confused_q': {1:5, 2:4, 3:3, 4:2, 5:1},
    'engagement_exhausted_q': {1:5, 2:4, 3:3, 4:2, 5:1},
}

BINS = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0]

QUESTIONS_GROUPS = {
    # Individually (not grouped): 'premium_subscription_q', 'which_suscriptions_q', 'attention_check_q'
    'usage_experience': [
        'use_frequency_q', 'expertise_level_q'
    ],
    'perception': [
        'perception_pleasant_q', 'perception_capable_q', 'perception_attentive_q',
        'perception_polite_q', 'perception_responsive_q', 'perception_stimulating_q'
    ],
    'entrepreneurship_knowledge': [
        'entrepreneurship_self_knowledge_q', 'entrepreneurship_friends_q',
        'entrepreneurship_compared_q', 'entrepreneurship_feel_q'
    ],
    'affective_state': [
        'panava_satisfaction_q', 'panava_energy_q', 'panava_stress_q', 'panava_tiredness_q',
        'panava_peacefulness_q', 'panava_happiness_q', 'panava_motivation_q',
        'panava_nervousness_q', 'panava_boringness_q', 'panava_worryness_q'
    ],
    'humanness_perception': [
        'humanness_artificial_q', 'humanness_made_by_humans_q', 'humanness_no_moral_consciousness_q',
        'humanness_no_lifespan_q', 'humanness_sexless_q', 'humanness_automatically_q',
        'humanness_lifeless_q', 'humanness_mechanical_q', 'humanness_synthetic_q'
    ],
    'feelings': [
        'feelings_calmness_q', 'feelings_creepiness_q', 'feelings_naturalness_q',
        'feelings_scaryness_q', 'feelings_goosebumps_q', 'feelings_inspirational_q',
        'feelings_excitement_q', 'feelings_shock_q', 'feelings_obtrusive_q',
        'feelings_complexity_q', 'feelings_spectacular_q', 'feelings_breathtaking_q',
        'feelings_striking_q', 'feelings_elegance_q', 'feelings_attractiveness_q',
        'feelings_pleasing_q', 'feelings_niceness_q', 'feelings_organized_q',
        'feelings_stilish_q'
    ],
    'behavioral_perception': [
        'behavior_human_contact_q', 'behavior_personal_touch_q', 'behavior_sociability_q',
        'behavior_warmth_q', 'behavior_sensitivity_q'
    ],
    'beliefs_trust_risk': [
        'beliefs_negative_consequences_q', 'beliefs_careful_q', 'beliefs_risky_q',
        'beliefs_act_in_my_best_interest_q', 'beliefs_help_me_q', 'beliefs_understands_me_q',
        'beliefs_competent_q', 'beliefs_fulfills_its_role_q', 'beliefs_can_rely_on_q',
        'beliefs_can_trust_information_q'
    ]
}


COLUMNS_DECODER = {
    # Page 3
    'use_frequency_q': {
        'question': 'How often do you use generative AI tools?',
        'answers': {
            1: 'Never',
            2: 'Rarely',
            3: 'A few times a month',
            4: 'A few times a week',
            5: 'Daily'
        }
    },
    'expertise_level_q': {
        'question': 'How do you rate your expertise in the field of artificial intelligence?',
        'answers': {
            1: 'Extremely low',
            2: 'Low',
            3: 'Medium',
            4: 'High',
            5: 'Extremely high'
        }
    },
    'premium_subscription_q': {
        'question': 'Do you currently have a premium subscription to any digital assistant (e.g. ChatGPT, Gemini, Copilot, etc.)?',
        'answers': {
            1: 'No',
            2: 'No, but I had one',
            3: 'Yes'
        }
    },
    'which_suscriptions_q': {
        'question': 'Which digital assistant do you currently have a premium subscription for?',
        'answers': ''
    },
    # Page 4
    'perception_pleasant_q': {
        'question': 'I perceive digital assistants as pleasant',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'perception_capable_q': {
        'question': 'I perceive digital assistants as capable',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'perception_attentive_q': {
        'question': 'I perceive digital assistants as attentive',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'perception_polite_q': {
        'question': 'I perceive digital assistants as polite',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'perception_responsive_q': {
        'question': 'I perceive digital assistants as responsive',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'perception_stimulating_q': {
        'question': 'I perceive digital assistants as stimulating',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    # Page 5
    'entrepreneurship_self_knowledge_q': {
        'question': 'I know quite a lot about entrepreneurship',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'entrepreneurship_friends_q': {
        'question': 'In my circle of friends I am one of the "experts" for entrepreneurship',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'entrepreneurship_feel_q': {
        'question': 'I don\'t feel very knowledgeable about entrepreneurship',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'entrepreneurship_compared_q': {
        'question': 'Compared to most other people, I know less about entrepreneurship',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    # Page 17
    'panava_satisfaction_q': {
        'question': 'I feel satisfied at the moment',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'panava_energy_q': {
        'question': 'I feel energetic at the moment',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'panava_stress_q': {
        'question': 'I feel stressed at the moment',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'panava_tiredness_q': {
        'question': 'I feel tired at the moment',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'panava_peacefulness_q': {
        'question': 'I feel peaceful at the moment',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'panava_happiness_q': {
        'question': 'I feel happy at the moment',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'panava_motivation_q': {
        'question': 'I feel motivated at the moment',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'panava_nervousness_q': {
        'question': 'I feel nervous at the moment',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'panava_boringness_q': {
        'question': 'I feel bored at the moment',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'panava_worryness_q': {
        'question': 'I feel worried at the moment',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    # Page 18
    'humanness_artificial_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as artificial?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'humanness_made_by_humans_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as made by humans?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'humanness_no_moral_consciousness_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as having no moral consciousness?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'humanness_no_lifespan_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as having no lifespan?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'humanness_sexless_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as sexless?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'humanness_automatically_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as automatically functioning?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'humanness_lifeless_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as lifeless?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'humanness_mechanical_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as mechanical?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'humanness_synthetic_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as synthetic?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    # Page 20
    'feelings_calmness_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as calm?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_creepiness_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as creepy?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_naturalness_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as natural?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_scaryness_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as scary?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_goosebumps_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as giving you goosebumps?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_inspirational_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as inspirational?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_excitement_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as exciting?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_shock_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as shocking?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    # Page 20
    'feelings_obtrusive_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as obtrusive?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_complexity_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as complex?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_spectacular_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as spectacular?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_breathtaking_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as breathtaking?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_striking_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as striking?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_elegance_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as elegant?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_attractiveness_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as attractive?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_pleasing_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as pleasing?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_niceness_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as nice?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_organized_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as organized?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'feelings_stilish_q': {
        'question': 'To what extent did you perceive the digital assistant you just interacted with as stylish?',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    # Page 21
    'behavior_human_contact_q': {
        'question': 'I felt a human contact with the digital assistant',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'behavior_personal_touch_q': {
        'question': 'I felt a personal touch with the digital assistant',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'behavior_sociability_q': {
        'question': 'I felt sociable with the digital assistant',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'behavior_warmth_q': {
        'question': 'I felt a human warmth with the digital assistant',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'behavior_sensitivity_q': {
        'question': 'I felt a human sensitivity with the digital assistant',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'attention_check_q': {
        'question': 'How carefully did you read the questions from 1 to 5?',
        'answers': {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five'
        }
    },
    # Page 22
    'engagement_time_flies_q': {
        'question': 'The time I spent with the digital assistant flew by',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'engagement_immersed_q': {
        'question': 'I was completely immersed in the interaction with the digital assistant',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'engagement_frustrated_q': {
        'question': 'I felt frustrated during the interaction with the digital assistant',
        'answers': {
            5: 'Strongly disagree',
            4: 'Disagree',
            3: 'Neutral',
            2: 'Agree',
            1: 'Strongly agree'
        }
    },
    'engagement_confused_q': {
        'question': 'I felt confused during the interaction with the digital assistant',
        'answers': {
            5: 'Strongly disagree',
            4: 'Disagree',
            3: 'Neutral',
            2: 'Agree',
            1: 'Strongly agree'
        }
    },
    'engagement_exhausted_q': {
        'question': 'I felt exhausted during the interaction with the digital assistant',
        'answers': {
            5: 'Strongly disagree',
            4: 'Disagree',
            3: 'Neutral',
            2: 'Agree',
            1: 'Strongly agree'
        }
    },
    'engagement_attracted_q': {
        'question': 'The digital assistant was attractive to me',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'engagement_aesthetic_q': {
        'question': 'The digital assistant was aesthetically pleasing to me',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'engagement_appealing_q': {
        'question': 'The digital assistant appealed to my senses',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'engagement_worthwhile_q': {
        'question': 'The interaction with the digital assistant was worthwhile for me',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'engagement_rewarding_q': {
        'question': 'The interaction with the digital assistant was rewarding for me',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'engagement_interesting_q': {
        'question': 'The interaction with the digital assistant was interesting for me',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    # Page 23
    'beliefs_negative_consequences_q': {
        'question': 'I believe that using the digital assistant could have negative consequences',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'beliefs_careful_q': {
        'question': 'I feel like I need to be careful when using the digital assistant.',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'beliefs_risky_q': {
        'question': 'I feel like using the digital assistant is risky.',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'beliefs_act_in_my_best_interest_q': {
        'question': 'I believe that the digital assistant will act in my best interest.',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'beliefs_help_me_q': {
        'question': 'I believe that the digital assistant will do its best to help me if I need support.',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'beliefs_understands_me_q': {
        'question': 'I believe that the digital assistant is interested in understanding my needs and preferences.',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'beliefs_competent_q': {
        'question': 'I believe that the digital assistant is competent and effective in assisting me with the task at hand.',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'beliefs_fulfills_its_role_q': {
        'question': 'I believe that the digital assistant fulfills its role very well.',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'beliefs_can_rely_on_q': {
        'question': 'I believe I can rely on the digital assistant completely.',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    },
    'beliefs_can_trust_information_q': {
        'question': 'I believe I can trust the information provided by the digital assistant.',
        'answers': {
            1: 'Strongly disagree',
            2: 'Disagree',
            3: 'Neutral',
            4: 'Agree',
            5: 'Strongly agree'
        }
    }
}
