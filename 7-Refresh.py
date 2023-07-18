def unhide():
	elem = doc.Models[0].RootItem
	collector = ModelItemCollection()
	for parent in elem.Children:
		for child in parent.Children:
			collector.Add(child)
	doc.Models.SetHidden(collector,False)


doc.Models.ResetAllPermanentMaterials()
doc.Models.ResetAllTemporaryMaterials()

unhide()