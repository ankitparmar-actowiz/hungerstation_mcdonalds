import json

file = open('hunderstation_mcdonalds.json', 'r')
jsonData = json.loads(file.read())

mainList = []

totalMenuItems = len(jsonData['menuitems'])
for menu in range(totalMenuItems):
    menu_group_id = jsonData['menuitems'][menu]['menugroup_id']
    menu_item_name = jsonData['menuitems'][menu]['name']
    menu_item_description = jsonData['menuitems'][menu]['description']
    menu_item_price = jsonData['menuitems'][menu]['price']
    menu_item_discount_price = jsonData['menuitems'][menu]['pre_discount_price']
    image = jsonData['menuitems'][menu]['images'][10]['url']

    totalMainAddOnsIDs = []
    lenOfIDs = len(jsonData['modifier_groups'])
    for i in range(lenOfIDs):
        ID = jsonData['modifier_groups'][i]['id']
        totalMainAddOnsIDs.append(ID)

    totalMenuIDs = []
    totalMenuName = []
    lenOfMenuIDs = len(jsonData['menugroups'])
    for i in range(lenOfMenuIDs):
        MenuID = jsonData['menugroups'][i]['id']
        category = jsonData['menugroups'][i]['name']
        totalMenuIDs.append(MenuID)
        totalMenuName.append(category)
    
    mainAddOns = {}
    getTotalMainAddOns = jsonData['menuitems'][menu]['modifier_group_ids']
    if len(getTotalMainAddOns) != 0:
        for mainAons in getTotalMainAddOns:
            if mainAons in totalMainAddOnsIDs:
                getIndex = totalMainAddOnsIDs.index(mainAons)
                getMainAddOnsName = jsonData['modifier_groups'][getIndex]['name']
                subAddOns =[]
                sunAddOnsDict = {}
                modifiers = jsonData['modifier_groups'][getIndex]['modifiers']
                for subAons in modifiers:
                    getSubAddOnsName = subAons['name']
                    etSubAddOnsPrice = subAons['price']
                    sunAddOnsDict = {
                        'name': getSubAddOnsName,
                        'price': etSubAddOnsPrice
                    }
                    subAddOns.append(sunAddOnsDict)
            else:
                print('Add Ons ID not found')
            mainAddOns[getMainAddOnsName] = subAddOns
    else:
        print(f"No Main Add Ons found for {menu}") 

    if menu_group_id in totalMenuIDs:
        getIndex = totalMenuIDs.index(menu_group_id)
        category = totalMenuName[getIndex]
    
    mainList.append({
        'menu_item_name': menu_item_name,
        'menu_item_description': menu_item_description,
        'menu_item_price': menu_item_price,
		'menu_item_discount_price': menu_item_discount_price,
		'AddOns': mainAddOns,
		'category': category,
        'image': image
    })

def exportToJSON():
	with open("output.json", "w", encoding="utf-8") as f:
		json.dump(mainList, f, ensure_ascii=False, indent=4)

exportToJSON()