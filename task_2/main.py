from pymongo import MongoClient, errors


# Підключення до MongoDB
def connect_to_mongodb():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["cats_database"]
        return db["cats_collection"]
    except errors.ConnectionFailure as e:
        print("Помилка підключення до MongoDB:", e)
        return None


# Функція для створення документа
def create_cat(collection, name, age, features):
    try:
        cat = {"name": name, "age": age, "features": features}
        collection.insert_one(cat)
        print(f"Кота '{name}' успішно додано.")
    except Exception as e:
        print("Помилка під час створення документа:", e)


# Функція для читання всіх записів
def read_all_cats(collection):
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except Exception as e:
        print("Помилка під час читання записів:", e)


# Функція для пошуку кота за ім'ям
def read_cat_by_name(collection, name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кіт із іменем '{name}' не знайдений.")
    except Exception as e:
        print("Помилка під час пошуку кота:", e)


# Функція для оновлення віку кота за ім'ям
def update_cat_age(collection, name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Вік кота '{name}' оновлено до {new_age}.")
        else:
            print(f"Кіт із іменем '{name}' не знайдений.")
    except Exception as e:
        print("Помилка під час оновлення віку:", e)


# Функція для додавання нової характеристики до кота
def add_cat_feature(collection, name, feature):
    try:
        result = collection.update_one({"name": name}, {"$addToSet": {"features": feature}})
        if result.matched_count > 0:
            print(f"Характеристику '{feature}' додано до кота '{name}'.")
        else:
            print(f"Кіт із іменем '{name}' не знайдений.")
    except Exception as e:
        print("Помилка під час додавання характеристики:", e)


# Функція для видалення запису за ім'ям
def delete_cat_by_name(collection, name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кота '{name}' видалено.")
        else:
            print(f"Кіт із іменем '{name}' не знайдений.")
    except Exception as e:
        print("Помилка під час видалення кота:", e)


# Функція для видалення всіх записів
def delete_all_cats(collection):
    try:
        collection.delete_many({})
        print("Усі записи видалено.")
    except Exception as e:
        print("Помилка під час видалення всіх записів:", e)


def main():
    collection = connect_to_mongodb()
    if collection is None:
        return

    create_cat(collection, "barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat(collection, "murzik", 5, ["хитрий", "білий"])

    print("\nВсі коти:")
    read_all_cats(collection)

    print("\nІнформація про кота 'barsik':")
    read_cat_by_name(collection, "barsik")

    print("\nОновлення віку кота 'barsik':")
    update_cat_age(collection, "barsik", 4)

    print("\nДодавання характеристики до кота 'barsik':")
    add_cat_feature(collection, "barsik", "любить молоко")

    print("\nВсі коти:")
    read_all_cats(collection)

    print("\nВидалення кота 'murzik':")
    delete_cat_by_name(collection, "murzik")

    print("\nВсі коти:")
    read_all_cats(collection)

    print("\nВидалення всіх записів:")
    delete_all_cats(collection)

    print("\nВсі коти:")
    read_all_cats(collection)


if __name__ == "__main__":
    main()
