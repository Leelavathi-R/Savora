from datetime import date
from data.food_shelf_life import FOOD_RULES
from data.price_data import PRICE_DATA
from data.weight_data import WEIGHT_DATA


DEFAULT_SHELF_LIFE = {
    "fridge": 5,
    "freezer": 30,
    "pantry": 5,
}


def normalize_storage(storage: str) -> str:
    return storage.strip().lower()


def get_shelf_life_days(item: str, storage: str) -> int:
    item_key = item.strip().lower()
    storage_key = normalize_storage(storage)

    if item_key in FOOD_RULES:
        return FOOD_RULES[item_key].get(storage_key, DEFAULT_SHELF_LIFE[storage_key])

    return DEFAULT_SHELF_LIFE[storage_key]


def get_days_since_purchase(purchase_date) -> int:
    return (date.today() - purchase_date).days


def get_days_left(item: str, storage: str, purchase_date) -> int:
    shelf_life = get_shelf_life_days(item, storage)
    days_used = get_days_since_purchase(purchase_date)
    return shelf_life - days_used

def get_usage_ratio(days_used: int, shelf_life: int) -> float:
    if shelf_life <= 0:
        return 1.0
    return days_used / shelf_life

def get_risk_level(days_used: int, shelf_life: int) -> str:
    ratio = get_usage_ratio(days_used, shelf_life)

    if ratio >= 1.1:
        return "High"
    if ratio >= 0.85:
        return "Medium"
    return "Low"


def analyze_items(items: list[str], storage: str, purchase_date) -> list[dict]:
    results = []

    days_used = get_days_since_purchase(purchase_date)

    for item in items:
        shelf_life = get_shelf_life_days(item, storage)
        days_left = shelf_life - days_used
        risk = get_risk_level(days_used, shelf_life)
        ratio = get_usage_ratio(days_used, shelf_life)

        results.append({
            "item": item,
            "storage": storage,
            "shelf_life_days": shelf_life,
            "days_since_purchase": days_used,
            "days_left": days_left,
            "risk": risk,
            "usage_ratio": round(ratio, 2),
        })

    return results

def estimate_impact(results: list[dict]) -> dict:
    total_price = 0
    total_weight = 0

    for r in results:
        # Only count risky items
        if 0 <= r["days_left"] <= 1:
            item = r["item"].lower()

            price = PRICE_DATA.get(item, 3)   # default $3
            weight = WEIGHT_DATA.get(item, 0.3)  # default 0.3kg

            total_price += price
            total_weight += weight

    return {
        "money_saved": round(total_price, 2),
        "waste_avoided": round(total_weight, 2),
    }

