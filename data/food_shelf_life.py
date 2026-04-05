FOOD_RULES = {
    # 🥛 DAIRY
    "milk": {
        "category": "dairy",
        "storage": "fridge",
        "days_min": 5,
        "days_max": 7,
        "confidence": "high",
        "source_note": "FoodSafety.gov"
    },
    "yogurt": {
        "category": "dairy",
        "storage": "fridge",
        "days_min": 7,
        "days_max": 10,
        "confidence": "high",
        "source_note": "USDA FoodKeeper"
    },
    "cheese": {
        "category": "dairy",
        "storage": "fridge",
        "days_min": 7,
        "days_max": 21,
        "confidence": "medium",
        "source_note": "USDA FoodKeeper"
    },
    "eggs": {
        "category": "dairy",
        "storage": "fridge",
        "days_min": 21,
        "days_max": 28,
        "confidence": "high",
        "source_note": "FoodSafety.gov"
    },

    # 🥬 VEGETABLES
    "spinach": {
        "category": "vegetable",
        "storage": "fridge",
        "days_min": 5,
        "days_max": 7,
        "confidence": "medium",
        "source_note": "USDA FoodKeeper"
    },
    "lettuce": {
        "category": "vegetable",
        "storage": "fridge",
        "days_min": 5,
        "days_max": 7,
        "confidence": "medium",
        "source_note": "USDA FoodKeeper"
    },
    "tomato": {
        "category": "vegetable",
        "storage": "counter",
        "days_min": 3,
        "days_max": 5,
        "confidence": "medium",
        "source_note": "USDA FoodKeeper"
    },
    "broccoli": {
        "category": "vegetable",
        "storage": "fridge",
        "days_min": 3,
        "days_max": 5,
        "confidence": "medium",
        "source_note": "USDA FoodKeeper"
    },

    # 🍎 FRUITS
    "banana": {
        "category": "fruit",
        "storage": "counter",
        "days_min": 2,
        "days_max": 5,
        "confidence": "medium",
        "source_note": "USDA FoodKeeper"
    },
    "apple": {
        "category": "fruit",
        "storage": "fridge",
        "days_min": 21,
        "days_max": 30,
        "confidence": "medium",
        "source_note": "USDA FoodKeeper"
    },
    "strawberry": {
        "category": "fruit",
        "storage": "fridge",
        "days_min": 3,
        "days_max": 5,
        "confidence": "medium",
        "source_note": "USDA FoodKeeper"
    },
    "grapes": {
        "category": "fruit",
        "storage": "fridge",
        "days_min": 7,
        "days_max": 10,
        "confidence": "medium",
        "source_note": "USDA FoodKeeper"
    },

    # 🍗 PROTEIN
    "chicken raw": {
        "category": "protein",
        "storage": "fridge",
        "days_min": 1,
        "days_max": 2,
        "confidence": "high",
        "source_note": "FoodSafety.gov"
    },
    "chicken cooked": {
        "category": "protein",
        "storage": "fridge",
        "days_min": 3,
        "days_max": 4,
        "confidence": "high",
        "source_note": "FoodSafety.gov"
    },
    "fish": {
        "category": "protein",
        "storage": "fridge",
        "days_min": 1,
        "days_max": 2,
        "confidence": "high",
        "source_note": "FoodSafety.gov"
    },
    "ground beef": {
        "category": "protein",
        "storage": "fridge",
        "days_min": 1,
        "days_max": 2,
        "confidence": "high",
        "source_note": "FoodSafety.gov"
    },

    # 🍚 LEFTOVERS
    "cooked rice": {
        "category": "leftover",
        "storage": "fridge",
        "days_min": 3,
        "days_max": 4,
        "confidence": "high",
        "source_note": "FoodSafety.gov"
    },
    "leftovers": {
        "category": "leftover",
        "storage": "fridge",
        "days_min": 3,
        "days_max": 4,
        "confidence": "high",
        "source_note": "FoodSafety.gov"
    },

    # 🍞 BAKERY
    "bread": {
        "category": "bakery",
        "storage": "counter",
        "days_min": 5,
        "days_max": 7,
        "confidence": "medium",
        "source_note": "USDA FoodKeeper"
    },
    "tortilla": {
        "category": "bakery",
        "storage": "counter",
        "days_min": 5,
        "days_max": 7,
        "confidence": "medium",
        "source_note": "USDA FoodKeeper"
    }
}