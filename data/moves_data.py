MOVES = {
    # =========================
    # MOVES NORMAL
    # =========================
    "Tackle": {
        "type": "Normal",
        "category": "Physical",
        "power": 40,
        "accuracy": 100,
        "pp": 35,
        "description": "A physical attack with no special effects."
    },
    "Scratch": {
        "type": "Normal",
        "category": "Physical",
        "power": 40,
        "accuracy": 100,
        "pp": 35,
        "description": "Scratches the target with sharp claws."
    },
    "Quick Attack": {
        "type": "Normal",
        "category": "Physical",
        "power": 40,
        "accuracy": 100,
        "pp": 30,
        "priority": 1,
        "description": "An extremely fast attack that always strikes first."
    },
    "Bite": {
        "type": "Normal",
        "category": "Physical",
        "power": 60,
        "accuracy": 100,
        "pp": 25,
        "flinch_chance": 0.3,
        "description": "Bites the target. May cause flinching."
    },
    "Body Slam": {
        "type": "Normal",
        "category": "Physical",
        "power": 85,
        "accuracy": 100,
        "pp": 15,
        "paralysis_chance": 0.3,
        "description": "Drops onto the target. May cause paralysis."
    },
    "Headbutt": {
        "type": "Normal",
        "category": "Physical",
        "power": 70,
        "accuracy": 100,
        "pp": 15,
        "flinch_chance": 0.3,
        "description": "Hits the target with a hard head. May cause flinching."
    },
    "Horn Attack": {
        "type": "Normal",
        "category": "Physical",
        "power": 65,
        "accuracy": 100,
        "pp": 25,
        "description": "Attacks with a sharp horn."
    },
    "Fury Attack": {
        "type": "Normal",
        "category": "Physical",
        "power": 15,
        "accuracy": 85,
        "pp": 20,
        "hits": [2, 5],
        "description": "Strikes 2-5 times in a row."
    },
    "Mega Kick": {
        "type": "Normal",
        "category": "Physical",
        "power": 120,
        "accuracy": 75,
        "pp": 5,
        "description": "A powerful kicking attack."
    },
    "Swift": {
        "type": "Normal",
        "category": "Special",
        "power": 60,
        "accuracy": 100,
        "pp": 20,
        "always_hits": True,
        "description": "Never misses."
    },
    "Rest": {
        "type": "Normal",
        "category": "Status",
        "power": 0,
        "accuracy": 100,
        "pp": 10,
        "heal": "MAX",
        "status": "Sleep",
        "status_duration": 2,
        "description": "Restores full HP and induces sleep for 2 turns."
    },

    # =========================
    # MOVES GRASS
    # =========================
    "Vine Whip": {
        "type": "Grass",
        "category": "Physical",
        "power": 45,
        "accuracy": 100,
        "pp": 25,
        "description": "Whips the target with vines."
    },
    "Razor Leaf": {
        "type": "Grass",
        "category": "Physical",
        "power": 55,
        "accuracy": 95,
        "pp": 25,
        "critical_ratio": 0.125,
        "description": "Has a high critical-hit ratio."
    },
    "Leech Seed": {
        "type": "Grass",
        "category": "Status",
        "power": 0,
        "accuracy": 90,
        "pp": 10,
        "leech": True,
        "leech_fraction": 0.125,
        "description": "Plants a seed that drains HP each turn."
    },
    "Solar Beam": {
        "type": "Grass",
        "category": "Special",
        "power": 120,
        "accuracy": 100,
        "pp": 10,
        "requires_charge": True,
        "description": "Charges on first turn, attacks on second."
    },

    # =========================
    # MOVES FIRE
    # =========================
    "Ember": {
        "type": "Fire",
        "category": "Special",
        "power": 40,
        "accuracy": 100,
        "pp": 25,
        "burn_chance": 0.1,
        "description": "A small flame attack. May cause burn."
    },
    "Flamethrower": {
        "type": "Fire",
        "category": "Special",
        "power": 90,
        "accuracy": 100,
        "pp": 15,
        "burn_chance": 0.1,
        "description": "Powerful flame attack. May cause burn."
    },
    "Fire Blast": {
        "type": "Fire",
        "category": "Special",
        "power": 110,
        "accuracy": 85,
        "pp": 5,
        "burn_chance": 0.1,
        "description": "Intense blast of fire. May cause burn."
    },
    "Metal Claw": {
        "type": "Steel",
        "category": "Physical",
        "power": 50,
        "accuracy": 95,
        "pp": 35,
        "attack_boost_chance": 0.1,
        "description": "Claws with metallic power. May raise Attack."
    },

    # =========================
    # MOVES WATER
    # =========================
    "Water Gun": {
        "type": "Water",
        "category": "Special",
        "power": 40,
        "accuracy": 100,
        "pp": 25,
        "description": "Shoots water at the target."
    },
    "Bubble": {
        "type": "Water",
        "category": "Special",
        "power": 40,
        "accuracy": 100,
        "pp": 30,
        "speed_reduction_chance": 0.1,
        "description": "Bubbles that may reduce target's Speed."
    },
    "Hydro Pump": {
        "type": "Water",
        "category": "Special",
        "power": 110,
        "accuracy": 80,
        "pp": 5,
        "description": "A powerful water jet attack."
    },
    "Surf": {
        "type": "Water",
        "category": "Special",
        "power": 90,
        "accuracy": 100,
        "pp": 15,
        "description": "Hits both opponents in double battles."
    },

    # =========================
    # MOVES ELECTRIC
    # =========================
    "Thunder Shock": {
        "type": "Electric",
        "category": "Special",
        "power": 40,
        "accuracy": 100,
        "pp": 30,
        "paralysis_chance": 0.1,
        "description": "Electric shock. May cause paralysis."
    },
    "Spark": {
        "type": "Electric",
        "category": "Physical",
        "power": 65,
        "accuracy": 100,
        "pp": 20,
        "paralysis_chance": 0.3,
        "description": "Electric attack. May cause paralysis."
    },

    # =========================
    # MOVES FLYING
    # =========================
    "Gust": {
        "type": "Flying",
        "category": "Special",
        "power": 40,
        "accuracy": 100,
        "pp": 35,
        "description": "Whips up a strong gust of wind."
    },
    "Wing Attack": {
        "type": "Flying",
        "category": "Physical",
        "power": 60,
        "accuracy": 100,
        "pp": 35,
        "description": "Strikes with sharp wings."
    },
    "Peck": {
        "type": "Flying",
        "category": "Physical",
        "power": 35,
        "accuracy": 100,
        "pp": 35,
        "description": "Pecks the target with beak."
    },

    # =========================
    # MOVES ROCK / GROUND
    # =========================
    "Rock Throw": {
        "type": "Rock",
        "category": "Physical",
        "power": 50,
        "accuracy": 90,
        "pp": 15,
        "description": "Throws a rock at the target."
    },
    "Rock Blast": {
        "type": "Rock",
        "category": "Physical",
        "power": 25,
        "accuracy": 90,
        "pp": 10,
        "hits": [2, 5],
        "description": "Hurls 2-5 rocks in succession."
    },
    "Bind": {
        "type": "Normal",
        "category": "Physical",
        "power": 15,
        "accuracy": 85,
        "pp": 20,
        "trapping": True,
        "trapping_duration": [2, 5],
        "description": "Traps the target for 2-5 turns."
    },
    "Dig": {
        "type": "Ground",
        "category": "Physical",
        "power": 80,
        "accuracy": 100,
        "pp": 10,
        "requires_charge": True,
        "description": "Digs underground on first turn, attacks on second."
    },
    "Sand Attack": {
        "type": "Ground",
        "category": "Status",
        "power": 0,
        "accuracy": 100,
        "pp": 15,
        "accuracy_reduction": 1,
        "description": "Lowers target's Accuracy."
    },

    # =========================
    # MOVES FIGHTING
    # =========================
    "Karate Chop": {
        "type": "Fighting",
        "category": "Physical",
        "power": 50,
        "accuracy": 100,
        "pp": 25,
        "critical_ratio": 0.125,
        "description": "A chopping attack with high critical-hit ratio."
    },
    "Low Kick": {
        "type": "Fighting",
        "category": "Physical",
        "power": 50,
        "accuracy": 100,
        "pp": 20,
        "weight_based": True,
        "description": "Damage depends on target's weight."
    },
    "Rolling Kick": {
        "type": "Fighting",
        "category": "Physical",
        "power": 60,
        "accuracy": 85,
        "pp": 15,
        "flinch_chance": 0.3,
        "description": "A spinning kick. May cause flinching."
    },
    "High Jump Kick": {
        "type": "Fighting",
        "category": "Physical",
        "power": 130,
        "accuracy": 90,
        "pp": 10,
        "recoil_on_miss": True,
        "description": "A powerful jump kick. Hurts user if it misses."
    },

    # =========================
    # MOVES GHOST
    # =========================
    "Lick": {
        "type": "Ghost",
        "category": "Physical",
        "power": 30,
        "accuracy": 100,
        "pp": 30,
        "paralysis_chance": 0.3,
        "description": "Licks the target. May cause paralysis."
    },
    "Night Shade": {
        "type": "Ghost",
        "category": "Special",
        "power": 0,
        "accuracy": 100,
        "pp": 15,
        "level_based_damage": True,
        "description": "Damages target equal to user's level."
    },
    "Shadow Punch": {
        "type": "Ghost",
        "category": "Physical",
        "power": 60,
        "accuracy": 100,
        "pp": 20,
        "always_hits": True,
        "description": "Never misses."
    },
    "Shadow Ball": {
        "type": "Ghost",
        "category": "Special",
        "power": 80,
        "accuracy": 100,
        "pp": 15,
        "sp_defense_reduction_chance": 0.2,
        "description": "May lower target's Special Defense."
    },
    "Dream Eater": {
        "type": "Ghost",
        "category": "Special",
        "power": 100,
        "accuracy": 100,
        "pp": 15,
        "requires_sleep": True,
        "heal_fraction": 0.5,
        "description": "Only works on sleeping targets. Heals user by 50% of damage."
    },
    "Dark Pulse": {
        "type": "Dark",
        "category": "Special",
        "power": 80,
        "accuracy": 100,
        "pp": 15,
        "flinch_chance": 0.2,
        "description": "May cause flinching."
    },

    # =========================
    # MOVES STEEL
    # =========================
    "Iron Tail": {
        "type": "Steel",
        "category": "Physical",
        "power": 100,
        "accuracy": 75,
        "pp": 15,
        "defense_reduction_chance": 0.3,
        "description": "Attacks with a steel tail. May lower Defense."
    },
}
