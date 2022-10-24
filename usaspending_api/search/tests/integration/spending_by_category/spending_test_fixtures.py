from model_bakery import baker
import pytest


@pytest.fixture
def basic_agencies(db):
    _setup_agency(1, [], "Awarding")

    _setup_agency(4, [], "Funding")


@pytest.fixture
def basic_award(db, basic_agencies):
    baker.make("awards.Award", id=1, latest_transaction_id=1)
    baker.make(
        "search.TransactionSearch",
        transaction_id=1,
        award_id=1,
        awarding_agency_id=1001,
        funding_agency_id=1004,
        federal_action_obligation=5,
        action_date="2020-01-01",
        is_fpds=False,
        awarding_agency_code="001",
        awarding_toptier_agency_abbreviation="Awarding Toptier Agency 1",
        funding_agency_code="004",
        funding_toptier_agency_abbreviation="Funding Toptier Agency 4",
        awarding_sub_tier_agency_c="1001",
        awarding_subtier_agency_abbreviation="Awarding Subtier Agency 1",
        funding_sub_tier_agency_co="1004",
        funding_subtier_agency_abbreviation="Funding Subtier Agency 4",
    )


@pytest.fixture
def agencies_with_subagencies(db):
    """Create some agencies with more than one subtier to toptier"""
    _setup_agency(3, [5], "Awarding")

    _setup_agency(2, [6], "Funding")


@pytest.fixture
def subagency_award(db, agencies_with_subagencies):
    baker.make("awards.Award", id=2, latest_transaction_id=2)

    baker.make(
        "search.TransactionSearch",
        transaction_id=2,
        award_id=2,
        awarding_agency_id=1005,
        funding_agency_id=1006,
        federal_action_obligation=10,
        action_date="2020-01-02",
        is_fpds=False,
        awarding_agency_code="003",
        awarding_toptier_agency_abbreviation="Awarding Toptier Agency 3",
        funding_agency_code="002",
        funding_toptier_agency_abbreviation="Funding Toptier Agency 2",
        awarding_sub_tier_agency_c="0005",
        awarding_subtier_agency_abbreviation="Awarding Subtier Agency 5",
        funding_sub_tier_agency_co="0006",
        funding_subtier_agency_abbreviation="Funding Subtier Agency 6",
    )


def _setup_agency(id, subtiers, special_name):
    baker.make(
        "references.ToptierAgency",
        toptier_agency_id=id + 2000,
        name=f"{special_name} Toptier Agency {id}",
        abbreviation=f"TA{id}",
        toptier_code=f"00{id}",
    )
    baker.make(
        "references.SubtierAgency",
        subtier_agency_id=id + 3000,
        name=f"{special_name} Subtier Agency {id}",
        abbreviation=f"SA{id}",
    )
    baker.make(
        "references.Agency", id=id + 1000, toptier_agency_id=id + 2000, subtier_agency_id=id + 3000, toptier_flag=True
    )

    for sub_id in subtiers:
        baker.make(
            "references.SubtierAgency",
            subtier_agency_id=sub_id + 3000,
            name=f"{special_name} Subtier Agency {sub_id}",
            abbreviation=f"SA{sub_id}",
        )
        baker.make(
            "references.Agency",
            id=sub_id + 1000,
            toptier_agency_id=id + 2000,
            subtier_agency_id=sub_id + 3000,
            toptier_flag=False,
        )


@pytest.fixture
def awards_and_transactions(db):
    # Awards
    baker.make("awards.Award", id=1, latest_transaction_id=10)
    baker.make("awards.Award", id=2, latest_transaction_id=20)
    baker.make("awards.Award", id=3, latest_transaction_id=30)
    baker.make("awards.Award", id=4, latest_transaction_id=40)
    baker.make("awards.Award", id=5, latest_transaction_id=50)
    baker.make("awards.Award", id=6, latest_transaction_id=60)
    baker.make("awards.Award", id=7, latest_transaction_id=70)

    baker.make("awards.FinancialAccountsByAwards", pk=1, award_id=1, treasury_account_id=1)
    baker.make("accounts.TreasuryAppropriationAccount", pk=1, federal_account_id=1)
    baker.make(
        "accounts.FederalAccount",
        pk=1,
        agency_identifier="012",
        main_account_code="1106",
        account_title="FA 1",
        federal_account_code="012-1106",
    )

    baker.make("awards.FinancialAccountsByAwards", pk=2, award_id=2, treasury_account_id=2)
    baker.make("accounts.TreasuryAppropriationAccount", pk=2, federal_account_id=2)
    baker.make(
        "accounts.FederalAccount",
        pk=2,
        agency_identifier="014",
        main_account_code="5110",
        account_title="FA 2",
        federal_account_code="014-5110",
    )

    baker.make("awards.FinancialAccountsByAwards", pk=3, award_id=2, treasury_account_id=3)
    baker.make("accounts.TreasuryAppropriationAccount", pk=3, federal_account_id=3)
    baker.make(
        "accounts.FederalAccount",
        pk=3,
        agency_identifier="014",
        main_account_code="1036",
        account_title="FA 3",
        federal_account_code="014-1036",
    )

    # Transaction Search
    baker.make(
        "search.TransactionSearch",
        transaction_id=10,
        award_id=1,
        federal_action_obligation=5,
        action_date="2020-01-01",
        is_fpds=False,
        cfda_number="10.100",
        pop_country_code="USA",
        pop_country_name="UNITED STATES",
        pop_state_code="SC",
        pop_state_name="SOUTH CAROLINA",
        pop_county_code="001",
        pop_county_name="CHARLESTON",
        pop_congressional_code="10",
        recipient_location_country_code="CAN",
        recipient_location_country_name="CANADA",
        recipient_location_state_code=None,
        recipient_location_state_name=None,
        recipient_location_county_code=None,
        recipient_location_county_name=None,
        recipient_location_congressional_code=None,
        recipient_name="RECIPIENT 1",
        recipient_unique_id=None,
        recipient_uei=None,
    )
    baker.make(
        "search.TransactionSearch",
        transaction_id=20,
        award_id=2,
        federal_action_obligation=50,
        action_date="2020-01-02",
        is_fpds=False,
        cfda_number="20.200",
        pop_country_code="USA",
        pop_country_name="UNITED STATES",
        pop_state_code="SC",
        pop_state_name="SOUTH CAROLINA",
        pop_county_code="005",
        pop_county_name="TEST NAME",
        pop_congressional_code="50",
        recipient_location_country_code="USA",
        recipient_location_country_name="UNITED STATES",
        recipient_location_state_code="SC",
        recipient_location_state_name="SOUTH CAROLINA",
        recipient_location_county_code="001",
        recipient_location_county_name="CHARLESTON",
        recipient_location_congressional_code="90",
        recipient_name="RECIPIENT 2",
        recipient_unique_id="456789123",
        recipient_uei="UEIAAABBBCCC",
    )
    baker.make(
        "search.TransactionSearch",
        transaction_id=30,
        award_id=3,
        federal_action_obligation=500,
        action_date="2020-01-03",
        is_fpds=False,
        cfda_number="20.200",
        pop_country_code="USA",
        pop_country_name="UNITED STATES",
        pop_state_code="WA",
        pop_state_name="WASHINGTON",
        pop_county_code="005",
        pop_county_name="TEST NAME",
        pop_congressional_code="50",
        recipient_location_country_code="USA",
        recipient_location_country_name="UNITED STATES",
        recipient_location_state_code="SC",
        recipient_location_state_name="SOUTH CAROLINA",
        recipient_location_county_code="001",
        recipient_location_county_name="CHARLESTON",
        recipient_location_congressional_code="50",
        recipient_name="RECIPIENT 3",
        recipient_unique_id="987654321",
        recipient_uei="987654321AAA",
    )
    baker.make(
        "search.TransactionSearch",
        transaction_id=40,
        award_id=4,
        federal_action_obligation=5000,
        action_date="2020-01-04",
        is_fpds=True,
        pop_country_code="USA",
        pop_country_name="UNITED STATES",
        pop_state_code="WA",
        pop_state_name="WASHINGTON",
        pop_county_code="005",
        pop_county_name="TEST NAME",
        pop_congressional_code="50",
        recipient_location_country_code="USA",
        recipient_location_country_name="UNITED STATES",
        recipient_location_state_code="WA",
        recipient_location_state_name="WASHINGTON",
        recipient_location_county_code="005",
        recipient_location_county_name="TEST NAME",
        recipient_location_congressional_code="50",
        recipient_name="MULTIPLE RECIPIENTS",
        recipient_unique_id="096354360",
        parent_uei="096354360AAA",
        product_or_service_code="1005",
        product_or_service_co_desc="PSC 1",
    )
    baker.make(
        "search.TransactionSearch",
        transaction_id=50,
        award_id=5,
        federal_action_obligation=50000,
        action_date="2020-01-05",
        is_fpds=True,
        pop_country_code="USA",
        pop_country_name="UNITED STATES",
        pop_state_code="SC",
        pop_state_name="SOUTH CAROLINA",
        pop_county_code="001",
        pop_county_name="CHARLESTON",
        pop_congressional_code="10",
        recipient_location_country_code="USA",
        recipient_location_country_name="UNITED STATES",
        recipient_location_state_code="WA",
        recipient_location_state_name="WASHINGTON",
        recipient_location_county_code="005",
        recipient_location_county_name="TEST NAME",
        recipient_location_congressional_code="50",
        recipient_name=None,
        recipient_unique_id="123456789",
        parent_uei="123456789AAA",
        product_or_service_code="M123",
        product_or_service_co_desc="PSC 2",
        naics="111110",
        naics_description="NAICS 1",
    )
    baker.make(
        "search.TransactionSearch",
        transaction_id=60,
        award_id=6,
        federal_action_obligation=500000,
        action_date="2020-01-06",
        is_fpds=True,
        pop_country_code="USA",
        pop_country_name="UNITED STATES",
        pop_state_code="SC",
        pop_state_name="SOUTH CAROLINA",
        pop_county_code="001",
        pop_county_name="CHARLESTON",
        pop_congressional_code="90",
        recipient_location_country_code="USA",
        recipient_location_country_name="UNITED STATES",
        recipient_location_state_code="SC",
        recipient_location_state_name="SOUTH CAROLINA",
        recipient_location_county_code="005",
        recipient_location_county_name="TEST NAME",
        recipient_location_congressional_code="50",
        recipient_name=None,
        recipient_unique_id="123456789",
        parent_uei="123456789AAA",
        naics="222220",
        naics_description="NAICS 2",
    )
    baker.make(
        "search.TransactionSearch",
        transaction_id=70,
        award_id=7,
        federal_action_obligation=5000000,
        action_date="2020-01-07",
        is_fpds=True,
        pop_country_code="CAN",
        pop_country_name="CANADA",
        pop_state_code=None,
        pop_state_name=None,
        pop_county_code=None,
        pop_county_name=None,
        pop_congressional_code=None,
        recipient_location_country_code="USA",
        recipient_location_country_name="UNITED STATES",
        recipient_location_state_code="SC",
        recipient_location_state_name="SOUTH CAROLINA",
        recipient_location_county_code="01",
        recipient_location_county_name="CHARLESTON",
        recipient_location_congressional_code="10",
        recipient_name="MULTIPLE RECIPIENTS",
        recipient_unique_id=None,
        parent_uei=None,
    )

    # References State Data
    baker.make("recipient.StateData", id="45-2020", fips="45", code="SC", name="South Carolina")
    baker.make("recipient.StateData", id="53-2020", fips="53", code="WA", name="Washington")

    # References Country
    baker.make("references.RefCountryCode", country_code="CAN", country_name="CANADA")
    baker.make("references.RefCountryCode", country_code="USA", country_name="UNITED STATES")

    # References Population County
    baker.make(
        "references.PopCounty",
        id=1,
        state_code="45",
        state_name="South Carolina",
        county_number="001",
        latest_population=1,
    )
    baker.make(
        "references.PopCounty",
        id=2,
        state_code="45",
        state_name="South Carolina",
        county_number="005",
        latest_population=10,
    )
    baker.make(
        "references.PopCounty",
        id=3,
        state_code="53",
        state_name="Washington",
        county_number="005",
        latest_population=100,
    )
    baker.make(
        "references.PopCounty",
        id=4,
        state_code="45",
        state_name="South Carolina",
        county_number="000",
        latest_population=1000,
    )
    baker.make(
        "references.PopCounty",
        id=5,
        state_code="53",
        state_name="Washington",
        county_number="000",
        latest_population=10000,
    )

    # References Population Congressional District
    baker.make(
        "references.PopCongressionalDistrict",
        id=1,
        state_code="45",
        state_name="South Carolina",
        congressional_district="90",
        latest_population=1,
    )
    baker.make(
        "references.PopCongressionalDistrict",
        id=2,
        state_code="45",
        state_name="South Carolina",
        congressional_district="10",
        latest_population=10,
    )
    baker.make(
        "references.PopCongressionalDistrict",
        id=2,
        state_code="45",
        state_name="South Carolina",
        congressional_district="50",
        latest_population=100,
    )
    baker.make(
        "references.PopCongressionalDistrict",
        id=3,
        state_code="53",
        state_name="Washington",
        congressional_district="50",
        latest_population=1000,
    )

    # References CFDA
    baker.make("references.Cfda", id=100, program_number="10.100", program_title="CFDA 1")
    baker.make("references.Cfda", id=200, program_number="20.200", program_title="CFDA 2")

    # Recipient Profile
    baker.make(
        "recipient.RecipientProfile",
        recipient_name="RECIPIENT 1",
        recipient_level="R",
        recipient_hash="5f572ec9-8b49-e5eb-22c7-f6ef316f7689",
        recipient_unique_id=None,
    )
    baker.make(
        "recipient.RecipientProfile",
        recipient_name="RECIPIENT 2",
        recipient_level="R",
        recipient_unique_id="456789123",
        uei="UEIAAABBBCCC",
    )
    baker.make(
        "recipient.RecipientProfile",
        recipient_name="RECIPIENT 3",
        recipient_level="P",
        recipient_hash="3523fd0b-c1f0-ddac-e217-7b7b25fad06f",
        recipient_unique_id="987654321",
        uei="987654321AAA",
    )
    baker.make(
        "recipient.RecipientProfile",
        recipient_name="RECIPIENT 3",
        recipient_level="C",
        recipient_hash="3523fd0b-c1f0-ddac-e217-7b7b25fad06f",
        recipient_unique_id="987654321",
        uei="987654321AAA",
    )
    baker.make(
        "recipient.RecipientProfile",
        recipient_name="MULTIPLE RECIPIENTS",
        recipient_level="R",
        recipient_hash="5bf6217b-4a70-da67-1351-af6ab2e0a4b3",
        recipient_unique_id="096354360",
        uei="096354360AAA",
    )
    baker.make(
        "recipient.RecipientProfile",
        recipient_name=None,
        recipient_level="R",
        recipient_hash="25f9e794-323b-4538-85f5-181f1b624d0b",
        recipient_unique_id="123456789",
        uei="123456789AAA",
    )

    # Recipient Lookup
    baker.make(
        "recipient.RecipientLookup",
        legal_business_name="RECIPIENT 3",
        recipient_hash="3523fd0b-c1f0-ddac-e217-7b7b25fad06f",
        duns="987654321",
        uei="987654321AAA",
    )

    # PSC
    baker.make("references.PSC", code="1005", description="PSC 1")
    baker.make("references.PSC", code="M123", description="PSC 2")

    # NAICS
    baker.make("references.NAICS", code="111110", description="NAICS 1")
    baker.make("references.NAICS", code="222220", description="NAICS 2")

    # Ref Country Code
    baker.make("references.RefCountryCode", country_code="USA", country_name="UNITED STATES")
    baker.make("references.RefCountryCode", country_code="CAN", country_name="CANADA")
