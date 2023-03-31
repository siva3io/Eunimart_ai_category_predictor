channel_id_name_mapping = {
   "1"  : "Amazon_USA",
   "12" : "Amazon_India",
   "14" : "Flipkart",
   "15" : "Bonanza",
   "3"  : "eBay",
   "24" : "Etsy" # temporary fix, might change in future
}
model_name_id_map = {
   "Amazon_India":{
        "Level_0_Images"                            :   "Amazon_India_0",
        "Beauty"                                    :   "Amazon_India_1",
        "Car_and_Motorbike"                         :   "Amazon_India_2",	
        "Clothing_and_Accessories"                  :   "Amazon_India_3",	
        "Computers_and_Accessories"                 :   "Amazon_India_4",	
        "Electronics"                               :   "Amazon_India_5",	
        "Health_and_Personal_Care"                  :   "Amazon_India_6",	
        "Home_and_Kitchen"                          :   "Amazon_India_7",	
        "Industrial_and_Scientific"                 :   "Amazon_India_8",
        "Outdoor_Living"                            :   "Amazon_India_9",
        "Pet_Supplies"                              :   "Amazon_India_10",
        "Shoes_and_Handbags"                        :   "Amazon_India_11",	
        "Sports__Fitness_and_Outdoors"              :   "Amazon_India_12",	
        "Toys_and_Games"                            :   "Amazon_India_13",
        "Watches"                                   :   "NA",
        "Jewellery"                                 :   "Amazon_India_15",
        "Bags__Wallets_and_Luggage"                 :   "Amazon_India_16",
        "Baby"                                      :   "Amazon_India_17",
        "Books"                                     :   "NA",
        "Office_Products"                           :   "Amazon_India_18",
        "Software"                                  :   "Amazon_India_19",
        "Video_Games"                               :   "Amazon_India_20",
        "GAGF"                                      :   "Amazon_India_21",
        "MI"                                        :   "Amazon_India_22"
   },
   "Amazon_USA":{
        "Level_0_Images"                            :   "Amazon_USA_0",
        "Accessories"                               :   "Amazon_USA_1",
        "AAC"                                       :   "Amazon_USA_2",
        "Automotive"                                :   "Amazon_USA_3",
        "Baby"                                      :   "Amazon_USA_4",
        "BAPC"                                      :   "Amazon_USA_5",
        "Clothing"                                  :   "Amazon_USA_6",
        "Computers"                                 :   "Amazon_USA_7",
        "Electronics"                               :   "Amazon_USA_8",
        "HAH"                                       :   "Amazon_USA_9",
        "HAK"                                       :   "Amazon_USA_10",
        "IAS"                                       :   "Amazon_USA_11",
        "Jewelry"                                   :   "Amazon_USA_12",
        "Luggage"                                   :   "Amazon_USA_13",
        "PS"                                        :   "Amazon_USA_14",
        "Shoes"                                     :   "Amazon_USA_15",
        "Software"                                  :   "Amazon_USA_16",
        "SAO"                                       :   "Amazon_USA_17",
        "TAHI"                                      :   "Amazon_USA_18",
        "TAG"                                       :   "Amazon_USA_19",
        "VG"                                        :   "Amazon_USA_20",
        "Watches"                                   :   "Amazon_USA_21"
   },
   "Flipkart":{
        "Level_0_Images"                            :   "Flipkart_0",
        "AAV"                                       :   "Flipkart_1",
        "AAR"                                       :   "Flipkart_2",
        "Automotive"                                :   "Flipkart_3",
        "BC"                                        :   "Flipkart_4",
        "BWAB"                                      :   "Flipkart_5",
        "BAG"                                       :   "Flipkart_6",
        "Books"                                     :   "NA",
        "BMAS"                                      :   "Flipkart_8",
        "CA"                                        :   "Flipkart_9",
        "Clothing"                                  :   "Flipkart_10",
        "Computers"                                 :   "Flipkart_11",
        "EAF"                                       :   "Flipkart_12",
        "FDAG"                                      :   "Flipkart_13",
        "FAN"                                       :   "Flipkart_14",
        "Footwear"                                  :   "Flipkart_15",
        "Furniture"                                 :   "Flipkart_16",
        "Gaming"                                    :   "Flipkart_17",
        "HAPCA"                                     :   "Flipkart_18",
        "HC"                                        :   "Flipkart_19",
        "HAK"                                       :   "Flipkart_20",
        "HCABA"                                     :   "Flipkart_21",
        "HD"                                        :   "Flipkart_22",
        "HE"                                        :   "Flipkart_23",
        "HF"                                        :   "Flipkart_24",
        "HI"                                        :   "Flipkart_25",
        "HL"                                        :   "Flipkart_26",
        "IASS"                                      :   "Flipkart_27",
        "Jewellery"                                 :   "Flipkart_28",
        "KA"                                        :   "NA",
        "KCAS"                                      :   "Flipkart_30",
        "MAA"                                       :   "Flipkart_31",
        "MMAP"                                      :   "NA",
        "MI"                                        :   "Flipkart_33",
        "PAS"                                       :   "Flipkart_34",
        "PS"                                        :   "Flipkart_35",
        "Sports"                                    :   "Flipkart_36",
        "Toys"                                      :   "Flipkart_37",
        "Watches"                                   :   "NA",
        "WSD"                                       :   "NA"
   },
   "eBay":{
      "Level_0_Images"     :"eBay_0",
      "BAI"                :"eBay_1",
      "CAA"                :"eBay_2",
      "Electronics"        :"eBay_3",
      "Fashion"            :"eBay_4",
      "HAB"                :"eBay_5",
      "HAG"                :"eBay_6",
      "TAH"                :"eBay_7",
      "BMAM"               :"eBay_8"
   },
   "Bonanza":{
      "Level_0_Images"        :"Bonanza_0",
      "Antiques"              :"Bonanza_1",
      "Baby"                  :"Bonanza_2",
      "Books"                 :"Bonanza_3",
      "BAI"                   :"Bonanza_4",
      "CAP"                   :"Bonanza_5",
      "CPAA"                  :"Bonanza_6",
      "CAPM"                  :"Bonanza_7",
      "Collectibles"          :"Bonanza_8",
      "CAN"                   :"Bonanza_9",
      "CE"                    :"Bonanza_10",
      "Crafts"                :"Bonanza_11",
      "DAB"                   :"Bonanza_12",
      "EM"                    :"Bonanza_13",
      "EE"                    :"Bonanza_14",
      "Fashion"               :"Bonanza_15",
      "HAB"                   :"Bonanza_16",
      "HAG"                   :"Bonanza_17"
   },
   "Etsy":{
      "Level_0_Images"     :"Etsy_0",
      "Accessories"        :"Etsy_1",
      "AAC"                :"Etsy_2",
      "BAP"                :"Etsy_3",
      "BAB"                :"Etsy_4",
      "BFAM"               :"Etsy_5",
      "Clothing"           :"Etsy_6",
      "CSAT"               :"Etsy_7",
      "EAA"                :"Etsy_8",
      "HAL"                :"Etsy_9",
      "Jewellery"          :"Etsy_10",
      "PAPS"               :"Etsy_11",
      "PS"                 :"Etsy_12",
      "Shoes"              :"Etsy_13",
      "TAG"                :"Etsy_14",
      "Wedding"            :"Etsy_15"
   }
}

NA_model_names = {
   "Amazon_India":{
      "Watches"                                   :   "Accessories",
      "Books"                                     :   "Books",
      "Jewellery"                                 :   "Jewellery"
   },
   "Amazon_USA":{
      "Accessories"                               :   "Accessories"
   },
   "Flipkart":{
      # "Automotive"                                :   "CABA",
      "Books"                                     :   "Books",
      "MMAP"                                      :   "MATS",
      "KA"                                        :   "SS",
      # "Sports"                                    :   "Sports",
      "Watches"                                   :   "WA",
      "WSD"                                       :   "WA"
   }
}

error_codes = {
    
    "REQUIRED_FIELD_IS_MISSING": {
        "error_code":"",
        "message": "Required fied is not given"
    },
}

cat_sub_cat_abbreviations = { 
   'Amazon_India':{ 
      'Beauty':{ 
         'BAB':{ 
            'category_name':'Beauty',
            'sub_category_name':'Bath_and_Body'
         },
         'Fragrance':{ 
            'category_name':'Beauty',
            'sub_category_name':'Fragrance'
         },
         'HCAS':{ 
            'category_name':'Beauty',
            'sub_category_name':'Hair_Care_and_Styling'
         },
         'MUAN':{ 
            'category_name':'Beauty',
            'sub_category_name':'Make_up_and_Nails'
         },
         'SC':{ 
            'category_name':'Beauty',
            'sub_category_name':'Skin_Care'
         },
         'TAA':{ 
            'category_name':'Beauty',
            'sub_category_name':'Tools_and_Accessories'
         }
      },
      'Car_and_Motorbike':{ 
         'CP':{ 
            'category_name':'Car_and_Motorbike',
            'sub_category_name':'Car_Parts'
         },
         'CTAR':{ 
            'category_name':'Car_and_Motorbike',
            'sub_category_name':'Car_Tyres_and_Rims'
         },
         'CAMC':{ 
            'category_name':'Car_and_Motorbike',
            'sub_category_name':'Car_and_Motorbike_Care'
         },
         'CAVE':{ 
            'category_name':'Car_and_Motorbike',
            'sub_category_name':'Car_and_Vehicle_Electronics'
         },
         'GAM':{ 
            'category_name':'Car_and_Motorbike',
            'sub_category_name':'Gifts_and_Merchandise'
         },
         'MAAP':{ 
            'category_name':'Car_and_Motorbike',
            'sub_category_name':'Motorbike_Accessories_and_Parts'
         },
         'OAF':{ 
            'category_name':'Car_and_Motorbike',
            'sub_category_name':'Oils_and_Fluids'
         },
         'Paintwork':{ 
            'category_name':'Car_and_Motorbike',
            'sub_category_name':'Paintwork'
         }
      },
      'Clothing_and_Accessories':{ 
         'Baby':{ 
            'category_name':'Clothing_and_Accessories',
            'sub_category_name':'Baby'
         },
         'Boys':{ 
            'category_name':'Clothing_and_Accessories',
            'sub_category_name':'Boys'
         },
         'Girls':{ 
            'category_name':'Clothing_and_Accessories',
            'sub_category_name':'Girls'
         },
         'Men':{ 
            'category_name':'Clothing_and_Accessories',
            'sub_category_name':'Men'
         },
         'Women':{ 
            'category_name':'Clothing_and_Accessories',
            'sub_category_name':'Women'
         }
      },
      'Computers_and_Accessories':{ 
         'AAP':{ 
            'category_name':'Computers_and_Accessories',
            'sub_category_name':'Accessories_and_Peripherals'
         },
         'Components':{ 
            'category_name':'Computers_and_Accessories',
            'sub_category_name':'Components'
         },
         'Desktops':{ 
            'category_name':'Computers_and_Accessories',
            'sub_category_name':'Desktops'
         },
         'EDADS':{ 
            'category_name':'Computers_and_Accessories',
            'sub_category_name':'External_Devices_and_Data_Storage'
         },
         'ND':{ 
            'category_name':'Computers_and_Accessories',
            'sub_category_name':'Networking_Devices'
         },
         'Laptops':{ 
            'category_name':'Computers_and_Accessories',
            'sub_category_name':'Laptops'
         },
         'Monitors':{ 
            'category_name':'Computers_and_Accessories',
            'sub_category_name':'Monitors'
         },
         'Scanners':{ 
            'category_name':'Computers_and_Accessories',
            'sub_category_name':'Scanners'
         },
         'Tablets':{ 
            'category_name':'Computers_and_Accessories',
            'sub_category_name':'Tablets'
         },
         'Warranties':{ 
            'category_name':'Computers_and_Accessories',
            'sub_category_name':'Warranties'
         }
      },
      'Health_and_Personal_Care':{ 
         'BAS':{ 
            'category_name':'Health_and_Personal_Care',
            'sub_category_name':'Bath_and_Shower'
         },
         'BTAA':{ 
            'category_name':'Health_and_Personal_Care',
            'sub_category_name':'Beauty_Tools_and_Accessories'
         },
         'DAN':{ 
            'category_name':'Health_and_Personal_Care',
            'sub_category_name':'Diet_and_Nutrition'
         },
         'HCAS':{ 
            'category_name':'Health_and_Personal_Care',
            'sub_category_name':'Hair_Care_and_Styling'
         },
         'HC':{ 
            'category_name':'Health_and_Personal_Care',
            'sub_category_name':'Health_Care'
         },
         'HMSAE':{ 
            'category_name':'Health_and_Personal_Care',
            'sub_category_name':'Home_Medical_Supplies_and_Equipment'
         },
         'HS':{ 
            'category_name':'Health_and_Personal_Care',
            'sub_category_name':'Household_Supplies'
         },
         'PC':{ 
            'category_name':'Health_and_Personal_Care',
            'sub_category_name':'Personal_Care'
         },
         'PCAHA':{ 
            'category_name':'Health_and_Personal_Care',
            'sub_category_name':'Personal_Care_and_Health_Appliances'
         },
         'SWAS':{ 
            'category_name':'Health_and_Personal_Care',
            'sub_category_name':'Sexual_Wellness_and_Sensuality'
         },
         'SC':{ 
            'category_name':'Health_and_Personal_Care',
            'sub_category_name':'Skin_Care'
         }
      },
      'Electronics':{ 
         'Accessories':{ 
            'category_name':'Electronics',
            'sub_category_name':'Accessories'
         },
         'CAP':{ 
            'category_name':'Electronics',
            'sub_category_name':'Cameras_and_Photography'
         },
         'CAVE':{ 
            'category_name':'Electronics',
            'sub_category_name':'Car_and_Vehicle_Electronics'
         },
         'CompAA':{ 
            'category_name':'Electronics',
            'sub_category_name':'Computers_and_Accessories'
         },
         'GAA':{ 
            'category_name':'Electronics',
            'sub_category_name':'GPS_and_Accessories'
         },
         'HA':{ 
            'category_name':'Electronics',
            'sub_category_name':'Home_Audio'
         },
         'HTTAV':{ 
            'category_name':'Electronics',
            'sub_category_name':'Home_Theater__TV_and_Video'
         },
         'MAA':{ 
            'category_name':'Electronics',
            'sub_category_name':'Mobiles_and_Accessories'
         },
         'PMP':{ 
            'category_name':'Electronics',
            'sub_category_name':'Portable_Media_Players'
         },
         'TAA':{ 
            'category_name':'Electronics',
            'sub_category_name':'Telephones_and_Accessories'
         },
         'Warranties':{ 
            'category_name':'Electronics',
            'sub_category_name':'Warranties'
         }
      },
      'Home_and_Kitchen':{ 
         'Artwork':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Artwork'
         },
         'CM':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Craft_Materials'
         },
         'FF':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Fresh_Flowers'
         },
         'Furniture':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Furniture'
         },
         'HCAAQ':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Heating__Cooling_and_Air_Quality'
         },
         'HF':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Home_Furnishing'
         },
         'HI':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Home_Improvement'
         },
         'HSAO':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Home_Storage_and_Organization'
         },
         'HAD':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Home_and_Décor'
         },
         'IL':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Indoor_Lighting'
         },
         'KAD':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Kitchen_and_Dining'
         },
         'KAHA':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Kitchen_and_Home_Appliances'
         },
         'LA':{ 
            'category_name':'Home_and_Kitchen',
            'sub_category_name':'Large_Appliances'
         }
      },
      'Industrial_and_Scientific':{ 
         'CDP':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Commercial_Door_Products'
         },
         'CT ':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Cutting_Tools'
         },
         'Fasteners':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Fasteners'
         },
         'Filtration':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Filtration'
         },
         'FSEAS':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Food_Service_Equipment_and_Supplies'
         },
         'HPAP':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Hydraulics__Pneumatics_and_Plumbing'
         },
         'IE':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Industrial_Electrical'
         },
         'JASS':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Janitorial_and_Sanitation_Supplies'
         },
         'LASP':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Lab_and_Scientific_Products'
         },
         'MHP':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Material_Handling_Products'
         },
         'OHASP':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Occupational_Health_and_Safety_Products'
         },
         'PASS':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Packaging_and_Shipping_Supplies'
         },
         'PAHT':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Power_and_Hand_Tools'
         },
         'PDS':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Professional_Dental_Supplies'
         },
         'PMS':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Professional_Medical_Supplies'
         },
         'PTP':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Power_Transmission_Products'
         },
         'Robotics':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Robotics'
         },
         'TAAS':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Tapes__Adhesives_and_Sealers'
         },
         'TMAI':{ 
            'category_name':'Industrial_and_Scientific',
            'sub_category_name':'Test__Measure_and_Inspect'
         }
      },
      'Outdoor_Living':{ 
         'BBS':{ 
            'category_name':'Outdoor_Living',
            'sub_category_name':'Backyard_Birding_Supplies'
         },
         'BAOD':{ 
            'category_name':'Outdoor_Living',
            'sub_category_name':'Barbecue_and_Outdoor_Dining'
         },
         'GAOF':{ 
            'category_name':'Outdoor_Living',
            'sub_category_name':'Garden_and_Outdoor_Furniture'
         },
         'Gardening':{ 
            'category_name':'Outdoor_Living',
            'sub_category_name':'Gardening'
         },
         'MAOPT':{ 
            'category_name':'Outdoor_Living',
            'sub_category_name':'Mowers_and_Outdoor_Power_Tools'
         },
         'OD':{ 
            'category_name':'Outdoor_Living',
            'sub_category_name':'Outdoor_Décor'
         },
         'PC':{ 
            'category_name':'Outdoor_Living',
            'sub_category_name':'Pest_Control'
         },
         'PSAB':{ 
            'category_name':'Outdoor_Living',
            'sub_category_name':'Plants__Seeds_and_Bulbs'
         },
         'SAWP':{ 
            'category_name':'Outdoor_Living',
            'sub_category_name':'Solar_and_Wind_Power'
         }
      },
      'Pet_Supplies':{ 
         'Birds':{ 
            'category_name':'Pet_Supplies',
            'sub_category_name':'Birds'
         },
         'Cats':{ 
            'category_name':'Pet_Supplies',
            'sub_category_name':'Cats'
         },
         'Dogs':{ 
            'category_name':'Pet_Supplies',
            'sub_category_name':'Dogs'
         },
         'FAA':{ 
            'category_name':'Pet_Supplies',
            'sub_category_name':'Fish_and_Aquatics'
         }
      },
      'Shoes_and_Handbags':{ 
         'HPAC':{ 
            'category_name':'Shoes_and_Handbags',
            'sub_category_name':'Handbags__Purses_and_Clutches'
         },
         'SCAA':{ 
            'category_name':'Shoes_and_Handbags',
            'sub_category_name':'Shoe_Care_and_Accessories'
         },
         'Shoes':{ 
            'category_name':'Shoes_and_Handbags',
            'sub_category_name':'Shoes'
         }
      },
      'Sports__Fitness_and_Outdoors':{ 
         'Accessories':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Accessories'
         },
         'Archery':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Archery'
         },
         'Badminton':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Badminton'
         },
         'Baseball':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Baseball'
         },
         'Basketball':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Basketball'
         },
         'Billiards':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Billiards'
         },
         'Boxing':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Boxing'
         },
         'CAH':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Camping_and_Hiking'
         },
         'Climbing':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Climbing'
         },
         'Cricket':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Cricket'
         },
         'Cycling':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Cycling'
         },
         'DAD':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Darts_and_Dartboards'
         },
         'DS':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Disc_Sports'
         },
         'ES':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Equestrian_Sports'
         },
         'EAF':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Exercise_and_Fitness'
         },
         'FS':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Fan_Shop'
         },
         'FH':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Field_Hockey'
         },
         'Fishing':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Fishing'
         },
         'Football':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Football'
         },
         'Footwear':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Footwear'
         },
         'Golf':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Golf'
         },
         'Gymnastics':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Gymnastics'
         },
         'MA':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Martial_Arts'
         },
         'Rugby':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Rugby'
         },
         'Running':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Running'
         },
         'SSAS':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Skates__Skateboards_and_Scooters'
         },
         'Snooker':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Snooker'
         },
         'SC':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Sports_Clothing'
         },
         'SG':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Sports_Gadgets'
         },
         'Squash':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Squash'
         },
         'TT':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Table_Tennis'
         },
         'TH':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Team_Handball'
         },
         'Tennis':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Tennis'
         },
         'TAF':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Track_and_Field'
         },
         'Volleyball':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Volleyball'
         },
         'WS':{ 
            'category_name':'Sports__Fitness_and_Outdoors',
            'sub_category_name':'Water_Sports'
         }
      },
      'Toys_and_Games':{ 
         'AATF':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Action_and_Toy_Figures'
         },
         'AAC':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Arts_and_Crafts'
         },
         'BATT':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Baby_and_Toddler_Toys'
         },
         'BACT':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Building_and_Construction_Toys'
         },
         'BTARO':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Bikes__Trikes_and_Ride_Ons'
         },
         'CAJ':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Cosmetics_and_Jewellery'
         },
         'CASC':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Coin_and_Stamp_Collecting'
         },
         'CTCAA':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Collectible_Trading_Cards_and_Accessories'
         },
         'DCATV':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Die_Cast_and_Toy_Vehicles'
         },
         'DAA':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Dolls_and_Accessories'
         },
         'DUAC':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Dressing_Up_and_Costumes'
         },
         'ET':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Electronic_Toys'
         },
         'Games':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Games'
         },
         'LAE':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Learning_and_Education'
         },
         'MBK':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Model_Building_Kits'
         },
         'MTARS':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Model_Trains_and_Railway_Sets'
         },
         'MR':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Marble_Runs'
         },
         'MTI':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Musical_Toy_Instruments'
         },
         'NAGT':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Novelty_and_Gag_Toys'
         },
         'PS':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Party_Supplies'
         },
         'PP':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Pretend_Play'
         },
         'PAPT':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Puppets_and_Puppet_Theatres'
         },
         'Puzzles':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Puzzles'
         },
         'RARC':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Radio_and_Remote_Control'
         },
         'RFA':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Real_Food_Appliances'
         },
         'SS':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'School_Supplies'
         },
         'SAO':{ 
            'category_name':'Toys_and_Games',
            'sub_category_name':'Sport_and_Outdoor'
         }
      },
      'Office_Products':{ 
         'EAPS':{ 
            'category_name':'Office_Products',
            'sub_category_name':'Envelopes_and_Postal_Supplies'
         },
         'CPAPO':{ 
            'category_name':'Office_Products',
            'sub_category_name':'Calendars_Planners_and_Personal_Organisers'
         },
         'Calculators':{ 
            'category_name':'Office_Products',
            'sub_category_name':'Calculators'
         },
         'OE':{ 
            'category_name':'Office_Products',
            'sub_category_name':'Office_Electronics'
         },
         'OPP':{ 
            'category_name':'Office_Products',
            'sub_category_name':'Office_Paper_Products'
         },
         'OS':{ 
            'category_name':'Office_Products',
            'sub_category_name':'Office_Supplies'
         },
         'Stationery':{ 
            'category_name':'Office_Products',
            'sub_category_name':'Stationery'
         }
      },
      'Jewellery':{ 
         'Women':{
            'category_name':'Jewellery',
            'sub_category_name':'Women'
         },
         'Girls':{
            'category_name':'Jewellery',
            'sub_category_name':'Girls'
         },
         'Boys':{
            'category_name':'Jewellery',
            'sub_category_name':'Boys'
         },
         'Men':{
            'category_name':'Jewellery',
            'sub_category_name':'Men'
         },
         'JBAC':{
            'category_name':'Jewellery',
            'sub_category_name':'Jewellery_Boxes_and_Care'
         }
      },
      'Bags__Wallets_and_Luggage':{ 
         'BAB':{ 
            'category_name':'Bags__Wallets_and_Luggage',
            'sub_category_name':'Bags_and_Backpacks'
         },
         'HAC':{ 
            'category_name':'Bags__Wallets_and_Luggage',
            'sub_category_name':'Handbags_and_Clutches'
         },
         'Luggage':{ 
            'category_name':'Bags__Wallets_and_Luggage',
            'sub_category_name':'Luggage'
         },
         'TA':{ 
            'category_name':'Bags__Wallets_and_Luggage',
            'sub_category_name':'Travel_Accessories'
         },
         'WCCAMO':{ 
            'category_name':'Bags__Wallets_and_Luggage',
            'sub_category_name':'Wallets__Card_Cases_and_Money_Organizers'
         }
      },
      'Baby':{ 
         'AAPT':{ 
            'category_name':'Baby',
            'sub_category_name':'Activity_and_Play_Time'
         },
         'BC':{ 
            'category_name':'Baby',
            'sub_category_name':'Baby_Care'
         },
         'Baby_Clothing':{ 
            'category_name':'Baby',
            'sub_category_name':'Baby_Clothing'
         },
         'BFARD':{ 
            'category_name':'Baby',
            'sub_category_name':'Bedding__Furniture_and_Room_Décor'
         },
         'BS':{ 
            'category_name':'Baby',
            'sub_category_name':'Baby_Safety'
         },
         'CSAA':{ 
            'category_name':'Baby',
            'sub_category_name':'Car_Seats_and_Accessories'
         },
         'DANC':{ 
            'category_name':'Baby',
            'sub_category_name':'Diapering_and_Nappy_Changing'
         },
         'Feeding':{ 
            'category_name':'Baby',
            'sub_category_name':'Feeding'
         },
         'Maternity':{ 
            'category_name':'Baby',
            'sub_category_name':'Maternity'
         },
         'PAT':{ 
            'category_name':'Baby',
            'sub_category_name':'Pacifiers_and_Teethers'
         },
         'PTASS':{ 
            'category_name':'Baby',
            'sub_category_name':'Potty_Training_and_Step_Stools'
         },
         'SBAP':{ 
            'category_name':'Baby',
            'sub_category_name':'Strollers__Buggies_and_Prams'
         }
      },
      'Video_Games':{ 
         'MAH':{ 
            'category_name':'Video_Games',
            'sub_category_name':'Microconsoles_and_Handhelds'
         },
         'N3':{ 
            'category_name':'Video_Games',
            'sub_category_name':'Nintendo_3DS'
         },
         'ND':{ 
            'category_name':'Video_Games',
            'sub_category_name':'Nintendo_DS'
         },
         'P2':{ 
            'category_name':'Video_Games',
            'sub_category_name':'PlayStation_2'
         },
         'P3':{ 
            'category_name':'Video_Games',
            'sub_category_name':'PlayStation_3'
         },
         'P4':{ 
            'category_name':'Video_Games',
            'sub_category_name':'PlayStation_4'
         },
         'PG':{ 
            'category_name':'Video_Games',
            'sub_category_name':'PC_Games'
         },
         'PSP':{ 
            'category_name':'Video_Games',
            'sub_category_name':'PSP'
         },
         'PV':{ 
            'category_name':'Video_Games',
            'sub_category_name':'PlayStation_Vita'
         },
         'Wii':{ 
            'category_name':'Video_Games',
            'sub_category_name':'Wii'
         },
         'WU':{ 
            'category_name':'Video_Games',
            'sub_category_name':'Wii_U'
         },
         'X3':{ 
            'category_name':'Video_Games',
            'sub_category_name':'Xbox_360'
         },
         'PAWD':{ 
            'category_name':'Video_Games',
            'sub_category_name':'Programming_and_Web_Development'
         },
         'SUS':{ 
            'category_name':'Video_Games',
            'sub_category_name':'System_Utility_Software'
         }
      },
      'Software':{ 
         'AAF':{ 
            'category_name':'Software',
            'sub_category_name':'Accounting_and_Finance'
         },
         'AAS':{ 
            'category_name':'Software',
            'sub_category_name':'Antivirus_and_Security'
         },
         'BAO':{ 
            'category_name':'Software',
            'sub_category_name':'Business_and_Office'
         },
         'CS':{ 
            'category_name':'Software',
            'sub_category_name':'Childrens_Software'
         },
         'EAR':{ 
            'category_name':'Software',
            'sub_category_name':'Education_and_Reference'
         },
         'GAD':{ 
            'category_name':'Software',
            'sub_category_name':'Graphics_and_Design'
         },
         'OS':{ 
            'category_name':'Software',
            'sub_category_name':'Operating_Systems'
         }
      },
      'Watches':{ 
         'Watches':{ 
            'category_name':'Watches',
            'sub_category_name':'Watches'
         }
      },
      'Books':{ 
         'Books':{ 
            'category_name':'Books',
            'sub_category_name':'Books'
         }
      },
      'Music':{ 
         'IC':{ 
            'category_name':'Music',
            'sub_category_name':'Indian_Classical'
         },
         'WM':{ 
            'category_name':'Music',
            'sub_category_name':'World_Music'
         }
      },
      'MI':{ 
         'BGAG':{ 
            'category_name':'Musical_Instruments',
            'sub_category_name':'Bass_Guitars_and_Gear'
         },
         'DAVE':{ 
            'category_name':'Musical_Instruments',
            'sub_category_name':'DJ_and_VJ_Equipment'
         },
         'DAP':{ 
            'category_name':'Musical_Instruments',
            'sub_category_name':'Drums_and_Percussion'
         },
         'GAG':{ 
            'category_name':'Musical_Instruments',
            'sub_category_name':'Guitars_and_Gear'
         },
         'KE':{ 
            'category_name':'Musical_Instruments',
            'sub_category_name':'Karaoke_Equipment'
         },
         'Microphones':{ 
            'category_name':'Musical_Instruments',
            'sub_category_name':'Microphones'
         },
         'PAS':{ 
            'category_name':'Musical_Instruments',
            'sub_category_name':'PA_and_Stage'
         },
         'PAK':{ 
            'category_name':'Musical_Instruments',
            'sub_category_name':'Piano_and_Keyboard'
         },
         'RAC':{ 
            'category_name':'Musical_Instruments',
            'sub_category_name':'Recording_and_Computer'
         },
         'SI':{ 
            'category_name':'Musical_Instruments',
            'sub_category_name':'String_Instruments'
         },
         'WI':{ 
            'category_name':'Musical_Instruments',
            'sub_category_name':'Wind_Instruments'
         }
      },
      'GAGF':{ 
         'CAJF':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Canned_and_Jarred_Food'
         },
         'CAM':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Cereal_and_Muesli'
         },
         'CTAB':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Coffee__Tea_and_Beverages'
         },
         'CABS':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Cooking_and_Baking_Supplies'
         },
         'DFNAS':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Dried_Fruits__Nuts_and_Seeds'
         },
         'HAGG':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Hampers_and_Gourmet_Gifts'
         },
         'JHAS':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Jams__Honey_and_Spreads'
         },
         'PAN':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Pasta_and_Noodles'
         },
         'Pickles':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Pickles'
         },
         'RTEAC':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Ready_To_Eat_and_Cook'
         },
         'SF':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Snack_Foods'
         },
         'SCAG':{ 
            'category_name':'Grocery_and_Gourmet_Foods',
            'sub_category_name':'Sweets__Chocolate_and_Gum'
         }
      }
   },
   "Amazon_USA":{
      "AAC":{
         "BAJM":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Beading_and_Jewelry_Making"
         },
         "Crafting":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Crafting"
         },
         "FD":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Fabric_Decorating"
         },
         "GWS":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Gift_Wrapping_Supplies"
         },
         "KAC":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Knitting_and_Crochet"
         },
         "Needlework":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Needlework"
         },
         "OSAT":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Organization__Storage_and_Transport"
         },
         "PDAAS":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Painting__Drawing_and_Art_Supplies"
         },
         "PDAS":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Party_Decorations_and_Supplies"
         },
         "Printmaking":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Printmaking"
         },
         "SAS":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Scrapbooking_and_Stamping"
         },
         "Sewing":{
               "category_name":"Arts_and_Crafts",
               "sub_category_name":"Sewing"
         }
      },
      "Automotive":{
         "CC":{
               "category_name":"Automotive",
               "sub_category_name":"Car_Care"
         },
         "CEAA":{
               "category_name":"Automotive",
               "sub_category_name":"Car_Electronics_and_Accessories"
         },
         "EA":{
               "category_name":"Automotive",
               "sub_category_name":"Exterior_Accessories"
         },
         "HDACVE":{
               "category_name":"Automotive",
               "sub_category_name":"Heavy_Duty_and_Commercial_Vehicle_Equipment"
         },
         "IA":{
               "category_name":"Automotive",
               "sub_category_name":"Interior_Accessories"
         },
         "LALA":{
               "category_name":"Automotive",
               "sub_category_name":"Lights_and_Lighting_Accessories"
         },
         "MAP":{
               "category_name":"Automotive",
               "sub_category_name":"Motorcycle_and_Powersports"
         },
         "OAF":{
               "category_name":"Automotive",
               "sub_category_name":"Oils_and_Fluids"
         },
         "PAPS":{
               "category_name":"Automotive",
               "sub_category_name":"Paint_and_Paint_Supplies"
         },
         "PPAA":{
               "category_name":"Automotive",
               "sub_category_name":"Performance_Parts_and_Accessories"
         },
         "RP":{
               "category_name":"Automotive",
               "sub_category_name":"RV_Parts_and_Accessories"
         },
         "RPAA":{
               "category_name":"Automotive",
               "sub_category_name":"Replacement_Parts"
         },
         "TAE":{
               "category_name":"Automotive",
               "sub_category_name":"Tires_and_Wheels"
         },
         "TAW":{
               "category_name":"Automotive",
               "sub_category_name":"Tools_and_Equipment"
         }
      },
      "BAPC":{
         "FHANC":{
            "category_name":"Beauty_and_Personal_Care",
            "sub_category_name":"Foot__Hand_and_Nail_Care"
         },
         "Fragrance":{
            "category_name":"Beauty_and_Personal_Care",
            "sub_category_name":"Fragrance"
         },
         "HC":{
            "category_name":"Beauty_and_Personal_Care",
            "sub_category_name":"Hair_Care"
         },
         "Makeup":{
            "category_name":"Beauty_and_Personal_Care",
            "sub_category_name":"Makeup"
         },
         "OC":{
            "category_name":"Beauty_and_Personal_Care",
            "sub_category_name":"Oral_Care"
         },
         "PC":{
            "category_name":"Beauty_and_Personal_Care",
            "sub_category_name":"Personal_Care"
         },
         "SAHR":{
            "category_name":"Beauty_and_Personal_Care",
            "sub_category_name":"Shave_and_Hair_Removal"
         },
         "SC":{
            "category_name":"Beauty_and_Personal_Care",
            "sub_category_name":"Skin_Care"
         },
         "TAA":{
            "category_name":"Beauty_and_Personal_Care",
            "sub_category_name":"Tools_and_Accessories"
         }
      },
      "Baby":{
         "AAA":{
            "category_name":"Baby",
            "sub_category_name":"Apparel_and_Accessories"
         },
         "AAE":{
            "category_name":"Baby",
            "sub_category_name":"Activity_and_Entertainment"
         },
         "BC":{
            "category_name":"Baby",
            "sub_category_name":"Baby_Care"
         },
         "BS":{
            "category_name":"Baby",
            "sub_category_name":"Baby_Stationery"
         },
         "BATT":{
            "category_name":"Baby",
            "sub_category_name":"Baby_and_Toddler_Toys"
         },
         "CSAA":{
            "category_name":"Baby",
            "sub_category_name":"Car_Seats_and_Accessories"
         },
         "Diapering":{
            "category_name":"Baby",
            "sub_category_name":"Diapering"
         },
         "Feeding":{
            "category_name":"Baby",
            "sub_category_name":"Feeding"
         },
         "Gifts":{
            "category_name":"Baby",
            "sub_category_name":"Gifts"
         },
         "Nursery":{
            "category_name":"Baby",
            "sub_category_name":"Nursery"
         },
         "PAM":{
            "category_name":"Baby",
            "sub_category_name":"Pregnancy_and_Maternity"
         },
         "Safety":{
            "category_name":"Baby",
            "sub_category_name":"Safety"
         },
         "SAA":{
            "category_name":"Baby",
            "sub_category_name":"Strollers_and_Accessories"
         },
         "TG":{
            "category_name":"Baby",
            "sub_category_name":"Travel_Gear"
         }
      },
      "Clothing":{
         "MF":{
            "category_name":"Clothing",
            "sub_category_name":"Mens_Fashion"
         },
         "BF":{
            "category_name":"Clothing",
            "sub_category_name":"Boys_Fashion"
         },
         "WF":{
            "category_name":"Clothing",
            "sub_category_name":"Womens_Fashion"
         },
         "GF":{
            "category_name":"Clothing",
            "sub_category_name":"Girls_Fashion"
         }
      },
      "Computers":{
         "CAAP":{
            "category_name":"Computers",
            "sub_category_name":"Computer_Accessories_and_Peripherals"
         },
         "TRP":{
            "category_name":"Computers",
            "sub_category_name":"Tablet_Replacement_Parts"
         },
         "Scanners":{
            "category_name":"Computers",
            "sub_category_name":"Scanners"
         },
         "DS":{
            "category_name":"Computers",
            "sub_category_name":"Data_Storage"
         },
         "WAS":{
            "category_name":"Computers",
            "sub_category_name":"Warranties_and_Services"
         },
         "PSASP":{
            "category_name":"Computers",
            "sub_category_name":"Power_Strips_and_Surge_Protectors"
         },
         "CC":{
            "category_name":"Computers",
            "sub_category_name":"Computer_Components"
         },
         "Printers":{
            "category_name":"Computers",
            "sub_category_name":"Printers"
         },
         "TA":{
            "category_name":"Computers",
            "sub_category_name":"Tablet_Accessories"
         },
         "LA":{
            "category_name":"Computers",
            "sub_category_name":"Laptop_Accessories"
         },
         "CAT":{
            "category_name":"Computers",
            "sub_category_name":"Computers_and_Tablets"
         },
         "NP":{
            "category_name":"Computers",
            "sub_category_name":"Networking_Products"
         }
      },
      "Electronics":{
         "WT":{
            "category_name":"Electronics",
            "sub_category_name":"Wearable_Technology"
         },
         "VGCAA":{
            "category_name":"Electronics",
            "sub_category_name":"Video_Game_Consoles_and_Accessories"
         },
         "OE":{
            "category_name":"Electronics",
            "sub_category_name":"Office_Electronics"
         },
         "ERAA":{
            "category_name":"Electronics",
            "sub_category_name":"eBook_Readers_and_Accessories"
         },
         "CAA":{
            "category_name":"Electronics",
            "sub_category_name":"Computers_and_Accessories"
         },
         "AAS":{
            "category_name":"Electronics",
            "sub_category_name":"Accessories_and_Supplies"
         },
         "SAS":{
            "category_name":"Electronics",
            "sub_category_name":"Security_and_Surveillance"
         },
         "TAV":{
            "category_name":"Electronics",
            "sub_category_name":"Television_and_Video"
         },
         "CAP":{
            "category_name":"Electronics",
            "sub_category_name":"Camera_and_Photo"
         },
         "Headphones":{
            "category_name":"Electronics",
            "sub_category_name":"Headphones"
         },
         "PAAV":{
            "category_name":"Electronics",
            "sub_category_name":"Portable_Audio_and_Video"
         },
         "SP":{
            "category_name":"Electronics",
            "sub_category_name":"Service_Plans"
         },
         "GFAA":{
            "category_name":"Electronics",
            "sub_category_name":"GPS__Finders_and_Accessories"
         },
         "CPAA":{
            "category_name":"Electronics",
            "sub_category_name":"Cell_Phones_and_Accessories"
         },
         "CAVE":{
            "category_name":"Electronics",
            "sub_category_name":"Car_and_Vehicle_Electronics"
         },
         "HA":{
            "category_name":"Electronics",
            "sub_category_name":"Home_Audio"
         }
      },
      "HAH":{
         "PC":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Personal_Care"
         },
         "SN":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Sports_Nutrition"
         },
         "SAGWS":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Stationery_and_Gift_Wrapping_Supplies"
         },
         "WAR":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Wellness_and_Relaxation"
         },
         "HC":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Health_Care"
         },
         "MSAE":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Medical_Supplies_and_Equipment"
         },
         "HS":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Household_Supplies"
         },
         "VC":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Vision_Care"
         },
         "SW":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Sexual_Wellness"
         },
         "VADS":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Vitamins_and_Dietary_Supplements"
         },
         "BACC":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Baby_and_Child_Care"
         },
         "OC":{
            "category_name":"Health_and_Household",
            "sub_category_name":"Oral_Care"
         }
      },
      "HAK":{  
         "SAO":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Storage_and_Organization"
         },
         "Furniture":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Furniture"
         },
         "Bedding":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Bedding"
         },
         "HCAAQ":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Heating__Cooling_and_Air_Quality"
         },
         "WA":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Wall_Art"
         },
         "CS":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Cleaning_Supplies"
         },
         "SD":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Seasonal_Décor"
         },
         "EAPS":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Event_and_Party_Supplies"
         },
         "Bath":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Bath"
         },
         "HD":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Home_Décor"
         },
         "KAD":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Kitchen_and_Dining"
         },
         "KHS":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Kids_Home_Store"
         },
         "VAFC":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Vacuums_and_Floor_Care"
         },
         "LACF":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Lighting_and_Ceiling_Fans"
         },
         "IAS":{
            "category_name":"Home_and_Kitchen",
            "sub_category_name":"Irons_and_Steamers"
         }
      },
      "IAS":{
         "MHP":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Material_Handling_Products"
         },
         "PTP":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Power_Transmission_Products"
         },
         "RSFAE":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Retail_Store_Fixtures_and_Equipment"
         },
         "AMP":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Additive_Manufacturing_Products"
         },
         "LASP":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Lab_and_Scientific_Products"
         },
         "Robotics":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Robotics"
         },
         "JASS":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Janitorial_and_Sanitation_Supplies"
         },
         "IE":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Industrial_Electrical"
         },
         "FSEAS":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Food_Service_Equipment_and_Supplies"
         },
         "TMAI":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Test__Measure_and_Inspect"
         },
         "CDP":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Commercial_Door_Products"
         },
         "CL":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Commercial_Lighting"
         },
         "PDS":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Professional_Dental_Supplies"
         },
         "ASAL":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Adhesives__Sealants_and_Lubricants"
         },
         "CT":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Cutting_Tools"
         },
         "AIE":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Agricultural_Irrigation_Equipment"
         },
         "SE":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Science_Education"
         },
         "OHASP":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Occupational_Health_and_Safety_Products"
         },
         "HPAP":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Hydraulics__Pneumatics_and_Plumbing"
         },
         "RM":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Raw_Materials"
         },
         "DS":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Digital_Signage"
         },
         "PMS":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Professional_Medical_Supplies"
         },
         "Fasteners":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Fasteners"
         },
         "IH":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Industrial_Hardware"
         },
         "Filtration":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Filtration"
         },
         "PAHT":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Power_and_Hand_Tools"
         },
         "PASS":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Packaging_and_Shipping_Supplies"
         },
         "AAFP":{
            "category_name":"Industrial_and_Scientific",
            "sub_category_name":"Abrasive_and_Finishing_Products"
         }
      },
      "Jewelry":{
         "BF":{
            "category_name":"Jewelry",
            "sub_category_name":"Boys_Fashion"
         },
         "WF":{
            "category_name":"Jewelry",
            "sub_category_name":"Womens_Fashion"
         },
         "GF":{
            "category_name":"Jewelry",
            "sub_category_name":"Girls_Fashion"
         }
      },
      "Luggage":{
         "Backpacks":{
            "category_name":"Luggage",
            "sub_category_name":"Backpacks"
         },
         "TA":{
            "category_name":"Luggage",
            "sub_category_name":"Travel_Accessories"
         },
         "LB":{
            "category_name":"Luggage",
            "sub_category_name":"Laptop_Bags"
         },
         "Umbrellas":{
            "category_name":"Luggage",
            "sub_category_name":"Umbrellas"
         }
      },
      "PS":{
         "Cats":{
            "category_name":"Pet_Supplies",
            "sub_category_name":"Cats"
         },
         "SA":{
            "category_name":"Pet_Supplies",
            "sub_category_name":"Small_Animals"
         },
         "Horses":{
            "category_name":"Pet_Supplies",
            "sub_category_name":"Horses"
         },
         "Birds":{
            "category_name":"Pet_Supplies",
            "sub_category_name":"Birds"
         },
         "RAA":{
            "category_name":"Pet_Supplies",
            "sub_category_name":"Reptiles_and_Amphibians"
         },
         "Dogs":{
            "category_name":"Pet_Supplies",
            "sub_category_name":"Dogs"
         },
         "FAAP":{
            "category_name":"Pet_Supplies",
            "sub_category_name":"Fish_and_Aquatic_Pets"
         }
      },
      "SAO":{
         "FS":{
            "category_name":"Sports_and_Outdoors",
            "sub_category_name":"Fan_Shop"
         },
         "OR":{
            "category_name":"Sports_and_Outdoors",
            "sub_category_name":"Outdoor_Recreation"
         },
         "SAF":{
            "category_name":"Sports_and_Outdoors",
            "sub_category_name":"Sports_and_Fitness"
         }
      },
      "Shoes":{
         "MF":{
            "category_name":"Shoes",
            "sub_category_name":"Mens_Fashion"
         },
         "BF":{
            "category_name":"Shoes",
            "sub_category_name":"Boys_Fashion"
         },
         "WF":{
            "category_name":"Shoes",
            "sub_category_name":"Womens_Fashion"
         },
         "GF":{
            "category_name":"Shoes",
            "sub_category_name":"Girls_Fashion"
         }
      },
      "Software":{
         "Music":{
            "category_name":"Software",
            "sub_category_name":"Music"
         },
         "BAO":{
            "category_name":"Software",
            "sub_category_name":"Business_and_Office"
         },
         "Video":{
            "category_name":"Software",
            "sub_category_name":"Video"
         },
         "PAWD":{
            "category_name":"Software",
            "sub_category_name":"Programming_and_Web_Development"
         },
         "LAH":{
            "category_name":"Software",
            "sub_category_name":"Lifestyle_and_Hobbies"
         },
         "AAS":{
            "category_name":"Software",
            "sub_category_name":"Antivirus_and_Security"
         },
         "Childrens":{
            "category_name":"Software",
            "sub_category_name":"Childrens"
         },
         "Utilities":{
            "category_name":"Software",
            "sub_category_name":"Utilities"
         },
         "AAF":{
            "category_name":"Software",
            "sub_category_name":"Accounting_and_Finance"
         },
         "NAS":{
            "category_name":"Software",
            "sub_category_name":"Networking_and_Servers"
         },
         "PAGD":{
            "category_name":"Software",
            "sub_category_name":"Photography_and_Graphic_Design"
         },
         "EAR":{
            "category_name":"Software",
            "sub_category_name":"Education_and_Reference"
         }  
      },
      "TAG":{
         "PV":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Play_Vehicles"
         },
         "PAPT":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Puppets_and_Puppet_Theaters"
         },
         "AAC":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Arts_and_Crafts"
         },
         "KFDAS":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Kids_Furniture__Décor_and_Storage"
         },
         "LAE":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Learning_and_Education"
         },
         "DAA":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Dolls_and_Accessories"
         },
         "Hobbies":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Hobbies"
         },
         "PS":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Party_Supplies"
         },
         "SAAPT":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Stuffed_Animals_and_Plush_Toys"
         },
         "BATT":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Baby_and_Toddler_Toys"
         },
         "KE":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Kids_Electronics"
         },
         "Puzzles":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Puzzles"
         },
         "TSAW":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Tricycles__Scooters_and_Wagons"
         },
         "GAA":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Games_and_Accessories"
         },
         "NAGT":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Novelty_and_Gag_Toys"
         },
         "TFAP":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Toy_Figures_and_Playsets"
         },
         "BT":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Building_Toys"
         },
         "CT":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Collectible_Toys"
         },
         "SAOP":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Sports_and_Outdoor_Play"
         },
         "DUAPP":{
            "category_name":"Toys_and_Games",
            "sub_category_name":"Dress_Up_and_Pretend_Play"
         }
      },
      "TAHI":{
         "LB":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Light_Bulbs"
         },
         "Appliances":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Appliances"
         },
         "KABF":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Kitchen_and_Bath_Fixtures"
         },
         "PWTAS":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Paint__Wall_Treatments_and_Supplies"
         },
         "Electrical":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Electrical"
         },
         "SAHO":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Storage_and_Home_Organization"
         },
         "Hardware":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Hardware"
         },
         "SAS":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Safety_and_Security"
         },
         "WAS":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Welding_and_Soldering"
         },
         "RP":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Rough_Plumbing"
         },
         "MALT":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Measuring_and_Layout_Tools"
         },
         "PAHT":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Power_and_Hand_Tools"
         },
         "LACF":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Lighting_and_Ceiling_Fans"
         },
         "BS":{
            "category_name":"Tools_and_Home_Improvement",
            "sub_category_name":"Building_Supplies"
         }
      },
      "VG":{
         "PV":{
            "category_name":"Video_Games",
            "sub_category_name":"PlayStation_Vita"
         },
         "P4":{
            "category_name":"Video_Games",
            "sub_category_name":"PlayStation_4"
         },
         "Microconsoles":{
            "category_name":"Video_Games",
            "sub_category_name":"Microconsoles"
         },
         "PC":{
            "category_name":"Video_Games",
            "sub_category_name":"PC"
         },
         "P3":{
            "category_name":"Video_Games",
            "sub_category_name":"PlayStation_3"
         },
         "LS":{
            "category_name":"Video_Games",
            "sub_category_name":"Legacy_Systems"
         },
         "Mac":{
            "category_name":"Video_Games",
            "sub_category_name":"Mac"
         },
         "Wii":{
            "category_name":"Video_Games",
            "sub_category_name":"Wii"
         },
         "X3":{
            "category_name":"Video_Games",
            "sub_category_name":"Xbox_360"
         },
         "N3A2":{
            "category_name":"Video_Games",
            "sub_category_name":"Nintendo_3DS_and_2DS"
         },
         "ND":{
            "category_name":"Video_Games",
            "sub_category_name":"Nintendo_DS"
         },
         "NS":{
            "category_name":"Video_Games",
            "sub_category_name":"Nintendo_Switch"
         },
         "XO":{
            "category_name":"Video_Games",
            "sub_category_name":"Xbox_One"
         },
         "SP":{
            "category_name":"Video_Games",
            "sub_category_name":"Sony_PSP"
         }
      },
      "Watches":{
         "MF":{
            "category_name":"Watches",
            "sub_category_name":"Mens_Fashion"
         },
         "BF":{
            "category_name":"Watches",
            "sub_category_name":"Boys_Fashion"
         },
         "WF":{
            "category_name":"Watches",
            "sub_category_name":"Womens_Fashion"
         },
         "GF":{
            "category_name":"Watches",
            "sub_category_name":"Girls_Fashion"
         }
      }
   },
   "Flipkart": {
      "MI": {
         "Accessories": {
               "category_name": "Musical_Instruments",
               "sub_category_name": "Accessories"
         },
         "SEAA": {
               "category_name": "Musical_Instruments",
               "sub_category_name": "StudioorStage_Equipment_and_Accessories"
         },
         "KAS": {
               "category_name": "Musical_Instruments",
               "sub_category_name": "Keys_and_Synthesizers"
         },
         "SI": {
               "category_name": "Musical_Instruments",
               "sub_category_name": "String_Instruments"
         },
         "DAP": {
               "category_name": "Musical_Instruments",
               "sub_category_name": "Drums_and_Percussion"
         },
         "WI": {
               "category_name": "Musical_Instruments",
               "sub_category_name": "Wind_Instruments"
         }
      },
      "Automotive": {
         "CABA": {
               "category_name": "Automotive",
               "sub_category_name": "Car_and_Bike_Accessories"
         }
      },
      "BC": {
         "BBHASC": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Bath__Hair_and_Skin_Care"
         },
         "BOC": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Oral_Care"
         },
         "NABF": {
               "category_name": "Baby_Care",
               "sub_category_name": "Nursing_and_Breast_Feeding"
         },
         "DAPT": {
               "category_name": "Baby_Care",
               "sub_category_name": "Diaper_and_Potty_Training"
         },
         "IW": {
               "category_name": "Baby_Care",
               "sub_category_name": "Infant_Wear"
         },
         "BG": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Gear"
         },
         "BF": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Food"
         },
         "BPAS": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Proofing_and_Safety"
         },
         "BFBAA": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Feeding_Bottle_and_Accessories"
         },
         "BFUAA": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Feeding_Utensils_and_Accessories"
         },
         "BGSAC": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Gift_Sets_and_Combo"
         },
         "BBA": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Bathing_Accessories"
         },
         "BCAD": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Cleaners_and_Detergents"
         },
         "BMAHC": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Medical_and_Health_Care"
         },
         "BB": {
               "category_name": "Baby_Care",
               "sub_category_name": "Baby_Bedding"
         },
         "MC": {
               "category_name": "Baby_Care",
               "sub_category_name": "Maternity_Care"
         }
      },
      "MMAP": {
         "MATS": {
               "category_name": "Music__Movies_and_Posters",
               "sub_category_name": "Movies_and_TV_Show"
         }
      },
      "PAS": {
         "OS": {
               "category_name": "Pens_and_Stationery",
               "sub_category_name": "Office_Supplies"
         },
         "LE": {
               "category_name": "Pens_and_Stationery",
               "sub_category_name": "Lab_Equipment"
         },
         "DAN": {
               "category_name": "Pens_and_Stationery",
               "sub_category_name": "Diaries_and_Notebooks"
         },
         "Calculators": {
               "category_name": "Pens_and_Stationery",
               "sub_category_name": "Calculators"
         },
         "CS": {
               "category_name": "Pens_and_Stationery",
               "sub_category_name": "College_Supplies"
         },
         "OE": {
               "category_name": "Pens_and_Stationery",
               "sub_category_name": "Office_Equipments"
         },
         "AS": {
               "category_name": "Pens_and_Stationery",
               "sub_category_name": "Art_Supplies"
         },
         "Pens": {
               "category_name": "Pens_and_Stationery",
               "sub_category_name": "Pens"
         }
      },
      "HE": {
         "VPAA": {
               "category_name": "Home_Entertainment",
               "sub_category_name": "Video_Players_and_Accessories"
         },
         "AP": {
               "category_name": "Home_Entertainment",
               "sub_category_name": "Audio_Players"
         },
         "HA": {
               "category_name": "Home_Entertainment",
               "sub_category_name": "Home_Audio"
         },
         "MPA": {
               "category_name": "Home_Entertainment",
               "sub_category_name": "MP3_playersorIpods_Accessories"
         }
      },
      "Sports": {
         "Volleyball": {
               "category_name": "Sports",
               "sub_category_name": "Volleyball"
         },
         "HR": {
               "category_name": "Sports",
               "sub_category_name": "Horse_Riding"
         },
         "Cycling": {
               "category_name": "Sports",
               "sub_category_name": "Cycling"
         },
         "Bowling": {
               "category_name": "Sports",
               "sub_category_name": "Bowling"
         },
         "Handball": {
               "category_name": "Sports",
               "sub_category_name": "Handball"
         },
         "Fishing": {
               "category_name": "Sports",
               "sub_category_name": "Fishing"
         },
         "Carrom": {
               "category_name": "Sports",
               "sub_category_name": "Carrom"
         },
         "Cricket": {
               "category_name": "Sports",
               "sub_category_name": "Cricket"
         },
         "HH": {
               "category_name": "Sports",
               "sub_category_name": "Hobby_Hunting"
         },
         "Laccrose": {
               "category_name": "Sports",
               "sub_category_name": "Laccrose"
         },
         "Badminton": {
               "category_name": "Sports",
               "sub_category_name": "Badminton"
         },
         "Throwball": {
               "category_name": "Sports",
               "sub_category_name": "Throwball"
         },
         "Athletics": {
               "category_name": "Sports",
               "sub_category_name": "Athletics"
         },
         "SA": {
               "category_name": "Sports",
               "sub_category_name": "Sport_Accessories"
         },
         "Taekwondo": {
               "category_name": "Sports",
               "sub_category_name": "Taekwondo"
         },
         "Archery": {
               "category_name": "Sports",
               "sub_category_name": "Archery"
         },
         "Rugby": {
               "category_name": "Sports",
               "sub_category_name": "Rugby"
         },
         "Football": {
               "category_name": "Sports",
               "sub_category_name": "Football"
         },
         "Skating": {
               "category_name": "Sports",
               "sub_category_name": "Skating"
         },
         "JT": {
               "category_name": "Sports",
               "sub_category_name": "Jumping_Trainers"
         },
         "Basketball": {
               "category_name": "Sports",
               "sub_category_name": "Basketball"
         },
         "Hockey": {
               "category_name": "Sports",
               "sub_category_name": "Hockey"
         },
         "Tennis": {
               "category_name": "Sports",
               "sub_category_name": "Tennis"
         },
         "Frisbees": {
               "category_name": "Sports",
               "sub_category_name": "Frisbees"
         },
         "Slacklining": {
               "category_name": "Sports",
               "sub_category_name": "Slacklining"
         },
         "Squash": {
               "category_name": "Sports",
               "sub_category_name": "Squash"
         },
         "Boomerang": {
               "category_name": "Sports",
               "sub_category_name": "Boomerang"
         },
         "Boating": {
               "category_name": "Sports",
               "sub_category_name": "Boating"
         },
         "Running": {
               "category_name": "Sports",
               "sub_category_name": "Running"
         },
         "SD": {
               "category_name": "Sports",
               "sub_category_name": "Scuba_Diving"
         },
         "Swimming": {
               "category_name": "Sports",
               "sub_category_name": "Swimming"
         },
         "Boxing": {
               "category_name": "Sports",
               "sub_category_name": "Boxing"
         },
         "Chess": {
               "category_name": "Sports",
               "sub_category_name": "Chess"
         },
         "Foosball": {
               "category_name": "Sports",
               "sub_category_name": "Foosball"
         },
         "CAH": {
               "category_name": "Sports",
               "sub_category_name": "Camping_and_Hiking"
         },
         "Netball": {
               "category_name": "Sports",
               "sub_category_name": "Netball"
         },
         "AH": {
               "category_name": "Sports",
               "sub_category_name": "Air_hockey"
         },
         "DT": {
               "category_name": "Sports",
               "sub_category_name": "Discus_Throw"
         },
         "Baseball": {
               "category_name": "Sports",
               "sub_category_name": "Baseball"
         },
         "Golf": {
               "category_name": "Sports",
               "sub_category_name": "Golf"
         },
         "Climbing": {
               "category_name": "Sports",
               "sub_category_name": "Climbing"
         },
         "Surfing": {
               "category_name": "Sports",
               "sub_category_name": "Surfing"
         },
         "TT": {
               "category_name": "Sports",
               "sub_category_name": "Table_Tennis"
         },
         "Diving": {
               "category_name": "Sports",
               "sub_category_name": "Diving"
         },
         "OBS": {
               "category_name": "Sports",
               "sub_category_name": "Other_Ball_Sports"
         },
         "Shooting": {
               "category_name": "Sports",
               "sub_category_name": "Shooting"
         },
         "KF": {
               "category_name": "Sports",
               "sub_category_name": "Kite_Flying"
         },
         "WP": {
               "category_name": "Sports",
               "sub_category_name": "Water_Polo"
         }
      },
      "HD": {
         "HF": {
               "category_name": "Home_Decor",
               "sub_category_name": "Home_Fragrance"
         },
         "FAV": {
               "category_name": "Home_Decor",
               "sub_category_name": "Flowers_and_Vases"
         },
         "SAW": {
               "category_name": "Home_Decor",
               "sub_category_name": "Stickers_and_Wallpapers"
         },
         "Clocks": {
               "category_name": "Home_Decor",
               "sub_category_name": "Clocks"
         },
         "DCAH": {
               "category_name": "Home_Decor",
               "sub_category_name": "Diyas__Candles_and_Holders"
         },
         "PFAA": {
               "category_name": "Home_Decor",
               "sub_category_name": "Photo_Frames_and_Albums"
         },
         "WDI": {
               "category_name": "Home_Decor",
               "sub_category_name": "Wall_Decor_Items"
         },
         "PAP": {
               "category_name": "Home_Decor",
               "sub_category_name": "Paintings_and_Posters"
         },
         "SADA": {
               "category_name": "Home_Decor",
               "sub_category_name": "Showpieces_and_Decor_Accents"
         },
         "WADC": {
               "category_name": "Home_Decor",
               "sub_category_name": "Windchimes_and_Dream_catchers"
         }
      },
      "HCABA": {
         "BA": {
               "category_name": "Home_Cleaning_and_Bathroom_Accessories",
               "sub_category_name": "Bathroom_Accessories"
         },
         "CS": {
               "category_name": "Home_Cleaning_and_Bathroom_Accessories",
               "sub_category_name": "Cleaning_Supplies"
         },
         "HS": {
               "category_name": "Home_Cleaning_and_Bathroom_Accessories",
               "sub_category_name": "HouseHold_Supplies"
         }
      },
      "KCAS": {
         "TAD": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Tableware_and_Dinnerware"
         },
         "DS": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Disposable_Supplies"
         },
         "Barware": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Barware"
         },
         "KSAC": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Kitchen_Storage_and_Containers"
         },
         "HJAG": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Hand_Juicers_and_Grinders"
         },
         "OC": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Outdoor_Cooking"
         },
         "KT": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Kitchen_Tools"
         },
         "Cookware": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Cookware"
         },
         "Bakeware": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Bakeware"
         },
         "KCAC": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Knives__Choppers_and_Cutters"
         },
         "LBBAF": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Lunch_Boxes__Bottles_and_Flasks"
         },
         "GSAA": {
               "category_name": "Kitchen__Cookware_and_Serveware",
               "sub_category_name": "Gas_Stove_and_Accessories"
         }
      },
      "BMAS": {
         "PS": {
               "category_name": "Building_Materials_And_Supplies",
               "sub_category_name": "Plumbing_Supplies"
         },
         "BAKF": {
               "category_name": "Building_Materials_And_Supplies",
               "sub_category_name": "Bathroom_and_Kitchen_Fittings"
         },
         "BRM": {
               "category_name": "Building_Materials_And_Supplies",
               "sub_category_name": "Building_Raw_Materials"
         },
         "WS": {
               "category_name": "Building_Materials_And_Supplies",
               "sub_category_name": "Wooden_Supplies"
         },
         "PSAE": {
               "category_name": "Building_Materials_And_Supplies",
               "sub_category_name": "Paint_Supplies_and_Equipment"
         },
         "CTAE": {
               "category_name": "Building_Materials_And_Supplies",
               "sub_category_name": "Construction_Tools_and_Equipments"
         },
         "BSAO": {
               "category_name": "Building_Materials_And_Supplies",
               "sub_category_name": "Building_Supplies_Add_Ons"
         },
         "SAAE": {
               "category_name": "Building_Materials_And_Supplies",
               "sub_category_name": "Solar_and_Alternate_Energy"
         },
         "EH": {
               "category_name": "Building_Materials_And_Supplies",
               "sub_category_name": "Electrical_Hardware"
         },
         "DAWF": {
               "category_name": "Building_Materials_And_Supplies",
               "sub_category_name": "Door_and_Window_Fittings"
         }
      },
      "MAA": {
         "MA": {
               "category_name": "Mobiles_and_Accessories",
               "sub_category_name": "Mobile_Accessories"
         },
         "Tablets": {
               "category_name": "Mobiles_and_Accessories",
               "sub_category_name": "Tablets"
         },
         "TA": {
               "category_name": "Mobiles_and_Accessories",
               "sub_category_name": "Tablet_Accessories"
         }
      },
      "BAG": {
         "HM": {
               "category_name": "Beauty_And_Grooming",
               "sub_category_name": "Home_Medicines"
         },
         "HMS": {
               "category_name": "Beauty_And_Grooming",
               "sub_category_name": "Home_Medical_Supplies"
         },
         "PMS": {
               "category_name": "Beauty_And_Grooming",
               "sub_category_name": "Professional_medical_supplies"
         },
         "WS": {
               "category_name": "Beauty_And_Grooming",
               "sub_category_name": "Womens_Safety"
         }
      },
      "HF": {
         "CAP": {
               "category_name": "Home_Furnishing",
               "sub_category_name": "Cushions_and_Pillows"
         },
         "BL": {
               "category_name": "Home_Furnishing",
               "sub_category_name": "Bath_Linen"
         },
         "CAA": {
               "category_name": "Home_Furnishing",
               "sub_category_name": "Curtains_and_Accessories"
         },
         "SACF": {
               "category_name": "Home_Furnishing",
               "sub_category_name": "Sofa_and_Curtain_Fabrics"
         },
         "KATL": {
               "category_name": "Home_Furnishing",
               "sub_category_name": "Kitchen_and_Table_Linen"
         },
         "FC": {
               "category_name": "Home_Furnishing",
               "sub_category_name": "Floor_Coverings"
         },
         "BLAB": {
               "category_name": "Home_Furnishing",
               "sub_category_name": "Bed_Linen_and_Blankets"
         }
      },
      "PS": {
         "HAS": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Health_and_Safety"
         },
         "SA": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Small_Animals"
         },
         "Birds": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Birds"
         },
         "GAH": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Grooming_and_Hygiene"
         },
         "Dogs": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Dogs"
         },
         "LA": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Large_Animals"
         },
         "Cats": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Cats"
         },
         "FAA": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Fish_and_Aquatic"
         }
      },
      "EAF": {
         "Pilates": {
               "category_name": "Exercise_and_Fitness",
               "sub_category_name": "Pilates"
         },
         "FE": {
               "category_name": "Exercise_and_Fitness",
               "sub_category_name": "Fitness_Equipment"
         },
         "Yoga": {
               "category_name": "Exercise_and_Fitness",
               "sub_category_name": "Yoga"
         },
         "FA": {
               "category_name": "Exercise_and_Fitness",
               "sub_category_name": "Fitness_Accessories"
         },
         "MAAE": {
               "category_name": "Exercise_and_Fitness",
               "sub_category_name": "Mobility_Aids_and_Equipments"
         }
      },
      "Furniture": {
         "Chairs": {
               "category_name": "Furniture",
               "sub_category_name": "Chairs"
         },
         "Cabinets": {
               "category_name": "Furniture",
               "sub_category_name": "Cabinets"
         },
         "Showcases": {
               "category_name": "Furniture",
               "sub_category_name": "Showcases"
         },
         "Drawers": {
               "category_name": "Furniture",
               "sub_category_name": "Drawers"
         },
         "Tables": {
               "category_name": "Furniture",
               "sub_category_name": "Tables"
         },
         "Mattresses": {
               "category_name": "Furniture",
               "sub_category_name": "Mattresses"
         },
         "Stands": {
               "category_name": "Furniture",
               "sub_category_name": "Stands"
         },
         "Sofas": {
               "category_name": "Furniture",
               "sub_category_name": "Sofas"
         },
         "DTAS": {
               "category_name": "Furniture",
               "sub_category_name": "Dining_Tables_and_Sets"
         },
         "Shelves": {
               "category_name": "Furniture",
               "sub_category_name": "Shelves"
         },
         "FA": {
               "category_name": "Furniture",
               "sub_category_name": "Furniture_Accessories"
         },
         "TUAC": {
               "category_name": "Furniture",
               "sub_category_name": "TV_Units_and_Cabinets"
         }
      },
      "WSD": {
         "WA": {
               "category_name": "Wearable_Smart_Devices",
               "sub_category_name": "Wearable_Accessories"
         }
      },
      "CA": {
         "Cameras": {
               "category_name": "Cameras_Accessories",
               "sub_category_name": "Cameras"
         },
         "CA": {
               "category_name": "Cameras_Accessories",
               "sub_category_name": "Camera_Accessories"
         }
      },
      "HAPCA": {
         "HC": {
               "category_name": "Health_and_Personal_Care_Appliances",
               "sub_category_name": "Health_Care"
         },
         "PCA": {
               "category_name": "Health_and_Personal_Care_Appliances",
               "sub_category_name": "Personal_Care_Appliances"
         }
      },
      "BWAB": {
         "BAB": {
               "category_name": "Bags__Wallets_and_Belts",
               "sub_category_name": "Bags_and_Backpacks"
         },
         "LAT": {
               "category_name": "Bags__Wallets_and_Belts",
               "sub_category_name": "Luggage_and_Travel"
         },
         "HAC": {
               "category_name": "Bags__Wallets_and_Belts",
               "sub_category_name": "Handbags_and_Clutches"
         },
         "WAC": {
               "category_name": "Bags__Wallets_and_Belts",
               "sub_category_name": "Wallets_and_Clutches"
         }
      },
      "Clothing": {
         "WC": {
               "category_name": "Clothing",
               "sub_category_name": "Womens_Clothing"
         },
         "MC": {
               "category_name": "Clothing",
               "sub_category_name": "Mens_Clothing"
         },
         "KC": {
               "category_name": "Clothing",
               "sub_category_name": "Kids_Clothing"
         }
      },
      "Computers": {
         "LA": {
               "category_name": "Computers",
               "sub_category_name": "Laptop_Accessories"
         },
         "Storage": {
               "category_name": "Computers",
               "sub_category_name": "Storage"
         },
         "Software": {
               "category_name": "Computers",
               "sub_category_name": "Software"
         },
         "Supplies": {
               "category_name": "Computers",
               "sub_category_name": "Supplies"
         },
         "AP": {
               "category_name": "Computers",
               "sub_category_name": "Audio_Players"
         },
         "TA": {
               "category_name": "Computers",
               "sub_category_name": "Tablet_Accessories"
         },
         "DP": {
               "category_name": "Computers",
               "sub_category_name": "Desktop_PCs"
         },
         "PAI": {
               "category_name": "Computers",
               "sub_category_name": "Printers_and_Inks"
         },
         "CP": {
               "category_name": "Computers",
               "sub_category_name": "Computer_Peripherals"
         },
         "CC": {
               "category_name": "Computers",
               "sub_category_name": "Computer_Components"
         },
         "TAVA": {
               "category_name": "Computers",
               "sub_category_name": "TV_and_Video_Accessories"
         },
         "NC": {
               "category_name": "Computers",
               "sub_category_name": "Network_Components"
         }
      },
      "Toys": {
         "BT": {
               "category_name": "Toys",
               "sub_category_name": "Baby_Toys"
         },
         "PABG": {
               "category_name": "Toys",
               "sub_category_name": "Puzzles_and_Board_Games"
         },
         "ET": {
               "category_name": "Toys",
               "sub_category_name": "Educational_Toys"
         },
         "DADH": {
               "category_name": "Toys",
               "sub_category_name": "Dolls_and_Doll_Houses"
         },
         "Sports": {
               "category_name": "Toys",
               "sub_category_name": "Sports"
         },
         "HK": {
               "category_name": "Toys",
               "sub_category_name": "Hobby_Kits"
         },
         "PS": {
               "category_name": "Toys",
               "sub_category_name": "Party_Supplies"
         }
      },
      "Watches": {
         "WA": {
               "category_name": "Watches",
               "sub_category_name": "Watch_Accessories"
         }
      },
      "FDAG": {
         "FG": {
               "category_name": "Festive_Decor_and_Gifting",
               "sub_category_name": "Festive_Gifts"
         },
         "FD": {
               "category_name": "Festive_Decor_and_Gifting",
               "sub_category_name": "Festive_Decor"
         },
         "SI": {
               "category_name": "Festive_Decor_and_Gifting",
               "sub_category_name": "Spiritual_Items"
         },
         "FAC": {
               "category_name": "Festive_Decor_and_Gifting",
               "sub_category_name": "Fireworks_and_Crackers"
         }
      },
      "HI": {
         "LAG": {
               "category_name": "Home_Improvement",
               "sub_category_name": "Lawn_and_Gardening"
         },
         "HUAO": {
               "category_name": "Home_Improvement",
               "sub_category_name": "Home_Utilities_and_Organizers"
         },
         "HS": {
               "category_name": "Home_Improvement",
               "sub_category_name": "Home_Safety"
         },
         "TAME": {
               "category_name": "Home_Improvement",
               "sub_category_name": "Tools_and_Measuring_Equipment"
         }
      },
      "HC": {
         "HM": {
               "category_name": "Health_Care",
               "sub_category_name": "Home_Medicines"
         },
         "HMS": {
               "category_name": "Health_Care",
               "sub_category_name": "Home_Medical_Supplies"
         },
         "PMS": {
               "category_name": "Health_Care",
               "sub_category_name": "Professional_medical_supplies"
         },
         "WS": {
               "category_name": "Health_Care",
               "sub_category_name": "Womens_Safety"
         }
      },
      "Footwear": {
         "MF": {
               "category_name": "Footwear",
               "sub_category_name": "Mens_Footwear"
         },
         "KAIF": {
               "category_name": "Footwear",
               "sub_category_name": "Kids_and_Infant_Footwear"
         },
         "WF": {
               "category_name": "Footwear",
               "sub_category_name": "Womens_Footwear"
         }
      },
      "Gaming": {
         "Games": {
               "category_name": "Gaming",
               "sub_category_name": "Games"
         },
         "GC": {
               "category_name": "Gaming",
               "sub_category_name": "Gaming_Components"
         },
         "GA": {
               "category_name": "Gaming",
               "sub_category_name": "Gaming_Accessories"
         }
      },
      "KA": {
         "SS": {
               "category_name": "Kids_Accessories",
               "sub_category_name": "School_Supplies"
         }
      },
      "Jewellery": {
         "SJ": {
               "category_name": "Jewellery",
               "sub_category_name": "Silver_Jewellery"
         },
         "AJ": {
               "category_name": "Jewellery",
               "sub_category_name": "Artificial_Jewellery"
         },
         "PA": {
               "category_name": "Jewellery",
               "sub_category_name": "Precious_Articles"
         },
         "GCAB": {
               "category_name": "Jewellery",
               "sub_category_name": "Gemstones__Coins_and_Bars"
         },
         "PJ": {
               "category_name": "Jewellery",
               "sub_category_name": "Precious_Jewellery"
         }
      },
      "HAK": {
         "HA": {
               "category_name": "Home_and_Kitchen",
               "sub_category_name": "Home_Appliances"
         },
         "KA": {
               "category_name": "Home_and_Kitchen",
               "sub_category_name": "Kitchen_Appliances"
         }
      },
      "FAN": {
         "Staples": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Staples"
         },
         "Beverages": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Beverages"
         },
         "EOAG": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Edible_Oils_and_Ghee"
         },
         "SCAS": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Spices__Condiments_and_Sauces"
         },
         "RTCAE": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Ready_to_Cook_and_Eat"
         },
         "SAN": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Snacks_and_Nibbles"
         },
         "HAN": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Health_and_Nutrition"
         },
         "BMAC": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Breakfast_Mixes_and_Cereals"
         },
         "NDFAC": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Nuts__Dry_Fruits_and_Combos"
         },
         "BABE": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Bakery_and_Baking_Essentials"
         },
         "NAP": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Noodles_and_Pasta"
         },
         "CAS": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Confectioneries_and_Sweets"
         },
         "JSAH": {
               "category_name": "Food_and_Nutrition",
               "sub_category_name": "Jams__Spreads_and_Honey"
         }
      },
      "AAR": {
         "SAA": {
               "category_name": "Automation_and_Robotics",
               "sub_category_name": "Sensors_and_Alarms"
         },
         "SD": {
               "category_name": "Automation_and_Robotics",
               "sub_category_name": "Surveillance_Devices"
         }
      },
      "HL": {
         "UL": {
               "category_name": "Home_Lighting",
               "sub_category_name": "Utility_Lighting"
         },
         "DLAA": {
               "category_name": "Home_Lighting",
               "sub_category_name": "Decor_lighting_and_Accessories"
         }
      },
      "IASS": {
         "PASP": {
               "category_name": "Industrial_and_Scientific_Supplies",
               "sub_category_name": "Packaging_and_Shipping_Products"
         },
         "LASP": {
               "category_name": "Industrial_and_Scientific_Supplies",
               "sub_category_name": "Lab_and_Scientific_Products"
         },
         "IMD": {
               "category_name": "Industrial_and_Scientific_Supplies",
               "sub_category_name": "Industrial_Measurement_Devices"
         },
         "ITD": {
               "category_name": "Industrial_and_Scientific_Supplies",
               "sub_category_name": "Industrial_Testing_Devices"
         },
         "SP": {
               "category_name": "Industrial_and_Scientific_Supplies",
               "sub_category_name": "Safety_Products"
         }
      },
      "AAV": {
         "PAS": {
               "category_name": "Audio_and_Video",
               "sub_category_name": "Professional_Audio_Systems"
         },
         "APAR": {
               "category_name": "Audio_and_Video",
               "sub_category_name": "Audio_Players_and_Recorders"
         },
         "VA": {
               "category_name": "Audio_and_Video",
               "sub_category_name": "Video_Accessories"
         },
         "AA": {
               "category_name": "Audio_and_Video",
               "sub_category_name": "Audio_Accessories"
         }
      },
      "Books": {
         "Books" :{
            "category_name": "Books",
            "sub_category_name": "Books"
         },
         "LHASB": {
               "category_name": "Books",
               "sub_category_name": "Lifestyle__Hobby_and_Sport_Books"
         },
         "CAYAB": {
               "category_name": "Books",
               "sub_category_name": "Children_and_Young_Adult_Books"
         },
         "BMAGNFB": {
               "category_name": "Books",
               "sub_category_name": "Biographies__Memoirs_and_General_Non_Ficton_Books"
         },
         "LB": {
               "category_name": "Books",
               "sub_category_name": "Literature_Books"
         },
         "SHB": {
               "category_name": "Books",
               "sub_category_name": "Self_Help_Books"
         },
         "SSB": {
               "category_name": "Books",
               "sub_category_name": "Social_Science_Books"
         },
         "SB": {
               "category_name": "Books",
               "sub_category_name": "School_Books"
         },
         "TPB": {
               "category_name": "Books",
               "sub_category_name": "Test_Preparation_Books"
         },
         "EBAMB": {
               "category_name": "Books",
               "sub_category_name": "Economics__Business_and_Management_Books"
         },
         "HLAWB": {
               "category_name": "Books",
               "sub_category_name": "Healthy_Living_and_Wellness_Books"
         },
         "GNAC": {
               "category_name": "Books",
               "sub_category_name": "Graphic_Novels_and_Comics"
         },
         "HAAB": {
               "category_name": "Books",
               "sub_category_name": "History_and_Archaeology_Books"
         },
         "PARB": {
               "category_name": "Books",
               "sub_category_name": "Philosophy_and_Religion_Books"
         },
         "HEAPB": {
               "category_name": "Books",
               "sub_category_name": "Higher_Education_and_Professional_Books"
         },
         "FB": {
               "category_name": "Books",
               "sub_category_name": "Fiction_Books"
         },
         "ALALB": {
               "category_name": "Books",
               "sub_category_name": "Arts__Language_and_Linguistic_Books"
         }
      }
   },
   "Bonanza": {
      "Crafts": {
         "HAFP": {
               "category_name": "Crafts",
               "sub_category_name": "Handcrafted_and_Finished_Pieces"
         },
         "FPAD": {
               "category_name": "Crafts",
               "sub_category_name": "Fabric_Painting_and_Decorating"
         },
         "AS": {
               "category_name": "Crafts",
               "sub_category_name": "Art_Supplies"
         },
         "SMAC": {
               "category_name": "Crafts",
               "sub_category_name": "Sculpting__Molding_and_Ceramics"
         },
         "WL": {
               "category_name": "Crafts",
               "sub_category_name": "Wholesale_Lots"
         },
         "Leathercrafts": {
               "category_name": "Crafts",
               "sub_category_name": "Leathercrafts"
         }
      },
      "CAPM": {
         "Exonumia": {
               "category_name": "Coins_and_Paper_Money",
               "sub_category_name": "Exonumia"
         },
         "CU": {
               "category_name": "Coins_and_Paper_Money",
               "sub_category_name": "Coins:_US"
         },
         "CA": {
               "category_name": "Coins_and_Paper_Money",
               "sub_category_name": "Coins:_Ancient"
         },
         "CW": {
               "category_name": "Coins_and_Paper_Money",
               "sub_category_name": "Coins:_World"
         },
         "PAS": {
               "category_name": "Coins_and_Paper_Money",
               "sub_category_name": "Publications_and_Supplies"
         },
         "CM": {
               "category_name": "Coins_and_Paper_Money",
               "sub_category_name": "Coins:_Medieval"
         },
         "Bullion": {
               "category_name": "Coins_and_Paper_Money",
               "sub_category_name": "Bullion"
         },
         "PMU": {
               "category_name": "Coins_and_Paper_Money",
               "sub_category_name": "Paper_Money:_US"
         },
         "PMW": {
               "category_name": "Coins_and_Paper_Money",
               "sub_category_name": "Paper_Money:_World"
         },
         "SABS": {
               "category_name": "Coins_and_Paper_Money",
               "sub_category_name": "Stocks_and_Bonds__Scripophily"
         },
         "CC": {
               "category_name": "Coins_and_Paper_Money",
               "sub_category_name": "Coins:_Canada"
         }
      },
      "EE": {
         "Metaphysical": {
               "category_name": "Everything_Else",
               "sub_category_name": "Metaphysical"
         },
         "RPAS": {
               "category_name": "Everything_Else",
               "sub_category_name": "Religious_Products_and_Supplies"
         },
         "PD": {
               "category_name": "Everything_Else",
               "sub_category_name": "Personal_Development"
         },
         "Genealogy": {
               "category_name": "Everything_Else",
               "sub_category_name": "Genealogy"
         },
         "WS": {
               "category_name": "Everything_Else",
               "sub_category_name": "Weird_Stuff"
         },
         "CDAE": {
               "category_name": "Everything_Else",
               "sub_category_name": "Career_Development_and_Education"
         },
         "PS": {
               "category_name": "Everything_Else",
               "sub_category_name": "Personal_Security"
         },
         "FAC": {
               "category_name": "Everything_Else",
               "sub_category_name": "Funeral_and_Cemetery"
         },
         "IP": {
               "category_name": "Everything_Else",
               "sub_category_name": "Information_Products"
         }
      },
      "CE": {
         "VE": {
               "category_name": "Consumer_Electronics",
               "sub_category_name": "Vintage_Electronics"
         },
         "PAAH": {
               "category_name": "Consumer_Electronics",
               "sub_category_name": "Portable_Audio_and_Headphones"
         },
         "RC": {
               "category_name": "Consumer_Electronics",
               "sub_category_name": "Radio_Communication"
         },
         "VR": {
               "category_name": "Consumer_Electronics",
               "sub_category_name": "Virtual_Reality"
         },
         "VEAG": {
               "category_name": "Consumer_Electronics",
               "sub_category_name": "Vehicle_Electronics_and_GPS"
         },
         "HTAA": {
               "category_name": "Consumer_Electronics",
               "sub_category_name": "Home_Telephones_and_Accessories"
         },
         "SASHE": {
               "category_name": "Consumer_Electronics",
               "sub_category_name": "Surveillance_and_Smart_Home_Electronics"
         },
         "TVAHA": {
               "category_name": "Consumer_Electronics",
               "sub_category_name": "TV__Video_and_Home_Audio"
         },
         "MBAP": {
               "category_name": "Consumer_Electronics",
               "sub_category_name": "Multipurpose_Batteries_and_Power"
         }
      },
      "DAB": {
         "DM": {
               "category_name": "Dolls_and_Bears",
               "sub_category_name": "Dollhouse_Miniatures"
         },
         "Dolls": {
               "category_name": "Dolls_and_Bears",
               "sub_category_name": "Dolls"
         },
         "PD": {
               "category_name": "Dolls_and_Bears",
               "sub_category_name": "Paper_Dolls"
         },
         "WL": {
               "category_name": "Dolls_and_Bears",
               "sub_category_name": "Wholesale_Lots"
         },
         "Bears": {
               "category_name": "Dolls_and_Bears",
               "sub_category_name": "Bears"
         }
      },
      "CAN": {
         "HNAC": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Home_Networking_and_Connectivity"
         },
         "DAAIO": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Desktops_and_All_In_Ones"
         },
         "MPAA": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Monitors__Projectors_and_Accs"
         },
         "3PAS": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "3D_Printers_and_Supplies"
         },
         "DSABM": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Drives__Storage_and_Blank_Media"
         },
         "LADA": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Laptop_and_Desktop_Accessories"
         },
         "ENS": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Enterprise_Networking__Servers"
         },
         "Software": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Software"
         },
         "LAN": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Laptops_and_Netbooks"
         },
         "IA": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "iPadorTabletoreBook_Accessories"
         },
         "VC": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Vintage_Computing"
         },
         "CCAC": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Computer_Cables_and_Connectors"
         },
         "CCAP": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Computer_Components_and_Parts"
         },
         "PPD": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Power_Protection__Distribution"
         },
         "PSAS": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Printers__Scanners_and_Supplies"
         },
         "KMAP": {
               "category_name": "ComputersorTablets_and_Networking",
               "sub_category_name": "Keyboards__Mice_and_Pointing"
         }
      },
      "Antiques": {
         "AAG": {
               "category_name": "Antiques",
               "sub_category_name": "Architectural_and_Garden"
         },
         "RAC": {
               "category_name": "Antiques",
               "sub_category_name": "Restoration_and_Care"
         },
         "MAAG": {
               "category_name": "Antiques",
               "sub_category_name": "Maps__Atlases_and_Globes"
         },
         "Maritime": {
               "category_name": "Antiques",
               "sub_category_name": "Maritime"
         },
         "LAT": {
               "category_name": "Antiques",
               "sub_category_name": "Linens_and_Textiles_(Pre_1930)"
         },
         "Ethnographic": {
               "category_name": "Antiques",
               "sub_category_name": "Ethnographic"
         },
         "DA": {
               "category_name": "Antiques",
               "sub_category_name": "Decorative_Arts"
         },
         "Antiquities": {
               "category_name": "Antiques",
               "sub_category_name": "Antiquities"
         },
         "MI": {
               "category_name": "Antiques",
               "sub_category_name": "Musical_Instruments_(Pre_1930)"
         },
         "SAM": {
               "category_name": "Antiques",
               "sub_category_name": "Science_and_Medicine_(Pre_1930)"
         },
         "Furniture": {
               "category_name": "Antiques",
               "sub_category_name": "Furniture"
         },
         "PAS": {
               "category_name": "Antiques",
               "sub_category_name": "Periods_and_Styles"
         },
         "MTAF": {
               "category_name": "Antiques",
               "sub_category_name": "Mercantile__Trades_and_Factories"
         },
         "Silver": {
               "category_name": "Antiques",
               "sub_category_name": "Silver"
         },
         "HAH": {
               "category_name": "Antiques",
               "sub_category_name": "Home_and_Hearth"
         },
         "AA": {
               "category_name": "Antiques",
               "sub_category_name": "Asian_Antiques"
         },
         "S": {
               "category_name": "Antiques",
               "sub_category_name": "Sewing_(Pre_1930)"
         }
      },
      "Baby": {
         "KABA": {
               "category_name": "Baby",
               "sub_category_name": "Keepsakes_and_Baby_Announcements"
         },
         "Diapering": {
               "category_name": "Baby",
               "sub_category_name": "Diapering"
         },
         "Feeding": {
               "category_name": "Baby",
               "sub_category_name": "Feeding"
         },
         "BAG": {
               "category_name": "Baby",
               "sub_category_name": "Bathing_and_Grooming"
         },
         "NF": {
               "category_name": "Baby",
               "sub_category_name": "Nursery_Furniture"
         },
         "ND": {
               "category_name": "Baby",
               "sub_category_name": "Nursery_D\u00e9cor"
         },
         "NB": {
               "category_name": "Baby",
               "sub_category_name": "Nursery_Bedding"
         },
         "CSS": {
               "category_name": "Baby",
               "sub_category_name": "Car_Safety_Seats"
         },
         "BG": {
               "category_name": "Baby",
               "sub_category_name": "Baby_Gear"
         },
         "BSAH": {
               "category_name": "Baby",
               "sub_category_name": "Baby_Safety_and_Health"
         },
         "SAA": {
               "category_name": "Baby",
               "sub_category_name": "Strollers_and_Accessories"
         },
         "TFB": {
               "category_name": "Baby",
               "sub_category_name": "Toys_for_Baby"
         }
      },
      "HAG": {
         "TAWE": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Tools_and_Workshop_Equipment"
         },
         "KATAH": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Kids_and_Teens_at_Home"
         },
         "HASD": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Holiday_and_Seasonal_D\u00e9cor"
         },
         "MA": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Major_Appliances"
         },
         "WTAH": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Window_Treatments_and_Hardware"
         },
         "WS": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Wedding_Supplies"
         },
         "GCAPS": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Greeting_Cards_and_Party_Supply"
         },
         "HSAC": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Household_Supplies_and_Cleaning"
         },
         "Bath": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Bath"
         },
         "Bedding": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Bedding"
         },
         "KDAB": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Kitchen__Dining_and_Bar"
         },
         "RAC": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Rugs_and_Carpets"
         },
         "FAB": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Food_and_Beverages"
         },
         "Furniture": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Furniture"
         },
         "FCFAS": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Fresh_Cut_Flowers_and_Supplies"
         },
         "HD": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Home_D\u00e9cor"
         },
         "LLACF": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Lamps__Lighting_and_Ceiling_Fans"
         },
         "WL": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Wholesale_Lots"
         },
         "YGAOL": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Yard__Garden_and_Outdoor_Living"
         },
         "HI": {
               "category_name": "Home_and_Garden",
               "sub_category_name": "Home_Improvement"
         }
      },
      "CAP": {
         "TAS": {
               "category_name": "Cameras_and_Photo",
               "sub_category_name": "Tripods_and_Supports"
         },
         "FP": {
               "category_name": "Cameras_and_Photo",
               "sub_category_name": "Film_Photography"
         },
         "FAFA": {
               "category_name": "Cameras_and_Photo",
               "sub_category_name": "Flashes_and_Flash_Accessories"
         },
         "VPAE": {
               "category_name": "Cameras_and_Photo",
               "sub_category_name": "Video_Production_and_Editing"
         },
         "RPAT": {
               "category_name": "Cameras_and_Photo",
               "sub_category_name": "Replacement_Parts_and_Tools"
         },
         "LAF": {
               "category_name": "Cameras_and_Photo",
               "sub_category_name": "Lenses_and_Filters"
         },
         "BAT": {
               "category_name": "Cameras_and_Photo",
               "sub_category_name": "Binoculars_and_Telescopes"
         },
         "VMAP": {
               "category_name": "Cameras_and_Photo",
               "sub_category_name": "Vintage_Movie_and_Photography"
         },
         "CAPA": {
               "category_name": "Cameras_and_Photo",
               "sub_category_name": "Camera_and_Photo_Accessories"
         },
         "LAS": {
               "category_name": "Cameras_and_Photo",
               "sub_category_name": "Lighting_and_Studio"
         }
      },
      "Books": {
         "CAYA": {
               "category_name": "Books",
               "sub_category_name": "Children_and_Young_Adults"
         },
         "Accessories": {
               "category_name": "Books",
               "sub_category_name": "Accessories"
         },
         "WABL": {
               "category_name": "Books",
               "sub_category_name": "Wholesale_and_Bulk_Lots"
         },
         "TEAR": {
               "category_name": "Books",
               "sub_category_name": "Textbooks__Education_and_Reference"
         }
      },
      "Collectibles": {
         "RFAM": {
               "category_name": "Collectibles",
               "sub_category_name": "Rocks__Fossils_and_Minerals"
         },
         "RAS": {
               "category_name": "Collectibles",
               "sub_category_name": "Religion_and_Spirituality"
         },
         "PI": {
               "category_name": "Collectibles",
               "sub_category_name": "Photographic_Images"
         },
         "Clocks": {
               "category_name": "Collectibles",
               "sub_category_name": "Clocks"
         },
         "Barware": {
               "category_name": "Collectibles",
               "sub_category_name": "Barware"
         },
         "Animals": {
               "category_name": "Collectibles",
               "sub_category_name": "Animals"
         },
         "PAWI": {
               "category_name": "Collectibles",
               "sub_category_name": "Pens_and_Writing_Instruments"
         },
         "VPAS": {
               "category_name": "Collectibles",
               "sub_category_name": "Vanity__Perfume_and_Shaving"
         },
         "KAH": {
               "category_name": "Collectibles",
               "sub_category_name": "Kitchen_and_Home"
         },
         "DC": {
               "category_name": "Collectibles",
               "sub_category_name": "Decorative_Collectibles"
         },
         "PBL": {
               "category_name": "Collectibles",
               "sub_category_name": "Pinbacks__Bobbles__Lunchboxes"
         },
         "Tobacciana": {
               "category_name": "Collectibles",
               "sub_category_name": "Tobacciana"
         },
         "CAE": {
               "category_name": "Collectibles",
               "sub_category_name": "Cultures_and_Ethnicities"
         },
         "Postcards": {
               "category_name": "Collectibles",
               "sub_category_name": "Postcards"
         },
         "PKPG": {
               "category_name": "Collectibles",
               "sub_category_name": "Pez__Keychains__Promo_Glasses"
         },
         "Beads": {
               "category_name": "Collectibles",
               "sub_category_name": "Beads"
         },
         "BB": {
               "category_name": "Collectibles",
               "sub_category_name": "Breweriana__Beer"
         },
         "Metalware": {
               "category_name": "Collectibles",
               "sub_category_name": "Metalware"
         },
         "AJAP": {
               "category_name": "Collectibles",
               "sub_category_name": "Arcade__Jukeboxes_and_Pinball"
         },
         "AAAC": {
               "category_name": "Collectibles",
               "sub_category_name": "Animation_Art_and_Characters"
         },
         "Transportation": {
               "category_name": "Collectibles",
               "sub_category_name": "Transportation"
         },
         "BRAV": {
               "category_name": "Collectibles",
               "sub_category_name": "Banks__Registers_and_Vending"
         },
         "Advertising": {
               "category_name": "Collectibles",
               "sub_category_name": "Advertising"
         },
         "Autographs": {
               "category_name": "Collectibles",
               "sub_category_name": "Autographs"
         },
         "LAT": {
               "category_name": "Collectibles",
               "sub_category_name": "Linens_and_Textiles_(1930_Now)"
         },
         "Paper": {
               "category_name": "Collectibles",
               "sub_category_name": "Paper"
         },
         "THAL": {
               "category_name": "Collectibles",
               "sub_category_name": "Tools__Hardware_and_Locks"
         },
         "SFAH": {
               "category_name": "Collectibles",
               "sub_category_name": "Science_Fiction_and_Horror"
         },
         "HM": {
               "category_name": "Collectibles",
               "sub_category_name": "Historical_Memorabilia"
         },
         "SAM": {
               "category_name": "Collectibles",
               "sub_category_name": "Science_and_Medicine_(1930_Now)"
         },
         "KSAB": {
               "category_name": "Collectibles",
               "sub_category_name": "Knives__Swords_and_Blades"
         },
         "LL": {
               "category_name": "Collectibles",
               "sub_category_name": "Lamps__Lighting"
         },
         "Casino": {
               "category_name": "Collectibles",
               "sub_category_name": "Casino"
         },
         "BAI": {
               "category_name": "Collectibles",
               "sub_category_name": "Bottles_and_Insulators"
         },
         "Militaria": {
               "category_name": "Collectibles",
               "sub_category_name": "Militaria"
         },
         "S": {
               "category_name": "Collectibles",
               "sub_category_name": "Sewing_(1930_Now)"
         },
         "NSTC": {
               "category_name": "Collectibles",
               "sub_category_name": "Non_Sport_Trading_Cards"
         },
         "Comics": {
               "category_name": "Collectibles",
               "sub_category_name": "Comics"
         },
         "WL": {
               "category_name": "Collectibles",
               "sub_category_name": "Wholesale_Lots"
         },
         "VRMC": {
               "category_name": "Collectibles",
               "sub_category_name": "Vintage__Retro__Mid_Century"
         },
         "SATM": {
               "category_name": "Collectibles",
               "sub_category_name": "Souvenirs_and_Travel_Memorabilia"
         },
         "HAS": {
               "category_name": "Collectibles",
               "sub_category_name": "Holiday_and_Seasonal"
         },
         "FMAM": {
               "category_name": "Collectibles",
               "sub_category_name": "Fantasy__Mythical_and_Magic"
         },
         "RPTP": {
               "category_name": "Collectibles",
               "sub_category_name": "Radio__Phonograph__TV__Phone"
         },
         "Disneyana": {
               "category_name": "Collectibles",
               "sub_category_name": "Disneyana"
         }
      },
      "EM": {
         "AO": {
               "category_name": "Entertainment_Memorabilia",
               "sub_category_name": "Autographs_Original"
         },
         "MM": {
               "category_name": "Entertainment_Memorabilia",
               "sub_category_name": "Movie_Memorabilia"
         },
         "AR": {
               "category_name": "Entertainment_Memorabilia",
               "sub_category_name": "Autographs_Reprints"
         },
         "TM": {
               "category_name": "Entertainment_Memorabilia",
               "sub_category_name": "Theater_Memorabilia"
         }
      },
      "CPAA": {
         "SWA": {
               "category_name": "Cell_Phones_and_Accessories",
               "sub_category_name": "Smart_Watch_Accessories"
         },
         "CPA": {
               "category_name": "Cell_Phones_and_Accessories",
               "sub_category_name": "Cell_Phone_Accessories"
         }
      },
      "HAB": {
         "SASE": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Salon_and_Spa_Equipment"
         },
         "Massage": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Massage"
         },
         "ECVAA": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "E_Cigarettes__Vapes_and_Accs"
         },
         "SPAT": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Sun_Protection_and_Tanning"
         },
         "SC": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Skin_Care"
         },
         "OC": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Oral_Care"
         },
         "Fragrances": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Fragrances"
         },
         "SAHR": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Shaving_and_Hair_Removal"
         },
         "BAB": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Bath_and_Body"
         },
         "HC": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Health_Care"
         },
         "VADS": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Vitamins_and_Dietary_Supplements"
         },
         "Makeup": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Makeup"
         },
         "WL": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Wholesale_Lots"
         },
         "NAAR": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Natural_and_Alternative_Remedies"
         },
         "VC": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Vision_Care"
         },
         "NCMAP": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Nail_Care__Manicure_and_Pedicure"
         },
         "MAM": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Medical_and_Mobility"
         },
         "HCAS": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Hair_Care_and_Styling"
         },
         "TABA": {
               "category_name": "Health_and_Beauty",
               "sub_category_name": "Tattoos_and_Body_Art"
         }
      },
      "Fashion": {
         "Dancewear": {
               "category_name": "Fashion",
               "sub_category_name": "Dancewear"
         },
         "Specialty": {
               "category_name": "Fashion",
               "sub_category_name": "Specialty"
         },
         "Women": {
               "category_name": "Fashion",
               "sub_category_name": "Women"
         },
         "Men": {
               "category_name": "Fashion",
               "sub_category_name": "Men"
         },
         "CRT": {
               "category_name": "Fashion",
               "sub_category_name": "Costumes__Reenactment__Theater"
         },
         "UAWC": {
               "category_name": "Fashion",
               "sub_category_name": "Uniforms_and_Work_Clothing"
         },
         "Baby": {
               "category_name": "Fashion",
               "sub_category_name": "Baby"
         },
         "WS": {
               "category_name": "Fashion",
               "sub_category_name": "Womens_Shoes"
         },
         "WAFO": {
               "category_name": "Fashion",
               "sub_category_name": "Wedding_and_Formal_Occasion"
         },
         "Kids": {
               "category_name": "Fashion",
               "sub_category_name": "Kids"
         }
      },
      "BAI": {
         "HPPAP": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Hydraulics__Pneumatics__Pumps_and_Plumbing"
         },
         "IAAMC": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Industrial_Automation_and_Motion_Controls"
         },
         "BMAS": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Building_Materials_and_Supplies"
         },
         "TMAI": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Test__Measurement_and_Inspection"
         },
         "Construction": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Construction"
         },
         "CAJS": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Cleaning_and_Janitorial_Supplies"
         },
         "WABFS": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Websites_and_Businesses_for_Sale"
         },
         "MH": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Material_Handling"
         },
         "AAF": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Agriculture_and_Forestry"
         },
         "HEPAA": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Heavy_Equipment__Parts_and_Attachments"
         },
         "FAH": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Fasteners_and_Hardware"
         },
         "Office": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Office"
         },
         "RAFS": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Restaurant_and_Food_Service"
         },
         "EEAS": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Electrical_Equipment_and_Supplies"
         },
         "RAS": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Retail_and_Services"
         },
         "CMAM": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "CNC__Metalworking_and_Manufacturing"
         },
         "LEAT": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Light_Equipment_and_Tools"
         },
         "HAR": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "HVAC_and_Refrigeration"
         },
         "ASAT": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Adhesives__Sealants_and_Tapes"
         },
         "PAGA": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Printing_and_Graphic_Arts"
         },
         "FAE": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Fuel_and_Energy"
         },
         "HLAD": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Healthcare__Lab_and_Dental"
         },
         "FMAS": {
               "category_name": "Business_and_Industrial",
               "sub_category_name": "Facility_Maintenance_and_Safety"
         }
      }
   },
   "eBay": {
      "CAA":{
         "Collectibles":{
            "category_name":"Collectibles_and_Art",
            "sub_category_name":"Collectibles"
         },
         "AACS":{
            "category_name":"Collectibles_and_Art",
            "sub_category_name":"Art_and_Craft_Supplies"
         },
         "CAPM":{
            "category_name":"Collectibles_and_Art",
            "sub_category_name":"Coins_and_Paper_Money"
         },
         "EM":{
            "category_name":"Collectibles_and_Art",
            "sub_category_name":"Entertainment_Memorabilia"
         },
         "Antiques":{
            "category_name":"Collectibles_and_Art",
            "sub_category_name":"Antiques"
         },
         "SMFSASC":{
            "category_name":"Collectibles_and_Art",
            "sub_category_name":"Sports_Memorabilia__Fan_Shop_and_Sports_Cards"
         },
         "PAG":{
            "category_name":"Collectibles_and_Art",
            "sub_category_name":"Pottery_and_Glass"
         },
         "Stamps":{
            "category_name":"Collectibles_and_Art",
            "sub_category_name":"Stamps"
         },
         "DATB":{
            "category_name":"Collectibles_and_Art",
            "sub_category_name":"Dolls_and_Teddy_Bears"
         },
         "Art":{
            "category_name":"Collectibles_and_Art",
            "sub_category_name":"Art"
         }
      },
      "TAH":{
         "SC":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Slot_Cars"
         },
         "OTAS":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Outdoor_Toys_and_Structures"
         },
         "VAAT":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Vintage_and_Antique_Toys"
         },
         "CCG":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Collectible_Card_Games"
         },
         "BT":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Building_Toys"
         },
         "DATV":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Diecast_and_Toy_Vehicles"
         },
         "RCACL":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Radio_Control_and_Control_Line"
         },
         "Games":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Games"
         },
         "AF":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Action_Figures"
         },
         "PTAPP":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Preschool_Toys_and_Pretend_Play"
         },
         "MRAT":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Model_Railroads_and_Trains"
         },
         "MAK":{
            "category_name":"Toys_and_Hobbies",
            "sub_category_name":"Models_and_Kits"
         }
      },
      "Fashion":{
         "Jewelry":{
            "category_name":"Fashion",
            "sub_category_name":"Jewelry"
         },
         "COASCSAA":{
            "category_name":"Fashion",
            "sub_category_name":"Costume__Occasion_and_Specialized_Clothing__Shoes_and_Accessories"
         },
         "Shoes":{
            "category_name":"Fashion",
            "sub_category_name":"Shoes"
         },
         "Baby":{
            "category_name":"Fashion",
            "sub_category_name":"Baby"
         },
         "WA":{
            "category_name":"Fashion",
            "sub_category_name":"Womens_Accessories"
         },
         "MA":{
            "category_name":"Fashion",
            "sub_category_name":"Mens_Accessories"
         }
      },
      "BAI":{
         "TMAI":{
            "category_name":"Business_and_Industrial",
            "sub_category_name":"Test__Measurement_and_Inspection"
         },
         "IAAMC":{
            "category_name":"Business_and_Industrial",
            "sub_category_name":"Industrial_Automation_and_Motion_Controls"
         },
         "MH":{
            "category_name":"Business_and_Industrial",
            "sub_category_name":"Material_Handling"
         },
         "LEAT":{
            "category_name":"Business_and_Industrial",
            "sub_category_name":"Light_Equipment_and_Tools"
         },
         "BMAS":{
            "category_name":"Business_and_Industrial",
            "sub_category_name":"Building_Materials_and_Supplies"
         },
         "HPPAP":{
            "category_name":"Business_and_Industrial",
            "sub_category_name":"Hydraulics__Pneumatics__Pumps_and_Plumbing"
         },
         "FAH":{
            "category_name":"Business_and_Industrial",
            "sub_category_name":"Fasteners_and_Hardware"
         }
      },
      "HAG":{
         "GCAPS":{
            "category_name":"Home_and_Garden",
            "sub_category_name":"Greeting_Cards_and_Party_Supply"
         },
         "HASD":{
            "category_name":"Home_and_Garden",
            "sub_category_name":"Holiday_and_Seasonal_Décor"
         },
         "WTAH":{
            "category_name":"Home_and_Garden",
            "sub_category_name":"Window_Treatments_and_Hardware"
         },
         "LLACF":{
            "category_name":"Home_and_Garden",
            "sub_category_name":"Lamps__Lighting_and_Ceiling_Fans"
         },
         "Bath":{
            "category_name":"Home_and_Garden",
            "sub_category_name":"Bath"
         },
         "FAB":{
            "category_name":"Home_and_Garden",
            "sub_category_name":"Food_and_Beverages"
         },
         "RAC":{
            "category_name":"Home_and_Garden",
            "sub_category_name":"Rugs_and_Carpets"
         },
         "WS":{
            "category_name":"Home_and_Garden",
            "sub_category_name":"Wedding_Supplies"
         }
      },
      "HAB":{
         "HC":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Health_Care"
         },
         "Makeup":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Makeup"
         },
         "NCMAP":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Nail_Care__Manicure_and_Pedicure"
         },
         "TABA":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Tattoos_and_Body_Art"
         },
         "BAB":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Bath_and_Body"
         },
         "SC":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Skin_Care"
         },
         "HCAS":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Hair_Care_and_Styling"
         },
         "MAM":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Medical_and_Mobility"
         },
         "VC":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Vision_Care"
         },
         "OC":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Oral_Care"
         },
         "SAHR":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Shaving_and_Hair_Removal"
         },
         "NAAR":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Natural_and_Alternative_Remedies"
         },
         "Massage":{
            "category_name":"Health_and_Beauty",
            "sub_category_name":"Massage"
         }
      },
      "Electronics":{
         "CTANH":{
            "category_name":"Electronics",
            "sub_category_name":"Computers__Tablets_and_Network_Hardware"
         },
         "RC":{
            "category_name":"Electronics",
            "sub_category_name":"Radio_Communication"
         },
         "CAP":{
            "category_name":"Electronics",
            "sub_category_name":"Cameras_and_Photo"
         },
         "CPSWAA":{
            "category_name":"Electronics",
            "sub_category_name":"Cell_Phones__Smart_Watches_and_Accessories"
         },
         "VE":{
            "category_name":"Electronics",
            "sub_category_name":"Vintage_Electronics"
         },
         "PAAH":{
            "category_name":"Electronics",
            "sub_category_name":"Portable_Audio_and_Headphones"
         },
         "VGAC":{
            "category_name":"Electronics",
            "sub_category_name":"Video_Games_and_Consoles"
         },
         "SASHE":{
            "category_name":"Electronics",
            "sub_category_name":"Surveillance_and_Smart_Home_Electronics"
         },
         "VR":{
            "category_name":"Electronics",
            "sub_category_name":"Virtual_Reality"
         },
         "MBAP":{
            "category_name":"Electronics",
            "sub_category_name":"Multipurpose_Batteries_and_Power"
         }
      },
      "BMAM":{
         "MIAG":{
            "category_name":"Books__Movies_and_Music",
            "sub_category_name":"Musical_Instruments_and_Gear"
         },
         "Books":{
            "category_name":"Books__Movies_and_Music",
            "sub_category_name":"Books"
         },
         "Music":{
            "category_name":"Books__Movies_and_Music",
            "sub_category_name":"Music"
         },
         "DAM":{
            "category_name":"Books__Movies_and_Music",
            "sub_category_name":"DVDs_and_Movies"
         }
      }
   },
   "Etsy":{
      "Accessories": {
         "BA": {
               "category_name": "Accessories",
               "sub_category_name": "Baby_Accessories_"
         },
         "BAB": {
               "category_name": "Accessories",
               "sub_category_name": "Belts_and_Braces_"
         },
         "BAC": {
               "category_name": "Accessories",
               "sub_category_name": "Bouquets_and_Corsages_"
         },
         "CA": {
               "category_name": "Accessories",
               "sub_category_name": "Costume_Accessories_"
         },
         "GAM": {
               "category_name": "Accessories",
               "sub_category_name": "Gloves_and_Mittens_"
         },
         "HA": {
               "category_name": "Accessories",
               "sub_category_name": "Hair_Accessories_"
         },
         "HAC": {
               "category_name": "Accessories",
               "sub_category_name": "Hats_and_Caps_"
         },
         "KAL": {
               "category_name": "Accessories",
               "sub_category_name": "Keychains_and_Lanyards_"
         },
         "PAP": {
               "category_name": "Accessories",
               "sub_category_name": "Patches_and_Pins_"
         },
         "SAW": {
               "category_name": "Accessories",
               "sub_category_name": "Scarves_and_Wraps_"
         },
         "SATA": {
               "category_name": "Accessories",
               "sub_category_name": "Suit_and_Tie_Accessories_"
         },
         "SAE": {
               "category_name": "Accessories",
               "sub_category_name": "Sunglasses_and_Eyewear_"
         }
      },
      "AAC": {
         "C": {
               "category_name": "Art_and_Collectibles",
               "sub_category_name": "Collectibles_"
         },
         "DAM": {
               "category_name": "Art_and_Collectibles",
               "sub_category_name": "Dolls_and_Miniatures_"
         },
         "DAI": {
               "category_name": "Art_and_Collectibles",
               "sub_category_name": "Drawing_and_Illustration_"
         },
         "FA": {
               "category_name": "Art_and_Collectibles",
               "sub_category_name": "Fibre_Arts_"
         },
         "GA": {
               "category_name": "Art_and_Collectibles",
               "sub_category_name": "Glass_Art_"
         },
         "MMAC": {
               "category_name": "Art_and_Collectibles",
               "sub_category_name": "Mixed_Media_and_Collage_"
         },
         "P": {
               "category_name": "Art_and_Collectibles",
               "sub_category_name": "Prints_"
         },
         "S": {
               "category_name": "Art_and_Collectibles",
               "sub_category_name": "Sculpture_"
         }
      },
      "BAP": {
         "AC": {
               "category_name": "Bags_and_Purses",
               "sub_category_name": "Accessory_Cases_"
         },
         "CASB": {
               "category_name": "Bags_and_Purses",
               "sub_category_name": "Clothing_and_Shoe_Bags_"
         },
         "CATS": {
               "category_name": "Bags_and_Purses",
               "sub_category_name": "Cosmetic_and_Toiletry_Storage_"
         },
         "EC": {
               "category_name": "Bags_and_Purses",
               "sub_category_name": "Electronics_Cases_"
         },
         "FAIB": {
               "category_name": "Bags_and_Purses",
               "sub_category_name": "Food_and_Insulated_Bags_"
         },
         "H": {
               "category_name": "Bags_and_Purses",
               "sub_category_name": "Handbags_"
         },
         "KAL": {
               "category_name": "Bags_and_Purses",
               "sub_category_name": "Keychains_and_Lanyards_"
         },
         "LAT": {
               "category_name": "Bags_and_Purses",
               "sub_category_name": "Luggage_and_Travel_"
         },
         "SB": {
               "category_name": "Bags_and_Purses",
               "sub_category_name": "Sports_Bags_"
         },
         "WAMC": {
               "category_name": "Bags_and_Purses",
               "sub_category_name": "Wallets_and_Money_Clips_"
         }
      },
      "BAB": {
         "BACC": {
               "category_name": "Bath_and_Beauty",
               "sub_category_name": "Baby_and_Child_Care_"
         },
         "BA": {
               "category_name": "Bath_and_Beauty",
               "sub_category_name": "Bath_Accessories_"
         },
         "CATS": {
               "category_name": "Bath_and_Beauty",
               "sub_category_name": "Cosmetic_and_Toiletry_Storage_"
         },
         "HC": {
               "category_name": "Bath_and_Beauty",
               "sub_category_name": "Hair_Care_"
         },
         "MAC": {
               "category_name": "Bath_and_Beauty",
               "sub_category_name": "Makeup_and_Cosmetics_"
         },
         "PC": {
               "category_name": "Bath_and_Beauty",
               "sub_category_name": "Personal_Care_"
         },
         "SC": {
               "category_name": "Bath_and_Beauty",
               "sub_category_name": "Skin_Care_"
         },
         "S": {
               "category_name": "Bath_and_Beauty",
               "sub_category_name": "Soaps_"
         },
         "SAR": {
               "category_name": "Bath_and_Beauty",
               "sub_category_name": "Spa_and_Relaxation_"
         }
      },
      "BFAM": {
         "B": {
               "category_name": "Books__Films_and_Music",
               "sub_category_name": "Books_"
         },
         "M": {
               "category_name": "Books__Films_and_Music",
               "sub_category_name": "Music_"
         }
      },
      "Clothing": {
         "BC": {
               "category_name": "Clothing",
               "sub_category_name": "Boys_Clothing_"
         },
         "GC": {
               "category_name": "Clothing",
               "sub_category_name": "Girls_Clothing_"
         },
         "MC": {
               "category_name": "Clothing",
               "sub_category_name": "Mens_Clothing_"
         },
         "UKC": {
               "category_name": "Clothing",
               "sub_category_name": "Unisex_Kids_Clothing_"
         },
         "WC": {
               "category_name": "Clothing",
               "sub_category_name": "Womens_Clothing_"
         }
      },
      "CSAT": {
         "HAH": {
               "category_name": "Craft_Supplies_and_Tools",
               "sub_category_name": "Home_and_Hobby_"
         },
         "JAB": {
               "category_name": "Craft_Supplies_and_Tools",
               "sub_category_name": "Jewellery_and_Beauty_"
         },
         "PPAK": {
               "category_name": "Craft_Supplies_and_Tools",
               "sub_category_name": "Paper__Party_and_Kids_"
         },
         "SAF": {
               "category_name": "Craft_Supplies_and_Tools",
               "sub_category_name": "Sewing_and_Fiber_"
         },
         "VA": {
               "category_name": "Craft_Supplies_and_Tools",
               "sub_category_name": "Visual_Arts_"
         }
      },
      "EAA": {
         "A": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "Audio_"
         },
         "BAC": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "Batteries_and_Charging_"
         },
         "CAC": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "Cables_and_Cords_"
         },
         "C": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "Cameras_"
         },
         "CPAA": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "Car_Parts_and_Accessories_"
         },
         "CPA": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "Cell_Phone_Accessories_"
         },
         "CAP": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "Computers_and_Peripherals_"
         },
         "DAS": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "Docking_and_Stands_"
         },
         "EC": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "Electronics_Cases_"
         },
         "MS": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "Maker_Supplies_"
         },
         "PAE": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "Parts_and_Electrical_"
         },
         "TAP": {
               "category_name": "Electronics_and_Accessories",
               "sub_category_name": "TV_and_Projection_"
         }
      },
      "HAL": {
         "B": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Bedding_"
         },
         "CS": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Cleaning_Supplies_"
         },
         "FAR": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Floor_and_Rugs_"
         },
         "FAD": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Food_and_Drink_"
         },
         "F": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Furniture_"
         },
         "HA": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Home_Appliances_"
         },
         "HD": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Home_Decor_"
         },
         "HI": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Home_Improvement_"
         },
         "KAD": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Kitchen_and_Dining_"
         },
         "L": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Lighting_"
         },
         "O": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Office_"
         },
         "OAG": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Outdoor_and_Gardening_"
         },
         "SAR": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Spirituality_and_Religion_"
         },
         "SAO": {
               "category_name": "Home_and_Living",
               "sub_category_name": "Storage_and_Organisation_"
         }
      },
      "Jewellery": {
         "BJ": {
               "category_name": "Jewellery",
               "sub_category_name": "Body_Jewellery_"
         },
         "B": {
               "category_name": "Jewellery",
               "sub_category_name": "Bracelets_"
         },
         "BPAC": {
               "category_name": "Jewellery",
               "sub_category_name": "Brooches__Pins_and_Clips_"
         },
         "CLATC": {
               "category_name": "Jewellery",
               "sub_category_name": "Cuff_Links_and_Tie_Clips_"
         },
         "E": {
               "category_name": "Jewellery",
               "sub_category_name": "Earrings_"
         },
         "JS": {
               "category_name": "Jewellery",
               "sub_category_name": "Jewellery_Storage_"
         },
         "N": {
               "category_name": "Jewellery",
               "sub_category_name": "Necklaces_"
         },
         "R": {
               "category_name": "Jewellery",
               "sub_category_name": "Rings_"
         },
         "W": {
               "category_name": "Jewellery",
               "sub_category_name": "Watches_"
         }
      },
      "PAPS": {
         "P": {
               "category_name": "Paper_and_Party_Supplies",
               "sub_category_name": "Paper_"
         },
         "PS": {
               "category_name": "Paper_and_Party_Supplies",
               "sub_category_name": "Party_Supplies_"
         }
      },
      "PS": {
         "PB": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Pet_Bedding_"
         },
         "PCAH": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Pet_Carriers_and_Houses_"
         },
         "PCAAS": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Pet_Clothing__Accessories_and_Shoes_"
         },
         "PCAL": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Pet_Collars_and_Leashes_"
         },
         "PF": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Pet_Furniture_"
         },
         "PHAW": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Pet_Health_and_Wellness_"
         },
         "UAM": {
               "category_name": "Pet_Supplies",
               "sub_category_name": "Urns_and_Memorials_"
         }
      },
      "Shoes": {
         "BS": {
               "category_name": "Shoes",
               "sub_category_name": "Boys_Shoes_"
         },
         "GS": {
               "category_name": "Shoes",
               "sub_category_name": "Girls_Shoes_"
         },
         "IAA": {
               "category_name": "Shoes",
               "sub_category_name": "Insoles_and_Accessories_"
         },
         "MS": {
               "category_name": "Shoes",
               "sub_category_name": "Mens_Shoes_"
         },
         "WS": {
               "category_name": "Shoes",
               "sub_category_name": "Womens_Shoes_"
         }
      },
      "TAG": {
         "GAP": {
               "category_name": "Toys_and_Games",
               "sub_category_name": "Games_and_Puzzles_"
         },
         "SAOR": {
               "category_name": "Toys_and_Games",
               "sub_category_name": "Sports_and_Outdoor_Recreation_"
         },
         "T": {
               "category_name": "Toys_and_Games",
               "sub_category_name": "Toys_"
         }
      },
      "Weddings": {
         "A": {
               "category_name": "Weddings",
               "sub_category_name": "Accessories_"
         },
         "C": {
               "category_name": "Weddings",
               "sub_category_name": "Clothing_"
         },
         "D": {
               "category_name": "Weddings",
               "sub_category_name": "Decorations_"
         },
         "GAM": {
               "category_name": "Weddings",
               "sub_category_name": "Gifts_and_Mementos_"
         },
         "IAP": {
               "category_name": "Weddings",
               "sub_category_name": "Invitations_and_Paper_"
         },
         "J": {
               "category_name": "Weddings",
               "sub_category_name": "Jewellery_"
         },
         "S": {
               "category_name": "Weddings",
               "sub_category_name": "Shoes_"
         }
      }
   }
}

marketplace_vdezi_mapping = { 
   'Beauty':{ 
      'Bath_and_Body':{ 
         'category_id':10002,
         'category_name':'Beauty',
         'category_key':'beauty',
         'sub_category_id':20020,
         'sub_category_name':'Body Care Product',
         'sub_category_key':'body_care_product'
      },
      'Fragrance':{ 
         'category_id':10002,
         'category_name':'Beauty',
         'category_key':'beauty',
         'sub_category_id':20021,
         'sub_category_name':'Fragrance',
         'sub_category_key':'fragrance'
      },
      'Hair_Care_and_Styling':{ 
         'category_id':10002,
         'category_name':'Beauty',
         'category_key':'beauty',
         'sub_category_id':20022,
         'sub_category_name':'Hair Care Product',
         'sub_category_key':'hair_care_product'
      },
      'Make_up_and_Nails':{ 
         'category_id':10002,
         'category_name':'Beauty',
         'category_key':'beauty',
         'sub_category_id':20024,
         'sub_category_name':'Make Up',
         'sub_category_key':'make_up'
      },
      'Skin_Care':{ 
         'category_id':10002,
         'category_name':'Beauty',
         'category_key':'beauty',
         'sub_category_id':20025,
         'sub_category_name':'Skin Care Product',
         'sub_category_key':'skin_care_product'
      },
      'Tools_and_Accessories':{ 
         'category_id':10002,
         'category_name':'Beauty',
         'category_key':'beauty',
         'sub_category_id':20023,
         'sub_category_name':'Hair Removal And Shaving Product',
         'sub_category_key':'hair_removal_and_shaving_product'
      }
   },
   'Books':{ 
      'Books':{ 
         'category_id':10003,
         'category_name':'Books',
         'category_key':'books',
         'sub_category_id':20026,
         'sub_category_name':'Books Misc',
         'sub_category_key':'books_misc'
      }
   },
   'Car_and_Motorbike':{ 
      'Car_Parts':{ 
         'category_id':10001,
         'category_name':'Auto Accessory',
         'category_key':'auto_accessory',
         'sub_category_id':20005,
         'sub_category_name':'Auto Part',
         'sub_category_key':'auto_part'
      },
      'Car_Tyres_and_Rims':{ 
         'category_id':10001,
         'category_name':'Auto Accessory',
         'category_key':'auto_accessory',
         'sub_category_id':20017,
         'sub_category_name':'Tire And Wheel',
         'sub_category_key':'tire_and_wheel'
      },
      'Car_and_Motorbike_Care':{ 
         'category_id':10001,
         'category_name':'Auto Accessory',
         'category_key':'auto_accessory',
         'sub_category_id':20006,
         'sub_category_name':'Cleaning Or Repair Kit',
         'sub_category_key':'cleaning_or_repair_kit'
      },
      'Car_and_Vehicle_Electronics':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20090,
         'sub_category_name':'Car Electronics',
         'sub_category_key':'car_electronics'
      },
      'Gifts_and_Merchandise':{ 
         'category_id':10001,
         'category_name':'Auto Accessory',
         'category_key':'auto_accessory',
         'sub_category_id':20001,
         'sub_category_name':'Auto Accessory Misc',
         'sub_category_key':'auto_accessory_misc'
      },
      'Motorbike_Accessories_and_Parts':{ 
         'category_id':10001,
         'category_name':'Auto Accessory',
         'category_key':'auto_accessory',
         'sub_category_id':20008,
         'sub_category_name':'Motorcycle Accessory',
         'sub_category_key':'motorcycle_accessory'
      },
      'Navigation_Devices':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20107,
         'sub_category_name':'Gps Or Navigation Accessory',
         'sub_category_key':'gps_or_navigation_accessory'
      },
      'Oils_and_Fluids':{ 
         'category_id':10001,
         'category_name':'Auto Accessory',
         'category_key':'auto_accessory',
         'sub_category_id':20004,
         'sub_category_name':'Auto Oil',
         'sub_category_key':'auto_oil'
      },
      'Paintwork':{ 
         'category_id':10001,
         'category_name':'Auto Accessory',
         'category_key':'auto_accessory',
         'sub_category_id':20001,
         'sub_category_name':'Auto Accessory Misc',
         'sub_category_key':'auto_accessory_misc'
      }
   },
   'Clothing_and_Accessories':{ 
      'Baby':{ 
         'category_id':10008,
         'category_name':'Fashion',
         'category_key':'fashion',
         'sub_category_id':20139,
         'sub_category_name':'Baby',
         'sub_category_key':'baby'
      },
      'Boys':{ 
         'category_id':10008,
         'category_name':'Fashion',
         'category_key':'fashion',
         'sub_category_id':20140,
         'sub_category_name':'Boys',
         'sub_category_key':'boys'
      },
      'Girls':{ 
         'category_id':10008,
         'category_name':'Fashion',
         'category_key':'fashion',
         'sub_category_id':20141,
         'sub_category_name':'Girls',
         'sub_category_key':'girls'
      },
      'Men':{ 
         'category_id':10008,
         'category_name':'Fashion',
         'category_key':'fashion',
         'sub_category_id':20143,
         'sub_category_name':'Men',
         'sub_category_key':'men'
      },
      'Women':{ 
         'category_id':10008,
         'category_name':'Fashion',
         'category_key':'fashion',
         'sub_category_id':20144,
         'sub_category_name':'Women',
         'sub_category_key':'women'
      }
   },
   'Computers_and_Accessories':{ 
      'Accessories_and_Peripherals':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20137,
         'sub_category_name':'Video Projectors And Accessories',
         'sub_category_key':'video_projectors_and_accessories'
      },
      'Components':{ 
         "category_id": 10005,
         "category_name": "Computers",
         "category_key": "computers",
         "sub_category_id": 20055,
         "sub_category_name": "Computer Component",
         "sub_category_key": "computer_component"
      },
      'Desktops':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20117,
         'sub_category_name':'Pc',
         'sub_category_key':'pc'
      },
      'External_Devices_and_Data_Storage':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20114,
         'sub_category_name':'Media Storage',
         'sub_category_key':'media_storage'
      },
      'Laptops':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20117,
         'sub_category_name':'Pc',
         'sub_category_key':'pc'
      },
      'Monitors':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20117,
         'sub_category_name':'Pc',
         'sub_category_key':'pc'
      },
      'Networking_Devices':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20116,
         'sub_category_name':'Network Adapter',
         'sub_category_key':'network_adapter'
      },
      'Scanners':{ 
         'category_id':10021,
         'category_name':'Office',
         'category_key':'office',
         'sub_category_id':20241,
         'sub_category_name':'Office Scanner',
         'sub_category_key':'office_scanner'
      },
      'Tablets':{ 
         'category_id':10005,
         'category_name':'Computers',
         'category_key':'computers',
         'sub_category_id':20075,
         'sub_category_name':'Tablet Computer',
         'sub_category_key':'tablet_computer'
      },
      'Warranties':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20117,
         'sub_category_name':'Pc',
         'sub_category_key':'pc'
      }
   },
   'Electronics':{ 
      'Accessories':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20080,
         'sub_category_name':'Audio Video Accessory',
         'sub_category_key':'audio_video_accessory'
      },
      'Cameras_and_Photography':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20098,
         'sub_category_name':'Ce Digital Camera',
         'sub_category_key':'ce_digital_camera'
      },
      'Car_and_Vehicle_Electronics':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20090,
         'sub_category_name':'Car Electronics',
         'sub_category_key':'car_electronics'
      },
      'Computers_and_Accessories':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20137,
         'sub_category_name':'Video Projectors And Accessories',
         'sub_category_key':'video_projectors_and_accessories'
      },
      'GPS_and_Accessories':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20107,
         'sub_category_name':'Gps Or Navigation Accessory',
         'sub_category_key':'gps_or_navigation_accessory'
      },
      'Home_Audio':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20131,
         'sub_category_name':'Stereo Shelf System',
         'sub_category_key':'stereo_shelf_system'
      },
      'Home_Theater__TV_and_Video':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20111,
         'sub_category_name':'Home Theater System Or Htib',
         'sub_category_key':'home_theater_system_or_htib'
      },
      'Mobiles_and_Accessories':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20119,
         'sub_category_name':'Phone Accessory',
         'sub_category_key':'phone_accessory'
      },
      'Portable_Media_Players':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20112,
         'sub_category_name':'Media Player',
         'sub_category_key':'media_player'
      },
      'Telephones_and_Accessories':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20119,
         'sub_category_name':'Phone Accessory',
         'sub_category_key':'phone_accessory'
      },
      'Warranties':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20113,
         'sub_category_name':'Media Player Or E Reader Accessory',
         'sub_category_key':'media_player_or_e_reader_accessory'
      }
   },
   'Grocery_and_Gourmet_Foods':{ 
      'Canned_and_Jarred_Food':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20148,
         'sub_category_name':'Food',
         'sub_category_key':'food'
      },
      'Cereal_and_Muesli':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20148,
         'sub_category_name':'Food',
         'sub_category_key':'food'
      },
      'Coffee__Tea_and_Beverages':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20147,
         'sub_category_name':'Beverages',
         'sub_category_key':'beverages'
      },
      'Cooking_and_Baking_Supplies':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20149,
         'sub_category_name':'Household Supplies',
         'sub_category_key':'household_supplies'
      },
      'Dried_Fruits__Nuts_and_Seeds':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20148,
         'sub_category_name':'Food',
         'sub_category_key':'food'
      },
      'Hampers_and_Gourmet_Gifts':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20148,
         'sub_category_name':'Food',
         'sub_category_key':'food'
      },
      'Jams__Honey_and_Spreads':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20148,
         'sub_category_name':'Food',
         'sub_category_key':'food'
      },
      'Pasta_and_Noodles':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20148,
         'sub_category_name':'Food',
         'sub_category_key':'food'
      },
      'Pickles':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20148,
         'sub_category_name':'Food',
         'sub_category_key':'food'
      },
      'Ready_To_Eat_and_Cook':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20148,
         'sub_category_name':'Food',
         'sub_category_key':'food'
      },
      'Snack_Foods':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20148,
         'sub_category_name':'Food',
         'sub_category_key':'food'
      },
      'Sweets__Chocolate_and_Gum':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20148,
         'sub_category_name':'Food',
         'sub_category_key':'food'
      }
   },
   'Health_and_Personal_Care':{ 
      'Bath_and_Shower':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20159,
         'sub_category_name':'Personal Care Appliances',
         'sub_category_key':'personal_care_appliances'
      },
      'Beauty_Tools_and_Accessories':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20159,
         'sub_category_name':'Personal Care Appliances',
         'sub_category_key':'personal_care_appliances'
      },
      'Diet_and_Nutrition':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20155,
         'sub_category_name':'Dietary Supplements',
         'sub_category_key':'dietary_supplements'
      },
      'Hair_Care_and_Styling':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20159,
         'sub_category_name':'Personal Care Appliances',
         'sub_category_key':'personal_care_appliances'
      },
      'Health_Care':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20159,
         'sub_category_name':'Personal Care Appliances',
         'sub_category_key':'personal_care_appliances'
      },
      'Home_Medical_Supplies_and_Equipment':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20157,
         'sub_category_name':'Medical Supplies',
         'sub_category_key':'medical_supplies'
      },
      'Household_Supplies':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20159,
         'sub_category_name':'Personal Care Appliances',
         'sub_category_key':'personal_care_appliances'
      },
      'Personal_Care':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20159,
         'sub_category_name':'Personal Care Appliances',
         'sub_category_key':'personal_care_appliances'
      },
      'Personal_Care_and_Health_Appliances':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20159,
         'sub_category_name':'Personal Care Appliances',
         'sub_category_key':'personal_care_appliances'
      },
      'Sexual_Wellness_and_Sensuality':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20162,
         'sub_category_name':'Sexual Wellness',
         'sub_category_key':'sexual_wellness'
      },
      'Skin_Care':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20156,
         'sub_category_name':'Health Misc',
         'sub_category_key':'health_misc'
      }
   },
   'Home_and_Kitchen':{ 
      'Artwork':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20163,
         'sub_category_name':'Art',
         'sub_category_key':'art'
      },
      'Craft_Materials':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20163,
         'sub_category_name':'Art',
         'sub_category_key':'art'
      },
      'Fresh_Flowers':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20183,
         'sub_category_name':'Seeds And Plants',
         'sub_category_key':'seeds_and_plants'
      },
      'Furniture':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20177,
         'sub_category_name':'Furniture And Decor',
         'sub_category_key':'furniture_and_decor'
      },
      'Heating__Cooling_and_Air_Quality':{ 
         'category_id':10014,
         'category_name':'Home Improvement',
         'category_key':'home_improvement',
         'sub_category_id':20190,
         'sub_category_name':'Electrical',
         'sub_category_key':'electrical'
      },
      'Home_Furnishing':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20177,
         'sub_category_name':'Furniture And Decor',
         'sub_category_key':'furniture_and_decor'
      },
      'Home_Improvement':{ 
         'category_id':10014,
         'category_name':'Home Improvement',
         'category_key':'home_improvement',
         'sub_category_id':20193,
         'sub_category_name':'Major Home Appliances',
         'sub_category_key':'major_home_appliances'
      },
      'Home_Storage_and_Organization':{ 
         'category_id':10014,
         'category_name':'Home Improvement',
         'category_key':'home_improvement',
         'sub_category_id':20194,
         'sub_category_name':'Organizers And Storage',
         'sub_category_key':'organizers_and_storage'
      },
      'Home_and_Décor':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20177,
         'sub_category_name':'Furniture And Decor',
         'sub_category_key':'furniture_and_decor'
      },
      'Indoor_Lighting':{ 
         'category_id':10018,
         'category_name':'Lighting',
         'category_key':'lighting',
         'sub_category_id':20222,
         'sub_category_name':'Light Bulbs',
         'sub_category_key':'light_bulbs'
      },
      'Kitchen_and_Dining':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20179,
         'sub_category_name':'Kitchen',
         'sub_category_key':'kitchen'
      },
      'Kitchen_and_Home_Appliances':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20179,
         'sub_category_name':'Kitchen',
         'sub_category_key':'kitchen'
      },
      'Large_Appliances':{ 
         'category_id':10014,
         'category_name':'Home Improvement',
         'category_key':'home_improvement',
         'sub_category_id':20193,
         'sub_category_name':'Major Home Appliances',
         'sub_category_key':'major_home_appliances'
      }
   },
   'Industrial_and_Scientific':{ 
      'Abrasive_and_Finishing_Products':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20197,
         'sub_category_name':'Abrasives',
         'sub_category_key':'abrasives'
      },
      'Additive_Manufacturing_Products':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20206,
         'sub_category_name':'Mechanical Components',
         'sub_category_key':'mechanical_components'
      },
      'Commercial_Door_Products':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20177,
         'sub_category_name':'Furniture And Decor',
         'sub_category_key':'furniture_and_decor'
      },
      'Cutting_Tools':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20200,
         'sub_category_name':'Cutting Tools',
         'sub_category_key':'cutting_tools'
      },
      'Fasteners':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20202,
         'sub_category_name':'Gears',
         'sub_category_key':'gears'
      },
      'Filtration':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20206,
         'sub_category_name':'Mechanical Components',
         'sub_category_key':'mechanical_components'
      },
      'Food_Service_Equipment_and_Supplies':{ 
         'category_id':10010,
         'category_name':'Food Service And Jan San',
         'category_key':'food_service_and_jan_san',
         'sub_category_id':20151,
         'sub_category_name':'Food Service And Jan San',
         'sub_category_key':'food_service_and_jan_san'
      },
      'Hydraulics__Pneumatics_and_Plumbing':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20206,
         'sub_category_name':'Mechanical Components',
         'sub_category_key':'mechanical_components'
      },
      'Industrial_Electrical':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20201,
         'sub_category_name':'Electronic Components',
         'sub_category_key':'electronic_components'
      },
      'Industrial_Hardware':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20197,
         'sub_category_name':'Abrasives',
         'sub_category_key':'abrasives'
      },
      'Janitorial_and_Sanitation_Supplies':{ 
         'category_id':10010,
         'category_name':'Food Service And Jan San',
         'category_key':'food_service_and_jan_san',
         'sub_category_id':20151,
         'sub_category_name':'Food Service And Jan San',
         'sub_category_key':'food_service_and_jan_san'
      },
      'Lab_and_Scientific_Products':{ 
         'category_id':10017,
         'category_name':'Lab Supplies',
         'category_key':'lab_supplies',
         'sub_category_id':20218,
         'sub_category_name':'Lab Supply',
         'sub_category_key':'lab_supply'
      },
      'Material_Handling_Products':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20198,
         'sub_category_name':'Adhesives And Sealants',
         'sub_category_key':'adhesives_and_sealants'
      },
      'Occupational_Health_and_Safety_Products':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20157,
         'sub_category_name':'Medical Supplies',
         'sub_category_key':'medical_supplies'
      },
      'Packaging_and_Shipping_Supplies':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20149,
         'sub_category_name':'Household Supplies',
         'sub_category_key':'household_supplies'
      },
      'Power_Transmission_Products':{ 
         'category_id':10024,
         'category_name':'Power Transmission',
         'category_key':'power_transmission',
         'sub_category_id':20257,
         'sub_category_name':'Linear Guides And Rails',
         'sub_category_key':'linear_guides_and_rails'
      },
      'Power_and_Hand_Tools':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20200,
         'sub_category_name':'Cutting Tools',
         'sub_category_key':'cutting_tools'
      },
      'Professional_Dental_Supplies':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20157,
         'sub_category_name':'Medical Supplies',
         'sub_category_key':'medical_supplies'
      },
      'Professional_Medical_Supplies':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20157,
         'sub_category_name':'Medical Supplies',
         'sub_category_key':'medical_supplies'
      },
      'Robotics':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20201,
         'sub_category_name':'Electronic Components',
         'sub_category_key':'electronic_components'
      },
      'Tapes__Adhesives_and_Sealers':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20199,
         'sub_category_name':'Adhesive Tapes',
         'sub_category_key':'adhesive_tapes'
      },
      'Test__Measure_and_Inspect':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20208,
         'sub_category_name':'Precision Measuring',
         'sub_category_key':'precision_measuring'
      }
   },
   'Movies_and_TV_Shows':{ 
      'Movies':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20134,
         'sub_category_name':'Tv Combos',
         'sub_category_key':'tv_combos'
      },
      'TV_Shows':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20134,
         'sub_category_name':'Tv Combos',
         'sub_category_key':'tv_combos'
      }
   },
   'Musical_Instruments':{ 
      'Bass_Guitars_and_Gear':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20225,
         'sub_category_name':'Guitars',
         'sub_category_key':'guitars'
      },
      'DJ_and_VJ_Equipment':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20230,
         'sub_category_name':'Sound And Recording Equipment',
         'sub_category_key':'sound_and_recording_equipment'
      },
      'Drums_and_Percussion':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20229,
         'sub_category_name':'Percussion Instruments',
         'sub_category_key':'percussion_instruments'
      },
      'Guitars_and_Gear':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20225,
         'sub_category_name':'Guitars',
         'sub_category_key':'guitars'
      },
      'Karaoke_Equipment':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20230,
         'sub_category_name':'Sound And Recording Equipment',
         'sub_category_key':'sound_and_recording_equipment'
      },
      'Microphones':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20230,
         'sub_category_name':'Sound And Recording Equipment',
         'sub_category_key':'sound_and_recording_equipment'
      },
      'PA_and_Stage':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20230,
         'sub_category_name':'Sound And Recording Equipment',
         'sub_category_key':'sound_and_recording_equipment'
      },
      'Piano_and_Keyboard':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20227,
         'sub_category_name':'Keyboard Instruments',
         'sub_category_key':'keyboard_instruments'
      },
      'Recording_and_Computer':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20230,
         'sub_category_name':'Sound And Recording Equipment',
         'sub_category_key':'sound_and_recording_equipment'
      },
      'String_Instruments':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20231,
         'sub_category_name':'Stringed Instruments',
         'sub_category_key':'stringed_instruments'
      },
      'Synthesizer_and_Sampler':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20226,
         'sub_category_name':'Instrument Parts And Accessories',
         'sub_category_key':'instrument_parts_and_accessories'
      },
      'Wind_Instruments':{ 
         'category_id':10020,
         'category_name':'Musical Instruments',
         'category_key':'musical_instruments',
         'sub_category_id':20229,
         'sub_category_name':'Percussion Instruments',
         'sub_category_key':'percussion_instruments'
      }
   },
   'Outdoor_Living':{ 
      'Abrasive_and_Finishing_Products':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20182,
         'sub_category_name':'Outdoor Living',
         'sub_category_key':'outdoor_living'
      },
      'Additive_Manufacturing_Products':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20249,
         'sub_category_name':'Outdoor Recreation Product',
         'sub_category_key':'outdoor_recreation_product'
      },
      'Backyard_Birding_Supplies':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20249,
         'sub_category_name':'Outdoor Recreation Product',
         'sub_category_key':'outdoor_recreation_product'
      },
      'Barbecue_and_Outdoor_Dining':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20182,
         'sub_category_name':'Outdoor Living',
         'sub_category_key':'outdoor_living'
      },
      'Beekeeping_Equipment':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20249,
         'sub_category_name':'Outdoor Recreation Product',
         'sub_category_key':'outdoor_recreation_product'
      },
      'Commercial_Door_Products':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20249,
         'sub_category_name':'Outdoor Recreation Product',
         'sub_category_key':'outdoor_recreation_product'
      },
      'Cutting_Tools':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20249,
         'sub_category_name':'Outdoor Recreation Product',
         'sub_category_key':'outdoor_recreation_product'
      },
      'Fasteners':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20249,
         'sub_category_name':'Outdoor Recreation Product',
         'sub_category_key':'outdoor_recreation_product'
      },
      'Filtration':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20249,
         'sub_category_name':'Outdoor Recreation Product',
         'sub_category_key':'outdoor_recreation_product'
      },
      'Food_Service_Equipment_and_Supplies':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20149,
         'sub_category_name':'Household Supplies',
         'sub_category_key':'household_supplies'
      },
      'Garden_and_Outdoor_Furniture':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20182,
         'sub_category_name':'Outdoor Living',
         'sub_category_key':'outdoor_living'
      },
      'Gardening':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20182,
         'sub_category_name':'Outdoor Living',
         'sub_category_key':'outdoor_living'
      },
      'Hydraulics,_Pneumatics_and_Plumbing':{ 
         'category_id':10014,
         'category_name':'Home Improvement',
         'category_key':'home_improvement',
         'sub_category_id':20195,
         'sub_category_name':'Plumbing Fixtures',
         'sub_category_key':'plumbing_fixtures'
      },
      'Industrial_Electrical':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20201,
         'sub_category_name':'Electronic Components',
         'sub_category_key':'electronic_components'
      },
      'Industrial_Hardware':{ 
         'category_id':10014,
         'category_name':'Home Improvement',
         'category_key':'home_improvement',
         'sub_category_id':20191,
         'sub_category_name':'Hardware',
         'sub_category_key':'hardware'
      },
      'Janitorial_and_Sanitation_Supplies':{ 
         'category_id':10010,
         'category_name':'Food Service And Jan San',
         'category_key':'food_service_and_jan_san',
         'sub_category_id':20151,
         'sub_category_name':'Food Service And Jan San',
         'sub_category_key':'food_service_and_jan_san'
      },
      'Lab_and_Scientific_Products':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20182,
         'sub_category_name':'Outdoor Living',
         'sub_category_key':'outdoor_living'
      },
      'Material_Handling_Products':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20182,
         'sub_category_name':'Outdoor Living',
         'sub_category_key':'outdoor_living'
      },
      'Mowers_and_Outdoor_Power_Tools':{ 
         'category_id':10006,
         'category_name':'Consumer Electronics',
         'category_key':'consumer_electronics',
         'sub_category_id':20124,
         'sub_category_name':'Power Supplies Or Protection',
         'sub_category_key':'power_supplies_or_protection'
      },
      'Occupational_Health_and_Safety_Products':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20157,
         'sub_category_name':'Medical Supplies',
         'sub_category_key':'medical_supplies'
      },
      'Outdoor_Décor':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20177,
         'sub_category_name':'Furniture And Decor',
         'sub_category_key':'furniture_and_decor'
      },
      'Packaging_and_Shipping_Supplies':{ 
         'category_id':10009,
         'category_name':'Food And Beverages',
         'category_key':'food_and_beverages',
         'sub_category_id':20149,
         'sub_category_name':'Household Supplies',
         'sub_category_key':'household_supplies'
      },
      'Pest_Control':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20182,
         'sub_category_name':'Outdoor Living',
         'sub_category_key':'outdoor_living'
      },
      'Plants__Seeds_and_Bulbs':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20183,
         'sub_category_name':'Seeds And Plants',
         'sub_category_key':'seeds_and_plants'
      },
      'Power_and_Hand_Tools':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20182,
         'sub_category_name':'Outdoor Living',
         'sub_category_key':'outdoor_living'
      },
      'Professional_Dental_Supplies':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20157,
         'sub_category_name':'Medical Supplies',
         'sub_category_key':'medical_supplies'
      },
      'Professional_Medical_Supplies':{ 
         'category_id':10012,
         'category_name':'Health',
         'category_key':'health',
         'sub_category_id':20157,
         'sub_category_name':'Medical Supplies',
         'sub_category_key':'medical_supplies'
      },
      'Robotics':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20182,
         'sub_category_name':'Outdoor Living',
         'sub_category_key':'outdoor_living'
      },
      'Solar_and_Wind_Power':{ 
         'category_id':10013,
         'category_name':'Home',
         'category_key':'home',
         'sub_category_id':20182,
         'sub_category_name':'Outdoor Living',
         'sub_category_key':'outdoor_living'
      },
      'Tapes,_Adhesives_and_Sealers':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20199,
         'sub_category_name':'Adhesive Tapes',
         'sub_category_key':'adhesive_tapes'
      },
      'Test,_Measure_and_Inspect':{ 
         'category_id':10015,
         'category_name':'Industrial',
         'category_key':'industrial',
         'sub_category_id':20208,
         'sub_category_name':'Precision Measuring',
         'sub_category_key':'precision_measuring'
      }
   },
   'Pet_Supplies':{ 
      'Birds':{ 
         'category_id':10023,
         'category_name':'Pet Supplies',
         'category_key':'pet_supplies',
         'sub_category_id':20250,
         'sub_category_name':'Pet Supplies Misc',
         'sub_category_key':'pet_supplies_misc'
      },
      'Cats':{ 
         'category_id':10023,
         'category_name':'Pet Supplies',
         'category_key':'pet_supplies',
         'sub_category_id':20250,
         'sub_category_name':'Pet Supplies Misc',
         'sub_category_key':'pet_supplies_misc'
      },
      'Dogs':{ 
         'category_id':10023,
         'category_name':'Pet Supplies',
         'category_key':'pet_supplies',
         'sub_category_id':20250,
         'sub_category_name':'Pet Supplies Misc',
         'sub_category_key':'pet_supplies_misc'
      },
      'Fish_and_Aquatics':{ 
         'category_id':10023,
         'category_name':'Pet Supplies',
         'category_key':'pet_supplies',
         'sub_category_id':20250,
         'sub_category_name':'Pet Supplies Misc',
         'sub_category_key':'pet_supplies_misc'
      },
      'Small_Animals':{ 
         'category_id':10023,
         'category_name':'Pet Supplies',
         'category_key':'pet_supplies',
         'sub_category_id':20250,
         'sub_category_name':'Pet Supplies Misc',
         'sub_category_key':'pet_supplies_misc'
      }
   },
   'Shoes_and_Handbags':{ 
      'Handbags__Purses_and_Clutches':{ 
         'category_id':10026,
         'category_name':'Shoes',
         'category_key':'shoes',
         'sub_category_id':20283,
         'sub_category_name':'Handbag',
         'sub_category_key':'handbag'
      },
      'Shoe_Care_and_Accessories':{ 
         'category_id':10026,
         'category_name':'Shoes',
         'category_key':'shoes',
         'sub_category_id':20286,
         'sub_category_name':'Shoe Accessory',
         'sub_category_key':'shoe_accessory'
      },
      'Shoes':{ 
         'category_id':10026,
         'category_name':'Shoes',
         'category_key':'shoes',
         'sub_category_id':20285,
         'sub_category_name':'Shoes',
         'sub_category_key':'shoes'
      }
   },
   'Software':{ 
      'Accounting_and_Finance':{ 
         'category_id':10021,
         'category_name':'Office',
         'category_key':'office',
         'sub_category_id':20240,
         'sub_category_name':'Office Products',
         'sub_category_key':'office_products'
      },
      'Antivirus_and_Security':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20289,
         'sub_category_name':'Software',
         'sub_category_key':'software'
      },
      'Business_and_Office':{ 
         'category_id':10021,
         'category_name':'Office',
         'category_key':'office',
         'sub_category_id':20240,
         'sub_category_name':'Office Products',
         'sub_category_key':'office_products'
      },
      "Children's_Software":{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20289,
         'sub_category_name':'Software',
         'sub_category_key':'software'
      },
      'Childrens_Software':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20289,
         'sub_category_name':'Software',
         'sub_category_key':'software'
      },
      'Education_and_Reference':{ 
         'category_id':10021,
         'category_name':'Office',
         'category_key':'office',
         'sub_category_id':20235,
         'sub_category_name':'Educational Supplies',
         'sub_category_key':'educational_supplies'
      },
      'Graphics_and_Design':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20289,
         'sub_category_name':'Software',
         'sub_category_key':'software'
      },
      'Home_and_Hobbies':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20289,
         'sub_category_name':'Software',
         'sub_category_key':'software'
      },
      'Language_and_Travel':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20289,
         'sub_category_name':'Software',
         'sub_category_key':'software'
      },
      'Networking_and_Servers':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20289,
         'sub_category_name':'Software',
         'sub_category_key':'software'
      },
      'Operating_Systems':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20289,
         'sub_category_name':'Software',
         'sub_category_key':'software'
      },
      'Photography':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20289,
         'sub_category_name':'Software',
         'sub_category_key':'software'
      },
      'Programming_and_Web_Development':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20289,
         'sub_category_name':'Software',
         'sub_category_key':'software'
      },
      'System_Utility_Software':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20289,
         'sub_category_name':'Software',
         'sub_category_key':'software'
      }
   },
   'Sports__Fitness_and_Outdoors':{ 
      'Accessories':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20249,
         'sub_category_name':'Outdoor Recreation Product',
         'sub_category_key':'outdoor_recreation_product'
      },
      'Archery':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Badminton':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Baseball':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Basketball':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Billiards':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Boxing':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Camping_and_Hiking':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20246,
         'sub_category_name':'Camping Equipment',
         'sub_category_key':'camping_equipment'
      },
      'Climbing':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20246,
         'sub_category_name':'Camping Equipment',
         'sub_category_key':'camping_equipment'
      },
      'Cricket':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Cycling':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20247,
         'sub_category_name':'Cycling Equipment',
         'sub_category_key':'cycling_equipment'
      },
      'Darts_and_Dartboards':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20249,
         'sub_category_name':'Outdoor Recreation Product',
         'sub_category_key':'outdoor_recreation_product'
      },
      'Disc_Sports':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Equestrian_Sports':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Exercise_and_Fitness':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20249,
         'sub_category_name':'Outdoor Recreation Product',
         'sub_category_key':'outdoor_recreation_product'
      },
      'Fan_Shop':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Field_Hockey':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Fishing':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20248,
         'sub_category_name':'Fishing Equipment',
         'sub_category_key':'fishing_equipment'
      },
      'Football':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Footwear':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Golf':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20296,
         'sub_category_name':'Golfclub Iron',
         'sub_category_key':'golfclub_iron'
      },
      'Gymnastics':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Martial_Arts':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Ripsticking':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20249,
         'sub_category_name':'Outdoor Recreation Product',
         'sub_category_key':'outdoor_recreation_product'
      },
      'Rugby':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Running':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Skates__Skateboards_and_Scooters':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Snooker':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Sports_Clothing':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Sports_Gadgets':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Squash':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Table_Tennis':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Team_Handball':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Tennis':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Track_and_Field':{ 
         'category_id':10022,
         'category_name':'Outdoors',
         'category_key':'outdoors',
         'sub_category_id':20247,
         'sub_category_name':'Cycling Equipment',
         'sub_category_key':'cycling_equipment'
      },
      'Volleyball':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      },
      'Water_Sports':{ 
         'category_id':10028,
         'category_name':'Sports',
         'category_key':'sports',
         'sub_category_id':20300,
         'sub_category_name':'Sporting Goods',
         'sub_category_key':'sporting_goods'
      }
   },
   'Toys_and_Games':{ 
      'Action_and_Toy_Figures':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Arts_and_Crafts':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Baby_and_Toddler_Toys':{ 
         'category_id':10032,
         'category_name':'Toys Baby',
         'category_key':'toys_baby',
         'sub_category_id':20319,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Bikes__Trikes_and_Ride_Ons':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Building_and_Construction_Toys':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Coin_and_Stamp_Collecting':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Collectible_Trading_Cards_and_Accessories':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20310,
         'sub_category_name':'Collectible Card',
         'sub_category_key':'collectible_card'
      },
      'Cosmetics_and_Jewellery':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Die-Cast_and_Toy_Vehicles':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Die_Cast_and_Toy_Vehicles':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Dolls_and_Accessories':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Dressing_Up_and_Costumes':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20311,
         'sub_category_name':'Costume',
         'sub_category_key':'costume'
      },
      'Electronic_Toys':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Games':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20312,
         'sub_category_name':'Games',
         'sub_category_key':'games'
      },
      'Learning_and_Education':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Marble_Runs':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Model_Building_Kits':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Model_Trains_and_Railway_Sets':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Musical_Toy_Instruments':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Novelty_and_Gag_Toys':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Party_Supplies':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20315,
         'sub_category_name':'Party Supplies',
         'sub_category_key':'party_supplies'
      },
      'Pretend_Play':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20312,
         'sub_category_name':'Games',
         'sub_category_key':'games'
      },
      'Puppets_and_Puppet_Theatres':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Puzzles':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20316,
         'sub_category_name':'Puzzles',
         'sub_category_key':'puzzles'
      },
      'Radio_and_Remote_Control':{ 
         'category_id':10032,
         'category_name':'Toys Baby',
         'category_key':'toys_baby',
         'sub_category_id':20319,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Real-Food_Appliances':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Real_Food_Appliances':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'School_Supplies':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Soft_Toys':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      },
      'Sport_and_Outdoor':{ 
         'category_id':10031,
         'category_name':'Toys',
         'category_key':'toys',
         'sub_category_id':20317,
         'sub_category_name':'Toys And Games',
         'sub_category_key':'toys_and_games'
      }
   },
   'Video_Games':{ 
      'Microconsoles_and_Handhelds':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'Nintendo_3DS':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'Nintendo_DS':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'PC_Games':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'PSP':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'PlayStation_2':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'PlayStation_3':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'PlayStation_4':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'PlayStation_Vita':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'Wii':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'Wii_U':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'Xbox_360':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      },
      'Xbox_One':{ 
         'category_id':10027,
         'category_name':'Software Video Games',
         'category_key':'software_video_games',
         'sub_category_id':20291,
         'sub_category_name':'Video Games',
         'sub_category_key':'video_games'
      }
   },
   'Bags__Wallets_and_Luggage':{
      'Bags_and_Backpacks':{ 
         "category_id": 10008,
         "category_name": "Fashion",
         "category_key": "fashion",
         "sub_category_id": 20142,
         "sub_category_name": "Luggage And Travel Gear",
         "sub_category_key": "luggage_and_travel_gear"
      },
      'Handbags_and_Clutches':{
         "category_id": 10008,
         "category_name": "Fashion",
         "category_key": "fashion",
         "sub_category_id": 20142,
         "sub_category_name": "Luggage And Travel Gear",
         "sub_category_key": "luggage_and_travel_gear"
      },
      'Luggage':{
         "category_id": 10008,
         "category_name": "Fashion",
         "category_key": "fashion",
         "sub_category_id": 20142,
         "sub_category_name": "Luggage And Travel Gear",
         "sub_category_key": "luggage_and_travel_gear"
      },
      'Travel_Accessories':{
         "category_id": 10008,
         "category_name": "Fashion",
         "category_key": "fashion",
         "sub_category_id": 20142,
         "sub_category_name": "Luggage And Travel Gear",
         "sub_category_key": "luggage_and_travel_gear"
      },
      'Wallets__Card_Cases_and_Money_Organizers':{
         "category_id": 10008,
         "category_name": "Fashion",
         "category_key": "fashion",
         "sub_category_id": 20142,
         "sub_category_name": "Luggage And Travel Gear",
         "sub_category_key": "luggage_and_travel_gear"
      }
   },
   'Watches':{
      'Watches':{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20217,
         "sub_category_name": "Watch",
         "sub_category_key": "watch"
      }
   },
   'Baby':{
      'Activity_and_Play_Time':{
         "category_id": 10032,
         "category_name": "Toys Baby",
         "category_key": "toys_baby",
         "sub_category_id": 20319,
         "sub_category_name": "Toys And Games",
         "sub_category_key": "toys_and_games"
      },
      'Baby_Care':{
         "category_id": 10032,
         "category_name": "Toys Baby",
         "category_key": "toys_baby",
         "sub_category_id": 20318,
         "sub_category_name": "Baby Products",
         "sub_category_key": "baby_products"
      },
      'Baby_Clothing':{
         "category_id": 10008,
         "category_name": "Fashion",
         "category_key": "fashion",
         "sub_category_id": 20139,
         "sub_category_name": "Baby",
         "sub_category_key": "baby"
      },
      'Baby_Safety':{
         "category_id": 10032,
         "category_name": "Toys Baby",
         "category_key": "toys_baby",
         "sub_category_id": 20318,
         "sub_category_name": "Baby Products",
         "sub_category_key": "baby_products"
      },
      'Baby_Shoes':{
         "category_id": 10026,
         "category_name": "Shoes",
         "category_key": "shoes",
         "sub_category_id": 20285,
         "sub_category_name": "Shoes",
         "sub_category_key": "shoes"
      },
      'Bedding__Furniture_and_Room_Décor':{
         "category_id": 10013,
         "category_name": "Home",
         "category_key": "home",
         "sub_category_id": 20177,
         "sub_category_name": "Furniture And Decor",
         "sub_category_key": "furniture_and_decor"
      },
      'Car_Seats_and_Accessories':{
         "category_id": 10001,
         "category_name": "Auto Accessory",
         "category_key": "auto_accessory",
         "sub_category_id": 20012,
         "sub_category_name": "Riding Apparel",
         "sub_category_key": "riding_apparel"
      },
      "Feeding":{
         "category_id": 10009,
         "category_name": "Food And Beverages",
         "category_key": "food_and_beverages",
         "sub_category_id": 20145,
         "sub_category_name": "Baby Food",
         "sub_category_key": "baby_food"
      },
      "Maternity":{
         "category_id": 10008,
         "category_name": "Fashion",
         "category_key": "fashion",
         "sub_category_id": 20144,
         "sub_category_name": "Women",
         "sub_category_key": "women"
      },
      "Pacifiers_and_Teethers":{
         "category_id": 10032,
         "category_name": "Toys Baby",
         "category_key": "toys_baby",
         "sub_category_id": 20318,
         "sub_category_name": "Baby Products",
         "sub_category_key": "baby_products"
      },
      "Potty_Training_and_Step_Stools":{
         "category_id": 10032,
         "category_name": "Toys Baby",
         "category_key": "toys_baby",
         "sub_category_id": 20318,
         "sub_category_name": "Baby Products",
         "sub_category_key": "baby_products"
      },
      "Strollers__Buggies_and_Prams":{
         "category_id": 10032,
         "category_name": "Toys Baby",
         "category_key": "toys_baby",
         "sub_category_id": 20318,
         "sub_category_name": "Baby Products",
         "sub_category_key": "baby_products"
      },
      "Diapering_and_Nappy_Changing":{
         "category_id": 10032,
         "category_name": "Toys Baby",
         "category_key": "toys_baby",
         "sub_category_id": 20318,
         "sub_category_name": "Baby Products",
         "sub_category_key": "baby_products"
      }
   },
   "Office_Products":{
      "Calendars__Planners_and_Personal_Organisers":{
         "category_id": 10021,
         "category_name": "Office",
         "category_key": "office",
         "sub_category_id": 20240,
         "sub_category_name": "Office Products",
         "sub_category_key": "office_products"
      },
      "Envelopes_and_Postal_Supplies":{
         "category_id": 10021,
         "category_name": "Office",
         "category_key": "office",
         "sub_category_id": 20240,
         "sub_category_name": "Office Products",
         "sub_category_key": "office_products"
      },
      "Office_Electronics":{
         "category_id": 10021,
         "category_name": "Office",
         "category_key": "office",
         "sub_category_id": 20237,
         "sub_category_name": "Office Electronics",
         "sub_category_key": "office_electronics"
      },
      "Office_Paper_Products":{
         "category_id": 10021,
         "category_name": "Office",
         "category_key": "office",
         "sub_category_id": 20242,
         "sub_category_name": "Paper Products",
         "sub_category_key": "paper_products"
      },
      "Office_Supplies":{
         "category_id": 10021,
         "category_name": "Office",
         "category_key": "office",
         "sub_category_id": 20235,
         "sub_category_name": "Educational Supplies",
         "sub_category_key": "educational_supplies"
      },
      "Stationery":{
         "category_id": 10021,
         "category_name": "Office",
         "category_key": "office",
         "sub_category_id": 20240,
         "sub_category_name": "Office Products",
         "sub_category_key": "office_products"
      }
   },
   "Jewellery":{
      "Earrings":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20209,
         "sub_category_name": "Fashion Earring",
         "sub_category_key": "fashion_earring"
      },
      "Chains_and_Necklaces":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20210,
         "sub_category_name": "Fashion Necklace Bracelet Anklet",
         "sub_category_key": "fashion_necklace_bracelet_anklet"
      },
      "Bangles_and_Bracelets":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20210,
         "sub_category_name": "Fashion Necklace Bracelet Anklet",
         "sub_category_key": "fashion_necklace_bracelet_anklet"
      },
      "Rings":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20212,
         "sub_category_name": "Fashion Ring",
         "sub_category_key": "fashion_ring"
      },
      "Pendants":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20215,
         "sub_category_name": "Fine Other",
         "sub_category_key": "fine_other"
      },
      "Jewellery_Sets":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Mangalsutras_and_Tanmaniyas":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20210,
         "sub_category_name": "Fashion Necklace Bracelet Anklet",
         "sub_category_key": "fashion_necklace_bracelet_anklet"
      },
      "Nose_Rings_and_Pins":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20212,
         "sub_category_name": "Fashion Ring",
         "sub_category_key": "fashion_ring"
      },
      "Hair_Accessories":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Toe_Rings":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Anklets":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20210,
         "sub_category_name": "Fashion Necklace Bracelet Anklet",
         "sub_category_key": "fashion_necklace_bracelet_anklet"
      },
      "Body_Jewellery":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Brooches_and_Pins":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Beads_and_Charms":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Coins_and_Bars":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Loose_Gemstones_and_Diamonds":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20215,
         "sub_category_name": "Fine Other",
         "sub_category_key": "fine_other"
      },
      "Bracelets_and_Kadas":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20210,
         "sub_category_name": "Fashion Necklace Bracelet Anklet",
         "sub_category_key": "fashion_necklace_bracelet_anklet"
      },
      "Chains":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Cufflinks_and_Shirt_Accessories":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Baby":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20215,
         "sub_category_name": "Fine Other",
         "sub_category_key": "fine_other"
      },
      "Boxes_and_Organisers":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Cleaning_and_Care":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Pouches":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Ring_Cushions":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Ring_Sizers":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Women":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Men":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Girls":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Boys":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      },
      "Jewellery_Boxes_and_Care":{
         "category_id": 10016,
         "category_name": "Jewelry",
         "category_key": "jewelry",
         "sub_category_id": 20211,
         "sub_category_name": "Fashion Other",
         "sub_category_key": "fashion_other"
      }
   }
}
