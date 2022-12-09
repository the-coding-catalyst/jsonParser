from jsonParser import *
test1 = [
	{
		"id": "0001",
		"type": "donut",
		"name": "Cake",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" },
						{ "id": "1003", "type": "Blueberry" },
						{ "id": "1004", "type": "Devil's Food" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5007", "type": "Powdered Sugar" },
				{ "id": "5006", "type": "Chocolate with Sprinkles" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0002",
		"type": "donut",
		"name": "Raised",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5005", "type": "Sugar" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	},
	{
		"id": "0003",
		"type": "donut",
		"name": "Old Fashioned",
		"ppu": 0.55,
		"batters":
			{
				"batter":
					[
						{ "id": "1001", "type": "Regular" },
						{ "id": "1002", "type": "Chocolate" }
					]
			},
		"topping":
			[
				{ "id": "5001", "type": "None" },
				{ "id": "5002", "type": "Glazed" },
				{ "id": "5003", "type": "Chocolate" },
				{ "id": "5004", "type": "Maple" }
			]
	}
]


test2 = {
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
}

test3 = {"isbn": "123-456-222",  
 "author": 
    {
      "lastname": "Doe",
      "firstname": "Jane"
    },
"editor": 
    {
      "lastname": "Smith",
      "firstname": "Jane"
    },
  "title": "The Ultimate Database Study Guide",  
  "category": ["Non-Fiction", "Technology"]
}
test4 = {
"problems": [{
    "Diabetes":[{
        "medications":[{
            "medicationsClasses":[{
                "className":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }],
                "className2":[{
                    "associatedDrug":[{
                        "name":"asprin",
                        "dose":"",
                        "strength":"500 mg"
                    }],
                    "associatedDrug#2":[{
                        "name":"somethingElse",
                        "dose":"",
                        "strength":"500 mg"
                    }]
                }]
            }]
        }],
        "labs":[{
            "missing_field": "missing_value"
        }]
    }],
    "Asthma":[{}]
}]}

test5 = {
  "destination_addresses": [
    "Washington, DC, USA",
    "Philadelphia, PA, USA",
    "Santa Barbara, CA, USA",
    "Miami, FL, USA",
    "Austin, TX, USA",
    "Napa County, CA, USA"
  ],
  "origin_addresses": [
    "New York, NY, USA"
  ],
  "rows": [{
    "elements": [{
        "distance": {
          "text": "227 mi",
          "value": 365468
        },
        "duration": {
          "text": "3 hours 54 mins",
          "value": 14064
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "94.6 mi",
          "value": 152193
        },
        "duration": {
          "text": "1 hour 44 mins",
          "value": 6227
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "2,878 mi",
          "value": 4632197
        },
        "duration": {
          "text": "1 day 18 hours",
          "value": 151772
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "1,286 mi",
          "value": 2069031
        },
        "duration": {
          "text": "18 hours 43 mins",
          "value": 67405
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "1,742 mi",
          "value": 2802972
        },
        "duration": {
          "text": "1 day 2 hours",
          "value": 93070
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "2,871 mi",
          "value": 4620514
        },
        "duration": {
          "text": "1 day 18 hours",
          "value": 152913
        },
        "status": "OK"
      }
    ]
  }],
  "status": "OK"
}

test5 = {"menu": {  
  "id": "file",  
  "value": "File",  
  "popup": {  
    "menuitem": [  
      {"value": "New", "onclick": "CreateDoc()"},  
      {"value": "Open", "onclick": "OpenDoc()"},  
      {"value": "Save", "onclick": "SaveDoc()"}  
    ]  
  }  
}}  

testCases = [test1, test2, test3, test4, test5]
