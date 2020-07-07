-- WITH latest_submissions AS (
--     SELECT
--         "dabs_submission_window_schedule"."submission_fiscal_year",
--         "dabs_submission_window_schedule"."is_quarter",
--         MAX("dabs_submission_window_schedule"."submission_fiscal_month") AS "submission_fiscal_month"
--     FROM "dabs_submission_window_schedule"
--     WHERE
--         "dabs_submission_window_schedule"."submission_reveal_date" <= now()
--     GROUP BY
--         "dabs_submission_window_schedule"."submission_fiscal_year",
--         "dabs_submission_window_schedule"."is_quarter"
-- )
WITH recent_submission AS (
    SELECT
        "dabs_submission_window_schedule"."submission_fiscal_year",
        "dabs_submission_window_schedule"."is_quarter",
        "dabs_submission_window_schedule"."submission_fiscal_month"
    FROM "dabs_submission_window_schedule"
    WHERE
        "dabs_submission_window_schedule"."submission_reveal_date" <= now()
        AND "dabs_submission_window_schedule"."is_quarter" = False
    ORDER BY "dabs_submission_window_schedule"."submission_fiscal_year" DESC, "dabs_submission_window_schedule"."submission_fiscal_month" DESC
    LIMIT 1
)
SELECT
    "toptier_agency"."name" AS "owning_agency_name",
    "submission_attributes"."reporting_agency_name" AS "reporting_agency_name",
    CASE
        WHEN "submission_attributes"."quarter_format_flag" = True THEN
            CONCAT ('FY' , EXTRACT (YEAR FROM ("financial_accounts_by_program_activity_object_class"."reporting_period_end") + INTERVAL '3 months') , 'Q' , EXTRACT (QUARTER FROM ("financial_accounts_by_program_activity_object_class"."reporting_period_end") + INTERVAL '3 months'))
        ELSE
            CONCAT ('FY' , EXTRACT (YEAR FROM ("financial_accounts_by_program_activity_object_class"."reporting_period_end") + INTERVAL '3 months') , 'P' , EXTRACT (MONTH FROM ("financial_accounts_by_program_activity_object_class"."reporting_period_end") + INTERVAL '3 months'))
    END AS "last_reported_submission_period",
    "treasury_appropriation_account"."allocation_transfer_agency_id" AS "allocation_transfer_agency_identifier_code",
    "treasury_appropriation_account"."agency_id" AS "agency_identifier_code",
    "treasury_appropriation_account"."beginning_period_of_availability" AS "beginning_period_of_availability",
    "treasury_appropriation_account"."ending_period_of_availability" AS "ending_period_of_availability",
    "treasury_appropriation_account"."availability_type_code" AS "availability_type_code",
    "treasury_appropriation_account"."main_account_code" AS "main_account_code",
    "treasury_appropriation_account"."sub_account_code" AS "sub_account_code",
    "treasury_appropriation_account"."tas_rendering_label" AS "treasury_account_symbol",
    "treasury_appropriation_account"."account_title" AS "treasury_account_name",
    (SELECT U0."agency_name" FROM "cgac" U0 WHERE U0."cgac_code" = ("treasury_appropriation_account"."agency_id")) AS "agency_identifier_name",
    (SELECT U0."agency_name" FROM "cgac" U0 WHERE U0."cgac_code" = ("treasury_appropriation_account"."allocation_transfer_agency_id")) AS "allocation_transfer_agency_identifier_name",
    "treasury_appropriation_account"."budget_function_title" AS "budget_function",
    "treasury_appropriation_account"."budget_subfunction_title" AS "budget_subfunction",
    "federal_account"."federal_account_code" AS "federal_account_symbol",
    "federal_account"."account_title" AS "federal_account_name",
    "disaster_emergency_fund_code"."code" AS "disaster_emergency_fund_code",
    "disaster_emergency_fund_code"."title" AS "disaster_emergency_fund_name",
    "ref_program_activity"."program_activity_code" AS "program_activity_code",
    "ref_program_activity"."program_activity_name" AS "program_activity_name",
    "object_class"."object_class" AS "object_class_code",
    "object_class"."object_class_name" AS "object_class_name",
    "object_class"."direct_reimbursable" AS "direct_or_reimbursable_funding_source",
    "financial_accounts_by_program_activity_object_class"."obligations_incurred_by_program_object_class_cpe" AS "obligations_incurred",
    "financial_accounts_by_program_activity_object_class"."deobligations_recoveries_refund_pri_program_object_class_cpe" AS "deobligations_or_recoveries_or_refunds_from_prior_year",
    "financial_accounts_by_program_activity_object_class"."gross_outlay_amount_by_program_object_class_cpe" AS "gross_outlay_amount",
    (MAX("submission_attributes"."published_date")) ::date AS "last_modified_date"
FROM "financial_accounts_by_program_activity_object_class"
LEFT OUTER JOIN "treasury_appropriation_account" ON ("financial_accounts_by_program_activity_object_class"."treasury_account_id" = "treasury_appropriation_account"."treasury_account_identifier")
INNER JOIN "submission_attributes" ON ("financial_accounts_by_program_activity_object_class"."submission_id" = "submission_attributes"."submission_id")
INNER JOIN "recent_submission" ON ("submission_attributes"."reporting_fiscal_period" = "recent_submission"."submission_fiscal_month"
    AND "submission_attributes"."quarter_format_flag" = "recent_submission"."is_quarter"
    AND "submission_attributes"."reporting_fiscal_year" = "recent_submission"."submission_fiscal_year")
INNER JOIN "disaster_emergency_fund_code" ON ("financial_accounts_by_program_activity_object_class"."disaster_emergency_fund_code" = "disaster_emergency_fund_code"."code")
INNER JOIN "ref_program_activity" ON ("financial_accounts_by_program_activity_object_class"."program_activity_id" = "ref_program_activity"."id")
INNER JOIN "object_class" ON ("financial_accounts_by_program_activity_object_class"."object_class_id" = "object_class"."id")
LEFT OUTER JOIN "toptier_agency" ON ("treasury_appropriation_account"."funding_toptier_agency_id" = "toptier_agency"."toptier_agency_id")
INNER JOIN "federal_account" ON ("treasury_appropriation_account"."federal_account_id" = "federal_account"."id")
WHERE (
    "disaster_emergency_fund_code"."group_name" = 'covid_19'
)
GROUP BY
    "financial_accounts_by_program_activity_object_class"."financial_accounts_by_program_activity_object_class_id",
    CASE
        WHEN "submission_attributes"."quarter_format_flag" = True THEN
            CONCAT ('FY' , EXTRACT (YEAR FROM ("financial_accounts_by_program_activity_object_class"."reporting_period_end") + INTERVAL '3 months') , 'Q' , EXTRACT (QUARTER FROM ("financial_accounts_by_program_activity_object_class"."reporting_period_end") + INTERVAL '3 months'))
        ELSE
            CONCAT ('FY' , EXTRACT (YEAR FROM ("financial_accounts_by_program_activity_object_class"."reporting_period_end") + INTERVAL '3 months') , 'P' , EXTRACT (MONTH FROM ("financial_accounts_by_program_activity_object_class"."reporting_period_end") + INTERVAL '3 months'))
    END,
    (SELECT U0."agency_name" FROM "cgac" U0 WHERE U0."cgac_code" = ("treasury_appropriation_account"."allocation_transfer_agency_id")),
    (SELECT U0."agency_name" FROM "cgac" U0 WHERE U0."cgac_code" = ("treasury_appropriation_account"."agency_id")) ,
    "toptier_agency"."name",
    "submission_attributes"."reporting_agency_name",
    "treasury_appropriation_account"."allocation_transfer_agency_id",
    "treasury_appropriation_account"."agency_id",
    "treasury_appropriation_account"."beginning_period_of_availability",
    "treasury_appropriation_account"."ending_period_of_availability",
    "treasury_appropriation_account"."availability_type_code",
    "treasury_appropriation_account"."main_account_code",
    "treasury_appropriation_account"."sub_account_code",
    "treasury_appropriation_account"."tas_rendering_label",
    "treasury_appropriation_account"."account_title",
    "treasury_appropriation_account"."budget_function_title",
    "treasury_appropriation_account"."budget_subfunction_title",
    "federal_account"."federal_account_code",
    "federal_account"."account_title",
    "disaster_emergency_fund_code"."code",
    "disaster_emergency_fund_code"."title",
    "ref_program_activity"."program_activity_code",
    "ref_program_activity"."program_activity_name",
    "object_class"."object_class",
    "object_class"."object_class_name",
    "object_class"."direct_reimbursable"
