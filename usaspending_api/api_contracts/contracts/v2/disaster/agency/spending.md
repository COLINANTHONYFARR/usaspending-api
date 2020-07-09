FORMAT: 1A
HOST: https://api.usaspending.gov

# Agencies Spending Disaster/Emergency Funding [/api/v2/disaster/agency/spending/]

This endpoint provides insights on the Agencies which received disaster/emergency funding per the requested filters.

## POST

Returns spending details of Agencies receiving supplemental funding budgetary resources

+ Request (application/json)
    + Schema

            {
                "$schema": "http://json-schema.org/draft-04/schema#",
                "type": "object"
            }

    + Attributes
        + `filter` (required, Filter, fixed-type)
        + `spending_type` (required, enum[string], fixed-type)
            Toggle if the outlay and obligation response values are total or only from awards only from awards
            + Members
                + `total`
                + `award`
        + `pagination` (optional, Pagination, fixed-type)

+ Response 200 (application/json)
    + Attributes (object)
        + `results` (required, array[Result], fixed-type)
        + `page_metadata` (required, PageMetadata, fixed-type)


    + Body

            {
                "results": [
                    {
                        "id": 168,
                        "code": "349",
                        "description": "District of Columbia Courts",
                        "children": [],
                        "count": 0,
                        "obligation": 148906061.27,
                        "outlay": 143265869.34,
                        "total_budgetary_resources": 18087913735.71
                    },
                    {
                        "id": 130,
                        "code": "413",
                        "description": "National Council on Disability",
                        "children": [],
                        "count": 0,
                        "obligation": 225185.66,
                        "outlay": 697329.0,
                        "total_budgetary_resources": 183466350.0
                    }
                ],
                "page_metadata": {
                    "page": 1,
                    "total": 62,
                    "limit": 2,
                    "next": 2,
                    "previous": null,
                    "hasNext": true,
                    "hasPrevious": false
                }
            }

# Data Structures

## Filter (object)
+ `def_codes` (required, array[DEFC], fixed-type)
+ `award_type_codes` (optional, array[AwardTypeCodes], fixed-type)
    Defaults to all Award Type Codes. Applicable only when requested `award` spending.
+ `query` (optional, string)
    A "keyword" or "search term" to filter down results based on this text snippet

## Pagination (object)
+ `page` (optional, number)
    Requested page of results
    + Default: 1
+ `limit` (optional, number)
    Page Size of results
    + Default: 10
+ `order` (optional, enum[string])
    Indicates what direction results should be sorted by. Valid options include asc for ascending order or desc for descending order.
    + Default: `desc`
    + Members
        + `desc`
        + `asc`
+ `sort` (optional, enum[string])
    Optional parameter indicating what value results should be sorted by
    + Default: `id`
    + Members
        + `id`
        + `code`
        + `description`
        + `count`
        + `total_budgetary_resources`
        + `obligation`
        + `outlay`

## Result (object)
+ `id` (required, string)
+ `code` (required, string)
+ `description` (required, string)
+ `children` (optional, array[Result], fixed-type)
+ `count` (required, number)
+ `obligation` (required, number, nullable)
+ `outlay` (required, number, nullable)
+ `total_budgetary_resources` (required, number, nullable)

## PageMetadata (object)
+ `page` (required, number)
+ `next` (required, number, nullable)
+ `previous` (required, number, nullable)
+ `hasNext` (required, boolean)
+ `hasPrevious` (required, boolean)
+ `total` (required, number)
+ `limit` (required, number)

## DEFC (enum[string])
List of Disaster Emergency Fund (DEF) Codes (DEFC) defined by legislation at the time of writing

### Members
+ `A`
+ `B`
+ `C`
+ `D`
+ `E`
+ `F`
+ `G`
+ `H`
+ `I`
+ `J`
+ `K`
+ `L`
+ `M`
+ `N`
+ `O`
+ `P`
+ `Q`
+ `R`
+ `S`
+ `T`
+ `9`

## AwardTypeCodes (enum[string])
List of procurement and assistance award type codes supported by USAspending.gov

### Members
+ `02`
+ `03`
+ `04`
+ `05`
+ `06`
+ `07`
+ `08`
+ `09`
+ `10`
+ `11`
+ `A`
+ `B`
+ `C`
+ `D`
+ `IDV_A`
+ `IDV_B_A`
+ `IDV_B_B`
+ `IDV_B_C`
+ `IDV_B`
+ `IDV_C`
+ `IDV_D`
+ `IDV_E`
