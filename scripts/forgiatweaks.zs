recipes.remove(<valkyrienwarfare:shipblock>);
recipes.remove(<valkyrienwarfarecombat:basiccannonspawner>);
recipes.remove(<valkyrienwarfarecombat:turretcannonball>);
recipes.remove(<valkyrienwarfarecombat:powderpouch>;
recipes.remove(<valkyrienwarfarecontrol:basicengine>);
recipes.remove(<valkyrienwarfarecontrol:advancedengine>);
recipes.remove(<valkyrienwarfarecontrol:eliteengine>);
recipes.remove(<valkyrienwarfarecontrol:ultimateengine>);
recipes.remove(<valkyrienwarfarecontrol:basicengine>);
recipes.remove(<valkyrienwarfarecombat:explosivearrow>);

recipes.addShaped(<valkyrienwarfarecontrol:basicengine>, [	[<extrautils2:machine>.withTag({Type: ""extrautils2:generator_survival""}), <minecraft:diamond>, <minecraft:diamond>],
															[<mekanism:enrichedalloy>, <mekanism:enrichedalloy>, <mekanism:controlcircuit>],
															[[<extrautils2:machine>.withTag({Type: ""extrautils2:generator_survival""}), <minecraft:diamond>, <minecraft:diamond>]	]);
															
recipes.addShaped(<valkyrienwarfarecontrol:advancedengine>, [	[<extrautils2:machine>.withTag({Type: ""extrautils2:generator_lava""}), <mekanism:reinforcedalloy>, <minecraft:diamond_block>],
															[<valkyrienwarfarecontrol:basicengine>, <valkyrienwarfarecontrol:basicengine>, <mekanism:controlcircuit:1>],
															[[<extrautils2:machine>.withTag({Type: ""extrautils2:generator_lava""}), <mekanism:reinforcedalloy>, <minecraft:diamond_block>]	]);
															
recipes.addShaped(<valkyrienwarfarecontrol:elitedengine>, [	[<extrautils2:machine>.withTag({Type: ""extrautils2:generator_survival""}), <minecraft:diamond>, <minecraft:diamond>],
															[<valkyrienwarfarecontrol:advancedengine>, <valkyrienwarfarecontrol:advancedengine>, <mekanism:controlcircuit:2>],
															[[<extrautils2:machine>.withTag({Type: ""extrautils2:generator_survival""}), <minecraft:diamond>, <minecraft:diamond>]	]);
															
recipes.addShaped(<valkyrienwarfarecontrol:ultimateengine>, [	[<extrautils2:machine>.withTag({Type: ""extrautils2:generator_survival""}), <minecraft:diamond>, <minecraft:diamond>],
															[<valkyrienwarfarecontrol:elitedengine>, <valkyrienwarfarecontrol:elitedengine>, <mekanism:controlcircuit:3>],
															[[<extrautils2:machine>.withTag({Type: ""extrautils2:generator_survival""}), <minecraft:diamond>, <minecraft:diamond>]	]);														