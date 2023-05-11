from usaspending_api.common.data_classes import TransactionColumn

TRANSACTION_FPDS_COLUMN_INFO = [
    TransactionColumn("a_76_fair_act_action", "a_76_fair_act_action", "STRING"),
    TransactionColumn("a_76_fair_act_action_desc", "a_76_fair_act_action_desc", "STRING"),
    TransactionColumn("action_date", "action_date", "STRING", "string_datetime_remove_timestamp"),
    TransactionColumn("action_type", "action_type", "STRING"),
    TransactionColumn("action_type_description", "action_type_description", "STRING"),
    TransactionColumn("agency_id", "agency_id", "STRING"),
    TransactionColumn("airport_authority", "airport_authority", "BOOLEAN"),
    TransactionColumn("alaskan_native_owned_corpo", "alaskan_native_owned_corpo", "BOOLEAN"),
    TransactionColumn("alaskan_native_servicing_i", "alaskan_native_servicing_i", "BOOLEAN"),
    TransactionColumn("american_indian_owned_busi", "american_indian_owned_busi", "BOOLEAN"),
    TransactionColumn("annual_revenue", "annual_revenue", "STRING"),
    TransactionColumn("asian_pacific_american_own", "asian_pacific_american_own", "BOOLEAN"),
    TransactionColumn("award_description", "award_description", "STRING"),
    TransactionColumn("award_modification_amendme", "award_modification_amendme", "STRING"),
    TransactionColumn("award_or_idv_flag", "award_or_idv_flag", "STRING"),
    TransactionColumn("awardee_or_recipient_legal", "awardee_or_recipient_legal", "STRING"),
    TransactionColumn("awardee_or_recipient_uei", "awardee_or_recipient_uei", "STRING"),
    TransactionColumn("awardee_or_recipient_uniqu", "awardee_or_recipient_uniqu", "STRING"),
    TransactionColumn("awarding_agency_code", "awarding_agency_code", "STRING"),
    TransactionColumn("awarding_agency_name", "awarding_agency_name", "STRING"),
    TransactionColumn("awarding_office_code", "awarding_office_code", "STRING"),
    TransactionColumn("awarding_office_name", "awarding_office_name", "STRING"),
    TransactionColumn("awarding_sub_tier_agency_c", "awarding_sub_tier_agency_c", "STRING"),
    TransactionColumn("awarding_sub_tier_agency_n", "awarding_sub_tier_agency_n", "STRING"),
    TransactionColumn("base_and_all_options_value", "base_and_all_options_value", "STRING"),
    TransactionColumn("base_exercised_options_val", "base_exercised_options_val", "STRING"),
    TransactionColumn("black_american_owned_busin", "black_american_owned_busin", "BOOLEAN"),
    TransactionColumn("c1862_land_grant_college", "c1862_land_grant_college", "BOOLEAN"),
    TransactionColumn("c1890_land_grant_college", "c1890_land_grant_college", "BOOLEAN"),
    TransactionColumn("c1994_land_grant_college", "c1994_land_grant_college", "BOOLEAN"),
    TransactionColumn("c8a_program_participant", "c8a_program_participant", "BOOLEAN"),
    TransactionColumn("cage_code", "cage_code", "STRING"),
    TransactionColumn("city_local_government", "city_local_government", "BOOLEAN"),
    TransactionColumn("clinger_cohen_act_pla_desc", "clinger_cohen_act_pla_desc", "STRING"),
    TransactionColumn("clinger_cohen_act_planning", "clinger_cohen_act_planning", "STRING"),
    TransactionColumn("commercial_item_acqui_desc", "commercial_item_acqui_desc", "STRING"),
    TransactionColumn("commercial_item_acquisitio", "commercial_item_acquisitio", "STRING"),
    TransactionColumn("commercial_item_test_desc", "commercial_item_test_desc", "STRING"),
    TransactionColumn("commercial_item_test_progr", "commercial_item_test_progr", "STRING"),
    TransactionColumn("community_developed_corpor", "community_developed_corpor", "BOOLEAN"),
    TransactionColumn("community_development_corp", "community_development_corp", "BOOLEAN"),
    TransactionColumn("consolidated_contract", "consolidated_contract", "STRING"),
    TransactionColumn("consolidated_contract_desc", "consolidated_contract_desc", "STRING"),
    TransactionColumn("construction_wage_rat_desc", "construction_wage_rat_desc", "STRING"),
    TransactionColumn("construction_wage_rate_req", "construction_wage_rate_req", "STRING"),
    TransactionColumn("contingency_humanitar_desc", "contingency_humanitar_desc", "STRING"),
    TransactionColumn("contingency_humanitarian_o", "contingency_humanitarian_o", "STRING"),
    TransactionColumn("contract_award_type", "contract_award_type", "STRING"),
    TransactionColumn("contract_award_type_desc", "contract_award_type_desc", "STRING"),
    TransactionColumn("contract_bundling", "contract_bundling", "STRING"),
    TransactionColumn("contract_bundling_descrip", "contract_bundling_descrip", "STRING"),
    TransactionColumn("contract_financing", "contract_financing", "STRING"),
    TransactionColumn("contract_financing_descrip", "contract_financing_descrip", "STRING"),
    TransactionColumn("contracting_officers_desc", "contracting_officers_desc", "STRING"),
    TransactionColumn("contracting_officers_deter", "contracting_officers_deter", "STRING"),
    TransactionColumn("contracts", "contracts", "BOOLEAN"),
    TransactionColumn("corporate_entity_not_tax_e", "corporate_entity_not_tax_e", "BOOLEAN"),
    TransactionColumn("corporate_entity_tax_exemp", "corporate_entity_tax_exemp", "BOOLEAN"),
    TransactionColumn("cost_accounting_stand_desc", "cost_accounting_stand_desc", "STRING"),
    TransactionColumn("cost_accounting_standards", "cost_accounting_standards", "STRING"),
    TransactionColumn("cost_or_pricing_data", "cost_or_pricing_data", "STRING"),
    TransactionColumn("cost_or_pricing_data_desc", "cost_or_pricing_data_desc", "STRING"),
    TransactionColumn("council_of_governments", "council_of_governments", "BOOLEAN"),
    TransactionColumn("country_of_product_or_desc", "country_of_product_or_desc", "STRING"),
    TransactionColumn("country_of_product_or_serv", "country_of_product_or_serv", "STRING"),
    TransactionColumn("county_local_government", "county_local_government", "BOOLEAN"),
    TransactionColumn("created_at", "created_at", "TIMESTAMP"),
    TransactionColumn("current_total_value_award", "current_total_value_award", "STRING"),
    TransactionColumn("detached_award_proc_unique", "detached_award_proc_unique", "STRING"),
    TransactionColumn("detached_award_procurement_id", "detached_award_procurement_id", "INTEGER"),
    TransactionColumn("division_name", "division_name", "STRING"),
    TransactionColumn("division_number_or_office", "division_number_or_office", "STRING"),
    TransactionColumn("dod_claimant_prog_cod_desc", "dod_claimant_prog_cod_desc", "STRING"),
    TransactionColumn("dod_claimant_program_code", "dod_claimant_program_code", "STRING"),
    TransactionColumn("domestic_or_foreign_e_desc", "domestic_or_foreign_e_desc", "STRING"),
    TransactionColumn("domestic_or_foreign_entity", "domestic_or_foreign_entity", "STRING"),
    TransactionColumn("domestic_shelter", "domestic_shelter", "BOOLEAN"),
    TransactionColumn("dot_certified_disadvantage", "dot_certified_disadvantage", "BOOLEAN"),
    TransactionColumn("economically_disadvantaged", "economically_disadvantaged", "BOOLEAN"),
    TransactionColumn("educational_institution", "educational_institution", "BOOLEAN"),
    TransactionColumn("emerging_small_business", "emerging_small_business", "BOOLEAN"),
    TransactionColumn("entity_data_source", "entity_data_source", "STRING"),
    TransactionColumn("epa_designated_produc_desc", "epa_designated_produc_desc", "STRING"),
    TransactionColumn("epa_designated_product", "epa_designated_product", "STRING"),
    TransactionColumn("evaluated_preference", "evaluated_preference", "STRING"),
    TransactionColumn("evaluated_preference_desc", "evaluated_preference_desc", "STRING"),
    TransactionColumn("extent_compete_description", "extent_compete_description", "STRING"),
    TransactionColumn("extent_competed", "extent_competed", "STRING"),
    TransactionColumn("fair_opportunity_limi_desc", "fair_opportunity_limi_desc", "STRING"),
    TransactionColumn("fair_opportunity_limited_s", "fair_opportunity_limited_s", "STRING"),
    TransactionColumn("fed_biz_opps", "fed_biz_opps", "STRING"),
    TransactionColumn("fed_biz_opps_description", "fed_biz_opps_description", "STRING"),
    TransactionColumn("federal_action_obligation", "federal_action_obligation", "NUMERIC(23,2)"),
    TransactionColumn("federal_agency", "federal_agency", "BOOLEAN"),
    TransactionColumn("federally_funded_research", "federally_funded_research", "BOOLEAN"),
    TransactionColumn("for_profit_organization", "for_profit_organization", "BOOLEAN"),
    TransactionColumn("foreign_funding", "foreign_funding", "STRING"),
    TransactionColumn("foreign_funding_desc", "foreign_funding_desc", "STRING"),
    TransactionColumn("foreign_government", "foreign_government", "BOOLEAN"),
    TransactionColumn("foreign_owned_and_located", "foreign_owned_and_located", "BOOLEAN"),
    TransactionColumn("foundation", "foundation", "BOOLEAN"),
    TransactionColumn("funding_agency_code", "funding_agency_code", "STRING"),
    TransactionColumn("funding_agency_name", "funding_agency_name", "STRING"),
    TransactionColumn("funding_office_code", "funding_office_code", "STRING"),
    TransactionColumn("funding_office_name", "funding_office_name", "STRING"),
    TransactionColumn("funding_sub_tier_agency_co", "funding_sub_tier_agency_co", "STRING"),
    TransactionColumn("funding_sub_tier_agency_na", "funding_sub_tier_agency_na", "STRING"),
    TransactionColumn("government_furnished_desc", "government_furnished_desc", "STRING"),
    TransactionColumn("government_furnished_prope", "government_furnished_prope", "STRING"),
    TransactionColumn("grants", "grants", "BOOLEAN"),
    TransactionColumn("hispanic_american_owned_bu", "hispanic_american_owned_bu", "BOOLEAN"),
    TransactionColumn("hispanic_servicing_institu", "hispanic_servicing_institu", "BOOLEAN"),
    TransactionColumn("historically_black_college", "historically_black_college", "BOOLEAN"),
    TransactionColumn("historically_underutilized", "historically_underutilized", "BOOLEAN"),
    TransactionColumn("hospital_flag", "hospital_flag", "BOOLEAN"),
    TransactionColumn("housing_authorities_public", "housing_authorities_public", "BOOLEAN"),
    TransactionColumn("idv_type", "idv_type", "STRING"),
    TransactionColumn("idv_type_description", "idv_type_description", "STRING"),
    TransactionColumn("indian_tribe_federally_rec", "indian_tribe_federally_rec", "BOOLEAN"),
    TransactionColumn("information_technolog_desc", "information_technolog_desc", "STRING"),
    TransactionColumn("information_technology_com", "information_technology_com", "STRING"),
    TransactionColumn("inherently_government_desc", "inherently_government_desc", "STRING"),
    TransactionColumn("inherently_government_func", "inherently_government_func", "STRING"),
    TransactionColumn("initial_report_date", "initial_report_date", "STRING", "string_datetime_remove_timestamp"),
    TransactionColumn("inter_municipal_local_gove", "inter_municipal_local_gove", "BOOLEAN"),
    TransactionColumn("interagency_contract_desc", "interagency_contract_desc", "STRING"),
    TransactionColumn("interagency_contracting_au", "interagency_contracting_au", "STRING"),
    TransactionColumn("international_organization", "international_organization", "BOOLEAN"),
    TransactionColumn("interstate_entity", "interstate_entity", "BOOLEAN"),
    TransactionColumn("joint_venture_economically", "joint_venture_economically", "BOOLEAN"),
    TransactionColumn("joint_venture_women_owned", "joint_venture_women_owned", "BOOLEAN"),
    TransactionColumn("labor_standards", "labor_standards", "STRING"),
    TransactionColumn("labor_standards_descrip", "labor_standards_descrip", "STRING"),
    TransactionColumn("labor_surplus_area_firm", "labor_surplus_area_firm", "BOOLEAN"),
    TransactionColumn("last_modified", "last_modified", "STRING"),
    TransactionColumn("legal_entity_address_line1", "legal_entity_address_line1", "STRING"),
    TransactionColumn("legal_entity_address_line2", "legal_entity_address_line2", "STRING"),
    TransactionColumn("legal_entity_address_line3", "legal_entity_address_line3", "STRING"),
    TransactionColumn("legal_entity_city_name", "legal_entity_city_name", "STRING"),
    TransactionColumn("legal_entity_congressional", "legal_entity_congressional", "STRING"),
    TransactionColumn("legal_entity_country_code", "legal_entity_country_code", "STRING"),
    TransactionColumn("legal_entity_country_name", "legal_entity_country_name", "STRING"),
    TransactionColumn("legal_entity_county_code", "legal_entity_county_code", "STRING"),
    TransactionColumn("legal_entity_county_name", "legal_entity_county_name", "STRING"),
    TransactionColumn("legal_entity_state_code", "legal_entity_state_code", "STRING"),
    TransactionColumn("legal_entity_state_descrip", "legal_entity_state_descrip", "STRING"),
    TransactionColumn("legal_entity_zip4", "legal_entity_zip4", "STRING"),
    TransactionColumn("legal_entity_zip5", "legal_entity_zip5", "STRING"),
    TransactionColumn("legal_entity_zip_last4", "legal_entity_zip_last4", "STRING"),
    TransactionColumn("limited_liability_corporat", "limited_liability_corporat", "BOOLEAN"),
    TransactionColumn("local_area_set_aside", "local_area_set_aside", "STRING"),
    TransactionColumn("local_area_set_aside_desc", "local_area_set_aside_desc", "STRING"),
    TransactionColumn("local_government_owned", "local_government_owned", "BOOLEAN"),
    TransactionColumn("major_program", "major_program", "STRING"),
    TransactionColumn("manufacturer_of_goods", "manufacturer_of_goods", "BOOLEAN"),
    TransactionColumn("materials_supplies_article", "materials_supplies_article", "STRING"),
    TransactionColumn("materials_supplies_descrip", "materials_supplies_descrip", "STRING"),
    TransactionColumn("minority_institution", "minority_institution", "BOOLEAN"),
    TransactionColumn("minority_owned_business", "minority_owned_business", "BOOLEAN"),
    TransactionColumn("multi_year_contract", "multi_year_contract", "STRING"),
    TransactionColumn("multi_year_contract_desc", "multi_year_contract_desc", "STRING"),
    TransactionColumn("multiple_or_single_aw_desc", "multiple_or_single_aw_desc", "STRING"),
    TransactionColumn("multiple_or_single_award_i", "multiple_or_single_award_i", "STRING"),
    TransactionColumn("municipality_local_governm", "municipality_local_governm", "BOOLEAN"),
    TransactionColumn("naics", "naics", "STRING"),
    TransactionColumn("naics_description", "naics_description", "STRING"),
    TransactionColumn("national_interest_action", "national_interest_action", "STRING"),
    TransactionColumn("national_interest_desc", "national_interest_desc", "STRING"),
    TransactionColumn("native_american_owned_busi", "native_american_owned_busi", "BOOLEAN"),
    TransactionColumn("native_hawaiian_owned_busi", "native_hawaiian_owned_busi", "BOOLEAN"),
    TransactionColumn("native_hawaiian_servicing", "native_hawaiian_servicing", "BOOLEAN"),
    TransactionColumn("nonprofit_organization", "nonprofit_organization", "BOOLEAN"),
    TransactionColumn("number_of_actions", "number_of_actions", "STRING"),
    TransactionColumn("number_of_employees", "number_of_employees", "STRING"),
    TransactionColumn("number_of_offers_received", "number_of_offers_received", "STRING"),
    TransactionColumn("officer_1_amount", "high_comp_officer1_amount", "NUMERIC(23,2)", "cast"),
    TransactionColumn("officer_1_name", "high_comp_officer1_full_na", "STRING"),
    TransactionColumn("officer_2_amount", "high_comp_officer2_amount", "NUMERIC(23,2)", "cast"),
    TransactionColumn("officer_2_name", "high_comp_officer2_full_na", "STRING"),
    TransactionColumn("officer_3_amount", "high_comp_officer3_amount", "NUMERIC(23,2)", "cast"),
    TransactionColumn("officer_3_name", "high_comp_officer3_full_na", "STRING"),
    TransactionColumn("officer_4_amount", "high_comp_officer4_amount", "NUMERIC(23,2)", "cast"),
    TransactionColumn("officer_4_name", "high_comp_officer4_full_na", "STRING"),
    TransactionColumn("officer_5_amount", "high_comp_officer5_amount", "NUMERIC(23,2)", "cast"),
    TransactionColumn("officer_5_name", "high_comp_officer5_full_na", "STRING"),
    TransactionColumn(
        "ordering_period_end_date", "ordering_period_end_date", "STRING", "string_datetime_remove_timestamp"
    ),
    TransactionColumn("organizational_type", "organizational_type", "STRING"),
    TransactionColumn("other_minority_owned_busin", "other_minority_owned_busin", "BOOLEAN"),
    TransactionColumn("other_not_for_profit_organ", "other_not_for_profit_organ", "BOOLEAN"),
    TransactionColumn("other_statutory_authority", "other_statutory_authority", "STRING"),
    TransactionColumn("other_than_full_and_o_desc", "other_than_full_and_o_desc", "STRING"),
    TransactionColumn("other_than_full_and_open_c", "other_than_full_and_open_c", "STRING"),
    TransactionColumn("parent_award_id", "parent_award_id", "STRING"),
    TransactionColumn("partnership_or_limited_lia", "partnership_or_limited_lia", "BOOLEAN"),
    TransactionColumn("performance_based_se_desc", "performance_based_se_desc", "STRING"),
    TransactionColumn("performance_based_service", "performance_based_service", "STRING"),
    TransactionColumn("period_of_perf_potential_e", "period_of_perf_potential_e", "STRING"),
    TransactionColumn("period_of_performance_curr", "period_of_performance_curr", "STRING"),
    TransactionColumn("period_of_performance_star", "period_of_performance_star", "STRING"),
    TransactionColumn("piid", "piid", "STRING"),
    TransactionColumn("place_of_manufacture", "place_of_manufacture", "STRING"),
    TransactionColumn("place_of_manufacture_desc", "place_of_manufacture_desc", "STRING"),
    TransactionColumn("place_of_perf_country_desc", "place_of_perf_country_desc", "STRING"),
    TransactionColumn("place_of_perfor_state_desc", "place_of_perfor_state_desc", "STRING"),
    TransactionColumn("place_of_perform_city_name", "place_of_perform_city_name", "STRING"),
    TransactionColumn("place_of_perform_country_c", "place_of_perform_country_c", "STRING"),
    TransactionColumn("place_of_perform_country_n", "place_of_perform_country_n", "STRING"),
    TransactionColumn("place_of_perform_county_co", "place_of_perform_county_co", "STRING"),
    TransactionColumn("place_of_perform_county_na", "place_of_perform_county_na", "STRING"),
    TransactionColumn("place_of_perform_state_nam", "place_of_perform_state_nam", "STRING"),
    TransactionColumn("place_of_perform_zip_last4", "place_of_perform_zip_last4", "STRING"),
    TransactionColumn("place_of_performance_congr", "place_of_performance_congr", "STRING"),
    TransactionColumn("place_of_performance_locat", "place_of_performance_locat", "STRING"),
    TransactionColumn("place_of_performance_state", "place_of_performance_state", "STRING"),
    TransactionColumn("place_of_performance_zip4a", "place_of_performance_zip4a", "STRING"),
    TransactionColumn("place_of_performance_zip5", "place_of_performance_zip5", "STRING"),
    TransactionColumn("planning_commission", "planning_commission", "BOOLEAN"),
    TransactionColumn("port_authority", "port_authority", "BOOLEAN"),
    TransactionColumn("potential_total_value_awar", "potential_total_value_awar", "STRING"),
    TransactionColumn("price_evaluation_adjustmen", "price_evaluation_adjustmen", "STRING"),
    TransactionColumn("private_university_or_coll", "private_university_or_coll", "BOOLEAN"),
    TransactionColumn("product_or_service_co_desc", "product_or_service_co_desc", "STRING"),
    TransactionColumn("product_or_service_code", "product_or_service_code", "STRING"),
    TransactionColumn("program_acronym", "program_acronym", "STRING"),
    TransactionColumn("program_system_or_equ_desc", "program_system_or_equ_desc", "STRING"),
    TransactionColumn("program_system_or_equipmen", "program_system_or_equipmen", "STRING"),
    TransactionColumn("pulled_from", "pulled_from", "STRING"),
    TransactionColumn("purchase_card_as_paym_desc", "purchase_card_as_paym_desc", "STRING"),
    TransactionColumn("purchase_card_as_payment_m", "purchase_card_as_payment_m", "STRING"),
    TransactionColumn("receives_contracts_and_gra", "receives_contracts_and_gra", "BOOLEAN"),
    TransactionColumn("recovered_materials_s_desc", "recovered_materials_s_desc", "STRING"),
    TransactionColumn("recovered_materials_sustai", "recovered_materials_sustai", "STRING"),
    TransactionColumn("referenced_idv_agency_desc", "referenced_idv_agency_desc", "STRING"),
    TransactionColumn("referenced_idv_agency_iden", "referenced_idv_agency_iden", "STRING"),
    TransactionColumn("referenced_idv_agency_name", "referenced_idv_agency_name", "STRING"),
    TransactionColumn("referenced_idv_modificatio", "referenced_idv_modificatio", "STRING"),
    TransactionColumn("referenced_idv_type", "referenced_idv_type", "STRING"),
    TransactionColumn("referenced_idv_type_desc", "referenced_idv_type_desc", "STRING"),
    TransactionColumn("referenced_mult_or_si_desc", "referenced_mult_or_si_desc", "STRING"),
    TransactionColumn("referenced_mult_or_single", "referenced_mult_or_single", "STRING"),
    # The referenced_multi_or_single field does not appear in the django model and may have been created inadvertently
    # in the Delta model previously.  Since it is always NULL, it is a candidate for elimination.
    TransactionColumn("referenced_multi_or_single", "NULL", "STRING", "literal"),
    TransactionColumn("research", "research", "STRING"),
    TransactionColumn("research_description", "research_description", "STRING"),
    TransactionColumn("sam_exception", "sam_exception", "STRING"),
    TransactionColumn("sam_exception_description", "sam_exception_description", "STRING"),
    TransactionColumn("sba_certified_8_a_joint_ve", "sba_certified_8_a_joint_ve", "BOOLEAN"),
    TransactionColumn("school_district_local_gove", "school_district_local_gove", "BOOLEAN"),
    TransactionColumn("school_of_forestry", "school_of_forestry", "BOOLEAN"),
    TransactionColumn("sea_transportation", "sea_transportation", "STRING"),
    TransactionColumn("sea_transportation_desc", "sea_transportation_desc", "STRING"),
    TransactionColumn("self_certified_small_disad", "self_certified_small_disad", "BOOLEAN"),
    TransactionColumn("service_disabled_veteran_o", "service_disabled_veteran_o", "BOOLEAN"),
    TransactionColumn("small_agricultural_coopera", "small_agricultural_coopera", "BOOLEAN"),
    TransactionColumn("small_business_competitive", "small_business_competitive", "BOOLEAN"),
    TransactionColumn("small_disadvantaged_busine", "small_disadvantaged_busine", "BOOLEAN"),
    TransactionColumn("sole_proprietorship", "sole_proprietorship", "BOOLEAN"),
    TransactionColumn("solicitation_date", "solicitation_date", "DATE", "cast"),
    TransactionColumn("solicitation_identifier", "solicitation_identifier", "STRING"),
    TransactionColumn("solicitation_procedur_desc", "solicitation_procedur_desc", "STRING"),
    TransactionColumn("solicitation_procedures", "solicitation_procedures", "STRING"),
    TransactionColumn("state_controlled_instituti", "state_controlled_instituti", "BOOLEAN"),
    TransactionColumn("subchapter_s_corporation", "subchapter_s_corporation", "BOOLEAN"),
    TransactionColumn("subcontinent_asian_asian_i", "subcontinent_asian_asian_i", "BOOLEAN"),
    TransactionColumn("subcontracting_plan", "subcontracting_plan", "STRING"),
    TransactionColumn("subcontracting_plan_desc", "subcontracting_plan_desc", "STRING"),
    TransactionColumn("the_ability_one_program", "the_ability_one_program", "BOOLEAN"),
    TransactionColumn("total_obligated_amount", "total_obligated_amount", "STRING"),
    TransactionColumn("township_local_government", "township_local_government", "BOOLEAN"),
    TransactionColumn("transaction_id", None, "LONG NOT NULL"),
    TransactionColumn("transaction_number", "transaction_number", "STRING"),
    TransactionColumn("transit_authority", "transit_authority", "BOOLEAN"),
    TransactionColumn("tribal_college", "tribal_college", "BOOLEAN"),
    TransactionColumn("tribally_owned_business", "tribally_owned_business", "BOOLEAN"),
    TransactionColumn("type_of_contract_pric_desc", "type_of_contract_pric_desc", "STRING"),
    TransactionColumn("type_of_contract_pricing", "type_of_contract_pricing", "STRING"),
    TransactionColumn("type_of_idc", "type_of_idc", "STRING"),
    TransactionColumn("type_of_idc_description", "type_of_idc_description", "STRING"),
    TransactionColumn("type_set_aside", "type_set_aside", "STRING"),
    TransactionColumn("type_set_aside_description", "type_set_aside_description", "STRING"),
    TransactionColumn("ultimate_parent_legal_enti", "ultimate_parent_legal_enti", "STRING"),
    TransactionColumn("ultimate_parent_uei", "ultimate_parent_uei", "STRING"),
    TransactionColumn("ultimate_parent_unique_ide", "ultimate_parent_unique_ide", "STRING"),
    TransactionColumn("undefinitized_action", "undefinitized_action", "STRING"),
    TransactionColumn("undefinitized_action_desc", "undefinitized_action_desc", "STRING"),
    TransactionColumn("unique_award_key", "unique_award_key", "STRING"),
    TransactionColumn("updated_at", "updated_at", "TIMESTAMP"),
    TransactionColumn("us_federal_government", "us_federal_government", "BOOLEAN"),
    TransactionColumn("us_government_entity", "us_government_entity", "BOOLEAN"),
    TransactionColumn("us_local_government", "us_local_government", "BOOLEAN"),
    TransactionColumn("us_state_government", "us_state_government", "BOOLEAN"),
    TransactionColumn("us_tribal_government", "us_tribal_government", "BOOLEAN"),
    TransactionColumn("vendor_alternate_name", "vendor_alternate_name", "STRING"),
    TransactionColumn("vendor_alternate_site_code", "vendor_alternate_site_code", "STRING"),
    TransactionColumn("vendor_doing_as_business_n", "vendor_doing_as_business_n", "STRING"),
    TransactionColumn("vendor_enabled", "vendor_enabled", "STRING"),
    TransactionColumn("vendor_fax_number", "vendor_fax_number", "STRING"),
    TransactionColumn("vendor_legal_org_name", "vendor_legal_org_name", "STRING"),
    TransactionColumn("vendor_location_disabled_f", "vendor_location_disabled_f", "STRING"),
    TransactionColumn("vendor_phone_number", "vendor_phone_number", "STRING"),
    TransactionColumn("vendor_site_code", "vendor_site_code", "STRING"),
    TransactionColumn("veteran_owned_business", "veteran_owned_business", "BOOLEAN"),
    TransactionColumn("veterinary_college", "veterinary_college", "BOOLEAN"),
    TransactionColumn("veterinary_hospital", "veterinary_hospital", "BOOLEAN"),
    TransactionColumn("woman_owned_business", "woman_owned_business", "BOOLEAN"),
    TransactionColumn("women_owned_small_business", "women_owned_small_business", "BOOLEAN"),
]

TRANSACTION_FPDS_COLUMNS = [col.dest_name for col in TRANSACTION_FPDS_COLUMN_INFO]

delta_columns_not_in_view = [
    "annual_revenue",
    "award_or_idv_flag",
    "division_name",
    "division_number_or_office",
    "entity_data_source",
    "initial_report_date",
    "number_of_employees",
    "place_of_perform_country_n",
    "place_of_perform_state_nam",
    "place_of_performance_locat",
    "referenced_idv_agency_name",
    "referenced_multi_or_single",
    "vendor_alternate_name",
    "vendor_alternate_site_code",
    "vendor_enabled",
    "vendor_legal_org_name",
    "vendor_location_disabled_f",
    "vendor_site_code",
    "created_at",
    "updated_at",
]

TRANSACTION_FPDS_VIEW_COLUMNS = [
    col.dest_name for col in TRANSACTION_FPDS_COLUMN_INFO if col.dest_name not in delta_columns_not_in_view
]

transaction_fpds_sql_string = rf"""
    CREATE OR REPLACE TABLE {{DESTINATION_TABLE}} (
        {", ".join([f'{col.dest_name} {col.delta_type}' for col in TRANSACTION_FPDS_COLUMN_INFO])}
    )
    USING DELTA
    LOCATION 's3a://{{SPARK_S3_BUCKET}}/{{DELTA_LAKE_S3_PATH}}/{{DESTINATION_DATABASE}}/{{DESTINATION_TABLE}}'
    """

# Mapping from raw.detached_award_procurement to int.transaction_normalized columns, where a simple mapping exists
DAP_TO_NORMALIZED_COLUMN_INFO = [
    TransactionColumn("action_date", "action_date", "DATE", "parse_string_datetime_to_date"),
    TransactionColumn("action_type", "action_type", "STRING"),
    TransactionColumn("action_type_description", "action_type_description", "STRING"),
    TransactionColumn("certified_date", "NULL", "DATE", "literal"),
    TransactionColumn("description", "award_description", "STRING"),
    TransactionColumn("face_value_loan_guarantee", "NULL", "NUMERIC(23, 2)", "literal"),
    TransactionColumn("federal_action_obligation", "federal_action_obligation", "NUMERIC(23,2)"),
    TransactionColumn("funding_amount", "NULL", "NUMERIC(23, 2)", "literal"),
    TransactionColumn("indirect_federal_sharing", "NULL", "NUMERIC(23, 2)", "literal"),
    TransactionColumn("is_fpds", "TRUE", "BOOLEAN", "literal"),
    TransactionColumn("last_modified_date", "last_modified", "DATE", "cast"),
    TransactionColumn("modification_number", "award_modification_amendme", "STRING"),
    TransactionColumn("non_federal_funding_amount", "NULL", "NUMERIC(23, 2)", "literal"),
    TransactionColumn("original_loan_subsidy_cost", "NULL", "NUMERIC(23, 2)", "literal"),
    # All period_of_performance_* fields seen as: YYYY-MM-DD 00:00:00, so cast works
    # BUT it's still just a string and could morph, so defensively smart-date-parsing the string
    TransactionColumn(
        "period_of_performance_current_end_date", "period_of_performance_curr", "DATE", "parse_string_datetime_to_date"
    ),
    TransactionColumn(
        "period_of_performance_start_date", "period_of_performance_star", "DATE", "parse_string_datetime_to_date"
    ),
    TransactionColumn("transaction_unique_id", "detached_award_proc_unique", "STRING"),
    TransactionColumn("unique_award_key", "unique_award_key", "STRING"),
    TransactionColumn("usaspending_unique_transaction_id", "NULL", "STRING", "literal"),
]